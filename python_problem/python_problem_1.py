
def brGame(player, num): 

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
        print(f"{player} : {num}")
        if num >= 31:
            return num
    return num

def playBR31():
    num = 0
    while num < 31:
        num = brGame("playerA", num)
        if num >= 31:
            print("playerB win!")
            break
        num = brGame("playerB", num)
        if num >= 31:
            print("playerA win!")
            break


playBR31()
    
        