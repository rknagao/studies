# Creating a simple project in a virtual environment and deploying it with Docker

## Virtual Environment

Before exploring Docker, let's prepare the setup.

**Step 1:** create a virtual environment.

    python -m venv /path/to/new/virtual/environment

**Step 2:** activate it.

    ./path/to/new/virtual/environment/Scripts/activate

> obs: this code works in Windows POwerShell. For more information about Linux build, check the oficial documentation: https://docs.python.org/pt-br/dev/library/venv.html. In case you are facing errors during the activation, it may be needed to redefine the user execution policy in Windows: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` 

**Step 3:** activate pip.

    python -m pip install --upgrade pip

**Step 4:** make sure python don't recognizes your previously installed libraries.

    pip freeze

You are good to go if none returned, otherwise, keep investigating. 
 
## Docker

After making sure the code works, we proceed with using docker to create a container. It means our code will be able to be executed smoothly from OS with different configurations.

**Step 1:** install docker using https://docs.docker.com/desktop/

**Step 2:** create dockerfile

    FROM python:3.8

    WORKDIR project_deploying_with_docker

    COPY  requirements.txt .

    RUN pip install -r requirements.txt

    COPY . .

    WORKDIR src

    CMD python main.py

**Step 3:** create an image of the container

    docker build . -t [choose_a_name]


**Step 4:** run the image on Docker Desktop and you'll see the container working