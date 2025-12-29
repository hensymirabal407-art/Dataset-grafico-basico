import pandas as pd

horas = []
aprueba = []

n = int(input("¿Cuántos estudiantes quieres ingresar? "))

for i in range(n):
    h = int(input(f"Horas de estudio estudiante {i+1}: "))
    horas.append(h)
    aprueba.append("Sí" if h >= 3 else "No")

dataset = pd.DataFrame({
    "Horas_Estudio": horas,
    "Aprueba": aprueba
})

print(dataset)
