# Dep-Finder [![Build Status](https://travis-ci.org/Marcdh3/Dep-Finder.svg?branch=master)](https://travis-ci.org/Marcdh3/Dep-Finder) [![Coverage Status](https://coveralls.io/repos/github/Marcdh3/Dep-Finder/badge.svg?branch=dev)](https://coveralls.io/github/Marcdh3/Dep-Finder?branch=dev)
Python package dependency finder
## Installation
### Dependencies
All of the project dependencies are listed in the [requirements.txt](requirements.txt).
### Install steps
Inside the base directory of the project run the following commands to install all dependencies and install the depfinder package:
```
pip install -r requirements.txt
pip install .
```
### Tests
Run the following commands to ensure depfinder installed correctly:
```
python -m depfinder.test
```
## Usage
The depfinder utility can be executed from the command line to find all of the dependencies of a package, and print to stdout all of the necessary packages in a format suitable to generate a requirement.txt file. 
### Example
```
python -m depfinder -i <query package>
```
