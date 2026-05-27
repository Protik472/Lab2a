def calculate_bmi(weight, height):
    print("Height ="+str(height))
    print("Weight ="+str(weight))
    bmi = weight / (height ** 2)
    print("BMI ="+str(bmi))
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")
calculate_bmi(78, 1.75)

if __name__ == "__main__":
    pass