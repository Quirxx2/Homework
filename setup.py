import os
from setuptools import setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(
    name="rss_reader",
    description="Python command-line RSS reader",
    version="4.0",
    author="Siarhei Yemelyanchykau",
    author_email="siarheiii@gmail.com",
    py_modules=['rss_reader'],
    install_requires=read("requirements.txt").splitlines(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "rss-reader = rss_reader:main"
        ]
    })
