"""Setuptools configuration for the Dici package."""

from pathlib import Path

from setuptools import find_packages, setup

HERE = Path(__file__).resolve().parent
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="dici-open",
    version="0.1.0a2",
    description="A lightweight terminal dictionary tool for quick word lookups.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/oJohnnyBoy/Dicio",
    author="oJohnnyMarcello",
    author_email="Bookman.Archive@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.15",
        "Topic :: Education",
        "Topic :: Utilities",
    ],
    keywords="dictionary cli japanese terminal",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.15",
    install_requires=[
        "rich<15.0.0",
        "prompt_toolkit==3.0.53",
        "requests==2.34.2",
    ],
    entry_points={
        "console_scripts": [
            "dici=dici.main:run",
        ],
    },
    project_urls={
        "Homepage": "https://github.com/oJohnnyBoy/Dicio",
        "Repository": "https://github.com/oJohnnyBoy/Dicio",
    },
)
