import setuptools

setuptools.setup(
    name='depfinder',
    version='0.1',
    packages=['depfinder', 'depfinder.test'],
    package_dir={'depfinder':'src', 'depfinder.test':'tests'},
    install_requires=[
        'coverage',
        'coveralls'
    ])
