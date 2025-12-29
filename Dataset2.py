import pandas as pd

horas = []
aprueba = []

for i in range (4):
    h = int(input(f"Ingrese las horas de estudio {i+1} => "))
    horas.append(h)
    aprueba.append("Si" if h >= 3 else "No")

data = pd.DataFrame({
    "Horas_Estudio": horas,
    "Aprueba": aprueba
})

print("\nDataset creado:")
print(data)
