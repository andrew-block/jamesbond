from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='jamesbond',
    version='0.0.12',
    description='James Bond tabular data package in Pandas dataframe',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Andrew Block',
    author_email='andrewblock87@gmail.com',
    keywords=['Bond', 'JamesBond', 'James Bond', '007'],
    url='https://github.com/andrew-block/jamesbond',
    download_url='https://test.pypi.org/project/jamesbond/'
)

install_requires = [
    'pandas>=1.1.0'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)