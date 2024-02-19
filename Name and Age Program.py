person1_age = int(input("Enter the age of person 1: "))
person1_name = input("Enter the name of person 1: ")
person2_age = int(input("Enter the age of person 2: "))
person2_name = input("Enter the name of person 2: ")

if person1_age > person2_age:
    print(person1_name ,"is older than", person2_name)
elif person1_age < person2_age:
    print(person2_name ,"is older than", person1_name)
else:
    print(person1_name ,"and", person2_name ,"are of the same age")