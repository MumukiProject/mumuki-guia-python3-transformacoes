Ao trabalhar com lotes de dados é normal que os nomes das colunas não sejam os melhores. Mas, ainda bem que temos a solução, `rename`! 

`rename`  permite, através de um dicionário, renomear colunas. Por exemplo, se tivéssemos o seguinte lote `pessoas` com uma escolha de nomes inexpressivos...

com_name|ag|add|count|
---|---|---|---|
Ricardo Guiraldes|60|Rua das pedras 1000|Brazil|
Billy Summers|42|5th Avenue 2332|USA|
Anna Prado|37|San Martin 1165|Argentina|

... e quiséssemos obter o `DataFrame` com suas colunas renomeadas poderíamos escrever:

```python
pessoas.rename(columns = {
  "com_name": "full_name",
  "ag": "age",
  "add": "address",
  "count": "country"
})
```

Dessa forma, fica um pouco mais claro que as colunas representam nome completo, idade, endereço e país, respectivamente. Para que esta operação tenha efeito no `DataFrame` original deveríamos escrever... exato!, `inplace=True`!

> Agora é a sua vez!  Renomeie no `DataFrame` em seu caderno as colunas `loc_code`, `prov_id` e `dep_id` por `city_id`, `province_id` e `department_id` respectivamente.
