# try:
#     file = open("./day_30/a_file.txt")
#     a_dict = {"key" : "value"}
#     print(a_dict["asvqvqvdfasdf"])
# except FileNotFoundError:
#     file = open("./day_30/a_file.txt", "w")
#     file.write("Somthing")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This in an error that I made up!")




height = float(input("Height : "))
weight = int(input("Weight : "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)