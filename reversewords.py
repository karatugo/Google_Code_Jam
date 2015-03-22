# Google Code Jam
# This is Problem B of Qualification Round Africa 2010
# https://code.google.com/codejam/contest/351101/dashboard#s=p1

from sys import argv
from os.path import exists

script, from_file, to_file = argv 

input_file = open (from_file);
output_file = open (to_file, 'w');

N_TEST = input_file.readline();

for testcase in range (0, int(N_TEST)):
	line = input_file.readline();
	list_of_words = line.split();

	for i in range (0, len(list_of_words)):
			if (i == 0):
				output_file.write("Case #%s: %s" %(testcase+1, list_of_words[-i-1]));
			else: 
				output_file.write(" %s" %list_of_words[-i-1]);

			if (i == len(list_of_words) - 1):
				output_file.write("\n");

	

input_file.close();
output_file.close();