¡Exacto!

Ahora nuestras fechas son efectivamente fechas. La ventaja de trabajar con el tipo de dato correcto es que ahora contamos con operaciones específicas de fechas, como por ejemplo [`dt.year`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.year.html) y [`dt.month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month.html): 

```python
ムcruceros["date"].dt.year
0        2016
1        2016
2        2016
...
12014    2020
12015    2020

ム cruceros["date"].dt.month
0        12
1        12
2        12
… 
12014     1
12015     2
```

[Acá](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html) vas a encontrar más información.
