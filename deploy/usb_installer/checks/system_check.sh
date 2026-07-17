#!/bin/bash

echo "SYNERGIA SYSTEM CHECK"

echo "Linux:"
uname -a

echo ""

echo "Python:"
python3 --version

echo ""

echo "Git:"
git --version

echo ""

echo "RAM:"
free -h
