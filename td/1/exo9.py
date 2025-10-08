def fusion_dict(d1, d2):
    for key, value in d2.items():
        if key in d1:
            if isinstance(value, int):
                d1[key] += value
            elif isinstance(value, list):
                d1[key] = list(set(d1[key] + value))
        else:
            d1[key] = value

d1 = {1: 10, 2: 20, 'a': [1, 2, 3]}
d2 = {1: 5, 2: 15, 'a': [2, 3, 4], 'b': 100}
fusion_dict(d1, d2)
print(d1)


            
