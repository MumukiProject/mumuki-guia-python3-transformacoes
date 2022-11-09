Além de criar e modificar colunas com base em mapeamentos e cálculos, muitas vezes precisamos converter seus tipos de dados. Por quê? Porque embora em um mundo ideal todos os dados devam ser adequadamente representados...

  * por um lado, os formatos em que os lotes de dados são distribuídos às vezes são muito limitados. Por exemplo, os CSVs suportam apenas strings e números; :sweat:
  * por outro lado, as pessoas cometem erros e acabam armazenando informações de forma incorreta. :stuck_out_tongue_closed_eyes:

Seja por um motivo ou outro, devemos fazer conversões. Felizmente, `pandas` nos fornece `to_numeric` que transforma uma string de um número em... um número!

``` python
ム pd.to_numeric("97")
97
```

E funciona com `Series` também!

``` python
ム numeros_mentirosos = pd.Series(["4", "9", "8"])
ム numeros_mentirosos
0 4
1 9
2 8
dtype: objeto
ム pd.to_numeric(numeros_mentirosos)
0 4
1 9
2 8
dtype: int64 # observe a mudança nesta linha
```

> 🧪 Hora de experimentar! Faça os testes necessários em seu caderno e selecione as afirmações verdadeiras:
