#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
nro = 3 #int
print(nro)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(8.5)




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(nro))




# 4) Crear una variable que contenga tu nombre

# In[2]:
MiNombre='Edgar'



# 5) Crear una variable que contenga un número complejo

# In[3]:
comple=3-9j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(MiNombre))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
nroPi=3.1416 

pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
verdadero=True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

# In[5]:
print(type(verdadero))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
mixta=8+2.4





# 11) Realizar una operación de suma de números complejos

# In[2]:
print(8j+3j-21j)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
print(9+5j)




# 13) Realizar una operación de multiplicación

# In[5]:
print(10*2.68)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
divi=27/4
print(divi)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(int(divi))




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(divi-int(divi))
print(27//4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
4*6+3





# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

MiNombre="Edgar"
MiApellido="Barbero"
print( MiNombre + " " + MiApellido )



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

2 == "2"



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(str(2)=="2")
print(2==int("2"))



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3,8') #da error porque debe ir punto decimal y no coma




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# In[15]:

x=3
x-=4
print(x)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1 << 2 # el 1 en binario es 0001 
       #cuando desplazo 2 digitos a la izquierda y completo con 0 da 0100
       #0100= 1 * (2^2) + 0 * (2^1) + 0 * (2^0) = 4 + 0 + 0 = 4



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

2 + "2" #da error por ser de distintos tipos




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

2 + int("2")


# %%
