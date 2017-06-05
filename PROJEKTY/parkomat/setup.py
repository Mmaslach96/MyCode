from cx_Freeze import setup, Executable
import cx_Freeze
import sys
import os


import os.path
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name='Parkomat',
      version='0.1',
      description='elo',
      options = {"build_exe": {"packages":["tkinter"]}},
      executables = {cx_Freeze.Executable("PROJEKT.PY", base=base)})