from setuptools import setup, find_packages

VERSION = "1.0.0"


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()


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
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Santiago Fraire Willemoës",
    author_email="de-ddci@kpn.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={"mkdocs.themes": ["kpn = kpn_theme",]},
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    keywords=["mkdocs", "documentation", "theme"],
)
