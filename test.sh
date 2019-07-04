#!/usr/bin/env bash

source ~/root/.bashrc

py_version=$1

echo "Testing with python version ${py_version}...."
pyenv global ${py_version}

echo "test: flake8..."
flake8 . --exclude venv

echo "Test for python version ${py_version}: done."
