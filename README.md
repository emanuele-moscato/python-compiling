# How Python compiles code automatically

Python is an interpreted language, meaning that an interpreter runs the code on-the-fly and no compiling is needed. Nevertheless, there are cases in which Python does compile code, or the user wants to have some code compiled.

As a rule,
```
Python compiles code for imported modules that are not installed system-wide.
```
For system-wide installed modules, the compiling is done once when installing, not every time the module is imported, while for other modules (e.g. the ones we might write ourselves and then import), compiling is done (almost) every time, which is reflected in the appearence of the `__pycache__/` directory after running the Python script that imports the module.

### Testing when code is compiled and when it isn't

The `compiling.py` script can be run with simple command line arguments that determine whether the module `utils.py` is imported or not. To have it imported, the first command line argument must be one among `utils`, `import` or `import_utils`, in all other cases the module is not imported.

Make sure that no `.__pycache__/` directory is present in the directory of the script (e.g. on Linux or MacOS, open the command line, navigate to the folder and execute `ls`). If it is present, on Linux and Mac you can delete it with `rm -rf __pycache__/`.

Run the script: you'll notice that if the module is imported then the directory is indeed created, and it will contain a binary file corresponding to the compiled version of the imported module.

### More info

- Using `sys.argv`: https://www.pythonforbeginners.com/system/python-sys-argv
- Compiling in Python: http://effbot.org/pyfaq/how-do-i-create-a-pyc-file.htm
