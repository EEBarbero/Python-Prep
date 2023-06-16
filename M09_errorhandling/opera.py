class Calculos:
    def __init__(self,lista) -> None:
        self.lista = lista
    
    def verifica_Primo(self):
        for elemento in self.lista:
            if(type(elemento) != int):
                print(f"{elemento} no se analiza por no ser un número entero")
                break
            if(self.__verifica_Primo(elemento)):
                print(f"El número {elemento} es primo")
            else:
                print(f"El número {elemento} NO es primo")

    def valor_modal(self,menor = True):
        frecuencia, numero = self.__valor_modal(self,menor)
        print(f"El número más frecuente es {numero} y se repite {frecuencia} veces")

    def convierte_grados(self,origen,destino):
        if(type(origen)!= str or type(destino)!= str or (origen != "c" and origen != "f" and origen != "k") or (destino != "c" and destino != "f" and destino != "k")):
            print("'origen' y 'destino' debe ser 'c' 'f' o 'k' (para celsius, farenheit, kelvin)")
            return None
    
        origen = origen.lower()
        destino = destino.lower()
        escalas = {'c':'Celsius','f':'Fahrenheit','k':'Kelvin'}

        for elemento in self.lista:
            print(elemento," en grados ",escalas[origen]," equivalen a ",self.__convierte_grados(elemento,origen,destino)," grados ",escalas[destino])
        
    def factorial(self):
        for elemento in self.lista:
            print(f"El factorial de {elemento} es {self.__factorial(elemento)}")

# ========================================
    def __verifica_Primo(self,numero):
        es_primo = True
        for i in range(2,numero):
            if(numero % i == 0):
                es_primo = False
                break
        return es_primo
    
    def __valor_modal(self,lista,menor): 
        # menor == True-> si hay +1 nro con igual frecuencia mayor devuelve el MENOR
        #          False-> si hay +1 nro con igual frecuencia mayor devuelve el MAYOR

        if(len(self.lista) == 0):
            return None

        if(menor == True):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)

        l_numeros = []
        l_cantidad = []

        for elemento in self.lista:
            if(elemento in l_numeros):
                posicion = l_numeros.index(elemento)
                l_cantidad[posicion] += 1
            else:
                l_numeros.append(elemento)
                l_cantidad.append(1)
        
        moda = l_cantidad[0]
        nro_moda = l_numeros[0]

        for i, elemento in enumerate(l_cantidad):
            if(elemento > moda):
                moda = elemento
                nro_moda = l_numeros[i]

        return moda,nro_moda
    
    def __convierte_grados(self,valor,origen,destino): 
        #origen/destino aceptan "c", "f" o "k" para las escalas de celsius, farenheit, kelvin

        origen = origen.lower()
        destino = destino.lower()

        valor_convertido = None

        if(origen != "c" and origen != "f" and origen != "k"):
            print("El origen debe ser 'c' 'f' o 'k' (celsius, farenheit, kelvin)")

        if(destino != "c" and destino != "f" and destino != "k"):
            print("El destino debe ser 'c' 'f' o 'k' (celsius, farenheit, kelvin)")

        if(origen=="c"):
            if(destino=="c"):
                valor_convertido=valor
            elif(destino=="f"):
                valor_convertido=valor*9/5+32
            else:
                valor_convertido=valor+273.15
        elif(origen=="f"):
            if(destino=="f"):
                valor_convertido=valor
            elif(destino=="c"):
                valor_convertido=(valor-32)*5/9
            else:
                valor_convertido=(valor-32)*5/9+273.15
        else:
            if(destino=="k"):
                valor_convertido=valor
            elif(destino=="c"):
                valor_convertido=valor-273.15
            else:
                valor_convertido=(valor-273.15)*9/5+32
        return valor_convertido

    def __factorial(self,numero):
        if(type(numero)!=int):
            resultado = "El argumento debe ser un número entero"
        elif(numero<0):
            resultado = "El número debe ser positivo"
        elif(numero<=1):
            resultado = 1
        else:
            resultado= numero * self.__factorial(numero-1)
        return resultado