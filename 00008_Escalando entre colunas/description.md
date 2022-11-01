`pandas` também nos permite operar em colunas para gerar novas `Series` de uma maneira muito semelhante ao que aprendemos no exercício anterior :person_climbing:. Por exemplo, se da nossa tabela hipotética de países...


|país|população|área|
|---|---|---|
|Argentina|39921833|2780400|
|Bolívia|8989046|1098581|
|Brasil|188078227|8515770|
|Chile|16134219|756102|
|Colômbia|43593035|1141748|
|México|107449525|1964375|

...queríamos gerar uma coluna de densidade populacional (expressa em habitantes/km²), poderíamos fazer o seguinte:

```python
paises["population_density"] = paises["population"] / paises["area"]
```

Com essa mudança, `paises` ficaria assim:

|país|população|área|
|---|---|---|
|Argentina|39921833|2780400|
|Bolívia|8989046|1098581|
|Brasil|188078227|8515770|
|Chile|16134219|756102|
|Colômbia|43593035|1141748|
|México|107449525|1964375|

> :mag: Observe que `cruise passageiros` tem uma coluna `total_expenses`, mas ela realmente reportará o valor total dos gastos? Haverá casos em que os gastos totais nele contidos não condizem com a soma dos gastos detalhados?
>
> :bulb: Para descobrir, crie uma coluna `actual_total_expenses` com a soma de todos os gastos e responda às seguintes perguntas. Que conclusões você pode tirar?
