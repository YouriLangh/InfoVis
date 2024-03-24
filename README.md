
# Setup process
Before running the project, run **pipenv install** to update all dependencies for the project on your local machine.
After this use **pipenv shell** to open a virtual environment and run **python main.py** to activate the project.
Alternatively you can use **pipenv run python main.py** to run a file in the virtual environment.

None of the csv files are on github, first download both the 2010-2019 dataset and the 2020-present one. After doing this, you can run the notebook to create the preprocessed and combined dataset.

# Installing and uninstalling packages
Use **pipenv install "package-name"** or **pipenv uninstall "package-name"** to manage the packages.

The Pipfile and Pipfile.lock are similar to package.json in JavaScript.

# Closing the environment
Run **exit** to exit the virtual environment.


Note: Switching the python interpreter to that of the virtual machine makes it so the setup and closing of the environment happens seemlessly behind the scenes.

