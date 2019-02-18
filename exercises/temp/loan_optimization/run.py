import loan_processor
import sys

loan_file = open('./loans.csv', 'r')

analyzer = loan_processor.analyzer.LoanProcessor(loan_processor.redistribute.Redistributor())

loan_file.readline() #remove first line since it is only header
analyzer.read_loan_data(loan_file)

_, old_net, old_gross, new_net, new_gross = analyzer.redistribute()
print("optimized gross from {old_gross} to {new_gross}".format(old_gross = old_gross, new_gross = new_gross))
output_file_path = './output.csv'
analyzer.write_to_csv(output_file_path)
print("generated new loan to file \"{}\"".format(output_file_path))
