
from setuptools import find_packages, setup
from typing import List

HIPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HIPHEN_E_DOT in requirements:
            requirements.remove(HIPHEN_E_DOT)

setup(name='Costumer-churn-prediction',
      version='0.0.1',
      description='Machine Learning Project to predict customer churn',
      author='Arjun Dadhich',
      author_email='arjun.dadhich004@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
     )