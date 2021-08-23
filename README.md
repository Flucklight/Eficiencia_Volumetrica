#Eficiencia Volumetrica

Es un algoritmo para verificar la eficiencia volumetrica del protocolo TCP/IP
en el cual verifica que tan eficiente es el protocolo con cierta cantidad de bytes
de un mensaje, en el programa se ejecuta una simulacion de mensajes desde 1 a 5000 bytes
en el cual el programa desplegara una grafica de los resultados y mostrara los datos obtenidos
en la terminal.

Algo importante a destacar es que la grafica muestra una serie de picos en caida en puntos 
especificos, al estudiarlos notamos que son en los puntos de 1025, 2049, 3073 y 4097; esto 
se produce por la fragmentacion del mensaje en la capa de transporte en el protocolo TCP
ya que al fragmentar estos mensajes generan un paquete de un solo byte de informacion el
cual hace decaer la eficiencia del protocolo en esos mensajes.
