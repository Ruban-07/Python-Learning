# Lesson 18 - For Loop

cars = ["Bmw","Benz", "Audi", "Rolls Royce"]

for car in cars:
    print(car)

for letter in "Ruban":
    print(letter)
    
for car in range(len(cars)):
    print(cars[car])

for index in range(5):
    if index == 0:
        print("First Iteration!")
    else:
        print("Not a First Iteration!")