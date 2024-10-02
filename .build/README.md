# Build Folder

If, for some reason, the runner executable breaks, you can build a new executable here using
the python file and pyinstaller on a unix system. 

### To do so, do the following:

1. Make any edits necessary to `runner.py`

2. Give builder.sh run permissions, if necessary (`chmod +x builder.sh`)

3. Create a virtual environment in the .build folder (`python3 -m venv venv`)

4. Activate the python virtual environment (`source venv/bin/activate`)

5. Install the necessary packages for the build (`pip install pyyaml && pip install pyinstaller`)

6. Run builder.sh while the venv is activate (`./builder.sh`)

7. Deactivate the python virtual environment (`deactivate`)

After doing this, if the pyinstaller build was successful, there should be a 
new version of the `runner` executable in the current folder. Move it to the
root of the repo so that it gets used by students.
