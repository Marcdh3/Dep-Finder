# Dep-Finder [![Build Status](https://travis-ci.org/Marcdh3/Dep-Finder.svg?branch=master)](https://travis-ci.org/Marcdh3/Dep-Finder) [![Coverage Status](https://coveralls.io/repos/github/Marcdh3/Dep-Finder/badge.svg?branch=master)](https://coveralls.io/github/Marcdh3/Dep-Finder?branch=master) ![Python Status](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)
This software retrieves all dependencies of local python packages that were installed via pip.
## Installation
### Dependencies
This project's dependencies are listed in the [requirements.txt](requirements.txt) file.
### Install steps
Inside the base directory of the project, run the following commands to install dependencies and the depfinder package:
```
pip install -r requirements.txt
pip install .
```
### Tests
Run the following command to ensure depfinder was installed correctly:
```
python tests/main.py
```
2 tests should run without any errors.
## Usage
The depfinder utility can print to stdout all dependencies of a package in a format that is suitable for requirements.txt files. 
### Example
```
python -m depfinder -i <query package>
```
