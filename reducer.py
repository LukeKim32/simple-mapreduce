#!/usr/bin/env python

# import modules
from itertools import groupby
from operator import itemgetter
import sys

# 'file' in this case is STDIN
def read_mapper_output(file, separator='\t'):
    # Go through each line
    for line in file:
        # Strip out the separator character
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # Read the data using read_mapper_output
    data = read_mapper_output(sys.stdin, separator=separator)
    # Group words and counts into 'group'
    #   Since MapReduce is a distributed process, each word
    #   may have multiple counts. 'group' will have all counts
    #   which can be retrieved using the word as the key.
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            # For each word, pull the count(s) for the word
            #   from 'group' and create a total count
            firstflag = 0
            #firstflag is for initializing maxval into first value from group
            for current_word,count in group :
                if firstflag == 0:
                    firstflag+=1
                    maxval = float(count)
                #compare count with maxval, and reassign maxval if count is bigger    
                if(maxval < float(count)):
                    maxval = float(count)

            # Write key and max value to stdout
            print("%s%s%f" % (current_word, separator, maxval))
        except ValueError:
            # Count was not a number, so do nothing
            pass

if __name__ == "__main__":
    main()                                                            
