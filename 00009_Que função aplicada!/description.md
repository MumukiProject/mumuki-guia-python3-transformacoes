Algumas vezes nos depararemos com transformações mais complexas, que não conseguiremos resolver simplesmente com operações entre escalares e colunas :slight_frown:. Para esses casos, temos `apply`, que nos permite aplicar uma função a cada linha da nossa tabela e obter uma nova `Series` com os resultados:

```python
# ao usar apply desta forma, devemos sempre passar o argumento axis="columns"
tabula.apply(funcao_que_transforma_uma_linha_inteira, axis="columns")
```

Isso nos permitirá gerar colunas mais interessantes de maneira simples! :open_mouth: Por exemplo, se no exercício anterior tivéssemos uma função que calculasse diretamente os gastos totais...

```python
# note que cruzeirista não é um DataFrame,
# mas um quase-dicionário representando
# uma fila
def calcular_gasto_total(cruzeirista):
  return (
      cruzeirista['tours_expenses'] +
      cruzeirista['feed_expenses'] +
      cruzeirista['transport_expenses'] +
      cruzeirista['shopping_expenses'] +
      cruzeirista['other_expenses']
    )
```

... poderíamos ter gerado `calcular_gasto_total` assim:

``` python
cruzeiristas["actual_total_expenses"] = cruzeiristas.apply(calcular_gasto_total, axis="columns")
```

E teria nos dado o mesmo resultado! :tada:

``` python
ム cruzeiristas["actual_total_expenses"]
0 0,00
1.200,00
2 100,00
3 600,00
4 200,00
          ...
12011 257,84
12012 128,92
12013 257,84
12014 128,92
12015 257,84
```


> Sua vez! Queremos estimar quanto dinheiro foi trazido para o país por meio de cruzeiristas do exterior. Vamos calcular como:
>
> * :flag_uy: `0`, para cruzeiristas vindos do Uruguai;
> * :earth_americas: o número de pessoas no grupo de cada cruzeirista (`total_people`), multiplicado pelo gasto total (`total_expenses`), caso contrário.
>
> Adicione a `cruzeiristas` uma coluna `estimated_foreign_income` com esta estimativa.
 