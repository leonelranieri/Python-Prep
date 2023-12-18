import sys

if(len(sys.argv) == 3):
    import datetime
    import os
    fecha = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(fecha))

    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]
    registro = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    informe_clima = open('clase09.ej2.csv', 'a') 
    informe_clima.write(registro+'\n')
    informe_clima.close()
else:
    print('Envíe 3 argumentos, por ejemplo clase09_mi_ej2.py <temperatura> <húmedad> <llovio(True-False)>')

