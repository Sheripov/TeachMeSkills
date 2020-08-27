import argparse
import csv
import os

file_path = os.path.realpath('__init__.py')  # __file__
dir_name = os.path.dirname(file_path)
os.mkdir('pathtodir')

#
# parser = argparse.ArgumentParser()
# parser.add_argument('-fn', '--first-name', required=True)
# parser.add_argument('-ln', '--last-name', required=True)
# parser.add_argument('echo')
# args = parser.parse_args()
#
# with open('test.csv', "a", newline='\r') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow([args.first_name, args.last_name])
# print(args)
# print('First name:', args.first_name)
# print('Last name:', args.last_name)
# print('echo:', args.echo)