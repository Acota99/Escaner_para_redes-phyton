import subprocess
import platform
import re

def obtener_os_por_ttl(ttl_str):
    try:
        ttl = int(ttl_str)
        # Clasificación basica por TTL
        if ttl <= 64:
            return "Linux/Unix/Mac"
        elif ttl <= 128:
            return "Windows"
        else:
            return "Router/Dispositivo de Red"
    except:
        return "Desconocido"

def Escaner_para_redes(ip_base, rango_inicio, rango_fin):
    print(f"[*] Iniciando escaneo avanzado en la red {ip_base}.{rango_inicio} hasta {ip_base}.{rango_fin}...\n")
    equipos_activos = []

    # Detectar tu sistema operativo para ajustar el comando de ping
    sistema_actual = platform.system().lower()
    parametro_ping = "-n" if sistema_actual == "windows" else "-c"

    for i in range(rango_inicio, rango_fin + 1):
        ip_objetivo = f"{ip_base}.{i}"
        comando = ["ping", parametro_ping, "1", ip_objetivo]
        
        try:
            # Ejecutamos el ping y capturamos el texto de la respuesta (capture_output=True)
            resultado = subprocess.run(comando, capture_output=True, text=True, timeout=2)
            
            # Si el ping fue exitoso (codigo 0, o sea, el equipo contestó)
            if resultado.returncode == 0:
                # Buscamos "TTL=" o "ttl=" y extraemos el numero usando expresiones regulares
                match = re.search(r"ttl=(\d+)", resultado.stdout, re.IGNORECASE)
                
                if match:
                    ttl_valor = match.group(1)
                    sistema_operativo = obtener_os_por_ttl(ttl_valor)
                    print(f"[+] {ip_objetivo} -> ACTIVO | Sistema deducido: {sistema_operativo} (TTL: {ttl_valor})")
                else:
                    print(f"[+] {ip_objetivo} -> ACTIVO | Sistema: Desconocido")
                
                equipos_activos.append(ip_objetivo)
        except subprocess.TimeoutExpired:
            pass # si la ip no contesta pasamos a la siguiente

    print("\n[*] Escaneo finalizado.")
    print(f"Total de equipos vivos: {len(equipos_activos)}")
    return equipos_activos

# --- Ejecución del script ---
if __name__ == "__main__":
    # Definimos la base de la red a escanear (ajústala según tu red local) "192.168.1.X" ES UN EJEMPLO
    red_base = "192.168.203" 
    
    # Escaneamos de la IP 1 a la 20 para la prueba rápida para no sobresturar nuestro sistema
    Escaner_para_redes(red_base, 1, 20)