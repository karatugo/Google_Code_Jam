# Google Code Jam
# This is Problem A of Qualification Round Africa 2010
# https://code.google.com/codejam/contest/351101/dashboard#s=p0

from sys import argv
from os.path import exists

script, from_file, to_file = argv 

input_file = open (from_file);
output_file = open (to_file, 'w');

N_TEST = input_file.readline();

for testcase in range (0, int(N_TEST)):
	CREDIT = input_file.readline();
	N_ITEMS = input_file.readline();
	PRICES = input_file.readline();
	LIST_OF_PRICES = PRICES.split();

	for i in range (0, len(LIST_OF_PRICES)):
		for j in range(i+1, len(LIST_OF_PRICES)):
			if (int(LIST_OF_PRICES[i]) + int(LIST_OF_PRICES[j]) == int(CREDIT)):
				output_file.write("Case #%r: %r %r" %(testcase + 1, i+1, j+1));
				output_file.write("\n");
	

input_file.close();
output_file.close();