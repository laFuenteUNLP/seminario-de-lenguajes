# C

[![N|Solid](https://github.com/laFuenteUNLP/seminario-de-lenguajes/blob/master/c/img/c-logo.png)](https://github.com/laFuenteUNLP/seminario-de-lenguajes/blob/master/c/img/c-logo.png)

## Qué es C

C es un lenguaje de programación de propósito general que ofrece economía sintáctica, control de flujo y estructuras sencillas y un buen conjunto de operadores.

C es apreciado por la eficiencia del código que produce y es el lenguaje de programación más popular para crear software de sistemas, aunque también se utiliza para crear aplicaciones.

Se trata de un lenguaje de tipos de datos estáticos, débilmente tipificado, de medio nivel, ya que dispone de las estructuras típicas de los lenguajes de alto nivel pero, a su vez, dispone de construcciones del lenguaje que permiten un control a muy bajo nivel. Los compiladores suelen ofrecer extensiones al lenguaje que posibilitan mezclar código en ensamblador con código C o acceder directamente a memoria o dispositivos periféricos.

## Donde y  para qué se puede usar C

- Sistemas Operativos: *hecho principalmente para la fluidez de programación en sistemas UNIX. Se usa también para el desarrollo de otros sistemas operativos como Windows o GNU/Linux. Igualmente para aplicaciones de escritorio como GIMP, cuyo principal lenguaje de programación es C.*

-  Aplicaciones Científicas: *para experimentos informáticos, físicos, químicos, matemáticos, entre otros, parte de ellos conocidos como modelos y simuladores.*

- Aplicaciones Industriales: *industria robótica, cibernética, sistemas de información y base de datos para la industria petrolera y petroquímica. Predominan también todo lo que se refiere a simulación de máquinas de manufactura.*

-  Simuladores de vuelo: *es la más delicada, ya que se tienen que usar demasiados recursos tanto de hardware como de software para desarrollar aplicaciones que permitan simular el vuelo real de una aeronave*

- Biblioteca: *Las bibliotecas más comunes son la biblioteca estándar de C y la biblioteca del estándar ANSI C, la cual provee las especificaciones de los estándares que son ampliamente compartidas entre bibliotecas. La biblioteca ANSI C estándar, incluye funciones para la entrada y salida de archivos, alojamiento de memoria y operaciones con datos comunes: funciones matemáticas, funciones de manejo de cadenas de texto y funciones de hora y fecha. Otras bibliotecas C son aquellas utilizadas para desarrollar sistemas Unix, las cuales proveen interfaces hacia el núcleo. Estas funciones son detalladas en varios estándares tales como POSIX y el Single UNIX Specification. Ya que muchos programas han sido escritos en el lenguaje C existe una gran variedad de bibliotecas disponibles. Muchas bibliotecas son escritas en C debido a que C genera código objeto rápido; los programadores luego generan interfaces a la biblioteca para que las rutinas puedan ser utilizadas desde lenguajes de mayor nivel, tales como Java, Perl y [Python](https://github.com/laFuenteUNLP/seminario-de-lenguajes/blob/master/python/python.md)*

- Vídeos Juegos: *muchos juegos clásicos (OTHELLO, AHORCADO, BUSCAMINAS, BATALLA NAVAL, CANION, etc) están hechos en éste lenguaje. Si bien hoy día existen lenguajes mucho más modernos para el desarrollo de vídeos juegos, gran parte de las librerías utilizadas por éstos, están en lenguaje C*.

- Multimedia: *se puede encontrar código C en grandes desarrollos de animaciones, modelados y escenas en 3D en películas y otras aplicaciones multimedia*

- Sistemas embebidos: *C es el lenguaje común para programar sistemas embebidos. El código ligero que un compilador C genera, combinado con la capacidad de acceso a capas del software cercanas al hardware son la causa de su popularidad en estas aplicaciones. Una característica donde C demuestra comodidad de uso particularmente valiosa en sistemas embebidos es la manipulación de bits* 

### Instalación

En linux:
Todas las distribuciones de Linux vienen por defecto con el compilador *gcc*.
Abrir una consola y escribir:
```sh
$ gcc -Wall codigo-fuente.c -o ejecutable.exe
```
###### Nota: *más adelante veremos para que sirven los parametros -Wall, -o*
En Windows descargar de la [http://www.tuxylinux.com/instalar-el-compilador-de-c-gcc-en-windows/) e instalar.


## Micro Tutorial de Python
---
####  Números

```
>>> 2+2
4
>>> (50-5*6)/4
5
>>> 216532163*8127321
1759826395525323
>>> 3*3.75/1.5
7.5
>>> (2+3j)*(8-4j)
(28+16j)
```
#### Cadenas
```
>>> 'Secuenciadecaracteres'
'Secuenciadecaracteres'
>>> "Hola"+"mundo"
'Holamundo'
>>> "Eco"*4
'EcoEcoEcoEco'
>>> saludo='Holamundo'
>>> saludo[0],saludo[-2]
('H','d')
>>> saludo[2:5]
'la'
```

### Listas
```
>>> a=[100,'huevos','sal']
>>> a
[100,'huevos','sal']
>>> a[0]
100
>>> a[-2:]
['huevos','sal']
>>> a+['oro',9]
[100,'huevos','sal','oro',9]
>>> a[0]="manteca"
>>> a
['manteca','huevos','sal']
```

### Conjuntos
```
>>> f=set("abracadabra")
>>> f
set(['a','r','b','c','d'])
>>> f&set(['a','e','i','o','u'])
set(['a'])
```

### Diccionarios
```
>>> dias={"Ene":31,"Jul":30}
>>> dias
{'Ene':31,'Jul':30}
>>> dias["Ene"]
31
>>> dias["Ago"]
>>> dias["Ago"]=31
>>> dias["Jul"]=31
>>> dias
{'Ago':31,'Ene':31,'Jul':31}
>>> "Mar"indias
False
>>> dias.keys()
['Ago','Ene','Jul']
>>> dias.values()
[31,31,31]
```
## Estructuras de Control
### Condicionales
```
>>> if <expression>:
... <suite>
elif <expression>:
... <suite>
else:
... <suite>
```
Una <expression> es algo que evalúa siempre a Verdadero o Falso.
Operadores lógicos: or,and,not.
Comparadores: <> == != inis.
Una <suite> es un bloque de código, de una o más líneas, delimitado por la sangría.

### while
```
while <expression>:
<suite>
```

### for
```
>>> bichos=["pulgas","piojos"]
>>> for bich in bichos:
... print "Mata-" + bich
...
Mata-pulgas
Mata-piojos
```
### List comprehensions
```
>>> vec=[3,7,12,0,3,-13,8]
>>> [x**2forxinvec]
[9,49,144,0,9,169,64]
>>> [x**2forxinvecifx<=7]
[9,49,0,9,169]
```

### Excepciones
```
>>> try:
...     5/0
... except ZeroDivisionError:
...     print “oops!”
oops!

try:
    <suite>
except [Excepcion1,...]:
    <suite>
finally:
    <suite>
else:
    <suite>
```

Si hay una excepción en la suite del try, se ejecuta la suite del except.
Si no hubo ninguna excepción, se ejecuta la suite del else. Y siempre se ejecuta la suite del finally.
```
>>> raiseValueError(“Ejemplo!”)
Traceback(mostrecentcalllast):
    File“<stdin>”,line1,in...
ValueError:Ejemplo!
```

### Funciones
```
>>> def alcuadrado(n):
... res=n**2
... returnres
...
>>> alcuadrado(3)
9
>>> def func(a,b=0,c=7):
... returna,b,c
...
>>> func(1)
(1,0,7)
>>> func(1,3)
(1,3,7)
>>> func(1,c=9)
(1,0,9)
>>> func(b=2,a=-3)
(-3,2,7)
```
### Clases
```
>>> import math

>>> classPosicion:
... def __init__(self,x,y):
... self.x=x
... self.y=y
... def distancia(self):
... x=self.x**2 + self.y**2
... return math.sqrt(x)
...
>>> p1=Posicion(3,4)
>>> p1.x
3
>>> p1.dist()
>>> p1.distancia()
>>> p1.distancia()
5.0
>>> p2=Posicion(7,9)
>>>
>>> p2.y
9
>>> p1.y
4
```

### Módulos

- Funciones, clases, y / o código suelto, todo es un archivo.
- Es un .py normal, sólo lo importamos y directamente lo usamos (Ej:import
math, math.sqrt(x))
- Fácil, rápido, ¡y funciona!

Armamos unos .py que contiene la clase definida arriba:

```
>>> importpos
>>> p=pos.Posicion(2,3)
>>> p.x
2
```

# El zen de Python

por Tim Peters

- Bello es mejor que feo.
- Explícito es mejor que implícito.
- Simple es mejor que complejo.
- Complejo es mejor que complicado.
- Plano es mejor que anidado.
- Disperso es mejor que denso.
- La legibilidad cuenta.
- Los casos especiales no son tan especiales como para quebrantar las reglas.
- Aunque lo práctico gana a la pureza.
- Los errores nunca deberían dejarse pasar silenciosamente.
- A menos que hayan sido silenciados explícitamente.
- Frente a la ambigüedad, rechaza la tentación de adivinar.
- Debería haber una ­y preferiblemente sólo una­ manera obvia de hacerlo.
- Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés.
- Ahora es mejor que nunca.
- Aunque nunca es a menudo mejor que ya mismo.
- Si la implementación es difícil de explicar, es una mala idea.
- Si la implementación es fácil de explicar, puede que sea una buena idea.
- Los espacios de nombres (namespaces) son una gran idea ¡Hagamos más de esas cosas!

**La Fuente - Coducción del CEFI**
