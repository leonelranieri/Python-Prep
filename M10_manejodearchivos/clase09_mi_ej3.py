montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

#importar librería os, y abrir/crear un archivo 'clase09_mi_ej3.csv' en modo escritura
import os
archivo = open("clase09_mi_ej3.csv", "w")

#recorres las claves del diccionario, si la clave es 'altura': salto de line, sino agregar comas entre claves
for key in montañas.keys():
    if(key == 'altura'):
        archivo.write(key+'\n')
    else:
        archivo.write(key+',')

#recorrer el diccionario:'montañas' agregando los valores al archivo
i=0
while(i < 10):
    archivo.write(montañas['nombre'][i]+',')
    archivo.write(str(montañas['orden'][i])+',')
    archivo.write(montañas['cordillera'][i]+',')
    archivo.write(montañas['pais'][i]+',')
    archivo.write(str(montañas['altura'][i])+'\n')
    i+=1

archivo.close()




