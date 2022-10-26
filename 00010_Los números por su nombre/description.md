Además de crear y modificar columnas en base a mapeos y cálculos, es frecuente que tengamos que convertir los tipos de datos de las mismas. ¿Por qué? Porque aunque en un mundo ideal todos los datos deberían estar adecuadamente representado...

  * por un lado, los formatos en que se distribuyen los lotes de datos a veces son muy limitados. Por ejemplo, los CSVs sólo soportan strings y números; :sweat: 
  * por otro lado, las personas cometemos errores y terminamos almacenando la información de manera incorrecta. :stuck_out_tongue_closed_eyes:

Ya sea por uno u otro motivo, deberemos hacer conversiones. `pandas` no se queda atrás y en respuesta a este problema nos provee funciones como `to_numeric` que transforma un string _numérico_ en... ¡un número!

```python
ム pd.to_numeric("97")
97
```

¡Y también funciona con `Series`!

```python
ム numeros_tramposos = pd.Series(["4", "9", "8"])
ム numeros_tramposos
0    4
1    9
2    8
dtype: object
ム pd.to_numeric(numeros_tramposos)
0    4
1    9
2    8
dtype: int64 # notá el cambio en esta línea 
```

> 🧪 ¡Hora de hacer experimentos! Realizá en tu cuaderno las pruebas que necesites y seleccioná las afirmaciones verdaderas:
