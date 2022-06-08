from dadata import Dadata
token = "442b94d3eb75c60f41c4212ff90538763c7b3e17"
dadata = Dadata(token)
result = dadata.suggest("address", "воронеж, пр-т патриотов д.31/2 кв.40")

print(result)