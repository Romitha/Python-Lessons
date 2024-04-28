# x = "python{}"
# y = 'elephant'
# z = """\nHello world....
#     jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
#     pppppppppppppppppppppppppppppppppppppppp
#     """
# # print(type(x),x)
# # checked the type.
# print(x,y,z)
# print(x[0])


# a = 0
# print(type(a))
# print(x.format(a))
# print(x+y+str(a))


# print(f"janith Algewatta {y}")

# b = 0.0
# print(type(b))

# print("configure git...")

#list
l1 = [1,2,3,"janith",0.0]
print(l1[3])
print(l1[0:4])
print(len(l1))

#tuple
tuple1 = (1,2,3,4)
print(tuple1)

is_created = False
is_failed = True
print(is_created, type(is_created))

if 2> 0:
    is_created = True

print(is_created)



set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(set1)

set2 = set({1, 2, 'Geeks', 4, 'For', 6, 'Geeks'})
print(set2)


dict = {}
dict1  = {
    "name": "Janith",
    "age": 16,
    "mobile": '0771818404'
}
dict2  = {
    "name": "Algewatta",
    "age": 16,
    "mobile": '0777100110'
}
print(dict1['mobile'])
list = []
list.append(dict1)
list.append(dict2)
print(list)

import pandas as pd

df = pd.DataFrame(list)
print(df.head())
print(type(df))