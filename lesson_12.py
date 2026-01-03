# Lesson 12 - If Statements

is_male = False
is_tall = True

if is_male and is_tall:
    print("You're male!")
elif is_male and not(is_tall):
    print("You're short male!")
elif not(is_male) and is_tall:
    print("You're not male but tall!")
else:
    print("You're neither male nor tall!")