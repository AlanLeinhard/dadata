from dadata import Dadata
token = "442b94d3eb75c60f41c4212ff90538763c7b3e17"
dadata = Dadata(token)
result = dadata.suggest("address", "Лазань")
print(result)