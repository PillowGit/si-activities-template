#!/bin/bash

pyinstaller --onefile runner.py
rm runner.spec
mv dist/runner .
rm -rf dist
rm -rf build
