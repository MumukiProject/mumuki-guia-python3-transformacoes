Para remover columnas contamos con el comando `del` ✖️ ...

```python
del tabla["columna"]
```

...que nos permite eliminar de a una columna por vez ☝️. Si en cambio queremos eliminar varias en un sólo paso, contamos con la operación `drop`, que funciona de la siguiente forma:

```python
tabla.drop(
  columns=[
    "primera_columna_a_borrar",
    "segunda_columna_a_borrar",
    "tercera_columna_a_borrar"],
  inplace=True)
```

Al igual que con otras operaciones, es importante agregar `inplace=True` si queremos que la operación tenga efecto en el `DataFrame`. En caso de omitirlo, `drop` retorna una nueva tabla sin esas columnas pero sin modificar la original.

> ¡Pongámoslo en práctica! Eliminá en tu cuaderno las columnas innecesarias que detectaste en el ejercicio anterior.
