#!/bin/bash

cd /mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO

export PYTHONPATH=.

gnome-terminal -- bash -c "python3 ai/run.py; exec bash"
