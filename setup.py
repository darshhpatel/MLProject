from setuptools import find_packages, setup
from typing import List

HYPEN_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Darshan',
    author_email='darshhpatel@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
