def count_digits(number):
    
    return len(str(abs(number)))  


number = int(input("Enter a number: "))


total_digits = count_digits(number)


print(f"The total number of digits in {number} is {total_digits}")
