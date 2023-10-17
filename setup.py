import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

extras_require = {
    'gsheet': [
        'gspread~=5.10.0',
        'oauth2client~=4.1.3',
        'gspread-dataframe~=3.3.1',
        'gspread-formatting~=1.1.2',
    ],
    'xmlutil': [
        'lxml~=4.9',
    ],
    'selenium': [
        'selenium~=4.14',
    ],
}
extras_require['all'] = [item for group in extras_require.values() for item in group]

setup(
    name="cllib",
    version="0.0.1",
    author="somebody",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=[]),
    scripts=[],
    install_requires=[],
    extras_require=extras_require,
)
