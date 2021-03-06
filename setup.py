from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "steak-xss",
    version = "0.2.3",
    keywords = ["steak", "xss","steak-xss"],
    description = "An advanced XSS exploitation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = "MIT",
    url = "https://github.com/LoveSteak/Steak",
    author = "LoveSteak",
    author_email = "hiramscu@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
        "Flask>=1.1.2",
        "pymetasploit3>=1.0.3",
        "colorama>=0.4.4",
        "gevent>=21.1.2"
    ]
)
