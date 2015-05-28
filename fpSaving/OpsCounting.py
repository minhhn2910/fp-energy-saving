#!/usr/bin/python
import sys
import subprocess
import os
import os.path


def OpsCounting(gcov_file, search_result):
    ###TODO: read mpfr config file and re

def main(argv):

    if len(argv) != 2 :
        print "Usage: ./OpsCounting.py gcov_output_file search_result_file"
    OpsCounting(argv[0],argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])








