import os

tamaño_en_bytes=os.path.getsize('clase09_mi_ej3.csv')
tamaño_en_MB=tamaño_en_bytes/(1024.0*1024.0)

print("El archivo clase09_mi_ej3.csv tiene un tamaño de ", str(tamaño_en_MB), " MB")