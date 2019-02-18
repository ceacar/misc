import sys
import io
import errors
import redistribute
from typing import Union

class LoanProcessor:
    def __init__(self, new_redistributor: redistribute.Redistributor):
        self.owned = {}
        self.name_id_mapper = {}
        self.name_id_index = 0
        self.id_name_mapper= {}
        self.set_redistributor(new_redistributor)
        self.net_gross_multipler_lookup = {
            "net": -1,
            "gross": 1,
        }

    def set_redistributor(self, new_redistributor: redistribute.Redistributor):
        self.redistributor = new_redistributor

    def get_new_debt_stats(self, old_owned_dict: dict,
                           new_owned_dict: dict) -> Union[bool, int, int, int, int]:
        """
        returns:
            is_net_unchanged(bool)
            --> is gross smaller(bool)
        """
        old_net_dict = self.get_net_dict(owned_dict = old_owned_dict)
        new_net_dict = self.get_net_dict(owned_dict = new_owned_dict)
        old_gross_dict = self.get_gross_dict(owned_dict = old_owned_dict)
        new_gross_dict = self.get_gross_dict(owned_dict = new_owned_dict)

        is_new_net_ok = self.is_every_one_has_net_unchanged(old_net_dict, new_net_dict)
        is_new_gross_ok = self.is_every_one_has_smaller_or_equal_gross(old_gross_dict, new_gross_dict )

        old_net_total = sum(old_net_dict.values())
        new_net_total = sum(new_net_dict.values())
        old_gross_total = sum(old_gross_dict.values())
        new_gross_total = sum(new_gross_dict.values())

        is_new_debt_ok = (is_new_net_ok and is_new_gross_ok)
        return is_new_debt_ok, old_net_total, old_gross_total, new_net_total, new_gross_total

    def is_every_one_has_net_unchanged(self, old_net_dict: dict, new_net_dict: dict) -> bool:
        if old_net_dict.keys() != new_net_dict.keys():
            return False

        for id, net in old_net_dict.items():
            if net != new_net_dict[id]:
                return False

        return True

    def is_every_one_has_smaller_or_equal_gross(self, old_gross_dict: dict, new_gross_dict: dict) -> bool:
        if old_gross_dict.keys() != new_gross_dict.keys():
            return False

        for id, old_gross in old_gross_dict.items():
            if old_gross < new_gross_dict[id]:
                return False

        return True

    def assess_improvement(self, old_owned_dict: dict,
                           new_owned_dict: dict):
        """
        1.new Net across each party doesn’t change. Also
        2.make sure that for each Lender and Borrower the abs(new owed or owes) <= abs(existing
        owed or owes)
        """
        is_constrain_matched, old_net_total, old_gross_total, new_net_total, new_gross_total = self.get_new_debt_stats(
            old_owned_dict, new_owned_dict)

        return is_constrain_matched, old_net_total, old_gross_total, new_net_total, new_gross_total

    def redistribute(self):
        """
        Gross = Net + 2X abs(owns)
        To minimize Gross:
            1. debt cancelling: this will minimize the borrowing for each lender to minimize gross

        result:
            Gross = Net
        """

        old_owned_dict = self.owned

        #redistribute all the debts here
        new_owned_dict = self.redistributor.redistribute(self.owned)

        #assess the net and gross
        assess_result, old_net, old_gross, new_net, new_gross = self.assess_improvement(old_owned_dict, new_owned_dict)
        owned_dict_with_name = self.populate_owned_map_with_name(new_owned_dict)
        return owned_dict_with_name, old_net, old_gross, new_net, new_gross

    def get_owned_dict(self, owned_dict: dict) -> dict:
        if not owned_dict:
            owned_dict = self.owned
        return owned_dict

    def get_total_owned(self, lender_id: int, owned_dict:dict = None) -> int:
        owned_dict = self.get_owned_dict(owned_dict)

        borrower_dict = owned_dict.get(lender_id, {})
        total_amount = 0
        for _, amount in borrower_dict.items():
            total_amount += amount

        return total_amount

    def get_sum_dict(self, owned_dict: dict = None, stat: str = "net") -> int:
        multiplier = self.net_gross_multipler_lookup[stat]
        owned_dict = self.get_owned_dict(owned_dict)
        sum_dict = {}
        for id, borrower_list in owned_dict.items():
            for borrower_id, amount in borrower_list.items():
                if id not in sum_dict:
                    sum_dict[id] = amount
                else:
                    sum_dict[id] += amount
                #for borrower the net is negative
                if borrower_id not in sum_dict:
                    sum_dict[borrower_id] = amount * multiplier
                else:
                    sum_dict[borrower_id] += amount * multiplier

        return sum_dict


    def get_net_dict(self, owned_dict: dict = None, stat: str= "net") -> int:
        return self.get_sum_dict(owned_dict, "net")

    def get_gross_dict(self, owned_dict: dict = None, stat: str= "net") -> int:
        return self.get_sum_dict(owned_dict, "gross")

    def cache_name(self, name: str):
        #create name id lookup to minimize memory size
        id = self.name_id_index
        if name not in self.name_id_mapper:
            self.name_id_mapper[name] = self.name_id_index
            self.name_id_index += 1

            self.id_name_mapper[id] = name

    def get_id(self, name: str) -> int:
        return self.name_id_mapper.get(name, -1)

    def get_name(self, id: int) -> str:
        return self.id_name_mapper.get(id, -1)

    def populate_owned_map_with_name(self, owned_dict: dict = None):
        owned_dict = self.get_owned_dict(owned_dict)
        owned_with_name = {}
        for lender_id, borrows_list in owned_dict.items():
            lender_name = self.get_name(lender_id)
            owned_with_name[lender_name] = {}
            borrower_dict = owned_with_name[lender_name]
            for borrower_id, amount in borrows_list.items():
                borrower_name= self.get_name(borrower_id)
                borrower_dict[borrower_name] = amount
        return owned_with_name

    def write_to_csv(self, output_file_abs_path: str, owned_dict: dict = None):
        owned_dict = self.get_owned_dict(owned_dict)
        output_file = open(output_file_abs_path, 'w')
        for lender_id, borrows_list in owned_dict.items():
            lender_name = self.get_name(lender_id)
            for borrower_id, amount in borrows_list.items():
                borrower_name= self.get_name(borrower_id)
                csv_str = ','.join([lender_name, borrower_name, str(amount)]) + '\n'
                output_file.write(csv_str)

    def print_all(self):
        #debug print
        print("id_name_map:", self.id_name_mapper)
        print("name_id_map:", self.name_id_mapper)
        print("owned map", self.owned)
        print("owned map", self.populate_owned_map_with_name())

    def cache_owned(self, lender_id, borrower_id, amount):
        if lender_id not in self.owned:
            self.owned[lender_id] = {}

        borrower_dict = self.owned[lender_id]
        borrower_dict[borrower_id] = amount

    def cache_ledger(self, lender, borrower, amount):
        self.cache_name(borrower)
        self.cache_name(lender)
        lender_id = self.get_id(lender)
        borrower_id = self.get_id(borrower)
        self.cache_owned(lender_id, borrower_id, amount)

    def parse_loan(self, line: str):
        line_arr = line.rstrip().split(',')
        if len(line_arr) < 3:
            raise errors.InvalidLoanInputFormat("invalid file input format {}".format(line))

        lender = line_arr[0].lower() # lender data may have name cap issue
        borrower = line_arr[1].lower()
        amount = int(line_arr[2].lower())

        self.cache_ledger(lender, borrower, amount)

    def read_loan_data(self, input_file: io.IOBase):
        try:
            for line in input_file:
                self.parse_loan(line)
        except errors.InvalidLoanInputFormat as e:
            sys.stderr.write(e.message + "\n skipked message:{}".format(line))
        except ValueError as e:
            sys.stderr.write( + "invalid loan amount\n skipked message:{}".format(line))


