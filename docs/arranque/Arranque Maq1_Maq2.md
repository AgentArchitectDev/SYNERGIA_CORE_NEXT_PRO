Perfecto, esto es clave para que no se te rompa el sistema entre MAQ1 y MAQ2.

Te dejo el procedimiento correcto para actualizar MAQ1 desde cero cuando no lo usás hace tiempo.

🧠 ACTUALIZAR SYNERGIA EN MAQ1 (FULL RESET CONTROLADO)
🚀 1. ENTRAR AL PROYECTO
cd ~/SYNERGIA_CORE_NEXT_PRO

o donde lo tengas clonado en MAQ1.

🔄 2. TRAER ÚLTIMO ESTADO DE GITHUB
git fetch origin
🔁 3. SINCRONIZAR RAMA PRINCIPAL

(si trabajás en main o rama estable)

git checkout synergia_v3_core_restructure
git pull origin synergia_v3_core_restructure
⚠️ SI MAQ1 ESTÁ DESACTUALIZADA O ROTA

Podés forzar alineación total:

git reset --hard origin/synergia_v3_core_restructure
🧼 4. LIMPIAR ENTORNO PYTHON (IMPORTANTE)
deactivate

Luego:

rm -rf tools/venv
🧪 5. RECREAR VENV
python3 -m venv tools/venv
source tools/venv/bin/activate
📦 6. REINSTALAR DEPENDENCIAS

Si tenés requirements:

pip install -r requirements.txt

Si no tenés:

pip install streamlit ollama flask fastapi uvicorn

(ajustamos luego fino)

🧠 7. VERIFICAR SYNERGIA
python SYNERGIA_RUNTIME/synergia_boot.py

o el entry point:

streamlit run SYNERGIA_RUNTIME/visual_os_v2/visual_os_v2/app.py
🔥 FLUJO MAQ1 IDEAL (REGLA SIMPLE)

Cada vez que vuelvas:

git fetch
git reset --hard origin/synergia_v3_core_restructure
activar venv
run app
🧠 IMPORTANTE (ESTRUCTURA MAQ1 vs MAQ2)
MAQ1 = limpio / ejecución / pruebas
MAQ2 = desarrollo / caos / experimentación
🚀 SI QUIERES MEJORARLO MÁS

Te puedo armar después:

🔥 SYNC AUTOMÁTICO MAQ1 ↔ MAQ2
un solo comando
actualiza todo
reconstruye venv
levanta SYNERGIA solo

Si mañana arrancas en MAQ1 te lo dejo en modo:

👉 “un botón = sistema completo vivo”

Solo dime: “automatizar MAQ1”
