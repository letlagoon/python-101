Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_duplicate_values(dict_obj):
...     unique_values = set()
...     duplicates = []
...     for key, value in dict_obj.items():
...         if value in unique_values:
...             duplicates.append(value)
...         else:
...             unique_values.add(value)
...     return duplicates
... 
>>> Food = {'Apple':'10','Banana':'10','Orange':'20','Papaya':'50'}
>>> result = find_duplicate_values(Food)
>>> 
>>> for key, value in Food.items():
...     if value in result:
...         print(f"Key: {key}, Value: {value}")
... 
...         
Key: Apple, Value: 10
Key: Banana, Value: 10
