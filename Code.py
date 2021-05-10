my_file = open("allRawFiles.txt",'r', encoding = "utf8")

Japanese_file = open("Japanese_part.txt",'w', encoding = "utf8")
English_file = open("English_part.txt",'w', encoding = "utf8")
iv = False
iv1 = False
for line in my_file:
    if '//' in line:
        iv = True
        if iv == True:
            Japanese_file.write(line)
    elif '<0' in line:
        iv1 = True
        if iv1 == True:
            English_file.write(line)
    else:
        print("Blank Line Present")

my_file.close()
Japanese_file.close()
English_file.close()
# Jpline = []

# for index, item in enumerate(string_list):
#     if .startswith("//"):
#         print(string_list)

# for element in string_list:
#     if element[0] == "/":
#         Jpline.append(element)
# print(Jpline)
# my_file.close()

# line = "{}\n".format(Jpline)
# Japanese_file.write(line)
# Japanese_file.close()
