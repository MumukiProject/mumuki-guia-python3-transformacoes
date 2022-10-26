Ya estuvimos eliminando y renombrando columnas, ¡ahora vamos a aprender a agregar nuevas! :heavy_plus_sign:

Sin embargo, antes de pasar a eso vamos a enseñarte a hacer una copia de un `DataFrame`. ¿Y por qué? Es que a veces nos interesará preservar un estado particular de un `DataFrame` y hacer modificaciones en una copia del mismo...

```python
copia = tabla.copy()
# ahora modificamos la copia
del copia["columna"]
```

...y si luego nos arrepentimos podremos aún usar el `DataFrame` original, o incluso restaurarla a su versión anterior:

```python
# ¡la tabla original aún tiene la columna eliminada!
pd.value_counts(tabla["columna"])
# restauramos la versión original 
copia = tabla.copy()
```

> Pegá el siguiente código en tu cuaderno y luego embarquémonos al siguiente ejercicio 🚢:
>
```python
import pandas as pd
cruceros_originales = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=751983160&single=true&output=csv")
cruceros = cruceros_originales.copy()
```
