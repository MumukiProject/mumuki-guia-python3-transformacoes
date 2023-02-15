Impecável! 👏

Caso tenhamos apenas strings "inteiras" em nossa coluna, outra operação útil é `astype` com o argumento `int`:

```python
ムnumeros_mentirosos.astype(int)
0 4
1 9
2 8
dtype: int64
```

É importante notar que esta opção converte nossos dados para `int` e não funcionaria se tivéssemos strings "decimais":

```python
ムpd.Series(["1.9", "12.0", "15.6"]).astype(int)
ValueError: invalid literal for int() with base 10: '1.9'
```

Mas se fossem verdadeiros números decimais, `astype(int)` truncaria os valores: 

```python
ムpd.Series([12.76, 45.2, 101]).astype(int)
0 12
1 45
2 101
dtype: int64
```

[Aqui](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html) você pode encontrar sua documentação.