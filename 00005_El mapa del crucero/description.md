Agregar nuevas columnas a una tabla existente es sencillo: ¡sólo tenemos que usar el operador de asignación sobre una columna en particular! 

```python
tabla["columna"] = un_series
```

Cuando hacemos ésto, si la columna no existe ya, será creada, y en caso contrario, será reemplazada. El verdadero problema entonces consiste en _con qué_ asignar esa columna. ¿Cómo podemos generar `Series` que nos sean útiles? 🤔

Una forma consiste en usar`map` 🗺️, que nos permitirá transformar valores en base a un diccionario. Si por ejemplo quisiéramos categorizar de forma más sencilla los `cines` públicos, privados y comunitarios en una nueva columna `sector_type`, podríamos hacer esto:

```python
ム cines["sector"]
0          Privado comercial
1          Privado comercial
2          Privado comercial
3          Público municipal
4          Privado comercial
               ...          
324        Privado comercial
325        Privado comercial
326         Público nacional
327        Público municipal
328    Privado independiente

ム cines["sector_type"] = cines["sector"].map({
    "Público municipal": "Público", 
    "Público provincial": "Público", 
    "Público nacional": "Público", 
    "Privado comercial": "Privado", 
    "Otros": "Comunitarios e Independientes",
    "Privado independiente": "Comunitarios e Independientes",
    "Privado comunitario": "Comunitarios e Independientes"})
ム cines["sector_type"]
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

En caso que no hayamos contemplado algún valor de entrada tendremos `nan` en la columna. Por ejemplo, si hubiéramos omitido `"Público municipal"` en nuestro `map`, el `sector_type` hubiera quedado como `nan` en las filas correspondientes a ese sector.: 

```python
ム cines["sector_type"] = cines["sector"].map({
    "Público provincial": "Público",
    "Público nacional": "Público",
    "Privado comercial": "Privado",
    "Otros": "Comunitarios e Independientes",
    "Privado independiente": "Comunitarios e Independientes",
    "Privado comunitario": "Comunitarios e Independientes"})
ム cines["sector_type"]
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


> ¡Probémoslo! Escribí una expresión que te permita crear la columna `region` en nuestro `DataFrame`  con el valor `"Nacional"` para los cruceros de Uruguay 🇺🇾 y  `"Regional"` para aquellos de Argentina 🇦🇷 y Brasil 🇧🇷. No nos vamos a preocupar por el resto de países por ahora. 
