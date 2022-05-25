# Creating a simple project in a virtual environment and deploying with Docker

## Virtual Environment

Before exploring Docker, let's prepare the setup.

The first step is to create a virtual environment:

    python -m venv /path/to/new/virtual/environment

And the second is to activate it:

    `./path/to/new/virtual/environment/Scripts/activate.bat`

obs1: this code works in Windows. For more information about Linux build, check the documentarion: https://docs.python.org/pt-br/dev/library/venv.html

In case you are facing errors during the activation, it may be needed to redefine the user execution policy in Windows:

    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

The final step is to make sure python don't recognizes your previouslly installed libraries:

    `pip freeze`

If it return a black or a message saying that are no libraries, you are good to go. Otherwise, it will be necessary to investigate furthermore.
 

