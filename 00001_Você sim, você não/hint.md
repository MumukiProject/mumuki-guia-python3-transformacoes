Para saber se todas as colunas são iguais ou sem valores (ou seja, apenas com `nan`s) você pode usar `pd.unique`. Outra forma rápida de saber quais são os valores únicos e não nulos de cada coluna é fazendo uma descrição _categórica_ do `DataFrame`:

```python
cinemas.astype('object').describe() 
```

As colunas que têm `0` ou `1` na linha `unique` são candidatas a serem eliminadas! :wink:
