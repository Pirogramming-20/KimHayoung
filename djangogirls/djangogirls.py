#파이썬 시작하기

len(str(304023))

name = 'Ola'
print(name)
name = "sonja"
print(name)

a = 4
b = 6
print(a*b)

city = "tokyo"
print('city')
print(city)

lottery = [3, 42, 12, 19, 30, 59]
lottery.append(199)
print(lottery)
lottery.sort()
print(lottery)
lottery.reverse()
print(lottery)
print(lottery[4])
lottery.pop(0) #왜 199가 아니라 19가 나오지?
print(lottery)
print(' ')

participant = {

    'name': 'Ola', 
    'country': 'Poland', 
    'favorite_numbers': [7, 42, 92]

    }
print(participant['name'])
print(participant['country'])
print(participant['favorite_numbers'])
#participant['favorite_numbers'] = 'python'
participant['favorite_numbers'].append('python')
len1 = len(participant['favorite_numbers'])
print(len1)
print(participant['favorite_numbers'])
participant['country'] = 'germany'
print(participant)
print(' ')

print(2>3)
print( 5 > 2*2)
print( 5 != 2)
print(1 == 1 )
print( 6 >= 12/2 )
print(3 <=2  )
print( 3 < 1)
print( 6> 2 and 6 <3) #false
print( 6 <2 or 6<8) #true
print( 3>2 and 2>1) #true

a = 2>5
print(a)
print(' ')

if 3 >2 : 
    print("it's true!")

if 5>2 : 
    print("this is ture")
else :
    print("this is false")


name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

volume = 19
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
    print('volume : ', volume)

print(' ')

def hi() :
    print("hi there!")
hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("$")

def hi(name) : 
    print('hello', name)
hi('hayoung')

def hi(name):
    print('hello', name)
girls = ['a', 'b', 'c', 'd']
for name in girls : 
    hi(name)

for i in range(1, 11) :
    print(i) 










