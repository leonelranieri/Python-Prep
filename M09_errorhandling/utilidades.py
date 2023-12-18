class Utilidades:
    def __init__(self, lista_de_numeros):
        if(type(lista_de_numeros) != list):
            self.lista=[]
            raise ValueError('Se esperaba un tipo de dato list con número enteros. Se crea una lista vacía')
        else:
            self.lista=lista_de_numeros
    

    def es_primo(self):
        '''Función que, dada una lista determina si un número es primo o no.
        Retorna un booleano. '''
        conj=set(self.lista)
        for i in conj:
            if(self.__es_primo(i)):
                print("El número ", str(i), " ES primo")
            else:
                print("El número ", str(i), " NO ES primo")
    
    def es_primo_con_lista(self):
        lista_p=[]
        for i in self.lista:
            if(self.__es_primo(i)):
                lista_p.append(True)
            else:
                lista_p.append(False)
        return lista_p

    def __es_primo(self, num):
        '''Función que determina si un número es primo o no.
        Retorna un booleano. '''
        if(num < 2):
            return False
        for i in range(2, num):
            if(num%i==0):
                return False
        return True


    def mayor_ocurrencia(self):
        '''Determina, dada una lista, el número que aparece más veces,
            y la cantidad de veces que aparece.'''
        if(len(self.lista)==0):
            print("La lista está vacía")
            return None
        else:
            max_ocurrencia=-999
            num_ocurrencia=-1
            for num in self.lista:
                cant=self.lista.count(num)
                if(cant>max_ocurrencia):
                    max_ocurrencia=cant
                    num_ocurrencia=num  
        return num_ocurrencia, max_ocurrencia

    def conversion_de_grados(self, origen, destino):
        medidas=["celcius", "farenheit", "kelvin"]
        lista_result=[]
        if(str(origen) not in medidas):
            print(f'Se ve que {origen} no es una medida esperada. Se espera alguno de los siguientes valores {medidas}')
            return lista_result
        if(str(destino) not in medidas):
            print(f'Se ve que {destino} no es una medida esperada. Se espera alguno de los siguientes valores {medidas}')
            return lista_result    
        conjunto=set(self.lista)
        for i in conjunto:
            #print(i, " grado ", origen, " son ", self.__conversion_de_grados(i, origen, destino), 
            #        " grados")
            lista_result.append(self.__conversion_de_grados(i, origen, destino))
        return lista_result


    #CONVERSIÓN DE UNIDADES 
    def __conversion_de_grados(self, valor, medida_origen, medida_destino):
        '''Dado un valor y dos unidades de medida, se realiza
            la conversión desde la medida de origen a la medida destino'''
        def de_celcius_a_farenheit(c):
            return (c*(9/5))+32
        def de_celcius_a_kelvin(c):
            return c+273.15
        def de_farenheit_a_celcius(f):
            return (f-32)/(9/5)
        def de_kelvin_a_celcius(k):
            return k-273.15
        def de_farenheit_a_kelvin(f):
            return de_celcius_a_kelvin(de_farenheit_a_celcius(f))
        def de_kelvin_a_farenheit(k):
            return de_celcius_a_farenheit(de_kelvin_a_celcius(k))
        if(medida_origen.lower()=="celcius"):
            if(medida_destino.lower()=="farenheit"):
                return de_celcius_a_farenheit(valor)
            elif(medida_destino.lower()=="kelvin"):
                return de_celcius_a_kelvin(valor)
            elif(medida_destino.lower()=="celcius"):
                return valor
            else:
                print("Medida destino incorrecta")
        elif(medida_origen.lower()=="farenheit"):   
            if(medida_destino.lower()=="celcius"):
                return de_farenheit_a_celcius(valor)
            elif(medida_destino.lower()=="kelvin"):
                return de_farenheit_a_kelvin(valor)
            elif(medida_destino.lower()=="farenheit"):
                return valor
            else:
                print("Medida destino incorrecta")
        elif(medida_origen.lower()=="kelvin"):
            if(medida_destino.lower()=="celcius"):
                return de_kelvin_a_celcius(valor)
            elif (medida_destino.lower()=="farenheit"):
                return de_kelvin_a_farenheit(valor)
            elif(medida_destino.lower()=="kelvin"):
                return valor
            else:
                print("Medida destino incorrecta")
        else:
            print("Medida origen incorrecta")
    
    def factorial(self):
        conj=set(self.lista)
        for i in conj:
            print("El factorial de ", i, " es ", self.__factorial(i))

    def factorial_con_lista(self):
        lista_fact=[]
        for i in self.lista:
            lista_fact.append(self.__factorial(i))
        return lista_fact

    def __factorial(self, num):
        '''Calcula el factorial de un número natural'''
        if(type(num)!=int):
            return "El número debe ser del conjunto de los Naturales"
        if(num<0):
            return "El número no debe ser negativo"
        if(num <=1):
            return 1
        num=num*self.__factorial(num-1)
        return num