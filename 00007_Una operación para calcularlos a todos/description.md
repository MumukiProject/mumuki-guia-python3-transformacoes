Otra forma de crear columnas es a partir de operaciones _escalares_ aplicadas a cada uno de sus valores. ¿Qué, qué? 🤨 ¡Veámoslo con un ejemplo de `cines`! Supongamos que tenemos un `DataFrame` con datos de población y extensión de disintos `paises`... 

|country|population|area|
|---|---|---|
|Argentina|39921833|1073513|
|Bolivia|8989046|424162|
|Brazil|188078227|3287942|
|Chile|16134219|291931|
|Colombia|43593035|440829|
|Mexico|107449525|758445|


...y necesitamos hacer algunos cálculos sobre éstos. :eyes: Pero si miramos detenidamente, notaremos que el área no está expresada en kilómetros cuadrados (km²) como esperaríamos, sino en millas cuadradas (mi²), lo cual ocurrirá con cierta frecuencia al usar lotes de datos expresados en el [sistema anglosajón](https://es.wikipedia.org/wiki/Sistema_anglosaj%C3%B3n_de_unidades) :shrug:. 

Para resolver esto, podemos aplicar, justamente, una operación escalar: 

```python
paises["area"] = paises["area"] * 2.59 # conversión imprecisa pero rápida de mi² a km²
```

:rainbow: Ahora, nuestra área estará expresada en la unidad correcta: 

|country|population|area|
|---|---|---|
|Argentina|39921833|2780400|
|Bolivia|8989046|1098581|
|Brazil|188078227|8515770|
|Chile|16134219|756102|
|Colombia|43593035|1141748|
|Mexico|107449525|1964375|

(:pencil: _los valores del ejemplo fueron redondeados por claridad_)

>  :first_place: ¡Pongámoslo en práctica! Cuando estudiemos gastos o precios, usualmente haremos ajustes por inflación, es decir, multiplicaremos a todos los valores monetarios por un cierto coeficiente. 
> 
> :money_with_wings: Sabiendo eso, escribí una función `ajustar_gastos` que tome un `DataFrame` con la misma estructura de nuestra tabla de `cruceristas` y un coeficiente, y devuelva una **nueva** tabla con todos sus gastos actualizados apropiadamente.
