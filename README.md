# Integración de Código

## índice

**1.** [Descripción](#descripción)

**2.** [¿Cómo puede ser clonado?](#cómo-puede-ser-clonado)

**3.** [Descripción](#descripción)

## Descripción 
Este software fue creado a través de Python en Visual Studio Code. Su funcionalidad es que nos muestra una lista de elementos, esta lista tiene adentro un bucle que ayuda a la ejecución de si misma. Por otra parte, tenemos otro algoritmo que imprime la lista de elementos que cada usuario elija. 

### Primera parte:

El código imprime un mensaje introductorio: "Ejercicio propuesto por el docente:".
Luego, genera una lista de números del 1 al 10 utilizando la comprensión de listas: num = [x for x in range(1, 11)].
Muestra la lista resultante con el mensaje: "La lista por comprensión es: {num}".
Imprime un espacio en blanco y una línea separadora: "///////////////////////////////////////////////////".

### Segunda parte:

Se imprime un mensaje informativo para el usuario, explicando que podrá visualizar una lista generada por comprensión con los números que desee.
Solicita al usuario que ingrese dos números a través del teclado:
z: el número inicial desde el cual se comenzará la lista.
m: el número final hasta donde llegará la lista (incluyendo este número, ya que luego se incrementa m en 1 con m += 1).
Nuevamente, se genera una lista utilizando la comprensión de listas, pero esta vez con los límites dados por el usuario: num = [x for x in range(z, m)].

Finalmente, imprime la lista generada: "Su lista por comprensión es la siguiente: {num}".

## ¿Cómo puede ser clonado?

### 1. Clona este repositorio en tu máquina local

git clone (https://github.com/lppz16/Integraci-n-de-c-digo.git)

## 2. Navega al directorio del proyecto:

   cd Python-EST_DAT

### 3. Ejecuta el script:

Asegúrate de tener *Python* instalado (preferiblemente la versión 3.8 o superior).

## Instalación

**1.** Asegúrate de tener Python 3.11 o superior instalado en tu sistema.

**2.** Instala Git si aún lo tienes.

**3.** Clona el repositorio desde Github con el siguiente comando:
  git clone (https://github.com/lppz16/Integraci-n-de-c-digo.git)

## Herramientas utilizadas:

**1. Comprensión de listas:** Es una herramienta poderosa en Python que permite crear listas de una manera concisa y legible.

**2. Función print():** Se usa para mostrar mensajes en la consola.

**3. Función input():** Se utiliza para solicitar entradas del usuario desde el teclado.

**4. Función range():** Genera una secuencia de números en un rango determinado.

**5. Operadores matemáticos:** El incremento de variables con += también se utiliza para ajustar el límite superior del rango.

**6. Conversión de tipo:** La función int() convierte la entrada del usuario (que por defecto es una cadena) en un número entero.

## Uso

**1. Aprendizaje de comprensión de listas:**
El código es útil para demostrar cómo se utiliza la comprensión de listas en Python. Este concepto permite crear listas de manera eficiente y es fundamental para quienes están aprendiendo programación, ya que combina bucles y generación de secuencias en una sola línea.

**2. Interacción con el usuario:**
Permite al usuario personalizar los rangos de una lista a través de la entrada de datos desde el teclado. Esto hace que el programa sea interactivo, ayudando a los estudiantes a comprender cómo manejar entradas del usuario y generar resultados dinámicos basados en esas entradas.

**3. Generación de secuencias numéricas:**
El algoritmo es útil para generar secuencias numéricas personalizadas, lo cual puede ser aplicado en varios escenarios, como simulaciones, cálculos matemáticos o simplemente para crear listas de números con ciertos criterios.

**4. Práctica de conversión de tipos de datos:**
Se utiliza int() para convertir las entradas del usuario de cadenas de texto (strings) a enteros. Esto es un ejemplo clave de cómo convertir tipos de datos en Python, algo que es crucial en programación cuando se trabaja con diferentes tipos de datos.

**5. Introducción a rangos y bucles:**
El uso de range() en el código muestra cómo generar un conjunto de valores numéricos dentro de un rango específico. Esto es especialmente útil en la programación para crear listas de números o realizar iteraciones con bucles.

**6. Fomentar la flexibilidad y reutilización del código:**
El algoritmo enseña cómo construir soluciones flexibles y reutilizables, ya que el rango de números no está predefinido, sino que depende de la entrada del usuario. Esto permite aplicar el mismo código en diferentes contextos sin modificarlo.

**7. Visualización de resultados:**
Muestra cómo usar la función print() para mostrar los resultados de una operación de manera clara, lo que ayuda al usuario a visualizar el resultado en tiempo real.

**8. Validación y ajuste de rangos:**
El incremento del valor final del rango (m += 1) enseña cómo ajustar límites de rangos para garantizar que el resultado incluya el número final ingresado por el usuario, un detalle importante en el manejo de rangos en Python.

## Estructura del código:

**1. Introducción:**
Mensaje informativo del ejercicio.

**2. Lista fija:**
Generación de una lista por comprensión (del 1 al 10).

**3. Separadores:**
Espacio y separador para una mejor legibilidad.

**4. Instrucciones al usuario:**
Mensaje que introduce al usuario sobre cómo interactuar con el programa.

**5. Entrada del usuario:**
Solicitud de límites para la generación de la lista personalizada.

**6. Lista personalizada:**
Generación de la lista basada en la entrada del usuario.

## Captura del código:

![Python](https://github.com/lppz16/Integraci-n-de-c-digo/blob/71b35beaf64e2e027dbe3167e2a0e74881540f82/Material%20Digital/Captura%20de%20pantalla%202024-09-23%20145340.png)


## Captura de la ejecución del código:
![Python](https://github.com/lppz16/Integraci-n-de-c-digo/blob/main/Material%20Digital/Captura%20de%20pantalla%202024-09-23%20145653.png)

## Video:
https://github.com/lppz16/Integraci-n-de-c-digo/blob/a64205c1a4259f5a1503e91216420823c045c363/Material%20Digital/Video.mp4


## Autor

Yan Frank Ríos López

