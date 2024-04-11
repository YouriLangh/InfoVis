# Setup process

Before running the project, run `pipenv install` to update all dependencies
for the project on your local machine. After this use `pipenv shell` to open
a virtual environment and run `python app.py` to activate the project.
Alternatively you can use `pipenv run python app.py` to run a file in the
virtual environment.

The CSV files are downloaded upon running `app.py` (or by calling
`fetch_datasets()` from the `src/data/fetch.py` module) should they
not be present yet. After the datasets are downloaded, you can run
the notebook to create the preprocessed and combined dataset.
The datasets can also be found here:

* [City of Los Angeles - Crime Data from 2010 to 2019](https://catalog.data.gov/dataset/crime-data-from-2010-to-2019)
* [City of Los Angeles - Crime Data from 2020 to Present](https://catalog.data.gov/dataset/crime-data-from-2020-to-present)

# Installing and uninstalling packages

Use `pipenv install <package-name>` or `pipenv uninstall <package-name>` to
manage the packages.

The `Pipfile` and `Pipfile.lock` are similar to the `package.json` and
`package-lock.json` of `npm` (JavaScript).

# Closing the environment

Run `exit` to exit the virtual environment.

Note: Switching the python interpreter to that of the virtual machine makes it
so the setup and closing of the environment happens seemlessly behind the
scenes.
