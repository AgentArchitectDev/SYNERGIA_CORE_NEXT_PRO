# SYNERGIA CORE NEXT PRO V3
# Universal USB Installer

Release:
SYNERGIA_CORE_NEXT_PRO_V3_RELEASE_17_07_2026


## Objetivo

Instalar SYNERGIA CORE NEXT PRO en cualquier máquina Linux.


## Requisitos

- Linux Mint / Ubuntu / Debian
- Python 3.12 recomendado
- Git
- conexión a internet


## Instalación

Copiar carpeta desde USB.

Ejecutar:

chmod +x INSTALL_SYNERGIA_V3.sh

./INSTALL_SYNERGIA_V3.sh


## Instalación manual

Clonar:

git clone git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git


Entrar:

cd SYNERGIA_CORE_NEXT_PRO


Cambiar release:

git checkout SYNERGIA_CORE_NEXT_PRO_V3_RELEASE_17_07_2026


Crear entorno:

python3 -m venv .venv


Activar:

source .venv/bin/activate


Instalar:

pip install -r requirements.txt


## Iniciar SYNERGIA

Backend:

uvicorn backend.api.app:app --reload


## Restaurar versión limpia

git checkout SYNERGIA_CORE_NEXT_PRO_V3_RELEASE_17_07_2026


## Notas

Nunca copiar .venv entre máquinas.

Cada máquina debe crear su propio entorno Python.
