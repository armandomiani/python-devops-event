#!/bin/bash

PYTHON_BIN_PATH=`which python3`

export $PYTHONPATH=/usr/local/lib/python3.7

virtualenv -p $PYTHON_BIN_PATH env


# PYTHON 3 FOLDER = /usr/local/lib/python3.7
# PYTHON 2 FOLDER = /usr/lib6/python2.7

# PYTHON3
# export PYTHONHOME=/usr/local/lib/python3.7/ && export PYTHONPATH=/usr/local/lib/python3.7/

# PYTHON 2
# unset PYTHONHOME && unset PYTHONPATH

# export PYTHONPATH="/usr/lib64/python2.7; /usr/lib64/python2.7/site-packages"
# export PYTHONHOME=/usr/lib/python2.7  



