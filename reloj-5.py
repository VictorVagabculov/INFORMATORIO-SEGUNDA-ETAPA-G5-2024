import datetime  
import time  
def iniciar_cronometro():  
    # Tiempo de preparación en minutos  
    tiempo_preparacion = 5  
    tiempo_servicio=0
    # Obtener la hora actual  
    hora_actual = datetime.datetime.now()  
    # Calcular el tiempo total (tiempo de servicio + tiempo de preparación)  
    tiempo_total = tiempo_servicio + tiempo_preparacion  
    # Sumar el tiempo total a la hora actual  
    hora_final = hora_actual + datetime.timedelta(minutes=tiempo_total)   
    print(f"Hora actual: {hora_actual.strftime}")  
    print(f"Tiempo de servicio: {tiempo_servicio} minutos")  
    print(f"Hora final (después de {tiempo_total} minutos): {hora_final.strftime}")  
# Simulación del cronómetro  
    print("Iniciando cronómetro...")  
    for i in range(tiempo_preparacion * 60, 0, -1):  
        mins, secs = divmod(i, 60)  
        timer = '{:02d}:{:02d}'.format(mins, secs)  
        print(timer, end="\r")  
        time.sleep(1)  
    print("¡Cronómetro finalizado!")
#Codigo de Noemi 
iniciar_cronometro()
