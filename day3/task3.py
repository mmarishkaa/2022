# input , % , if , +=   >>გამოყენებით
#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი 
#აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს ჯამი

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
oddsum = 0
if num1%2==1:
    print("odd")
    oddsum+=num1
if num2%2==1:
    print("odd")
    oddsum+=num2
if num3%2==1:
    print("odd")
    oddsum+=num3

print(oddsum)