¡Impecable! 👏

En caso de que solo tengamos números enteros en nuestra columna, otra operación útil es `astype` con el argumento `int`:

```python
ム numeros_tramposos.astype(int)
0    4
1    9
2    8
dtype: int64
ム  pd.Series([12.76, 45.2, 101]).astype(int)
0     12
1     45
2    101
dtype: int64
```

Es importante tener en cuenta que esta opción transforma nuestros datos a `int` y no nos serviría si tenemos strings con números decimales. 

```python
ム pd.Series(["1.9", "12.0", "15.6"]).astype(int)
ValueError: invalid literal for int() with base 10: '1.9'
```

[Acá](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html) podés encontrar su documentación.
