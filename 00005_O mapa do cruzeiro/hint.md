`map` pode utilizar não apenas um dicionário como argumento, mas também uma função que transforma individualmente cada elemento:


```python
def transformar_setor(sector):
  if sector.startswith("Público"):
    return "Público"
  elif sector == "Privado comercial":
    return "Privado"
  else:
    return "Comunitarios e Independientes"
   
ム cines["sector"].map(convertir_setor)
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

Se achar melhor pra você, também poderá resolver este exercício dessa forma… 
