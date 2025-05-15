from pathlib import Path

from setuptools import setup


INSTALL_REQUIRE = [
    "requests>=2.31.0",
]

cli_reqs = ["click==8.1.3", "tabulate==0.9.0"]


EXTRA_REQUIRE = {
    "cli": cli_reqs,
    "all": INSTALL_REQUIRE + cli_reqs,
}

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="kofnet",
    version="0.0.3",
    license="MIT",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description="Extract SNI bug host for different ISPs based on country",
    packages=["kofnet"],
    url="https://github.com/Simatwa/kofnet",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/kofnet/issues/new",
        "Homepage": "https://github.com/Simatwa/kofnet",
        "Source Code": "https://github.com/Simatwa/kofnet",
        "Issue Tracker": "https://github.com/Simatwa/kofnet/issues",
        "Download": "https://github.com/Simatwa/kofnet/releases",
        "Documentation": "https://github.com/Simatwa/kofnet/blob/main/docs",
    },
    entry_points={
        "console_scripts": [
            "kofnet = kofnet.console:main",
        ],
    },
    install_requires=INSTALL_REQUIRE,
    extras_require=EXTRA_REQUIRE,
    python_requires=">=3.10",
    keywords=["kofnet"],
    long_description=Path.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Free For Home Use",
        "Intended Audience :: Customer Service",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
