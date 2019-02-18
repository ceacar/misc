def is_every_one_has_net_unchanged(old_net_dict: dict,
                                   new_net_dict: dict) -> bool:
    if old_net_dict.keys() != new_net_dict.keys():
        return False

    for id, net in old_net_dict.items():
        if net != new_net_dict[id]:
            return False

    return True

def is_every_one_has_smaller_or_equal_gross(old_gross_dict: dict,
                                            new_gross_dict: dict) -> bool:
    if old_gross_dict.keys() != new_gross_dict.keys():
        return False

    for id, old_gross in old_gross_dict.items():
        if old_gross < new_gross_dict[id]:
            return False

    return True

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

    is_new_net_ok = is_every_one_has_net_unchanged(old_net_dict, new_net_dict)
    is_new_gross_ok = is_every_one_has_smaller_or_equal_gross(old_gross_dict, new_gross_dict )

    old_net_total = sum(old_net_dict.values())
    new_net_total = sum(new_net_dict.values())
    old_gross_total = sum(old_gross_dict.values())
    new_gross_total = sum(new_gross_dict.values())

    is_new_debt_ok = (is_new_net_ok and is_new_gross_ok)
    print("new debt stats",is_new_net_ok, is_new_gross_ok, old_net_total, new_net_total, old_gross_total, new_gross_total)
    return is_new_debt_ok, old_net_total, old_gross_total, new_net_total, new_gross_total


def assess_improvement(old_owned_dict: dict,
                       new_owned_dict: dict):
    """
    1.new Net across each party doesn’t change. Also
    2.make sure that for each Lender and Borrower the abs(new owed or owes) <= abs(existing
    owed or owes)
    """
    is_constrain_matched, _, _, new_net_total, new_gross_total = self.get_new_debt_stats(
        old_owned_dict, new_owned_dict)

    print("assess {}".format(is_constrain_matched))

    return is_constrain_matched, new_net_total, new_gross_total

