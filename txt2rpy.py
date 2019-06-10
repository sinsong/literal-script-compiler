import sys
import re

from core.row_file import row_file_open
from core.lparser import lparse
from core.llparser import llparse
from core.parser import parse
from core.codegen import codegen

from core.context import Context

# raw_content -> raw_line
# raw_line -> logic_lines
# logic_lines -> ir
# ir -> code_gen


def main():
    
    if len(sys.argv) < 2:
        return
    
    raw_content = row_file_open(sys.argv[1])
    raw_lines = lparse(raw_content)

    context = Context()

    llparse(context, raw_lines)
    parse(context)

    codegen(context)


if __name__ == '__main__':
	main()