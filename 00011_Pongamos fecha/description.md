⏰ A _la hora_ de trabajar con datos frecuentemente vamos a tener que lidiar con … ¡horas! (y fechas 😛). Si bien en Python contamos con tipos como [`date`, `time` y `datetime`](https://docs.python.org/3/library/datetime.html), al cargarlas desde un CSV las recibiremos como strings 😔. Por suerte, una vez más, `pandas` tiene la solución con `to_datetime`. ¿Te imaginás que hace?

> Respondé qué afirmaciones son correctas luego de probar en en tu cuaderno las siguientes expresiones en orden:
>
```python
cruceros.info()
```
>
```python
cruceros["date"] = pd.to_datetime(cruceros["date"])
```
>
```python
cruceros.info()
```
