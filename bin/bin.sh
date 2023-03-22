#!/bin/bash

export PYTHONPATH=$(dirname $(dirname $(realpath $0)))
chmod +x $PYTHONPATH/bin/cli.py
export PATH=$PATH:$PYTHONPATH/bin