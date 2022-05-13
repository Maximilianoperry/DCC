# Tarea X: Nombre de la tarea :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Menú de Inicio (14pts) (14%)
##### ✅ Requisitos
##### ✅ Iniciar sesión
##### ✅ Ingresar como usuario anónimo
##### ✅ Registrar usuario
##### ✅ Salir
#### Flujo del programa (35pts) (35%) 
##### ✅ Menú Principal
##### ✅ Menú Publicaciones
##### ✅ Menú Publicaciones Realizadas
#### Entidades 15pts (15%)
##### ✅ Usuarios
##### ✅ Publicaciones
##### ✅ Comentarios
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos
#### General: 21 pts (21%)
##### ✅ Menús
##### 🟠 Parámetros
##### 🟠 Módulos
##### 🟠 PEP8
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```T0_MaximilianoPerryNazar.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```comentarios.csv``` en ```/Desktop/UC/Asignaturas/4 - Semestre [2021]/Programación Avanzada/Maximilianoperry-iic2233-2021-2/Tareas/T0```
2. ```publicaciones.csv``` en ```/Desktop/UC/Asignaturas/4 - Semestre [2021]/Programación Avanzada/Maximilianoperry-iic2233-2021-2/Tareas/T0```
3. ```usuarios.csv``` en ```/Desktop/UC/Asignaturas/4 - Semestre [2021]/Programación Avanzada/Maximilianoperry-iic2233-2021-2/Tareas/T0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```datetime()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Menus```: Contiene a ```Menu``` (imprime dos menús en específico)...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <No utilicé supuestos> 

PD: <El exceso de lineas de mi código se dió a causa de que de tal forma podía crear listas que contenían información útil, sin embargo, y a falta de mala organización del tiempo, no logré una forma de guardar estos códigos largos en un archivo aparte, de modo de poder utilizarlo en el código principal. Una consideración adicinal, es que aún no me manejo del todo bien con las ubicaciones de archvivos en GitHub (por si la ubicación dada de los archivos .csv es errónea otra opción de ubicación podría ser C: \windows\System32\WindowsPowerShell\v1.0\, lo comento porque tuve problemas con la apertura de archivos en vscode, pero en pycharm no, sin embargo finalmente probé el codigo en vscode y me funcionó, pero el problema podría seguir dándose). Por útlimo, subí los archivos .csv originales de modo que de esa forma sé que el código funciona (en caso de que exista cualquier inconveniente con ello).>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.delftstack.com/es/howto/python/how-to-get-the-current-time-in-python/>: este hace \<entrega la hora actual> y está implementado en el archivo <T0_MaximilianoPerryNazar.py> en las líneas <en 60 lineas distitnas> y hace <entrega la hora actual, de modo de poder ordenar las publicaciones>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
