from setuptools import setup
from setuptools.command.test import test as TestCommand
import casconfig

requirements = [
    'configsmash'
]

setup(
    name="casconfig",
    version=casconfig.__version__,
    author="Robby Ranshous",
    author_email="rranshous@gmail.com",
    description="Tiered cascading simple configs",
    keywords="configuration",
    url="https://github.com/rranshous/casconfig",
    py_modules=["casconfig"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=requirements,
)
