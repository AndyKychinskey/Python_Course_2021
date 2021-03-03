from setuptools import setup

setup(
    name = 'a_kychinskii_s_package',
    version = '0.0.1',
    description = 'Just test package :-)',
    author = 'Andrei Kychinskii',
    author_email = 'my_email@gmail.com',
    packages = ['a_kychinskii_s_package', 'a_kychinskii_s_package.utils'],
    install_requires = ['numpy']
)