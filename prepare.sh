#!/bin/bash

rm -rf env
virtualenv env
source env/bin/active
python setup.py install
