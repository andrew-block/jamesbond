from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["twine>=3", "wheel", "pip", "pandas"]

setup(
    name="jamesbond",
    version="0.0.1",
    author="Andrew Block",
    author_email="andrewblock87@gmail.com",
    description="James Bond tabular data package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)