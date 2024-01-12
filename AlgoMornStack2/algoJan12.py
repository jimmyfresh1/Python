
keys1 = ["abc", 3, "yo"]
vals1 = [42, "wassup", True]

def zip(keys,values):

    dict = {}
    x=range(3)
    print(x)

    for n in x:
        dict[keys[n]] = values[n]
        print(dict)


zip(keys1,vals1)

# dictionary_container = zip_into_dictionary(keys1,vals1)
# print(dictionary_container)