from . import table
from .word2tex import word2tex
from . import equation

import argparse

__version__ = "0.1.7"


def excel2table():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "excelPath", help="the excel file path", type=str)
    parser.add_argument(
        "--type", help="the output type(`tex` or `md`)", choices=['tex', 'md', 'latex'])
    # parser.add_argument(
    #     "--ilim", help="row limits. Can be stop or (begin, stop)", dest="ilim")
    # parser.add_argument(
    #     "--jlim", help="vol limits. Can be stop or (begin, stop)", dest="jlim")
    parser.add_argument(
        "--border", help="tex mode, set the table border. Default as '|'", type=str)
    parser.add_argument(
        "--hline", help="tex mode, set the table border.", type=str)
    parser.add_argument(
        "--cap", help="tex mode, set the table caption. Default as '实验数据：'", type=str)
    parser.add_argument(
        "--clipboard", help="auto send text to clipboard")

    parser.add_argument(
        "-v", "--version", help="output version", action="store_true")

    args = parser.parse_args()

    if args.version:
        print(f'AutoLaTeX {__version__}')

    if args.excelPath in ["version", "v"]:
        print(f'AutoLaTeX {__version__}')
    else:
        df = table.read_excel(args.excelPath)
        print(table.convert(df, typ=args.type,  # ilim=args.ilim, jlim=args.jlim,
                            clipboard=args.clipboard, border=args.border, hline=args.hline, caption=args.cap))
