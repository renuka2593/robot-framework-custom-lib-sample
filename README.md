# Sample Custom Library for Robot Framework

![License](https://img.shields.io/badge/license-MIT-blue)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Python Implementation of Library (Actions)](#python-implementation-of-library-actions)
- [Create the setup.py for Packaging](#create-the-setuppy-for-packaging)
- [Create a tests/test_message.robot File](#create-a-testsmessagerobot-file)
- [Build the Package](#build-the-package)
- [Install the Package Locally](#install-the-package-locally)
- [Run the Robot Framework Tests](#run-the-robot-framework-tests)
- [Expected Output](#expected-output)
- [Troubleshooting](#troubleshooting)
- [Conclusion](#conclusion)

## Overview

This project defines a custom library for Robot Framework called Actions. It contains keywords for performing basic arithmetic operations such as addition and multiplication. These operations are implemented in Python, and the library is designed to be used directly within Robot Framework test cases.

## Features

- **Addition**: Adds two numbers together.
- **Multiplication**: Multiplies two numbers together.
- Supports string input conversion to integers before performing operations.

## Requirements

- Robot Framework version 3.2.2 or higher.
- Python 3.6 or higher.

## Installation

1. Clone or download the repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```sh
   pip install robotframework
   ```
3. Set up the library for testing:
   ```sh
   mkdir -p src/actions
   touch src/actions/__init__.py
   touch src/actions/math_operations.py
   ```

## Usage

Here is an example of how to use the Actions library in your Robot Framework test cases:

```robot
*** Settings ***
Library    actions.MathOperation

*** Test Cases ***
Test Add Numbers With String Inputs
    ${result}=    Add Numbers    "2"    "3"
    Should Be Equal As Numbers    ${result}    5

Test Multiply Numbers With String Inputs
    ${result}=    Multiply Numbers    "4"    "5"
    Should Be Equal As Numbers    ${result}     20
```

## Python Implementation of Library (Actions)

Create custom keyword file named like `math_operations.py` in the `src/actions` directory and the following sample code:

```python
from robot.api.deco import keyword

class MathOperation:

    @keyword
    def add_numbers(self, a, b):
        """
        Adds two numbers together.
        Converts inputs to integers before performing the addition.
        """
        a = int(a)
        b = int(b)
        return a + b

    @keyword
    def multiply_numbers(self, a, b):
        """
        Multiplies two numbers together.
        Converts inputs to integers before performing the multiplication.
        """
        a = int(a)
        b = int(b)
        return a * b
```

## Create the setup.py for Packaging

Create a `setup.py` file in the root directory with the following content:

```python
from setuptools import setup, find_packages

VERSION = "1.0.0"
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
    packages=find_packages("src"),
    package_dir={"actions": "src/actions"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: Robot Framework",
    ],
    python_requires=">=3.6",
)
```

## Create a tests/test_message.robot File

Create a `tests/test_message.robot` file with the following content:

```robot
*** Settings ***
Library    actions.MathOperation

*** Test Cases ***
Test Add Numbers With String Inputs
    ${result}=    Add Numbers    "2"    "3"
    Should Be Equal As Numbers    ${result}    5

Test Multiply Numbers With String Inputs
    ${result}=    Multiply Numbers    "4"    "5"
    Should Be Equal As Numbers    ${result}    20
```

## Build the Package

To build the Python package for distribution, run the following commands:

```sh
python setup.py sdist bdist_wheel
```

## Install the Package Locally

After building the package, install it locally using:

```sh
pip install dist/actions-1.0.0-py3-none-any.whl
```

## Run the Robot Framework Tests

To execute the test cases, run the following command:

```sh
robot tests/test_message.robot
```

## Expected Output

The test should pass, confirming that the addition and multiplication keywords work with string inputs converted to integers.

## Troubleshooting

If you encounter errors like ModuleNotFoundError, make sure that the library is properly installed and that your PYTHONPATH includes the directory where the library is located. You can verify this with:

```sh
echo $PYTHONPATH
```

Additionally, ensure that the correct version of Python is used:

```sh
python --version
```

## Conclusion

You’ve successfully created a custom Robot Framework library that includes keywords for basic arithmetic operations. The steps outlined here guide you from setting up the project structure to packaging, installing, and testing the library.

Let me know if you need any further assistance!
