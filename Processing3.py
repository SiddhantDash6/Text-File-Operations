import re
import glob
z = glob.glob('Japwrite01.txt')
# with open('English_part.txt', encoding="utf8") as fin, open('Engwrite.txt', 'w', encoding="utf8") as fout:
#     for line in fin:
#         matches = re.sub('<(.*?)>','',line)
#         fout.writelines(str(matches))


with open('Japanese_part.txt', encoding="utf8") as fin2, open('Japwrite01.txt', 'w', encoding="utf8") as fout2:
    for line1 in fin2:
        matches1 = re.sub('// <(.*?)> ','', line1)
        fout2.writelines(str(matches1))


# with open('Japwrite.txt','w+',encoding="utf8") as f:
#     d = f.readlines()
#     f.seek(0)
#     for i in d:
#         if i != "\//(.*)":
#             f.write(i)
#     f.truncate()
   
#     # def word_exists(wordlist, word_fragment):
#     #     return any(w.startswith(word_fragment) for w in wordlist)
#     # word_exists(fin3, "// NOTE:")

#     # fout3.writelines(fin3)

