def hello():
    print("hello user!")

def pack(arg1, arg2, arg3):
    return [arg1,arg2,arg3]

def eat_lunch(list_1):
    if len(list_1) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list_1)):
            if i == 0:
                print(f"First I eat {list_1[0]}")
            else:
                print(f"Next I eat {list_1[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])