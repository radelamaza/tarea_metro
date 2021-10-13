# Tarea Buda.com Metro

Código hecho en base a la Tarea Metro del proceso de postulación a buda.com

Para su funcionamiento se crea un archivo .json que describe la red de metro con la cual se quiere trabajar, la estructura de este json es la siguiente:

"lineas": se deberá poner en esta key una lista con listas de cada linea que pertenezca a la red, se considerará linea a las estaciones unidas entre sí, donde pueden iniciar y/o terminar en la intercepción con otra linea. Por lo que no podrá haber una linea con una conexión a otra en la mitad del recorrido.

"rojo": se pondrá en esta llave, una lista con las estaciones que sean de color rojo.

"verde": se pondrá en esta llave, una lista con las estaciones que sean de color verde.

Se pueden incluir más colores siguendo el mismo formato.

Por ejemplo, el archivo de red basado en el ejemplo de la tarea quedaría de la siguiente manera:

```
 { "lineas": [ ["A","B","C"], ["C","G","H","I","F"], ["C","D","E","F"] ], "rojo":[ "H" ], "verde":["G","I"] }
```

Para correr el programa se debe hacer desde la terminal con el siguiente código:

```
python main.py red.json A F rojo
```

Donde red.json es el archivo json que describe la red, A es la estación de inicio, F es la estación de llegada y rojo es el color del tipo de tren a tomar (opcional).

El programa entregará el resultado de la red más óptima printeando en consola "Mejor ruta: ["ruta optima"]"
