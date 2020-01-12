'''
Finds all the dependencies of package.
'''
#Author: Marcus Hill

import re
import os
import argparse

def find_deps(query_package, current_package=None, package_list=[]):
    '''
    Recursively finds all dependencies of a package.

    Paramaters
    ----------
    query_package: string
        Name of the query package.
    current_package: string
        Current package to recursively search.
    package_list: list of string
        List that will be populated with dependencies of
        the query package.

    Returns
    ----------
    package_list: list of string
        Complete list of unique dependencies.
    '''

    if current_package == None:
        current_package = query_package
    
    reqs = None
    os.system('pip show ' + current_package + ' > /tmp/req.txt')
    with open('/tmp/req.txt') as fp:
        for line in fp.read().split('\n'):
            if 'Requires' in line:
                reqs = line

    if reqs != None:
        reqs = re.sub('Requires:| ', '', reqs).split(',')
        if reqs != ['']:
            for dep in reqs:
                if dep not in package_list:
                    package_list = find_deps(query_package, dep, package_list)

    if(current_package not in package_list 
        and current_package != query_package):
        package_list.append(current_package)
    
    return package_list

def generate_requirements(dependencies):
    '''
    Prints to stdout the dependencies in a format suitable
    for a "requirements.txt" file.

    Parameters
    ----------
    dependencies: list of string
        list of dependencies

    Returns
    ---------
    NoneType object
    '''
    dependencies.sort()
    for package in dependencies:
        os.system('pip freeze | grep -i ' + package + '==')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find and print to stdout \
                                                  all the dependencies of a \
                                                  package.')
    parser.add_argument('-i', '--input', required=True,
                        help='Name of the query package.')
    args = vars(parser.parse_args())

    dependencies = find_deps(args['input'])
    generate_requirements(dependencies)
