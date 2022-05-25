# Creating a simple project in a virtual environment and deploying it with Docker

## Virtual Environment

Before exploring Docker, let's prepare the setup.

**Step 1:** create a virtual environment:

    python -m venv /path/to/new/virtual/environment

**Step 2:** activate it:

    ./path/to/new/virtual/environment/Scripts/activate.bat

> obs: this code works in Windows. For more information about Linux build, check the oficial documentation: https://docs.python.org/pt-br/dev/library/venv.html. In case you are facing errors during the activation, it may be needed to redefine the user execution policy in Windows: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` 

**Step 3:** to activate pip:

    python -m pip install --upgrade pip

**Step 4:** make sure python don't recognizes your previously installed libraries:

    pip freeze

You are good to go if none returned, otherwise, keep investigating.
 

