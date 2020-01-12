'''
Interface to finds all the dependencies of package.
'''

import argparse

from .finder import find_deps, generate_requirements

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find and print to stdout \
                                                  all the dependencies of a \
                                                  package.')
    parser.add_argument('-i', '--input', required=True,
                        help='Name of the query package.')
    args = vars(parser.parse_args())

    dependencies = find_deps(args['input'])
    generate_requirements(dependencies)
