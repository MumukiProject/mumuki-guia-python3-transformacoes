Ao longo desta lição já modificamos muitos `DataFrame`s, mas ainda não criamos nenhum do zero! Para fazer isso, vamos escrever `pd.DataFrame()` e depois adicionar as colunas que queremos. Por exemplo, com o seguinte código...

```python
publico = cinemas[cinemas["setor"] == "Público"]
privado = cinemas[cinemas["setor"] == "Privado"]

private_vs_public = pd.DataFrame()
privados_vs_publicos["privados"] = pd.value_counts(privados["screens"])
privados_vs_publicos["publicos"] = pd.value_counts(publico["screens"])
privados_vs_publicos
```

... obteríamos um `DataFrame` como este:

||privados|publicos|
---|---|---|
1|91|66|
2|43|5|
3|21|2|
4|14|NaN|
5|15|NaN|
(..)|(..)|(..)

Isso nos permite comparar facilmente o número de telas em cinemas privados e públicos. Neste caso podemos dizer que temos 91 cinemas privados e 66 públicos com 1 ecrã. Também que não temos cinemas públicos com 4 ou 5 salas.

 

> 📞 Ligue para você! Deste [lote de dados sobre antenas telefônicas no Chile](https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=1436832020&single=true&output=csv), crie em seu caderno um `DataFrame` que contenha quantas antenas foram instaladas por região, nas décadas de 2000 e 2010, respectivamente:
>
>
> ||2000_decade|2010_decade|
> |---|---|---|
> |I|100|50|
> |II|20|30|
> |III|30|10|
> |(...)|
>
> Em seguida, responda às perguntas abaixo.


<style>
#hint-section .table {
  width: fit-content; 
}
blockquote .table {
  background: white;
  border-radius: 5px;
  margin: 9px 0;
}

</style>