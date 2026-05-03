from setuptools import setup, find_packages

setup(
    name="morning-brief",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "morning-brief=morning_brief.__main__:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.8",
)