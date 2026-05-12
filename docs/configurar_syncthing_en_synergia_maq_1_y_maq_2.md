# 🧠 Configuración y Uso de Syncthing en SYNERGIA (MAQ1 / MAQ2)

Este documento explica cómo configurar Syncthing para sincronizar el ecosistema SYNERGIA_CORE_NEXT_PRO entre dos máquinas:

- **MAQ1 (CASA)** → entorno de desarrollo, laboratorio y experimentación
- **MAQ2 (TRABAJO)** → entorno productivo y estable

El objetivo es lograr sincronización automática en tiempo real de archivos, proyectos y documentación.

---

# 1. ¿Qué es Syncthing en SYNERGIA?

Syncthing es el sistema de sincronización descentralizado que permite que ambas máquinas compartan carpetas sin nube externa.

Dentro de SYNERGIA funciona como:

- 🔄 Motor de sincronización MAQ1 ↔ MAQ2
- 🧠 Canal de continuidad del sistema
- 💾 Backup vivo del ecosistema

---

# 2. Instalación en Linux (Ubuntu / Mint / Debian)

## Instalar Syncthing

```bash
sudo apt update
sudo apt install syncthing -y
```

## Iniciar Syncthing

```bash
syncthing
```

O en segundo plano:

```bash
nohup syncthing &
```

---

# 3. Acceso a la interfaz

Abrir en el navegador:

```
http://localhost:8384
```

---

# 4. Configuración MAQ1 (CASA)

## Paso 1 — Agregar carpeta principal

En Syncthing:

- Click: **Agregar carpeta**

### ID sugerido:
```
SYNERGIA_CORE_NEXT
```

### Ruta recomendada:
```
/home/usuario/Escritorio/DISCO_TRABAJO/SYNERGIA_CORE_NEXT_PRO
```

(o solo docs si querés más liviano)

```
.../SYNERGIA_CORE_NEXT_PRO/docs
```

---

## Paso 2 — Compartir carpeta

- Ir a pestaña **Compartir**
- Seleccionar dispositivo MAQ2 (cuando esté agregado)

---

# 5. Configuración MAQ2 (TRABAJO)

Repetir el mismo proceso:

## Paso 1

- Instalar Syncthing
- Abrir interfaz

## Paso 2

Cuando MAQ1 envíe la carpeta:

- Aceptar solicitud
- Definir ruta local:

```
/home/usuario/Escritorio/SYNERGIA_CORE_NEXT_PRO
```

---

# 6. Vincular MAQ1 ↔ MAQ2

## Agregar dispositivos

Cada máquina tiene un ID único.

- En MAQ1: agregar ID de MAQ2
- En MAQ2: agregar ID de MAQ1

Confirmar ambos lados.

---

# 7. Estructura recomendada de sincronización

No sincronizar todo siempre. Mejor dividir:

## Opción PRO

### Carpeta 1
```
/docs → documentación e IA
```

### Carpeta 2
```
/core → sistema operativo SYNERGIA
```

### Carpeta 3
```
/projects → clientes y SaaS
```

---

# 8. Cómo saber si está funcionando

✔ Estado: “Actualizado”
✔ Sin errores de “Out of Sync”
✔ Velocidad de subida/bajada activa
✔ Archivos aparecen en ambas máquinas

---

# 9. Flujo real del sistema SYNERGIA

```
MAQ1 (CASA) → desarrollo / IA / pruebas
        ↓
     Syncthing
        ↓
MAQ2 (TRABAJO) → producción / estabilidad / deploy
```

---

# 10. Recomendaciones importantes

- No editar el mismo archivo en ambas máquinas al mismo tiempo
- Dejar Syncthing siempre activo
- Usar MAQ1 para experimentar
- Usar MAQ2 para versión final

---

# 11. Resultado final

Con esta configuración SYNERGIA se convierte en:

🧠 Un sistema distribuido en dos entornos sincronizados
🔄 Un cerebro dual MAQ1 / MAQ2
💾 Un sistema vivo de desarrollo continuo

