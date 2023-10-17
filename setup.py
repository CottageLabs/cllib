import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="cllib",
    version="0.0.1",
    author="somebody",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=[]),
    scripts=[],
    install_requires=[],
)
