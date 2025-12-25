import matplotlib.pyplot as plt
import pandas as pd

import pandas as pd

datos = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Notas": [85, 90, 78]
})

plt.scatter(datos.index, datos["Notas"])
plt.show()


