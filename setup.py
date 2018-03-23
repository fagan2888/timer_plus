from setuptools import setup, find_packages

setup(
        name='timer_plus',
        version='0.0.0',
        install_requires=[
            'pandas',
            ],
        packages=find_packages(exclude=['example']),
    )
