Adicionar novas colunas a uma tabela existente é fácil: basta usar o operador de atribuição em uma coluna específica!


```python
tabela["coluna"] = uma_series
```

Quando fazemos isso, se a coluna ainda não existir, ela será criada, caso contrário será substituída. O verdadeiro problema então consiste em _com o que_ atribuir essa coluna. Como podemos gerar `Series` que sejam úteis? 🤔

Uma forma é usar `map` 🗺️, que  transforma valores com base em um dicionário. Se, por exemplo, quisermos categorizar mais facilmente `cinemas` públicos, privados e comunitários em uma nova coluna `sector_type`, poderíamos fazer isso:


```python
ムcinemas["sector"]
0          Privado comercial
1          Privado comercial
2          Privado comercial
3          Público municipal
4          Privado comercial
               ...          
324        Privado comercial
325        Privado comercial
326        Público nacional
327        Público municipal
328        Privado independente

ムcinemas["sector_type"] = cinemas["sector"].map({
    "Público municipal": "Público", 
    "Público provincial": "Público", 
    "Público nacional": "Público", 
    "Privado comercial": "Privado", 
    "Otros": "Comunitarios e Independientes",
    "Privado independiente": "Comunitarios e Independientes",
    "Privado comunitario": "Comunitarios e Independientes"})
ムcinemas["sector_type"]
0                            Privado
1                            Privado
2                            Privado
3                            Público
4                            Privado
                   ...              
324                          Privado
325                          Privado
326                          Público
327                          Público
328    Comunitarios e Independientes
```

Caso não tenhamos contemplado nenhum valor de entrada teremos `nan` na coluna. Por exemplo, se tivéssemos omitido `"Público municipal"` do nosso `map`, o `sector_type` teria sido deixado como `nan` nas linhas correspondentes a esse setor:

```python
ムcinemas["sector_type"] = cinemas["sector"].map({
    "Público provincial": "Público",
    "Público nacional": "Público",
    "Privado comercial": "Privado",
    "Otros": "Comunitarios e Independientes",
    "Privado independiente": "Comunitarios e Independientes",
    "Privado comunitario": "Comunitarios e Independientes"})
ムcinemas["sector_type"]
0                            Privado
1                            Privado
2                            Privado
3                                NaN
4                            Privado
                   ...              
324                          Privado
325                          Privado
326                          Público
327                              NaN
328    Comunitarios e Independientes
```

> Vamos testar! Escreva uma expressão que permita criar a coluna `region` (_região_) em nosso `DataFrame` com o valor `"Nacional"` para cruzeiros do Uruguai 🇺🇾 e `"Regional"` para os cruzeiros da Argentina 🇦🇷 e do Brasil 🇧🇷. Não precisamos nos preocupar com o resto dos países por enquanto.
