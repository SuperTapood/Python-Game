import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

os.system(f'cmd /c "cd "{dir_path}""')

os.system(f'cmd /c "python setup.py build"')