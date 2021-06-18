## Description

Using Python Selenium 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install venv.

```bash
pip install virtualenv

python3 -m venv nameOfVirtualEnv
```

## Usage

Activating the virtual enviroment on Linux, in bash you need to be in the project folder where your venv folder is located

```bash

source nameOfVirtualEnv/bin/activate

```

Activating the virtual enviroment on Windows, in bash you need to be in the project folder where your venv folder is located

```bash

fullPath\nameOfVirtualEnv\Scripts\activate

```

## Installing the necessary requirements from requirements.txt

```bash

pip install -r requirements.txt

```

## Select Python Interpreter - use virtualenv Python 3.8.5 64-bit 'venv'

## SeleniumBase

After the installation of SeleniumBase, we need to download chromeDriver

```bash

sbase install chromedriver latest

```

Using seleniumBase to run tests

```bash

py.test folder/file.py --browser=nameOfTheBrowser(firefox,chrome,opera...)

```

In order for test running to be visible in Linux(headed and not headless - headless is default in Linux), it needs a following command
at the end of the line

```bash

--headed

```

