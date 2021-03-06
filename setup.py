from setuptools import setup, find_packages

setup(
    name = "steak-xss",
    version = "0.2.1",
    keywords = ["steak", "xss","steak-xss"],
    description = "An automatic XSS vulnerability exploit tool",
    license = "MIT",

    url = "https://hiram.wang/",          # your module home page, such as
    author = "LoveSteak",                         # your name
    author_email = "hiramscu@163.com",    # your email

    packages = find_packages(),
    #packages = ['steak'],
    include_package_data = True,
    platforms = "any",
    install_requires = [
        "Flask>=1.1.2",
        "pymetasploit3>=1.0.3",
        "colorama>=0.4.4",
        "gevent>=21.1.2"
    ]
)