# Aplicación de Recepción para Spa

## Descripción

Este proyecto es una aplicación de recepción para un spa, desarrollada como parte de la Etapa 2 del Informatorio, Grupo 5 de la comision 3. Utiliza **Python** junto con **Tkinter** para la interfaz gráfica, y permite gestionar los servicios que los clientes solicitan en el spa. 

## Características

- **Ingreso de datos del cliente**: Los recepcionistas pueden ingresar el nombre del cliente y asignarles un número de box.
- **Selección de servicios**: Los clientes pueden elegir entre una variedad de servicios principales como masajes, manicuras, pedicuras, entre otros.
- **Extras**: Además de los servicios principales, se pueden añadir extras como comida, bebida y masajeadores.
- **Temporizador**: La aplicación incluye un temporizador para llevar la cuenta del tiempo total del servicio, que se actualiza automáticamente y muestra la hora estimada de salida.
- **Reloj en tiempo real**: Se incluye un reloj en tiempo real para mostrar la hora actual.
- **Gestión de servicios**: Se pueden eliminar los servicios seleccionados, y una vez iniciado el servicio, se abre una ventana con la información del cliente, el tiempo de servicio y los servicios seleccionados.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/VictorVagabculov/INFORMATORIO-SEGUNDA-ETAPA-G5-2024

2. Instalar las dependencias necesarias. El proyecto utiliza Pillow para la manipulación de imágenes:

pip install Pillow

3. Ejecutar la aplicación:

python Recepcion_spa.py

Archivos principales

-Recepcion_spa.py: Archivo principal que contiene la lógica de la aplicación y la interfaz gráfica.
-servicios.py: Contiene diccionarios de con los servicios principales, clasificados por tipo y su duracion estimada.
-extras.py: Contiene las listas de los extras disponibles (comidas, bebidas, masajeadores).
-.gitignore: Define los archivos y directorios que se deben ignorar en el repositorio.

Uso


-Inicio: Al ejecutar la aplicación, aparecerá una ventana principal donde se podrá ingresar el nombre del cliente y el número de box.
-Selección de servicios: Se pueden seleccionar servicios desde los menús desplegables de "Servicios Principales" y "Extras".
-Iniciar servicio: Una vez seleccionados los servicios, se puede iniciar el servicio, lo que abrirá una nueva ventana con un temporizador y detalles del cliente.
-Temporizador: Se puede visualizar el tiempo restante del servicio y la hora estimada de salida.
-Fin de servicio: Al finalizar el temporizador de la nueva ventana se abrirá un popup avisando que el servicio finalizó.

Requisitos del sistema

-Python 3.x
-Módulo Pillow (para trabajar con imágenes)
