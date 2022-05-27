# Project Object-Oriented Programming

### Objective
To present the mainstream practices in object-oriented programming.

### Practices

    if __name__ == "__main__":
        do_something()

Everytime we run a python script, its name is stored at `__name__` and `__main__`. The difference is that a single python script may execute a second python script, and in this case, all the subsquent scripts will not be `__main__`. In practice, it means that all the code inside the `if` will not be used when the original script have been called by other scripts.