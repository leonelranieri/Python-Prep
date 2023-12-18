import os

#crear carpeta
os.makedirs('clase09_mis_montañas_altas')

#copiar archivo de montañas a la carpeta anteriormente creada
os.system('copy clase09_mi_ej3.csv clase09_mis_montañas_altas') 

#listar el contenido del archivo
print(os.listdir('./clase09_mis_montañas_altas'))