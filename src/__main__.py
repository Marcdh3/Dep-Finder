'''
Interface to finds all the dependencies of package.
'''
import sys
import argparse

from depfinder.finder import find_deps, generate_requirements

def parse(args):
    '''
    Parses arguments using argparse
    
    Parameters
    ----------
    args: list of strings
        argument options and values

    Returns
    ---------
    parsed_args: dict of strings
        argument options are the keys and the accompanying
        input are the values
    '''

    parser = argparse.ArgumentParser(description='Find and print to stdout'
                                                  + ' all the dependencies of a'
                                                  + ' package.')
    parser.add_argument('-i', '--input', required=True,
                        help='Name of the query package.')
    parsed_args = vars(parser.parse_args(args))
    return parsed_args


if __name__ == '__main__':
    args = parse(sys.argv[1:])
    dependencies = find_deps(args['input'])
    for req in generate_requirements(dependencies):
        print(req)
