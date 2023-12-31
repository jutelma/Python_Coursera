"""
Indexación y corte de cadenas

La indexación de cadenas le permite acceder a caracteres individuales en una cadena. Puede hacer esto usando corchetes
y la ubicación, o índice, del carácter al que desea acceder. Es importante recordar que Python inicia los índices en 0.
Entonces, para acceder al primer carácter de una cadena, usaría el índice [0]. Si intenta acceder a un índice que es
mayor que la longitud de su cadena, obtendrá un IndexError . ¡Esto se debe a que estás intentando acceder a algo que
no existe! También puede acceder a los índices desde el final de la cadena hacia el inicio de la cadena utilizando
valores negativos. El índice [-1] accedería al último carácter de la cadena y el índice [-2] accedería al penúltimo
carácter.

También puede acceder a una parte de una cadena, llamada segmento o subcadena. Esto le permite acceder a varios
caracteres de una cadena. Puede hacer esto creando un rango, usando dos puntos como separador entre el inicio y el
final del rango, como [2:5].

Este rango es similar a la función range() que vimos anteriormente. Incluye el primer número, pero llega a uno menos
que el último número. Por ejemplo:

>>> fruta = "Mangostán" >>> fruta[1:4] 'ang'

El segmento incluye el carácter en el índice 1 y excluye el carácter en el índice 4. También puede hacer referencia
fácilmente a una subcadena al principio o al final de la cadena especificando solo un extremo del rango. Por ejemplo,
dando solo el final del rango:

>>> fruta[:5] 'Mango'

Esto nos dio los caracteres desde el inicio de la cadena hasta el índice 4, excluyendo el índice 5. Por otro lado,
este ejemplo proporciona los caracteres que incluyen el índice 5, hasta el final de la cadena:

>>> fruta[5:] 'piedra'

Es posible que hayas notado que si juntas ambos resultados, ¡obtendrás la cadena original!

>>> fruta[:5] + fruta[5:] 'Mangostán'

¡Fresco!


Métodos básicos de cadenas En Python, las cadenas son inmutables. Esto significa que no se pueden modificar.
Entonces, si quisiéramos corregir un error tipográfico en una cadena, no podemos simplemente modificar el carácter
incorrecto. Tendríamos que crear una nueva cadena con el error tipográfico corregido. También podemos asignar un
nuevo valor a la variable que contiene nuestra cadena.

Si no estamos seguros de cuál es el índice de nuestro error tipográfico, podemos usar el método de cadena index para
localizarlo y devolver el índice. Imaginemos que tenemos la cadena "leones, tigres y osos" en la variable animales .
Podemos ubicar el índice que contiene la letra g usando animales.index("g") , que devolverá el índice; en este caso
8. También podemos usar subcadenas para ubicar el índice donde comienza la subcadena. Animales.index("osos")
devolvería 17, ya que ese es el comienzo de la subcadena. Si hay más de una coincidencia para una subcadena,
el método de índice devolverá la primera coincidencia. Si intentamos localizar una subcadena que no existe en la
cadena, recibiremos un ValueError que explica que no se encontró la subcadena.

"""
animals = "lions tigers and bears"
animals.index("g")

animals = "lions tigers and bears"
animals.index("bears")

"""
Podemos evitar un ValueError comprobando primero si la subcadena existe en la cadena. Esto se puede hacer usando 
la palabra clave in . Vimos esta palabra clave antes cuando cubrimos los bucles for . En este caso, es un condicional 
que será Verdadero o Falso. Si la subcadena se encuentra en la cadena, será Verdadera. Si la subcadena no se 
encuentra en la cadena, será False. Usando nuestra variable anterior animales , podemos hacer "caballos" en animales 
para verificar si la subcadena "caballos" se encuentra en nuestra variable. En este caso, la evaluación sería False, 
ya que los caballos no están incluidos en nuestra cadena de ejemplo. Si hiciéramos "tigres" en animales , 
obtendríamos Verdadero, ya que esta subcadena está contenida en nuestra cadena.

"""
# animals = "lions tigers and bears"
# "horses" in animals

# animals = "lions tigers and bears"
# "tigers" in animals

"""
Métodos de cadena avanzados
 
Ya hemos cubierto un montón de métodos de la clase String, así que sigamos basándose 
en ellos y analicemos algunos métodos más avanzados.

El método de cadena inferior devolverá la cadena con todos los caracteres cambiados a minúsculas. Lo inverso de esto 
es el método superior , que devolverá la cadena toda en mayúsculas. Al igual que con los métodos anteriores, 
los llamamos en una cadena usando notación de puntos, como "esto es una cadena".upper() . Esto devolvería la cadena 
"ESTA ES UNA CADENA" . Esto puede ser muy útil al verificar la entrada del usuario, ya que alguien puede escribir 
todo en minúsculas, todo en mayúsculas o incluso una combinación de casos.

Puede utilizar el método de tira para eliminar los espacios en blanco circundantes de una cadena. Los espacios en 
blanco incluyen espacios, tabulaciones y caracteres de nueva línea. También puede utilizar los métodos   strip y 
strip para eliminar espacios en blanco solo del lado izquierdo o derecho de la cadena, respectivamente.

El método count se puede utilizar para devolver el número de veces que aparece una subcadena en una cadena. Esto 
puede resultar útil para averiguar cuántos caracteres aparecen en una cadena o contar la cantidad de veces que 
aparece una determinada palabra en una oración o párrafo.

Si desea verificar si una cadena termina con una subcadena determinada, puede usar el método termina con . Esto 
devolverá Verdadero si la subcadena se encuentra al final de la cadena y Falso en caso contrario.

El método isnumeric puede comprobar si una cadena está compuesta únicamente de números. Si la cadena contiene solo 
números, este método devolverá Verdadero. Podemos usar esto para verificar si una cadena contiene números antes de 
pasar la cadena a la función int() para convertirla en un número entero, evitando un error. ¡Útil!

Anteriormente analizamos la concatenación de cadenas usando el signo más. También podemos utilizar el método de unión 
para concatenar cadenas. Este método se llama en una cadena que se utilizará para unir una lista de cadenas. El 
método toma una lista de cadenas a unir como parámetro y devuelve una nueva cadena compuesta por cada una de las 
cadenas de nuestra lista unidas usando la cadena inicial. Por ejemplo, " ".join(["Esto","es","una","frase"]) 
devolvería la cadena "Esto es una frase" .

Lo inverso del método de unión es el método de división . Esto nos permite dividir una cadena en una lista de 
cadenas. De forma predeterminada, se divide por cualquier carácter de espacio en blanco. También puedes dividir por 
cualquier otro carácter pasando un parámetro.

FORMATO DE CADENA


Puede utilizar el método de formato en cadenas para concatenar y formatear cadenas de todo tipo de formas potentes. 
Para hacer esto, cree una cadena que contenga llaves, {} , como marcador de posición, para ser reemplazada. Luego 
llame al método de formato en la cadena usando .format() y pase variables como parámetros. Las variables pasadas al 
método se utilizarán para reemplazar los marcadores de posición de llaves. Este método maneja automáticamente 
cualquier conversión entre tipos de datos por nosotros.

Si las llaves están vacías, se completarán con las variables pasadas en el orden en que se pasan. Sin embargo, 
puede poner ciertas expresiones dentro de las llaves para realizar operaciones de formato de cadenas aún más 
poderosas. Puede poner el nombre de una variable entre llaves y luego usar los nombres en los parámetros. Esto 
permite un código más fácil de leer y una mayor flexibilidad con el orden de las variables.

También puede colocar una expresión de formato dentro de las llaves, lo que le permite alterar la forma en que se 
formatea la cadena. Por ejemplo, la expresión de formato {:.2f} significa que lo formatearías como un número 
flotante, con dos dígitos después del punto decimal. Los dos puntos actúan como separador del nombre del campo, 
si hubiera especificado uno. También puede especificar la alineación del texto usando el operador mayor que: > . Por 
ejemplo, la expresión {:>3.2f} alinearía el texto tres espacios a la derecha, además de especificar un número 
flotante con dos decimales. El formato de cadena puede ser muy útil para generar resultados textuales fáciles de leer.

GUIA DE REFERENCIA DE CADENAS
 
En Python, hay muchas cosas que puedes hacer con cadenas. En esta guía, encontrará las operaciones y métodos de cadenas 
más comunes.

Operaciones de cadena

 · len(cadena) - Devuelve la longitud de la cadena

 · para carácter en cadena : itera sobre cada carácter en la cadena 

 · if substring in string - Comprueba si la subcadena es parte de la cadena

 · string[i] - Accede al carácter en el índice i de la cadena, comenzando en cero

 · string[i:j] : accede a la subcadena que comienza en el índice i y termina en el índice j menos 1. Si se omite i , 
   su valor predeterminado es 0 . Si se omite j , el valor predeterminado será len(string) .

Métodos de cadena

 · string.lower() - Devuelve una copia de la cadena con todos los caracteres en minúsculas

 · string.upper() - Devuelve una copia de la cadena con todos los caracteres en mayúsculas

 · string.strip() : devuelve una copia de la cadena sin el espacio en blanco del lado izquierdo 

 · string.strip() : devuelve una copia de la cadena sin el espacio en blanco del lado derecho 

 · string.strip() : devuelve una copia de la cadena sin los espacios en blanco del lado izquierdo y derecho.

 · string.count(substring) : devuelve el número de veces que la subcadena está presente en la cadena.

 · string.isnumeric() : devuelve True si solo hay caracteres numéricos en la cadena. Si no, devuelve Falso.

 · string.isalpha() : devuelve Verdadero si solo hay caracteres alfabéticos en la cadena. Si no, devuelve Falso.

 · string.split() : devuelve una lista de subcadenas que fueron separadas por espacios en blanco (los espacios en 
   blanco pueden ser un espacio, una tabulación o una nueva línea)

 · string.split(delimiter) : devuelve una lista de subcadenas que estaban separadas por espacios en blanco o un 
   delimitador

 · string.replace(antiguo, nuevo) : devuelve una nueva cadena donde todas las apariciones de lo antiguo han sido 
   reemplazadas por nuevas.

 · delimiter.join(lista de cadenas) : devuelve una nueva cadena con todas las cadenas unidas por el delimitador


GUIA DE FORMATO DE CADENAS 

Python ofrece diferentes formas de formatear cadenas. En el video, explicamos el método format(). En esta lectura, 
destacaremos tres formas diferentes de formatear cadenas. Para este curso sólo necesitas conocer el método format(). 
Pero en Internet es posible que encuentres cualquiera de los tres, por lo que es buena idea saber que los demás existen.

Usando el método formato()
 
El método de formato devuelve una copia de la cadena donde los marcadores de posición {} 
han sido reemplazados por los valores de las variables. Estas variables se convierten en cadenas si aún no lo eran. 
Los marcadores de posición vacíos se reemplazan por las variables pasadas al formato en el mismo orden.

"""

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

"""
Si los marcadores de posición indican un número, se reemplazan por la variable correspondiente a ese orden (
comenzando en cero).
"""
# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""
"""Si los marcadores de posición indican un nombre de campo, se reemplazan por la variable correspondiente a ese 
nombre de campo. Esto significa que los parámetros a formatear deben pasarse indicando el nombre del campo.
"""

# "{var1} {var2}".format(var1=value1, var2=value2)

"""Si los marcadores de posición incluyen dos puntos, lo que viene después de los dos puntos es una expresión de 
formato. Consulte a continuación la referencia de la expresión."""

# {:d} integer value
# '{:d}'.format(10.5) → '10'

"""
Dar formato a expresiones

     Expr.          Significado                                                    Ejemplo

     {:d}          valor entero                                           '{:d}'.formato(10.5) → '10'

     {:.2f}        coma flotante con tantos decimales                     '{:.2f}'.formato(0.5) → '0.50'

     {:.2s}        cadena con tantos caracteres                           '{:.2s}'.format('Python') → 'Py'

     {:<6s}        cadena alineada a la izquierda que muchos espacios     '{:<6s}'.format('Py') → 'Py '

     {:>6s}        cadena alineada a la derecha que muchos espacios       '{:>6s}'.format('Py') → 'Py'

     {:^6s}        cadena centrada en tantos espacios                     '{:^6s}'.format('Py') → 'Py'



Formato de cadena antiguo (opcional)
 
El método format() se introdujo en Python 2.6. Antes de eso, el operador % (
módulo) podría usarse para obtener un resultado similar. Si bien este método ya no se recomienda para código nuevo, 
es posible que lo encuentres en el código de otra persona. Esto es lo que parece:

"cadena base con %s marcador de posición" % variable

El operador % (módulo) devuelve una copia de la cadena donde los marcadores de posición indicados por % seguido de 
una expresión de formato se reemplazan por las variables después del operador.


"cadena base con %d y %d marcadores de posición" % (valor1, valor2)

Para reemplazar más de un valor, los valores deben escribirse entre paréntesis. La expresión de formato debe 
coincidir con el tipo de valor.

 

"%(var1) %(var2)" % {var1:valor1, var2:valor2}

Las variables se pueden reemplazar por nombre usando la sintaxis de un diccionario (aprenderemos sobre los 
diccionarios en un próximo video).

 
"Artículo: %s - Monto: %d - Precio: %.2f" % (artículo, monto, precio)

Las expresiones de formato son en su mayoría las mismas que las del método format(). 


Literales de cadena formateados (opcional) 

Esta característica se agregó en Python 3.6 y aún no se usa mucho. 
Nuevamente, se incluye aquí en caso de que lo encuentre en el futuro, pero no es necesario para este ni para ningún 
curso próximo.

Un literal de cadena formateado o cadena f es una cadena que comienza con 'f' o 'F' antes de las comillas. Estas 
cadenas pueden contener {} marcadores de posición que utilizan expresiones como las que se utilizan para las cadenas 
de métodos de formato.

La diferencia importante con el método de formato es que toma el valor de las variables del contexto actual, 
en lugar de tomar los valores de los parámetros.

Ejemplos:

>>> nombre = "Miqueas"

>>> imprimir(f'Hola {nombre}')

Hola Miqueas

 

>>> item = "Copa Púrpura"

>>> cantidad = 5

>>> precio = importe * 3,25

>>> print(f'Artículo: {artículo} - Monto: {monto} - Precio: {precio:.2f}')

Artículo: Copa Morada - Cantidad: 5 - Precio: 16.25

"""
"""
Guía de estudio  Strings

Esta guía de estudio proporciona un resumen de referencia rápida de lo que aprendió en esta lección y sirve como guía 
para la próxima prueba de práctica. Las lecturas de cadenas en esta sección son excelentes guías de sintaxis que lo 
ayudarán en el cuestionario de práctica de cadenas.

En el segmento Cadenas, aprendió sobre las partes de una cadena, la indexación y división de cadenas, la creación de 
nuevas cadenas, los métodos y operaciones de cadenas y el formato de cadenas.


Conocimiento

Operaciones y métodos de cadenas

    · .format() : método de cadena que se puede utilizar para concatenar y formatear cadenas. 

        · {:.2f} : dentro del método .format(), limita una variable de punto flotante a 2 decimales. El número de 
          decimales se puede personalizar.

    · len(cadena) : operación de cadena que devuelve la longitud de la cadena.

    · string[x] : operación de cadena que accede al carácter en el índice [x] de la cadena, donde la indexación 
      comienza en cero.

    · string[x:y] - Operación de cadena que accede a una subcadena que comienza en el índice [x] y termina en el 
      índice [y-1]. Si se omite x, su valor predeterminado será 0. Si se omite y, el valor predeterminado será 
      len(cadena).

    · string.replace(old, new) : método de cadena que devuelve una nueva cadena donde todas las apariciones de una 
      subcadena antigua han sido reemplazadas por una nueva subcadena.

    · string.lower() : método de cadena que devuelve una copia de la cadena con todos los caracteres en minúscula.

    
Habilidades de codificación

Grupo de habilidades 1
    · Utilice un bucle for para recorrer cada letra de una cadena.

    · Agrega un carácter al frente de una cadena.

    · Agrega un carácter al final de una cadena.

    · Utilice el método de cadena .lower() para convertir el caso (mayúsculas/minúsculas) de las letras dentro de una 
      variable de cadena. Este método se utiliza a menudo para eliminar casos como factor al comparar dos cadenas. Por 
      ejemplo, todo “gato” en minúscula no es igual a “Gato” porque “Gato” contiene una letra mayúscula. Para poder 
      comparar las dos cadenas y ver si son la misma palabra, puede usar el método de cadena .lower() para eliminar las 
      mayúsculas como factor en la comparación de cadenas.
      
"""


# Esta función acepta una cadena determinada y verifica cada carácter de
# la cadena para ver si es una letra o no.
# Si el personaje es una
# letra, esa letra se agrega al final de la variable de cadena
# "hacia adelante" y al principio de la variable de cadena "hacia atrás".
def mirrored_string(my_string):
    # Dos variables se inicializan como tipos de datos de cadena usando vacío
    # citas.
    # La variable "forwards" contendrá "my_string"
    # menos cualquier carácter que no sea una letra.
    # Los "al revés"
    # La variable contendrá las mismas letras que "forwards", pero en
    #  orden inverso.
    forwards = ""
    backwards = ""

    # El bucle for itera a través de cada carácter de "my_string"
    for character in my_string:

        # La declaración if verifica si el carácter no es un espacio.
        if character.isalpha():
            # Si es Verdadero, el cuerpo del bucle agrega el carácter al
            # final de "adelante" y al frente de
            # "al revés".
            forwards += character
            backwards = character + backwards

        # Si es falso (lo que significa que el carácter no es una letra), no se realiza ninguna acción
        # es necesario.
        # Los resultados de este enfoque de codificación evitan cualquier
        # carácter no alfabéticos que se escriben en la Variable
        #  "hacia adelante" y "hacia atrás".
        # El bucle for
        # reiniciar hasta que se hayan eliminado todos los caracteres de "my_string"
        # procesada.

        # La declaración if final compara "hacia adelante" y "hacia atrás"
        # cadenas para ver si las letras son iguales tanto hacia adelante como hacia atrás
        # al revés.
        # Dado que Python distingue entre mayúsculas y minúsculas, las dos cadenas
        # deben convertirse para utilizar el mismo caso en esta comparación.
    if forwards.lower() == backwards.lower():
        return True
    return False


print(mirrored_string("12 Noon"))  # Should be True
print(mirrored_string("Was it a car or cat I saw"))  # Should be False
print(mirrored_string("'eve, Madam Eve"))  # Should be True

"""
Grupo de habilidades 2

    · Utilice el método format() , con {} marcadores de posición para datos variables, para crear una nueva cadena.

    · Utilice una expresión de formato, como {:.2f} , para formatear una variable flotante y configurar el número de 
decimales que se mostrarán para la variable flotante.

"""


# Esta función convierte equivalentes de medidas.
# La salida está formateada
# como, "x onzas equivalen a y libras", con y limitada a 2 decimales.
def convert_weight(ounces):
    # Fórmula de conversión: 1 libra = 16 onzas
    pounds = ounces / 16

    # El resultado se compone utilizando el método .format().
    # Hay dos
    # marcadores de posición en la cadena: el primero es para las "onzas"
    # variable y la segunda es para la variable "libras".
    # El segundo
    # marcador de posición formatea el resultado flotante de la conversión
    # el cálculo se limitará a 2 decimales.
    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result


print(convert_weight(12))  # Should be: 12 ounces equal 0.75 pounds
print(convert_weight(50.5))  # Should be: 50.5 ounces equal 3.16 pounds
print(convert_weight(16))  # Should be: 16 ounces equal 1.00 pounds

"""
Grupo de habilidades 4  

    · Utilice el método .replace() para reemplazar parte de una cadena.  

    · Utilice la función len() para obtener el número de posiciones de índice en una cadena.

    · Corta una cadena en una posición de índice específica.
    
"""


# Esta función verifica una entrada de programación determinada para una fecha anterior y, si
# encontrado, la función lo reemplaza con una nueva fecha.
def replace_date(schedule, old_date, new_date):
    # Compruebe si la "fecha_antigua" dada aparece al final de la información dada
    # variable de cadena "horario".
    if schedule.endswith(old_date):
        # Si es Verdadero, se ejecutará el cuerpo del bloque if.
        # La variable "n" es
        # utilizado para mantener la posición del índice de corte.
        # La función len()
        # se utiliza para medir la longitud de la cadena "new_date".
        p = len(old_date)

        # La cadena "new_schedule" contiene la cadena actualizada con la
        # fecha anterior reemplazada por la nueva fecha.
        # La parte del cronograma[:-p] del
        # código recorta la subcadena "old_date" de "schedule"
        # comenzando en la posición final del índice (o lado derecho) contando
        # hacia la izquierda el mismo número de posiciones de índice que
        # calculado a partir de len(old_date).
        # Luego, el código de programación[-p:]
        # inicia la posición de indexación en la ranura donde se encuentra el primero
        # carácter de la "fecha_antigua" que solía colocarse.
        # El código .replace(old_date, new_date) inserta la "new_date" en
        # la posición donde solía existir la "fecha_antigua".
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Devuelve el cronograma con la nueva fecha.
        return new_schedule

    # Si el programa no termina con la fecha anterior, entonces devuelva la
    # frase original sin modificaciones.
    return schedule


print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
# Should display "Last year’s annual report be released in March 2024"?
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June"))
# Should display "The convention is scheduled for June"
