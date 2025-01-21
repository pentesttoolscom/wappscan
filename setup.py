from setuptools import find_packages, setup

setup(
    name="wappscan",  # Your app name
    version="0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple CLI app that runs scans on wappscan.io",
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["typer[all]"],  # Dependencies
    entry_points={
        "console_scripts": [
            "wappscan=wappscan.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify Python version compatibility
)
