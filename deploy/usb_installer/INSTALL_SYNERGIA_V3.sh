#!/bin/bash

set -e

echo "=========================================="
echo " SYNERGIA CORE NEXT PRO V3 USB INSTALLER "
echo " RELEASE 17_07_2026"
echo "=========================================="

INSTALL_DIR="$HOME/SYNERGIA"

REPO_SSH="git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git"
REPO_HTTPS="https://github.com/AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git"

TAG="SYNERGIA_CORE_NEXT_PRO_V3_RELEASE_17_07_2026"


echo "[1] Detectando sistema"

if [ -f /etc/os-release ]; then
    cat /etc/os-release | grep PRETTY_NAME
fi


echo "[2] Verificando Git"

if ! command -v git >/dev/null
then
    sudo apt update
    sudo apt install git -y
fi


echo "[3] Verificando Python"

if ! command -v python3 >/dev/null
then
    sudo apt install python3 python3-venv python3-pip -y
fi


echo "[4] Preparando carpeta"

mkdir -p $INSTALL_DIR

cd $INSTALL_DIR


echo "[5] Seleccionando método Git"

if [ -d ~/.ssh ]
then
    REPO=$REPO_SSH
else
    REPO=$REPO_HTTPS
fi


echo "Repositorio:"
echo $REPO


echo "[6] Descargando SYNERGIA"


if [ ! -d SYNERGIA_CORE_NEXT_PRO ]
then

git clone $REPO

fi


cd SYNERGIA_CORE_NEXT_PRO


echo "[7] Cambiando a Release"


git checkout $TAG


echo "[8] Creando entorno"


python3 -m venv .venv

source .venv/bin/activate


echo "[9] Instalando dependencias"


pip install --upgrade pip


if [ -f requirements.txt ]
then
pip install -r requirements.txt
fi


echo ""
echo "================================"
echo " SYNERGIA INSTALADO CORRECTAMENTE"
echo "================================"

echo ""
echo "Inicio:"
echo ""
echo "cd ~/SYNERGIA/SYNERGIA_CORE_NEXT_PRO"
echo "source .venv/bin/activate"
echo "uvicorn backend.api.app:app --reload"
