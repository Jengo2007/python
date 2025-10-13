name="Dovud"
age=17
height=175
print("My name",name,"\nI`m",age,"years old","\nMy height",height)



minut=60
hour=minut*60
day=hour*24
week=day*7
print("In week",week,"second")



age=int(input("Enter your age:"))
if age < 18:
    print("Ты  несовершеннолетний ")
elif age >=18 and age <65: 
    print("Ты взрослый")
else:
    print("Ты пенсионер")

# можно так же валидировать возраст до 0 и после условно 100


for i in range(1,21):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)




user=input()
result=user[::-1].upper()
print(result)

# Заполняй поле input на пример input("Введите что то")


fruits=["apple","orange","grape","melon","watermelon"]
fruits.append("peach")
fruits.remove("watermelon")
fruits.sort()
print(fruits)




cordinates=(11,22,33)
x,y,z=cordinates
print("x="x,"y="y,"z="z)
