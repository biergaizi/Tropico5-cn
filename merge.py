#!/usr/bin/env python3

# Copyright (c) 2014 Tom Li
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys
import csv


def load(csv_file):
    contents = []

    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            contents.append(row)

    return contents


def merge(old_tr, new_tr):
    translation = {}
    for i in old_tr:
        text = i[2]   # text
        trans = i[10] # NewTranslation
        if translation.get(text) and translation[text] != trans:
            print("Warning: multiple translation for \"%s\"" % text, file=sys.stderr)
        translation[text] = trans

    for i in new_tr:
        text = i[2]   # text
        try:
            i[10] = translation[text]  # NewTranslation
            i[11] = "OK"  # status
        except KeyError:
            pass


def output(tr):
    writer = csv.writer(sys.stdout)
    writer.writerows(tr)

if __name__ == "__main__":
    old = sys.argv[1]
    new = sys.argv[2]

    old_csv = load(old)
    new_csv = load(new)

    merge(old_csv, new_csv)

    output(new_csv)
