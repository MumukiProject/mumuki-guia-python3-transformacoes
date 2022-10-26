Al trabajar con lotes de datos, es frecuente que los nombres de sus columnas no nos fascinen. Por suerte tenemos la solución, ¡`rename`! 

`rename` nos permite, a través de un diccionario, renombrar columnas. Por ejemplo, si tuviéramos el siguiente lote `personas` con una elección de nombres _polémica_...

com_name|ag|add|count|
---|---|---|---|
Ricardo Guiraldes|60|Rua das pedras 1000|Brazil|
Billy Summers|42|5th Avenue 2332|USA|
Anna Prado|37|San Martin 1165|Argentina|

...y quisiéramos obtener el `DataFrame` con sus columnas renombradas podríamos escribir:

```python
personas.rename(columns = {
    "com_name": "complete_name",
    "ag": "age",
    "add": "address",
   "count": "country"
})
```

complete_name|age|address|country|
---|---|---|---|
Ricardo Guiraldes|60|Rua das pedras 1000|Brazil|
Billy Summers|42|5th Avenue 2332|USA|
Anna Prado|37|San Martin 1165|Argentina|

Para que esta operación tenga efecto en el `DataFrame` original deberíamos escribir… ¡exacto, `inplace=True`!

> ¡Ahora te toca a vos!  Renombrá en el `DataFrame` en tu cuaderno  las columnas `loc_code`, `prov_id` y `dep_id` por `city_id`, `province_id` y `department_id` respectivamente.
