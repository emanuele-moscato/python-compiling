#!/usr/bin/env python3

import sys

import_options = ['import', 'import_utils', 'utils']

def main():
    if len(sys.argv)==1 or sys.argv[1] not in import_options:
        print("No import.")
    else:
        import utils
        print("Importing module 'utils'.")
        utils.print_now()

if __name__=='__main__':
    main()
