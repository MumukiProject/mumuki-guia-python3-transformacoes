:bulb: `map` no sólo puede tomar un diccionario como argumento, sino también una función que transforme individualmente a cada elemento:

```python

def convertir_sector(sector):
 if sector.startswith("Público"):
   return "Público"
 elif sector == "Privado comercial":
   return "Privado"
 else:
   return "Comunitarios e Independientes"

ム cines["sector"].map(convertir_sector)
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

 Si te resulta más cómodo, podés también resolver este ejercicio de esa manera. 
