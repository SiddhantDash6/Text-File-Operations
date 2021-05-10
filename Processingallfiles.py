import glob2
filenames = glob2.glob('file2*.txt')
output = []
for text_file in filenames:
    with open(text_file, encoding="utf8") as f:
        for line in f.readlines():
            output.append(line)

    with open("allRawFiles.txt", 'w', encoding="utf8") as f1:
        for line in output:
            f1.write(line)