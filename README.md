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

## Usage

Here is an example of how to use the Actions library in your Robot Framework test cases:

```robot
*** Settings ***
Library    actions.MathOperation

*** Test Cases ***
Test Add Numbers With String Inputs
    ${result}=    Add Numbers    "2"    "3"
    Should Be Equal As Numbers    ${result}    5
```
