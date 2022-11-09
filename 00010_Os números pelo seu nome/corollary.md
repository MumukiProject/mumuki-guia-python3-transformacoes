Impecável! 👏

Caso tenhamos apenas inteiros em nossa coluna, outra operação útil é `astype` com o argumento `int`:

``` python
ム cheater_numbers.astype(int)
0 4
1 9
2 8
dtype: int64
ム pd.Series([12.76, 45.2, 101]).astype(int)
0 12
1 45
2 101
dtype: int64
```

É importante notar que esta opção converte nossos dados para `int` e não funcionaria se tivéssemos strings com números decimais.

```python
ム pd.Series(["1.9", "12.0", "15.6"]).astype(int)
ValueError: invalid literal for int() with base 10: '1.9'
```

[Aqui](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html) você pode encontrar sua documentação.