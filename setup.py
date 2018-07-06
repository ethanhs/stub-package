from distutils.core import setup


setup(
    name="typedpkg-stubs",
    url="https://github.com/ethanhs/stub-package",
    author="Ethan Smith",
    author_email="ethan@ethanhs.me",
    version="0.1",
    package_data={"typedpkg-stubs": ['sample.pyi',
                                     '__init__.pyi']},
    packages=["typedpkg-stubs"]
)