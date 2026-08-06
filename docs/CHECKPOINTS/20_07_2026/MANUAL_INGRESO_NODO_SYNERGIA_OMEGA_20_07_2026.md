MANUAL DE INGRESO NODO SYNERGIA OMEGA
Recuperación desde MAQ1 / MAQ2 / MAQ3 / Nueva Máquina

Fecha: 20_07_2026
Baseline: SYNERGIA OMEGA NODE SYNC READY
Fase actual: FASE 6.13 MESSAGE BROKER ACEA
Branch: synergia_v3_core_restructure
Tag: SYNERGIA_OMEGA_NODE_SYNC_READY_20_07_2026

1. Arquitectura actual de nodos

SYNERGIA trabaja con nodos distribuidos.

MAQ1

Nodo:

MAQ1_HOME_NODE

Función:

Desarrollo
Experimentación
Pruebas locales
NotebookLM
Documentación
AI Lab
MAQ2

Nodo actual validado:

MAQ2_WORK_NODE

Función:

Nodo maestro de validación
Integración
Testing
Confirmación de módulos OMEGA

Estado:

FASE 6.13 COMPLETA
MAQ3

Nodo futuro:

MAQ3_NODE

Función:

Nodo adicional distribuido
Pruebas cluster
Comunicación entre nodos
2. Requisitos de una máquina nueva

Antes de instalar SYNERGIA:

Sistema operativo recomendado

Linux:

Linux Mint
Ubuntu 22.04 LTS
Ubuntu Server
Paquetes necesarios

Instalar:

sudo apt update

sudo apt install git python3 python3-pip python3-venv -y

Verificar:

python3 --version

git --version
3. Configurar acceso GitHub

Verificar SSH:

ssh -T git@github.com

Respuesta correcta:

Hi AgentArchitectDev! You've successfully authenticated

Si falla:

Crear clave:

ssh-keygen -t ed25519

Copiar:

cat ~/.ssh/id_ed25519.pub

Agregar en GitHub:

Settings
 ↓
SSH Keys
 ↓
New SSH Key
4. Descargar SYNERGIA desde cero

En la máquina nueva:

Ir al lugar donde estará el proyecto:

Ejemplo:

cd /mnt

Clonar:

git clone -b synergia_v3_core_restructure \
git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git

Entrar:

cd SYNERGIA_CORE_NEXT_PRO
5. Verificar versión recuperada

Ejecutar:

git status

Debe mostrar:

En la rama synergia_v3_core_restructure

Ver últimos commits:

git log --oneline -10

Debe aparecer:

b25909e3 feat: add Incident Manager ACEA and FASE 6.13 node cluster checkpoint
6. Verificar Tag de recuperación

Ejecutar:

git tag

Debe existir:

SYNERGIA_OMEGA_NODE_SYNC_READY_20_07_2026

Consultar:

git show SYNERGIA_OMEGA_NODE_SYNC_READY_20_07_2026

Debe apuntar:

commit b25909e3
7. Usar script automático de sincronización

El proyecto incluye:

sync_synergia_node.sh

Dar permisos:

chmod +x sync_synergia_node.sh

Ejecutar:

./sync_synergia_node.sh

Resultado esperado:

SYNERGIA NODE LISTO

Checkpoint esperado:
FASE 6.13 MESSAGE BROKER ACEA

Próximo:
FASE 6.14 CLUSTER COMMUNICATION MANAGER ACEA
8. Verificar módulos OMEGA

Directorio:

ls ai/node

Debe contener:

self_healing_manager.py

autonomous_repair_loop.py

recovery_engine.py

fault_detector.py

incident_manager.py

event_bus.py

message_broker.py
9. Validación Python

Ejemplo:

python3 -m py_compile ai/node/event_bus.py

Ejecutar:

python3 ai/node/event_bus.py

Debe finalizar:

EVENT BUS VALIDATED

Probar Message Broker:

python3 ai/node/message_broker.py

Debe mostrar:

MESSAGE BROKER STARTED
10. Crear entorno virtual

Recomendado:

python3 -m venv venv

Activar:

source venv/bin/activate

Instalar:

pip install -r requirements.txt
11. Continuar desarrollo

Nunca trabajar sobre main.

Confirmar:

git branch

Debe ser:

* synergia_v3_core_restructure

Antes de desarrollar:

git pull origin synergia_v3_core_restructure

Después:

git add .

Commit:

git commit -m "feat: nuevo modulo OMEGA"

Push:

git push origin synergia_v3_core_restructure
12. Estado actual SYNERGIA OMEGA

Checkpoint oficial:

SYNERGIA_OMEGA_NODE_SYNC_READY_20_07_2026

Commit:

b25909e3

Incluye:

FASE 6.7 Self Healing
FASE 6.8 Autonomous Repair Loop
FASE 6.9 Recovery Engine
FASE 6.10 Fault Detector
FASE 6.11 Incident Manager
FASE 6.12 Event Bus
FASE 6.13 Message Broker
13. Próxima evolución

Siguiente módulo:

FASE 6.14
CLUSTER COMMUNICATION MANAGER ACEA

Objetivo:

comunicación entre MAQ1
comunicación MAQ2
comunicación MAQ3
sincronización distribuida
heartbeat de nodos
estado global OMEGA
REGLA PRINCIPAL

Una máquina nueva nunca copia archivos manualmente.

Siempre:

GitHub
   ↓
clone
   ↓
branch synergia_v3_core_restructure
   ↓
sync_synergia_node.sh
   ↓
validación
   ↓
continuar desarrollo

GAB, este sería el documento "llave maestra" para que SYNERGIA pueda sobrevivir a cambio de máquina, perfil o nodo. Mañana solamente necesitás llevar este procedimiento y el acceso GitHub.


