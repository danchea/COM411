def cwd():
    import os
    path = os.getcwd()
    print(f"the current working directory is:\n{path}")
    for file in os.listdir(path):
        print("The directory contains the following files:\n", file)

cwd()