from setuptools import setup, find_packages

setup(
    name="codeconvert",
    version="1.0.1",
    description="source code file convert to JPG file",
    author="norik00",
    packages=find_packages(),
    install_requires=['pygments', 'imgkit', 'BeautifulSoup4'],
    entry_points={
        "console_scripts": [
            "codeconvert=codeconvert.CodeConverter:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.7.7',
    ]
)