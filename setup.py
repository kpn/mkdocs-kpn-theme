from setuptools import setup, find_packages

VERSION = "0.15.0"

# Load list of dependencies
with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n") if line and not line.startswith("#")
    ]

setup(
    name="mkdocs-kpn",
    version=VERSION,
    url="https://github.com/kpn/mkdocs-kpn-theme",
    license="MIT",
    description="A KPN-styles theme for MkDocs",
    author="Santiago Fraire Willemoës",
    author_email="de-ddci@kpn.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={"mkdocs.themes": ["kpn = kpn_theme", ]},
    zip_safe=False,
)
