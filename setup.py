from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
with open('README.md') as f:
    long_description = f.read()

setup(
    name='pydivar',
    version='1.0.1',
    packages=find_packages(),
    install_requires=requirements,
    author='Ali Ardakani',
    author_email='aliardakani78@gmail.com',
    description='Python library for crawling and extracting data from Divar',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ali-ardakani/pydivar.git',
    license='MIT',
)
