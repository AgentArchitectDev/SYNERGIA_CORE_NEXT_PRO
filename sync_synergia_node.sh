#!/bin/bash

echo "=============================================="
echo " SYNERGIA OMEGA NODE SYNC"
echo " Preparando nodo de trabajo"
echo "=============================================="

PROJECT="SYNERGIA_CORE_NEXT_PRO"
BRANCH="synergia_v3_core_restructure"
REPO="git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git"

echo ""
echo "[1] Verificando entorno..."

if ! command -v git >/dev/null 2>&1
then
    echo "ERROR: Git no instalado"
    exit 1
fi


echo ""
echo "[2] Buscando proyecto..."

if [ -d "$PROJECT" ]
then

    echo "Proyecto encontrado"

    cd "$PROJECT" || exit

    echo ""
    echo "[3] Cambiando a rama SYNERGIA..."

    git checkout $BRANCH

    echo ""
    echo "[4] Actualizando desde GitHub..."

    git pull origin $BRANCH


else

    echo "Proyecto no encontrado"
    echo "Clonando SYNERGIA_CORE_NEXT_PRO..."

    git clone -b $BRANCH $REPO

    cd $PROJECT || exit

fi


echo ""
echo "[5] Verificando estado..."

git status


echo ""
echo "[6] Últimos commits..."

git log --oneline --decorate -10


echo ""
echo "[7] Tags OMEGA..."

git tag | tail -10


echo ""
echo "=============================================="
echo " SYNERGIA NODE LISTO"
echo ""
echo "Checkpoint esperado:"
echo "FASE 6.13 MESSAGE BROKER ACEA"
echo ""
echo "Próximo:"
echo "FASE 6.14 CLUSTER COMMUNICATION MANAGER ACEA"
echo "=============================================="
