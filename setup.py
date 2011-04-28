import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Selenium Redux',
    version="1.2.1",
    description="Selenium Redux picks up where Selenium 1 left off. It is backwards compatible, while adding new functionality and features, such as true implicit waits, methods that will allow you to wait for elements to become available, and much more.",
    author="Anthony Long",
    long_description=read('readme.rst'),
    url='http://github.com/antlong/selenium',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python', ],
)
