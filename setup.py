import setuptools

setuptools.setup(
    name='depfinder',
    version='0.1',
    packages=['depfinder'],
    package_dir={'depfinder':'src'},
    install_requires=[
        'coverage',
        'coveralls'
    ])
