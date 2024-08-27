import time

def cronometro():
    minutos = 0
    segundos = 0

    try:
        while True:
            print(f"{minutos:02}:{segundos:02}")  # Formato mm:ss
            time.sleep(1)  # Espera 1 segundo
            segundos += 1

            if segundos == 60:  # Si los segundos llegan a 60, reinicia y suma un minuto
                segundos = 0
                minutos += 1

    except KeyboardInterrupt:
        print("\nCronómetro detenido.")

# Ejecutar el cronómetro
cronometro()
    
















