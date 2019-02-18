from typing import Union
import errors
import copy


class Redistributor:
    def __init__(self):
        pass

    def extract_chain_debt(self, owned_dict: dict) -> list:
        """
        owned map {'d': {'c': 30, 'b': 20}, 'b': {'c': 50}, 'c': {'a': 40}, 'a': {'d': 30, 'b': 60}}
        return [[...]]
        element is [from_id, middle_id, to_id, amount]
        """
        owned_dict_keys = owned_dict.keys()

        for id in owned_dict_keys:
            borrower_list = list(owned_dict[id].items())
            for borrower_id, amount in borrower_list:
                sub_debt_dict = owned_dict[borrower_id]
                for sub_borrower_id, sub_borrow_amount in list(sub_debt_dict.items()):
                    new_chain_debt = [id, borrower_id, sub_borrower_id, min(amount, sub_borrow_amount)]
                    #only returns the first chain, since every chain debt cancelling will update iter list
                    #python will error out on changed list while iterating
                    return new_chain_debt

    def redistribute(self, owned_dict: dict) -> dict:
        """
        owned map {'d': {'c': 30, 'b': 20}, 'b': {'c': 50}, 'c': {'a': 40}, 'a': {'d': 30, 'b': 60}}
        owned map {0: {1: 60, 2: 30}, 1: {3: 50}, 2: {1: 20, 3: 30}, 3: {0: 40}}
        """

        owned_dict = self.deepcopy_dict(owned_dict)
        owned_dict_keys = owned_dict.keys()
        multiple_chain = False

        extracted_chain_debt = self.extract_chain_debt(owned_dict)

        #loop until no debt chain is found
        while extracted_chain_debt:
            self.cancel_chain_debt(extracted_chain_debt, owned_dict)
            extracted_chain_debt = self.extract_chain_debt(owned_dict)

        return owned_dict

    def cancel_chain_debt(self, chain_debt: list, owned_dict: dict):
        """
        input: [0,1,3,50], means loan of 0 -> 1 -> 3 with 50
        this function will remove the debt from 0 -> 1 and 1-> 3 and
        add a new debt 0 -> 3
        """
        lender_id, borrower_id, sub_borrower_id, reduce_amount = chain_debt

        if lender_id != sub_borrower_id:
            self.reduce_debt(owned_dict, lender_id , borrower_id, reduce_amount)
            self.reduce_debt(owned_dict, borrower_id, sub_borrower_id, reduce_amount)
            self.add_debt(owned_dict, lender_id, sub_borrower_id, reduce_amount)
        else:
            self.reduce_debt(owned_dict, lender_id , borrower_id, reduce_amount)
            self.reduce_debt(owned_dict, borrower_id, sub_borrower_id, reduce_amount)

    def add_debt(self, owned_dict: dict, id_from: int, id_to: int, amount: int):
        debt = owned_dict[id_from]
        if id_to not in debt:
            debt[id_to] = amount
        else:
            debt[id_to] += amount

    def reduce_debt(self, owned_dict: dict, id_from: int, id_to: int, amount: int):
        debt = owned_dict[id_from]
        id_to_amount = debt[id_to]
        if id_to_amount == amount:
            #debt clear from tier1 to tier2
            del debt[id_to]
        elif id_to_amount > amount:
            debt[id_to] = id_to_amount - amount
        else:
            raise errors.UnexpectedError("id_to_amount {0} should never be smaller than {1}".format(id_to_amount, amount))

    def deepcopy_dict(self, owned_dict: dict) -> Union[dict, dict]:
        return copy.deepcopy(owned_dict)
