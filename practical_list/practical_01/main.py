import os
import sys

if (sys.version_info.major >= 3):
    os.system('python3 my_prog-py3.py')
    sys.exit(0)
else:
    # assuming 'python' points to python v2.7 on your system
    os.system('python my_prog-py2.py')
    sys.exit(0)
