# SYNERGIA CORE NEXT PRO
# CLEAN V3 RELEASE NOTES
# 17_07_2026


## 1. Estado del Proyecto

SYNERGIA CORE NEXT PRO alcanzó un baseline limpio
después de una operación de saneamiento completo del repositorio Git.


## 2. Objetivo de la limpieza

Se realizó:

- Eliminación de credenciales expuestas.
- Eliminación de tokens GitHub históricos.
- Eliminación de archivos con secretos.
- Eliminación de entornos virtuales Python almacenados en Git.
- Actualización de .gitignore.
- Reescritura del historial Git mediante git filter-repo.


## 3. Seguridad

Validaciones realizadas:

```bash
git grep -n "ghp_"

Resultado:

Sin coincidencias.

Archivos eliminados del historial:

Github.md
gibhub.md
tools/venv
4. Estado Git Oficial

Rama principal de desarrollo:

synergia_v3_core_restructure

Commit base:

5b0df5db

Tag oficial:

SYNERGIA_CLEAN_V3_17_07_2026

Backup:

backup_CLEAN_V3_17_07_2026

5. Recuperación en cualquier máquina

Requisitos:

Linux recomendado
Git instalado
Python 3.12+
Ollama (si se utiliza IA local)
SSH configurado para GitHub
6. Clonar proyecto
git clone git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git

cd SYNERGIA_CORE_NEXT_PRO
7. Cambiar al estado limpio
git checkout synergia_v3_core_restructure

o directamente:

git checkout SYNERGIA_CLEAN_V3_17_07_2026
8. Configuración Python

Crear entorno:

python3 -m venv .venv

Activar:

source .venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt
9. Configuración IA local

Instalar Ollama.

Ver modelos:

ollama list

Ejemplo:

ollama run llama3.2:3b
10. Arranque SYNERGIA

Backend:

uvicorn backend.api.app:app --reload

Editor:

python -m http.server 8080
11. Estructura de trabajo

MAQ1:
Desarrollo principal

MAQ2:
Desarrollo secundario / backup

Nueva máquina:

Clonar repositorio.
Configurar SSH.
Crear entorno Python.
Instalar dependencias.
Recuperar modelos IA.
Ejecutar servicios.
12. Regla de checkpoints

Cada avance importante debe crear:

docs/CHECKPOINTS/DD_MM_YYYY/

Ejemplo:

17_07_2026

13. Estado actual

SYNERGIA CLEAN V3 BASELINE COMPLETED

Fecha:

17_07_2026

Autor:

GAB


Guardá:

`CTRL + O`

Enter

`CTRL + X`

---

## 2) Guardarlo en Git

Luego:

```bash
git add docs/CHECKPOINTS/17_07_2026/SYNERGIA_CLEAN_V3_RELEASE_NOTES_17_07_2026.md

Commit:

git commit -m "docs: add SYNERGIA CLEAN V3 release notes"

Push:

git push origin synergia_v3_core_restructure
Cómo usar SYNERGIA en MAQ1, MAQ2 o cualquier máquina

La idea correcta es que Git sea la fuente única.

Máquina nueva

Ejemplo MAQ2:

1) Instalar Git
sudo apt update
sudo apt install git
2) Configurar SSH GitHub

Crear llave:

ssh-keygen -t ed25519 -C "tu_email_github"

Mostrar clave:

cat ~/.ssh/id_ed25519.pub

Copiarla a:

GitHub → Settings → SSH and GPG keys → New SSH key

Probar:

ssh -T git@github.com

Debe responder algo como:

Hi AgentArchitectDev! You've successfully authenticated
3) Descargar SYNERGIA
git clone git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git

Entrar:

cd SYNERGIA_CORE_NEXT_PRO
4) Ir al baseline limpio

Para desarrollo:

git checkout synergia_v3_core_restructure

Para congelar versión:

git checkout SYNERGIA_CLEAN_V3_17_07_2026
5) Preparar Python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
6) Continuar desarrollo

MAQ1:

git pull

trabaja.

MAQ2:

git pull

recibe cambios.

La arquitectura queda así:

                 GitHub
                    |
        SYNERGIA_CORE_NEXT_PRO
                    |
        ----------------------
        |                    |
       MAQ1                 MAQ2
   desarrollo          desarrollo/backup
        |
        |
   checkpoints diarios

Con esto SYNERGIA deja de depender de una sola PC. Cualquier máquina puede reconstruir el sistema desde el repositorio limpio.
