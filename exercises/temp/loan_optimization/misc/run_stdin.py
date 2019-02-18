import loan_processor
import sys

loan_file = sys.stdin
analyzer = loan_processor.analyzer.LoanProcessor(loan_processor.redistribute.Redistributor())
loan_file.readline() #remove first line since it is only header
analyzer.read_loan_data(loan_file)
analyzer.redistribute()
analyzer.write_to_csv('./output.csv')
