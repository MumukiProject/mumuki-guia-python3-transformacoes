Para remover colunas contamos com o comando `del` ✖️ ...

```python
del tabela["coluna"]
```

...que nos permite eliminar uma coluna por vez ☝️. Se ao invés disso quisermos eliminar várias em um único passo, temos a operação `drop`, que funciona da seguinte forma:


```python
tabela.drop(
  columns=[
    "primeira_coluna_a_remover",
    "segunda_coluna_a_remover",
    "terceira_coluna_a_remover"],
  inplace=True)
```

Da mesma maneira que acontece com outras operações, é importante agregar `inplace=True` se queremos que a operação tenha efeito no `DataFrame`. Neste caso se o omitirmos, `drop` retorna uma nova tabela sem essas colunas mas sem modificar a original.

> Vamos colocar em prática! Elimine do seu caderno as colunas desnecessárias que você detectou no exercício anterior.
