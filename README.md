# 🔍 Escaner de Red Activa & Fingerprinting Pasivo

Un script ligero en Python diseñado para automatizar el mapeo de redes locales y deducir el sistema operativo de los dispositivos conectados mediante el análisis del TTL (Time To Live).

## 🚀 Caracteristicas
* **Ping Sweeper Automático:** Identifica rápidamente qué direcciones IP están vivas en un rango específico.
* **OS Fingerprinting:** Deduce si el dispositivo objetivo es Linux/Unix o Windows basándose en la respuesta ICMP (TTL).
* **Multiplataforma:** Ajusta automáticamente los comandos dependiendo de si se ejecuta desde Windows o Linux.

## 🛠️ Uso
1. Abre el archivo `Escaner_para_redes.py` 
2. Modifica la variable `red_base` con la subred que deseas escanear (ej. `192.168.1 <-coloca tu ip, el unico numero que cambiaria es el (1)`).
3. Ejecuta el script desde la terminal:
   
   python3 Escaner_para_redes.py

En este practica rapida yo le puse "20" por que solo quiero que analice los primeros 20 que tenemos aqui, pero conforme sean tus necesidades tu deberas de cambiar lo que necesites.
