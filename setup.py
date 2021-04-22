from setuptools import setup

setup(
    name="codeconvert",
    version="1.0.0",
    description="source code file convert to JPG file",
    author="norik00",
    install_requires=['pygments', 'imgkit', 'BeautifulSoup4'],
    entry_points={
        "console_scripts": [
            "codeconvert=tool.CodeConverter:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.7.7',
    ]
)