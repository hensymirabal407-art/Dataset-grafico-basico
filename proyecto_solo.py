import pandas as pd
import matplotlib.pyplot as plt

cantidad = []
precio = []

x = int(input("¿Cuántos productos desea ingresar?: "))

for i in range(x):
    print(f"\nProducto {i+1}")
    c = int(input("Ingrese la cantidad: "))
    p = int(input("Ingrese el precio: "))

    cantidad.append(c)
    precio.append(p)

data = pd.DataFrame({
    "cantidad": cantidad,
    "precio": precio
})

print("\nDataset creado")
print(data)

plt.bar(data["cantidad"], data["precio"])
plt.show()
