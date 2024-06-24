#function to add,subtract,multiply,divide 

def add(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2

print("PLEASE SELECT OPERATION \n"
        "1. ADD\n"
        "2. SUBTRACT\n"
        "3. MULTIPLY\n"
        "4. DIVIDE\n")

#get input from user

select=int(input("SELECT OPERATIONS 1,2,3,4:"))
number_1=int(input("ENTER FIRST NUMBER:"))
number_2=int(input("ENTER SECOND NUMBER:"))

if(select == 1):
    print(number_1,"+",number_2,"=",add(number_1, number_2))
elif(select == 2):
    print(number_1,"-",number_2,"=",subtract(number_1, number_2))
elif(select == 3):
    print(number_1,"*",number_2,"=",multiply(number_1, number_2))
elif(select == 4):
    print(number_1,"/",number_2,"=",divide(number_1, number_2))
else:
    print("INVALID INPUT")
