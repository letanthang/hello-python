import sys
print("helo python world!")
if sys.argv[1] == 'yes':
    print("you said yes")
elif sys.argv[1] == 'no':
    print("you said no")
print(sys.argv[0:])

for i in range(1, 11):
    print(i, end='')

print()
arr = [1, 2, 3, "a", "b"]
arr.append(44)
arr[3] = 4
print(arr)

for i in arr:
    print(i, end='')

print()
dic = {
    "tram": "tran thi bich tram",
    "thang": "le tan thang",
    "age": -100.1,
    "money": 1.1,
}

print("The one name %s at the age %i has the money of %f" %
      (dic["thang"], dic["age"], dic["money"]))
# print(dic)

for key in dic:
    print("%s->%s" % (key, dic[key]))

for key, value in dic.items():
    print("%s->%s" % (key, value))
