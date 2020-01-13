import setuptools

setuptools.setup(
    name='depfinder',
    version='1.0',
    description='This software retrieves all dependencies of local python '
                 + 'packages that were installed via pip.',
    author='Marcus Hill',
    author_email='n/a',
    url='https://github.com/Marcdh3/Dep-Finder',
    license='MIT',
    packages=['depfinder'],
    package_dir={'depfinder':'src'},
    install_requires=[
        'coverage',
        'coveralls'
    ])
