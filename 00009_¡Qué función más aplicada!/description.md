En ocasiones nos toparemos con transformaciones más complejas, que no podremos resolver simplemente con operaciones entre escalares y columnas :slight_frown:. Para esos casos, contamos contamos con `apply`, que permite aplicar una función a cada fila de nuestra tabla, y retornar un nuevo `Series` con los resultados: 

```python
# al usar apply de esta forma, siempre debemos pasar el argumento axis="columns"
tabla.apply(funcion_que_transforma_una_fila_completa, axis="columns")
```

¡Eso nos va a permitir generar columnas más interesantes de forma sencilla! :open_mouth: Por ejemplo, si en el ejercicio anterior hubiéramos contado con una función que nos calculara directamente los gastos totales...

```python
# notá que un_crucerista no es un DataFrame, 
# sino un símil-diccionario que representa 
# una fila
def calcular_gastos_totales(un_crucerista):
  return (
      un_crucerista['tours_expenses'] +
      un_crucerista['feed_expenses'] +
      un_crucerista['transport_expenses'] +
      un_crucerista['shopping_expenses'] +
      un_crucerista['other_expenses']
    )
```

...podríamos haber generado `actual_total_expenses` así: 

```python
cruceristas["actual_total_expenses"] = cruceristas.apply(calcular_gastos_totales, axis="columns")
```

¡Y nos hubiera dado el mismo resultado! :tada:

```python
ム cruceristas["actual_total_expenses"]
0          0.00
1        200.00
2        100.00
3        600.00
4        200.00
          ...  
12011    257.84
12012    128.92
12013    257.84
12014    128.92
12015    257.84
```


> ¡Tu turno! Queremos estimar cuánto dinero se ingresó al país a través de cruceristas procedentes del extranjero. El mismo lo calcularemos como: 
>
>  * :flag_uy: `0`, para cruceristas provenientes de Uruguay;
>  * :earth_americas: la cantidad de personas en el grupo de cada crucerista (`total_people`), multiplicado por el gasto total (`total_expenses`), en cualquier otro caso.
> 
> Agregá a `cruceristas` una columna `estimated_foreign_income` con esta estimación.
