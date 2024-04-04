#the authors' names are Abby Newton and Viviana Antimo
def my_get_method(key, default):
    dictionary={"a":1,"b":2,"c":3}
    if key in dictionary:
        return dictionary[key]
    else:
        return default

print(my_get_method("a",0))
print(my_get_method("d",7))
print(my_get_method("d","hi"))
print(my_get_method("d",False))
print(my_get_method("d",7.77))

