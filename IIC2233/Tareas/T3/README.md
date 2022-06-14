# Tarea 3: DCCalamar :school_satchel:

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<El programa funciona con cierta normalidad, pero no pasa de la sala de juegos, ya que no se alcanza a modelar correctamente el ganador de una ronda y eso evita que se siga trabajando en el resto del código. En cliente.py y servidor.py hay lineas comentadas que ayudan a visualizar la información que se envía que podrían ser útiles para la correción.>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 23 pts (18%)
##### ✅ Protocolo <Se hace uso de TCP - IP\>
##### ✅ Correcto uso de sockets <la información entre los clientes y el servidor se realiza únicamente a través de este medio\>
##### ✅ Conexión <Hasta donde se alcnanza a llegar (sala de juego) todos los mensajes se realizan de manera correcta\>
##### ✅ Manejo de clientes <Se pueden conectar múltiples clientes sin afectar al programa y cuando se llega a un máximo (4) se informa que no se pueden recepcionar más\>
#### Arquitectura Cliente - Servidor: 31 pts (24%)
##### ✅ Roles <Se separa al cliente del servidor y cada uno realiza las funciones correspondientes según enunciado\>
##### 🟠 Consistencia <La información se mantiene coordinada, pero no durante la sala de juego y siendo esta la parte más importante del programa, entonces sería erróneo afirmar que hay total consistencia\>
##### ✅ Logs <Se implementan logs cuando es necesario\>
#### Manejo de Bytes: 20 pts (15%)
##### 🟠 Codificación <La codificación pedida se realiza, pero no se separa en bloques\>
##### 🟠 Decodificación <mismo error que en Coficiación\>
##### ✅ Encriptación <Se realiza lo solicitado\>
##### ✅ Integración <Se utiliza el protocolo\>
#### Interfaz gráfica: 31 pts (24%)
##### 🟠 Modelación <Solo existe front-end\>
##### ✅ Ventana inicio <Cumple lo pedido\>
##### 🟠 Sala Principal <Cumple todo lo pedido, pero un usuario si puede ser retado en momentos que no debería poderse\>
##### ✅ Ventana de Invitación <Cumple lo pedido\>
##### 🟠 Sala de juego <Se crea la interfaz, pero no se actualiza cuando debería\>
##### ❌ Ventana final <No se llega a esta ventana\>
#### Reglas de DCCalamar: 21 pts (16%)
##### ✅ Inicio del juego <Se cumple\>
##### 🟠 Ronda <se avanza para calcular un ganador, pero la información nunca le llega a los clientes, por lo que mayormente no se cumplen los requerimiento de la ronda\>
##### ❌ Termino del juego <No se llega a esto\>
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) <Se cumple lo pedido\>
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode <No se realiza\>
##### ❌ Turnos con tiempo <No se realiza\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar depende de si se ejecuta el cliente o el servidor. El módulo principal de cliente es ```main.py``` en el directorio ```cliente```, mientras que, el módulo prinicpal del servidor es ```main.py``` dentro del directorio ```servidor```.

Además se crea un archivo ```datos.csv``` que almacena información de los clientes dentro del directorio ```servidor```.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```sala_juego```: Contiene a ```SalaJuego``` hecha para <simular la sala de juego>
2. ```sala_principal```: Contiene a ```SalaPrincipal``` hecha para <simular la sala principal>
3. ```ventana_inicio```: Contiene a ```VentanaInicio``` hecha para <simular la ventana de inicio>
4. ```ventana_invitacion```: Contiene a ```VentanaInvitacion``` hecha para <simular las invitaciones>
5. ```ventana_rechazo```: Contiene a ```VentanaRechazo``` hecha para <simular cuando una invitacion es rechazada :(>
6. ```cliente```: Contiene a ```Cliente``` hecha para <simular las acciones de un cliente>
7. ```cliente/funciones```: Contiene una función hecha para <revisar si las fechas son válidas>
8. ```interfaz```: Contiene a ```Controlador``` hecho para <manejar la información proveniente de un socket en cliente.py hacia la interfaz>
9. ```servidor/funciones```: Contiene funciones hechas para <manejar los mensajes y-o clasificarlos>
10. ```servidor```: Contiene a ```servidor``` hecha para <simular las acciones del servidor>

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Todos los meses tienen 31 días y se justifica porque es una aproximación a la realidad que evita que se llene de excesivamente de código la función hecha para revisar ello/a> 
2. <Solo se puede comenzar a retar a jugadores una vez que se haya llenado la sala y se justifica porque de no ser así uno podría escoger un rival más difícil que otro, sin saber las otras posibilidades que podría tener/a>




## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://github.com/IIC2233/syllabus-2021-1/tree/main/Actividades/AF7>: este guió para crear al controlador y está implementado en el archivo <interfaz.py> en la funcion __init__ y crea un controlador que regula mensajes provenientes del servidor con las interfaces gráficas.

2. \<https://github.com/IIC2233/Syllabus/tree/main/Ayudant%C3%ADas/AY7.5>: este ayudó a crear al cliente y al servidor y está implementado en el archivo <cliente.py> y <servidor.py> en la recepción de mensajes y creación de los threads.
