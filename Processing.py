my_file = open("0.txt", encoding = "utf8")
string_list = my_file.readlines()
# print(string_list[0])

for index, item in enumerate(string_list):
    if string_list[0].startswith("//"):
        print(string_list)

my_file.close()