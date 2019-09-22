PARTE 1: 

 

Cree un proyecto denominado LaboratorioFunciones (recuerde que algunas herramientas no crean proyectos, por lo que deberá crear una carpeta con el nombre LaboratorioFunciones en donde guardará los archivos de manera local). 

Inicialice un repositorio Git local en el proyecto creado en su computador. 

Cree un Repositorio en GitHub llamado LaboratorioFuncionesRemoto. 

En el proyecto local, cree archivo llamado instrucciones.txt, en donde guarde cada uno de los numerales de esta lista. 

 

PARTE 2: 

 

Resuelva los siguientes puntos: 

Crear una función llamada “a_power_b” que imprima el resultado de elevar un número a en b (es decir ab) SIN utilizar la librería math NI la operación ** de python. Hacer un algoritmo que permite leer tanto el número a como el número b mediante el teclado y calcule ab llamando la función creada “a_power_b”. Realice un commit y push al repositorio con los cambios. Recuerde que los valores se deben leer POR FUERA de la función. 

Modifique el algoritmo para seguir calculando tantas potencias como se desee, deteniéndose cuando se digite que a=0. Realice un commit y push al repositorio con los cambios. 

Modifique el algoritmo agregando manejo de errores (try) para controlar los casos en donde se digite una letra en lugar de un número o que la potencia sea demasiado grande y desborde la memoria asignada. Realice un commit y push al repositorio con los cambios. 

Finalmente agregue un contador que permita saber cuántas veces se calcularon potencias, indicando cuántas veces el resultado fue par o fue impar o cuántas veces se presentó un error. Realice un commit y push al repositorio con los cambios. 

 

PARTE 3: 

 

Realizar una función “is_prime” que permita saber si un número es o no primo, mediante un mensaje “Is a prime number” o “Is NOT a prime number”. Hacer un algoritmo que permite leer un número “n” mediante el teclado y determine si es un número primo o no. Recuerde que los valores se deben leer POR FUERA de la función. 

Modifique el algoritmo de manera tal que ya no imprima mensajes, sino que retorne 0 si no es primo, 1 si es primo o -1 si no se puede determinar o hubo error. Ahora permita que se pueda leer cualquier cantidad de números y determinar si son números primos, el algoritmo dejará de leer números cuando se digite un número menor o igual a cero. Realice un commit y push al repositorio con los cambios. 

Finalmente modifique el algoritmo de manera que permita saber cuántas veces se calcularon primos e indique si es cantidad de veces es también primo. 

 

PARTE 4: 

Realizar una función “perfect_number” que permita saber si un número es perfecto. Un número perfecto es un número cuyos divisores (exceptuando el mismo número obviamente) suman el mismo número. Por ejemplo:  

 

6 es perfecto porque sus divisores 1+2+3 = 6 

 

Modifique la función para que ahora calcule un número “casi perfecto”, el cual es un número en el que la suma de sus divisores máximo tiene 3 de diferencia con el número.  

 

20 es casi perfecto porque sus divisores 1+2+4+5+10 suman 22, que es sólo 2 más que el 20. 