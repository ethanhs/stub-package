from distutils.core import setup
import os
setup(
    name="typedpkg_stubs",
    url="ethanhs.me",
    author="Ethan Smith",
    author_email="ethan@ethanhs.me",
    version="0.1",
    package_data={"typedpkg_stubs": os.listdir('typedpkg_stubs')},
    packages=["typedpkg_stubs"]
)