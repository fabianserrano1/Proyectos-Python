import time
import random
import webbrowser

def leer_urls_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        urls = archivo.readlines()
    urls = [url.strip() for url in urls if url.strip()]
    return urls

def configurar_alarma(hora, minuto):
    while True:
        hora_actual = time.localtime()
        if hora_actual.tm_hour == hora and hora_actual.tm_min == minuto:
            print("¡Es la hora de la alarma!")  # Depuración
            return
        time.sleep(10)  # Esperar 10 segundos antes de verificar de nuevo

def reproducir_video(url):
    print(f"Abriendo URL: {url}")  # Depuración
    webbrowser.open(url)

def mostrar_tiempo_restante(hora, minuto):
    while True:
        hora_actual = time.localtime()
        horas_restantes = hora - hora_actual.tm_hour
        minutos_restantes = minuto - hora_actual.tm_min
        if minutos_restantes < 0:
            horas_restantes -= 1
            minutos_restantes += 60
        if horas_restantes < 0:
            horas_restantes += 24
        print(f"Tiempo restante para la alarma: {horas_restantes:02d}:{minutos_restantes:02d}")
        time.sleep(60)  # Actualizar cada minuto

def main():
    nombre_archivo = r'C:\Users\fabia\Desktop\Conquer Blocks\Python\Python avanzado\Proyectos a desarrollar para portofolio\Reloj Despertador\urls.txt'
    urls = leer_urls_archivo(nombre_archivo)

    if not urls:
        print("El archivo no contiene URLs.")
        return

    print("Configurando la alarma...")
    hora = int(input("Ingresa la hora para la alarma (0-23): "))
    minuto = int(input("Ingresa el minuto para la alarma (0-59): "))
    
    print(f"Alarma programada para las {hora:02d}:{minuto:02d}.")
    
    # Opción para mostrar el tiempo restante
    mostrar_tiempo = input("¿Quieres ver el tiempo restante hasta la alarma? (s/n): ").strip().lower()
    if mostrar_tiempo == 's':
        from threading import Thread
        thread = Thread(target=mostrar_tiempo_restante, args=(hora, minuto))
        thread.daemon = True
        thread.start()
    
    configurar_alarma(hora, minuto)
    
    url_aleatoria = random.choice(urls)
    print(f"Reproduciendo video: {url_aleatoria}")
    reproducir_video(url_aleatoria)

if __name__ == '__main__':
    main()
