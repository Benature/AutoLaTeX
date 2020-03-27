from . import table
from .word2tex import word2tex
from . import equation

import argparse


def excel2table():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--f", help="the excel file path", dest="excel")
    parser.add_argument(
        "--type", help="the output type(`tex` or `md`)", dest="type")

    args = parser.parse_args()
    if args.type == None:
        args.type = "tex"

    print(args[0])
    df = table.read_excel(args.excel)
    print(table.convert(df, typ=args.type))
