#un dataset es como una libreta donde se guardan datos en filas y columnas.

import pandas as pd 

horas1 = int(input("Ingrese la primera hora de estudio => "))
horas2 = int(input("Ingrese la segunda hora de estudio => "))
horas3 = int(input("Ingrese la tercera hora de estudio => "))
horas4 = int(input("Ingrese la cuarta hora de estudio => "))

aprueba1 = "Si" if horas1 >= 3 else "No"
aprueba2 = "Si" if horas2 >= 3 else "No"
aprueba3 = "Si" if horas3 >= 3 else "No"
aprueba4 = "Si" if horas4 >= 3 else "No"

data = pd.DataFrame({
    "Horas_Estdudio": [horas1, horas2, horas3, horas4],
    "Aprueba": ["Si", "No", "Si", "No"]
})

print("\nDataset creado:")
print(data)