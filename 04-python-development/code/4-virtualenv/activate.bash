# 1
pip install virtualenv

# 2
##  To use default python version:
virtualenv .venv

##  To use a different python version, on Windows:
gcm python      # To locate the python executable
virtualenv .venv310 --python=C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
##  To use a different python version, on Linux:
which python    # To locate the python executable
virtualenv .venv310 --python=...   # Fill in the right version

# 3
## To activate the environment, in Windows power shell:
# .venv\Scripts\activate
.venv\Scripts\activate.ps1
## To activate the environment, in Linux
source .venv/bin/activate

# 4
## To check that the virtual environment is installed:
python --version
pip list 

# 5 
### To install your library, go to its main folder and say:
pip install -e .
### To install required packages (otherwise the wrong pytest will be used):
pip install pytest

# 6
## To go back to the global environment:
deactivate
