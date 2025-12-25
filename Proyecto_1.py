import pandas as pd
import matplotlib.pyplot as plt

materias = []
calificaciones = []

x = int(input("Ingrese la cantidad de materias: "))

for i in range(x):
    materia = input(f"Ingrese el nombre de la materia {i+1}: ")
    nota = float(input(f"Ingrese la calificación de {materia}: "))

    materias.append(materia)
    calificaciones.append(nota)

data = pd.DataFrame({
    "Materia": materias,
    "Calificación": calificaciones
})

print("\nDatos ingresados:")
print(data)

plt.bar(data["Materia"], data["Calificación"])
plt.show()