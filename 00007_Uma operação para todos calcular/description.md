Outra maneira de criar colunas é a partir de operações _escalares_ aplicadas a cada um de seus valores. ¿Que, que? 🤨 Vamos ver um exemplo! Suponhamos que temos um `DataFrame` com dados de população e extensão de diferentes `países`...

|country|population|area|
|---|---|---|
|Argentina|39921833|1073513|
|Bolivia|8989046|424162|
|Brazil|188078227|3287942|
|Chile|16134219|291931|
|Colombia|43593035|440829|
|Mexico|107449525|758445|


Para resolver isso, podemos aplicar, justamente, uma operação escalar:

```python
paises["area"] = paises["area"] * 2.59 # conversão imprecisa, mas rápida de mi² a km²
```

:rainbow: Agora, nossa área estará expressa na unidade correta:

|country|population|area|
|---|---|---|
|Argentina|39921833|2780400|
|Bolivia|8989046|1098581|
|Brazil|188078227|8515770|
|Chile|16134219|756102|
|Colombia|43593035|1141748|
|Mexico|107449525|1964375|

(:pencil: _os valores do exemplo foram arredondados para clareza_)

>  :first_place: Vamos colocar em prática! Quando estudamos gastos ou preços, normalmente faremos ajustes pela inflação, ou seja, multiplicaremos todos os valores monetários por um determinado coeficiente.
>
> :money_with_wings: Sabendo disso, escreva uma função `ajustar_gastos` que utilize um `DataFrame` com a mesma estrutura da nossa tabela de `cruzeiristas` e um coeficiente, e retorne uma **nova** tabela com todos seus gastos atualizados apropriadamente.

