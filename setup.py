from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_reqirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    reqirements=[]
    with open(file_path)as file_obj:
        reqirements=file_obj.readlines()
        [req.replace("\n","")for req in reqirements]

        if HYPEN_E_DOT in reqirements:
            reqirements.remove(HYPEN_E_DOT)




setup(
    name='mlprojects',
    version='0.0.1',
    author='Sharath',
    author_email='sharathr751@gmail.com',
    packages=find_packages(),
    install_requires=get_reqirements('reqirements.txt')
)