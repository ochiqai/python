from collections import Counter


a = 10
str1 = "salam"
l = [1,2,3,4,5]

l_str = ['A', 'B', 'C']
lugat = {'book': "kitob, o'qiydigan narsa", "unique": "tanho yagona"}
sondanharfga = {0:"A", 1:"B", 2:"C"}
print(lugat['book'])
print(sondanharfga[0])

bormi = 'cat' in lugat

print(lugat.keys())
print(lugat.values())

for k, v in lugat.items():
    print(k, ":", v)

gollar_soni = {"Ronaldo": 100, "Pele": 200, "Messi": 250}

for key, value in gollar_soni.items():
    if value > 100 and key == "Messi":
        print(key)


l_sonlar = [1,1,1,1,2,2,2,2,4,4,4,4,5,6,7,7,8,1]
print(Counter(l_sonlar))

sondanharfga = {0:"A", 1:"B", 2:"C"}
sondanharfga[3] = "D"

L = []
D = {} # dict()


