#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "Detrich"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    specialFiles = re.compile(r'__(.*?)__')
    newList = []
    for dirpath, _, filenames in os.walk(dir):
        for f in filenames:
            result = specialFiles.search(f)
            if result:
                newList.append(os.path.abspath(os.path.join(dirpath, f)))
    return newList


def copy_to(paths, dir):
    Files = get_special_paths(paths)
    print(Files)
    os.makedirs(dir)
    for file in Files:
        check = shutil.copy2(file, dir)
        return check


def zip_to(paths, zippath):
    Files = get_special_paths(paths)
    makeStr = ",".join(Files)
    make_space = makeStr.replace(",", " ")
    print("Command I'm going to do: \n zip -j " + zippath + " " + make_space)
    try:
        check = subprocess.check_output(
            "zip -j " + zippath + " " + make_space, shell=True)
    except subprocess.CalledProcessError:
        check = subprocess.check_output(
            "zip -j " + zippath + " " + make_space + ";exit 0",
            stderr=subprocess.STDOUT, shell=True)
        print(check.decode("utf-8"))


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='matches directory')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    dirArgs = args.from_dir
    todirArg = args.todir
    tozipArg = args.tozip
    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    if not args:
        parser.print_usage()
        sys.exit(1)
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with
    # any
    # required args, the general rule is to print a usage message and exit(1).
    if todirArg and dirArgs:
        copy_to(dirArgs, todirArg)
    elif tozipArg and dirArgs:
        zip_to(dirArgs, tozipArg)
    else:
        print("\n".join(get_special_paths(dirArgs)))
    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
