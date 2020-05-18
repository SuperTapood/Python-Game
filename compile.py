import os

# get this file's (__file__) path to get to setup.py
dir_path = os.path.dirname(os.path.realpath(__file__))

# open the command prompt and change its directory to my directory
os.system(f'cmd /c "cd "{dir_path}""')

# run setup.py and pass the argument 'build'
os.system(f'cmd /c "python setup.py build"')