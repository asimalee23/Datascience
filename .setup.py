from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    """
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # remove editable install flag if present
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="datascience",
    version="0.1.0",
    author="Asim Ali Memon",
    author_email="your_email@gmail.com",
    description="Data Science and Machine Learning project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements"),
)
