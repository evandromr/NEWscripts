#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import os
import argparse


def gunzip_this(filename):
    """
    gunzip_this(filename)

    Decompress a *.gz file

    PARAMETERS
    ----------
    filename: str
       Name of the file to be decompressed

    RETURNS
    -------
    True: boolean

    NOTES
    -----
    The file will be extracted in the current directory

    """
    with gzip.GzipFile(filename, 'rb') as infile:
        content = infile.read()

    assert not os.path.isfile(filename.split(".gz")[0]), \
        'Output file already exists!!'

    with open(filename.split(".gz")[0], 'wb') as outfile:
        outfile.write(content)

    assert os.path.isfile(filename.split(".gz")[0]), "Something went wrong!!"

    return True

def gzip_this(filename):
    """
    gzip_this(filename)

    Compress a file using gzip format: *.gz

    PARAMETERS
    ----------
    filename: str
       Name of the file to be compressed

    RETURNS
    -------
    True: boolean

    NOTES
    -----
    The compressed file will be saved in the current directory

    """

    with open(filename, 'rb') as infile:
        content = infile.read()

    assert not os.path.isfile(filename+".gz"), 'Output file already exists!!'

    with gzip.GzipFile(filename+".gz", 'wb') as outfile:
        outfile.write(content)

    assert os.path.isfile(filename+".gz"), 'Something went wrong!!'

    return True
    

if __name__ == "__main__":

    # Get arguments from command line if runing as a script
    parser = argparse.ArgumentParser(description="A simple tool to handle gzip\
             tasks. NOTE: Please, use only one of the method flags -c OR -d.")
    parser.add_argument('filename', help="The file to be (de)compressed")
    parser.add_argument('-d', '--decompress', action='store_true',
                        help="Decompress FILENAME.gz")
    parser.add_argument('-c', '--compress', action='store_true',
                        help="Compress FILENAME using gzip")

    args = parser.parse_args()

    # check if login as anonymous or with user/passwd
    if args.decompress and args.compress:
        print("\nIncompatible methods chosen!!\n"
              "Please, run this script again with only one flag -c or -d\n"
              "run gziptools.py -h for help\n")
    elif args.decompress:
        if gunzip_this(args.filename):
            print("File sucessfully decompressed")
    elif args.compress:
        if gzip_this(args.filename):
            print("File sucessfully compressed")
    else:
        print("\nNo method chosen!!\n"
              "Please run this script again with The flags -d OR -c\n"
              "run gziptools.py -h for help\n")
