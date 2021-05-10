# my_file = open("0.txt",'r', encoding = "utf8")

# Japanese_file = open("Japanese_part.txt",'w', encoding = "utf8")
# English_file = open("English_part.txt",'w', encoding = "utf8")
# iv = False
# iv1 = False
# for line in my_file:
#     if '//' in line:
#         iv = True
#         if iv == True:
#             Japanese_file.write(line)
#     elif '<0' in line:
#         iv1 = True
#         if iv1 == True:
#             English_file.write(line)
#     else:
#         print("Blank Line Present")
        
        


# my_file.close()
# Japanese_file.close()
# English_file.close()

# for i in range(0:4):
# f

filenames = ["0.txt", "1.txt", "2.txt"]
output = []
for text_file in filenames:
    with open(text_file, encoding="utf8") as f:
        for line in f.readlines():
            output.append(line)

    with open("test_file.txt", 'w', encoding="utf8") as f1:
        for line in output:
            f1.write(line)

# Japanese_file = open("Japanese_part.txt",'w', encoding = "utf8")
# English_file = open("English_part.txt",'w', encoding = "utf8")
# iv = False
# iv1 = False
# for line in my_file:
#     if '//' in line:
#         iv = True
#         if iv == True:
#             Japanese_file.write(line)
#     elif '<0' in line:
#         iv1 = True
#         if iv1 == True:
#             English_file.write(line)
#     else:
#         print("Blank Line Present")
        
import glob2

filenames = glob2.glob('*.txt') 

with open('outfile.txt', 'w', encoding="utf8") as f:
    for file in filenames:
        with open(file) as infile:
            f.write(infile.read()+'\n')     