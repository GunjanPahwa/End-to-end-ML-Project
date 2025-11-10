#Responsible for creating ml application as a package
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: #function will return a list
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
#while we need -e , to activate setup.py, we dont need setup.py to consider it for installation

#on reading the requirements when we get to next line it will try to read \n as well and to avoid it we will replace it with blank space


setup(
name='mlproject',
version='0.0.1',
author='Gunjan',
author_email='gunjanpahwa70@gmail.com',
packages=find_packages(), #it will try to find the folders with __init__.py in them and consider those as packages
install_requires=get_requirements('requirements.txt')
)