import loan_processor

def main():
    loan_file = open('./loan_processor/tests/data/simple_loans.csv', 'r')
    loan_file.readline()
    analyzer = loan_processor.analyzer.LoanProcessor(loan_processor.redistribute.Redistributor())
    analyzer.read_loan_data(loan_file)
    res_dict, _, _, new_net, new_gross = analyzer.redistribute()
    assert (sorted(res_dict), new_net, new_gross) == (sorted({'c': {}, 'a': {'c': 20, 'b': 30}, 'b': {}, 'd': {'c': 20}}), 0, 140)

if __name__ == '__main__':
    main()
