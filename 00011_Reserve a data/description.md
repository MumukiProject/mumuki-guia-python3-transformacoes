⏰ Finalmente, chegou _a hora_ de lidar com... horas! (e datas 😛). Embora em Python tenhamos tipos como [`date`, `time` e `datetime`](https://docs.python.org/3/library/datetime.html), ao carregá-los de um CSV os receberemos como strings 😔. Felizmente, mais uma vez, `pandas` tem a solução com a funçao `to_datetime`. Você pode imaginar o que ela faz?

> Responda quais afirmações estão corretas depois de tentar as seguintes expressões em ordem em seu caderno:
>
```python
cruzeiristas.info()
```
>
```python
cruzeiristas["date"] = pd.to_datetime(cruzeiristas["date"])
```
>
```python
cruzeiristas.info()
```