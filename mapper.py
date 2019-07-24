#!/usr/bin/env python

# Use the sys module
import sys

# 'file' in this case is STDIN
def read_input(file):
    # Split each line into words
    for line in file:
        yield line.split(',')

def main(separator='\t'):
    # Read the data using read_input
    data = read_input(sys.stdin)
    # Process each word returned from read_input
    for words in data:
        # Process each word
        value = words[1][:]
        #refine the value if '\n' is concatenated
        if value[-1]=='\n':
            value = value[:len(value)-1]

        #Write key, and value to STDOUT
        print('%s%s%f' % (words[0],separator,float(value)))

if __name__ == "__main__":
    main()
