'''
Utility that performs the dependency searches.
'''

import re
import subprocess
from tqdm import tqdm

def find_deps(query_package, current_package=None, package_list=[]):
    '''
    Recursively finds all dependencies of a package.

    Paramaters
    ----------
    query_package: string
        Name of the query package.
    current_package: string
        Current package to recursively search.
    package_list: list of strings
        List that will be populated with dependencies of
        the query package.

    Returns
    ----------
    package_list: list of strings
        Complete list of unique dependencies.
    '''

    if current_package == None:
        current_package = query_package
    
    reqs = None
    pip_text = subprocess.run(['pip', 'show', current_package],
                   stdout=subprocess.PIPE, text=True).stdout.split('\n')
    for line in pip_text:
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
    Generates the dependencies in a format suitable
    for a "requirements.txt" file.

    Parameters
    ----------
    dependencies: list of strings
        list of dependencies

    Returns
    ---------
    results: list of strings
        Dependencies with thier version numbers
    '''
    
    results = []
    dependencies.sort()
    for package in dependencies:
        pip_freeze = subprocess.Popen(['pip', 'freeze'],
                       stdout=subprocess.PIPE)
        grep_text = subprocess.run(['grep', '-i', package + '=='],
                                   stdin=pip_freeze.stdout,
                                   stdout=subprocess.PIPE,
                                   text=True).stdout
        pip_freeze.stdout.close()
        pip_freeze.wait()
        req = re.sub('\n', '', grep_text)
        if req != '':
            results.append(req)

    return results
