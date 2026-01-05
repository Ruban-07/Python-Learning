# Lesson 13 - If Statements & Comparisons

def find_max_num(num1,num2, num3):
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3
    

print(find_max_num(200,302,250))