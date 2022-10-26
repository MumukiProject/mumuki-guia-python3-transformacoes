Para saber si todas las columnas son iguales o sin valores (es decir, sólo con `nan`s) podés utilizar `pd.unique`. Otra forma rápida de saber cuáles son los valores únicos y no nulos de cada columna es haciendo una descripción _categórica_ del `DataFrame`:

```python
cines.astype('object').describe() 
```

¡Las columnas que tengan `0` o `1` en la fila `unique` son candidatas a irse! :wink:
