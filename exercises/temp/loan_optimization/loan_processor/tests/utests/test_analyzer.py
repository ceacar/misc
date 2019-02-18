import unittest
import loan_processor
class TestLoanProcessor(unittest.TestCase):
    def get_analyzer(self):
        return loan_processor.analyzer.LoanProcessor(loan_processor.redistribute.Redistributor())

    def test_set_redistributor(self):
        analyzer = self.get_analyzer()
        assert analyzer.redistributor != None
        analyzer.set_redistributor(None)
        assert analyzer.redistributor == None

    def test_is_every_one_has_net_unchanged(self):
        analyzer = self.get_analyzer()
        a_dict = {'a':40, 'b':30}
        b_dict = {'a':99, 'b':11}
        c_dict = {'a':99, 'b':11, 'c':123}
        assert analyzer.is_every_one_has_net_unchanged(a_dict, a_dict)
        assert analyzer.is_every_one_has_net_unchanged(a_dict, b_dict) == False
        assert analyzer.is_every_one_has_net_unchanged(a_dict, c_dict) == False

    def test_is_every_one_has_smaller_or_equal_gross(self):
        analyzer = self.get_analyzer()
        a_dict = {'a':40, 'b':30}
        b_dict = {'a':99, 'b':55}
        c_dict = {'a':99, 'b':11, 'c':123}

        assert analyzer.is_every_one_has_smaller_or_equal_gross( b_dict, a_dict)
        assert analyzer.is_every_one_has_smaller_or_equal_gross( a_dict, b_dict) == False
        assert analyzer.is_every_one_has_smaller_or_equal_gross( b_dict, c_dict) == False

    def test_assess_improvement(self):
        analyzer = self.get_analyzer()
        a_owned_dict = {'a':{'b':20}, 'b':{'c':10}}
        b_owned_dict = {'a':{'b':10, 'c':10}, 'b':{}}
        c_owned_dict = {'a':{'b':20, 'c':10}, 'b':{}}
        d_owned_dict = {'a':{'b':20, 'c':99}, 'b':{}}

        ok, _, _,new_net, new_gross = analyzer.assess_improvement(a_owned_dict,  b_owned_dict)
        assert (ok, new_net, new_gross)  == (True, 0, 40)
        ok, _, _, old_net, new_gross = analyzer.assess_improvement(a_owned_dict,  c_owned_dict)
        assert (ok, new_net, new_gross)  == (False, 0, 60)
        ok, _, _, new_net, new_gross = analyzer.assess_improvement(d_owned_dict,  c_owned_dict)
        assert (ok, new_net, new_gross)  == (False, 0, 60)

    def test_get_owned_dict(self) -> dict:
        analyzer = self.get_analyzer()
        assert analyzer.get_owned_dict(None) == {}
        input_dict = {'a':1}
        owned_dict = analyzer.get_owned_dict(owned_dict = input_dict)
        assert owned_dict == input_dict

    def test_get_total_owned(self) -> int:
        analyzer = self.get_analyzer()
        analyzer.owned = {1:{2:10, 3:89}}
        assert analyzer.get_total_owned(1, None) == 99

    def test_get_net_dict(self) -> int:
        analyzer = self.get_analyzer()
        b_owned_dict = {'a':{'b':10, 'c':10}, 'b':{}}
        assert analyzer.get_net_dict(b_owned_dict) == {'a': 20, 'b': -10, 'c': -10}

    def test_get_gross_dict(self) -> int:
        analyzer = self.get_analyzer()
        b_owned_dict = {'a':{'b':10, 'c':10}, 'b':{}}
        assert analyzer.get_gross_dict(b_owned_dict) == {'a': 20, 'b': 10, 'c': 10}

    def test_cache_name(self):
        analyzer = self.get_analyzer()
        analyzer.cache_name('a')
        assert analyzer.id_name_mapper == {0:'a'}
        assert analyzer.name_id_mapper == {'a':0}

        analyzer.cache_name('b')
        assert analyzer.id_name_mapper == {0:'a', 1:'b'}
        assert analyzer.name_id_mapper == {'a':0, 'b':1}

    def test_get_id(self):
        analyzer = self.get_analyzer()
        analyzer.cache_name('a')
        assert analyzer.get_id('a') == 0

    def test_get_name(self):
        analyzer = self.get_analyzer()
        analyzer.cache_name('a')
        assert analyzer.get_name(0) == 'a'

    def test_populate_owned_map_with_name(self):
        analyzer = self.get_analyzer()
        analyzer.cache_name('a')
        analyzer.cache_name('b')
        analyzer.owned = {0:{1:10}}
        assert analyzer.populate_owned_map_with_name() == {'a':{'b':10}}

    def test_cache_owned(self):
        analyzer = self.get_analyzer()
        analyzer.cache_owned(0,1,99)
        assert analyzer.owned == {0:{1:99}}

    def test_parse_loan(self):
        analyzer = self.get_analyzer()
        analyzer.parse_loan("a,b,99")
        assert analyzer.owned == {1:{0:99}}
