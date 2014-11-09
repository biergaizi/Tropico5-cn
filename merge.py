#!/usr/bin/env python3


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
