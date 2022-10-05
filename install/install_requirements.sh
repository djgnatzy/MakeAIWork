#!/usr/bin/env bash

# # Activate virtual environment env
# source env/bin/activate

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     machine="Linux";;
    Darwin*)    
      machine="Mac"
      brew update && brew install freeglut
      export LIBGL_ALLOW_SOFTWARE=1
      ;;
    CYGWIN*)    machine="Cygwin";;
    MINGW*)     machine="Git Bash";;
    *)          machine="UNKNOWN:${os}"
esac

# Install all required libraries t
function install_with_pip {
  # Upgrade pip
  python -m pip install --upgrade pip

  # Install setuptools
  python -m pip install setuptools
  python -m pip install --no-cache-dir -r install/pip/requirements.txt

}

install_with_pip 