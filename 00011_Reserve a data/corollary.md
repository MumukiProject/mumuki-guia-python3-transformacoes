Exato!

Agora nossas datas são efetivamente datas. A vantagem de trabalhar com o tipo de dados correto é que agora temos operações específicas de data, como [`dt.year`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.year.html) e [`dt.month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month.html):

```python
ムcruzeiristas["date"].dt.year
0 2016
1 2016
2 2016
...
12014 2020
12015 2020

ムcruzeiristas["date"].dt.month
0 12
1 12
2 12
…
12014 1
12015 2
```

[Aqui](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html) você encontrará mais informações.