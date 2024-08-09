from setuptools import find_packages, setup
from typing import List
hyphen_e = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''this function will return list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
 
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements
             
setup( name = 'MLProject', version="0.0.1", author = "Kinshuk", author_email = "kinshukkochhar095@gmail.com",
packages = find_packages(), 
install_requires = get_requirements('requirements.txt') )