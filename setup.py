import setuptools

setuptools.setup(
    name='depfinder',
    version='0.1',
    packages=['depfinder'],
    package_dir={'depfinder':'src'},
    include_package_data=True,
    install_requires=[
        'coverage',
    ])
