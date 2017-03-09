# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  VPython

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Programación 3D para Mortales Ordinarios

![N|Solid](https://6aeea8a9-a-62cb3a1a-s-sites.googlegroups.com/site/archelangelo/teaching/tipsonwritingvpythonsimulatingprograms/solar-system.jpg?attachauth=ANoY7crT82eCMtZEbdhrjRF_UNQKNHmybkWAmxCP5kKYnP0yWa_aTlE0D18FX94OZh2OkSncr3zsk8lbYet9pklNjxG-f-evjETSxhgDw0Mz2CYUldmxChHYxUEKSGghaxujFJ3PI_4491lL-Xh2VvnjlcHLZ9C7CCLmzIxvKp4exz4heaGnCyRbJOvvCRlNFkqChxGlZsdL7acr3pRvkPA_aNf2VgW6_b02ZZtSsG4W3x6zRCz6Ubl9S07xziN2SBo4GP3q1Of2I_RhwuGR06s3Te_wUhzN_w%3D%3D&attredirects=0)

VPython hace sencilla crear vistas y animaciones 3D navegables, incluso para aquellos con limitada experiencia en programación. Debido a que está basado en Python, puede además ofrecer mucho para programadores experimentados e investigadores.

## Guía de instalación y uso de VPython
### Windows: http://vpython.org/contents/download_windows.html

Seguir los pasos e instalar todo.

### Linux: http://vpython.org/contents/download_linux.html

#### Descargar wine 

```sh
$ sudo add-apt-repository -y ppa:ubuntu-wine/ppa
$ sudo apt-get update
$ sudo apt-get install wine1.8 winetricks
```
Fuente descarga Wine: http://www.kacharreando.com/ubuntu/wine-ubuntu-16-04/

#### Descargar Python, librería y VPython
Para Linux 32-bit:
   Descargar [32-bit Python-2.7.9](http://www.python.org/ftp/python/2.7.9/python-2.7.9.msi) de python.org
   Descargar la librería para Windows 32-bit [python27.dll](http://vpython.org/contents/download/dll32/python27.dll)
   Descargar [VPython-Win-32-Py2.7-6.11](http://sourceforge.net/projects/vpythonwx/files/6.11-release/VPython-Win-32-Py2.7-6.11.exe/download)
	  Esta version de VPython requiere Python 2.7.x de python.org.
Para Linux 64-bit:
   Descargar [64-bit Python-2.7.9](http://python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi) from python.org
   Descargar la librería de Windows 64-bit [python27.dll](http://vpython.org/contents/download/dll64/python27.dll)
   Descargar [VPython-Win-64-Py2.7-6.11](http://sourceforge.net/projects/vpythonwx/files/6.11-release/VPython-Win-64-Py2.7-6.11.exe/download)
	  Esta version de VPython requiere Python 2.7.x de python.org.

Cómo saber si mi arquitectura de Linux es 32 o 64 bit?
Ejecutar en consola:
```sh
cat /etc/issue
```

#### Ejecutar Python con Wine:

Copiar librería de windows pyhton.dll a /home/user/.wine/drive_c/windows/system32
```sh
$ cp ~/Download/python27.dll /home/user/.wine/drive_c/windows/system32
$ cd ~/Downloads
$ wine msiexec /i python-2.7.9.amd64.msi /qn TARGETDIR=C:\python27 ALLUSERS=1
```

Ejecutar Configuraciones de Wine:

![wine_configuration_panel](http://i.imgur.com/W7YCahZ.png)

Añadir aplicación -> python27

![file_selection_dialog](http://i.imgur.com/HPlsRnn.png)

Agregamos python.exe

![select_python.exe file](http://i.imgur.com/fd12Ub5.png)

En este punto ya es posible ejecutrar python2.7 con wine desde una terminal Linux de la siguiente manera:

```sh
$ wine ~/.wine/drive_c/Python27/python
```

![executing python with wine](http://i.imgur.com/c7X4ueg.png)

#### Instalar VPython

```sh
$ wine VPython-Win-64-Py2.7-6.11.exe
```

![installing vpython in wine](http://i.imgur.com/ACT1HoP.png)

Una vez instalado ejecutar VIDLE for Python y cargar algún ejemplo en File -> Open
Ejecutar el código cargado en Run->Run Module

![vpython bounce.py code example](http://i.imgur.com/xTN9gGO.png)

#### Mover la Escena

Click derecho y mover el mouse para mover la escena
Click del medio y mover el mouse arriba y abajo para zoom

![vpython bounce1 scene](http://i.imgur.com/8YZ6Gpi.png)

