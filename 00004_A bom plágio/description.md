Já eliminamos e renomeamos colunas, agora vamos aprender a adicionar novas! :heavy_plus_sign:

No entanto, antes disso, vamos te ensinar a fazer uma cópia de um `DataFrame`. Mas, por que? Isso porque às vezes vamos querer  preservar um estado particular de um `DataFrame` e fazer modificações em uma cópia do mesmo...

```python
copia = tabela.copy()
# agora modificamos a cópia
del copia["coluna"]
```

...e se nos arrependemos poderemos ainda usar o `DataFrame` original, ou até restaurar para a versão anterior:

```python
# a tabela original ainda está com a coluna eliminada!
pd.value_counts(tabela["coluna"])
# restauramos a versão original 
cópia = tabela.copy()
```

> Cole o seguinte código em seu caderno e vamos embarcar ao próximo exercício 🚢:
>
> ```python
> import pandas as pd
> cruzeiros_originais = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6> u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=751983160&single=true&output=csv")
> cruzeiros = cruzeiros_originais.copy()
> ```
