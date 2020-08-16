from setuptools import setup, find_packages

with open('/Users/andrewblock/Documents/github/jamesbond/README.md') as readme_file:
    readme = readme_file.read()

with open('/Users/andrewblock/Documents/github/jamesbond/requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(
    name='jamesbond',
    version='0.0.14',
    description='James Bond tabular data package in Pandas dataframe',
    long_description_content_type="text/markdown",
    long_description=readme,
    install_requires=requirements,
    license='MIT',
    packages=find_packages(exclude=("tests",)),
    author='Andrew Block',
    author_email='andrewblock87@gmail.com',
    keywords=['Bond', 'JamesBond', 'James Bond', '007'],
    url='https://github.com/andrew-block/jamesbond',
    download_url='https://test.pypi.org/project/jamesbond/'
)