'''
    This setup.py is essential part of packaging and distribution of Python projects.
    It is used by setuptools to define the project metadata, dependencies, and other configurations.
    This file is used to package the project for distribution.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:

    requirement_lst:List[str]= []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")
    return requirement_lst

setup(
    name='Network-Security',
    version='0.0.1',
    author='Swasti Jain',
    author_email='swastijain1903@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)