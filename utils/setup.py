import os
# a setup.py file is required to make pip install work in editable mode
# https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
# https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install
# https://stackoverflow.com/questions/1471994/what-is-setup-py
# https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install
# so we create a setup.py file that will install the package in editable mode (this file)
# and a requirements.txt file that will install the dependencies (see requirements.txt)
os.system('rm -rf env') # remove the virtual environment if it exists already to refresh it with the new dependencies
# create a virtual environment
# python3 -m venv env
os.system('python3 -m venv env')
# activate the virtual environment
os.system('source env/bin/activate')
# install dependencies
os.system('pip install -r requirements.txt')
# install the package in editable mode
os.system('pip install -e .')
# the package is now installed in editable mode, which means that any changes to the source code will be immediately available the next time you import the package.