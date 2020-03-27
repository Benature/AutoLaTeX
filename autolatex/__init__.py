from . import table
from . import maths
from . import word2tex

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
