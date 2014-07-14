from setuptools import setup

setup(
    name='alurinium-image-processing',
    version='0.1.0',
    author='Vasiliy Sheredeko',
    author_email='piphon@gmail.com',
    packages=['alurinium'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful image processing utils using Pillow',
    long_description=open('README.md').read(),
    install_requires=[
        "Pillow >= 2.3.0",
    ],
)