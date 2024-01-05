num=0

count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

while not count.isdigit() or int(count) not in [1, 2, 3]:
    if not count.isdigit():
        print("정수를 입력하세요")
    else:
        print("1, 2, 3 중 하나를 입력하세요")
    count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
count = int(count)



for i in range(count):
    num += 1
    print(f"playerA: {num}")


count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

while not count.isdigit() or int(count) not in [1, 2, 3]:
    if not count.isdigit():
        print("정수를 입력하세요")
    else:
        print("1, 2, 3 중 하나를 입력하세요")
    count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
count = int(count)



for i in range(count):
    num += 1
    print(f"playerB: {num}")
    
        