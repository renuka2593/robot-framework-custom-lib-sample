from setuptools import setup, find_packages

VERSION = "1.0.4"
LONG_DESCRIPTION = open("README.md").read()

setup(
    name="actions",
    version=VERSION,
    description="Helper library for Robot Framework",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Renuka Sharma",
    license="MIT",
    install_requires=["robotframework>=3.2.2"],
    packages=find_packages(where="src"),  # Automatically finds packages in the 'src' directory
    package_dir={"": "src"},  # Maps the 'src' directory as the root of the package structure
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: Robot Framework",
    ],
    python_requires=">=3.6",  # Specifies supported Python versions (from 3.6 onward)
)
