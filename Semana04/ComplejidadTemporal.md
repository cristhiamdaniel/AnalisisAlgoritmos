# Algoritmos y Análisis de Complejidad Temporal

## Definición y Características de un Algoritmo

Consideremos las siguientes definiciones *informales* de Algoritmo: 

* Cualquier procedimiento computacional bien definido que toma algún valor, o conjunto de valores, como entrada y produce algún valor, o conjunto de valores, como salida. 
* Una secuencia de pasos computacionales que transforma una entrada en una salida. 
* Una herramienta para la solución de un problema computacional bien especificado. El **Planteamiento del Problema** define en términos generales la relación entre la entrada y la salida. El algoritmo describe un procedimiento computacional específico para lograr la relación entre la entrada y la salida.

Ejemplo:

Problema: Ordenamiento

Entrada: Un arreglo de números enteros $\{a_1, a_2, \dots, a_n\}$

Salida: Una permutación $\{a_1', a_2', \dots, a_n'\}$ de los elementos del arreglo de entrada, tal que $a_1' \leq a_2' \leq \dots \leq a_n'$

El planteamiento de un problema permite establecer el objetivo principal al momento de diseñar un algoritmo: tener bien identificado el problema que se resolverá. 

En función si de tal objetivo se cumple o no es que se asignan ciertas caracterizaciones al algoritmo obtenido: 

* Un **Algoritmo Correcto** es aquel en el que con toda instancia correcta de entrada siempre se finaliza con la salida correcta. 
* Se dice que un algoritmo **Soluciona** el problema computacional dado si éste es correcto. 
* Un **Algoritmo Incorrecto**: 
  * Puede no finalizar con algunas instancias correctas de entrada. 
  * Puede finalizar con una salida diferente de la deseada. 

Nótese que sin embargo, un algoritmo incorrecto puede ser útil si su porcentaje de error es identificable y controlable.

Ejemplo de Algoritmos Correctos e Incorrectos: 

Problema: Determinación del factorial. 

Entrada: Un entero no negativo $n$. 

Salida: $n!$

Nótese que también en ocasiones será sumamente difícil, o quizás imposible, determinar si un algoritmo termina para toda entrada correcta: Un problema de Teoría de Números conjetura que para todo entero positivo n el proceso siguiente, aplicado repetidamente, siempre terminará en 1:

* Si $n$ es par, dividirlo por 2. 
* Si $n$ es impar, multiplicarlo por tres y sumarle 1. 

Al proceso que acabamos de describir se le llama la **Función de Collatz**. 

Por ejemplo, sea $n=53$. Entonces, el proceso se ejecuta de la siguiente manera:

$$53 \rightarrow 160 \rightarrow 80 \rightarrow 40 \rightarrow 20 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$

Hemos verificado que la conjetura es correcta dado que se llego al número 1 en 11 pasos. Dado un entero arbitrario $n$, ¿cuántos pasos se requieren para llegar a 1?

¿Podemos garantizar que el algoritmo que implementa la Función de Collatz terminará su ejecución con todo entero positivo n? Hasta el momento no se sabe, es un problema abierto.

El ejemplo anterior podría dar a lugar a establecer la cuestión de si un humano será o no capaz de verificar para cualquier algoritmo si éste terminará siempre su ejecución (bajo entradas correctas). Por otro lado, ello también nos conduciría a la posibilidad de preguntarnos si una computadora podría ser capaz de efectuar tal tarea. Este último cuestionamiento es conocido como el **Problema de la Parada (Halting Problem)**. El problema fue formulado por Alan Turing en 1936 y se plantea de la siguiente manera: 

> Dada la descripción de un algoritmo y la descripción de sus parámetros de entrada, determinar si el algoritmo, cuando se ejecuta con tales parámetros terminará. 

Fue el mismo Turing quien también dio la respuesta formal final al *Halting Problem*. En nuestro caso, abordaremos el problema al establecer si existe o no un algoritmo que determine si otro algoritmo con una entrada dada terminará su ejecución. Procederemos mediante una **Prueba por Contradicción**. 

