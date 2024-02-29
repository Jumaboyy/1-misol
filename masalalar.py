# 1-masala
#
# import  csv
#
# mevalar= [
#     ["id", "produst name", "product price", "kg"],
#     [1, "apple", 10000, 10],
#     [2, "kiwi", 15000, 20],
#     [3, "banana", 22000, 15],
#     [4, "cherry", 8000, 18]
#     ]
# with open("product_info.csv", mode="w", newline="") as file:
#  writer = csv.writer(file)
#  writer.writerows(mevalar)
#
# print("Ma'lumotlar faylga yozildi.")

# 2- masala

import csv

mevalar= [
    ["id", "produst name", "product price", "kg"],
    [1, "apple", 10000, 10],
    [2, "kiwi", 15000, 20],
    [3, "banana", 22000, 15],
    [4, "cherry", 8000, 18]
    ]
file=open("product_info.csv", "w")
writer=csv.writer(file)
for i in mevalar:
    writer.writerow(i)

file2=open("product_max.csv", "w")
writer2=csv.writer(file2)
writer2.writerow(mevalar[0])
for j in mevalar[1:]:

    if j[2]>12000:
        writer2.writerow(j)
file2.close()
print("Ma'lumotlar faylga yozildi.")



# 3-masala

# file=open("orazin_yopqach.txt","w")
# file.write(" Orazin yopqach ko'zumdin sochilur har lahza yosh,\n "
#            "O'ylakim paydo bo'lur yulduz, nihon bo'lg'ach quyosh.\n "
#            "Qut bir bodomu yerim go'shan mehrob edi,\n"
#            " G'orati din etti nogah bir baloliq ko'zu qosh.\n"
#            " Bu damodam ohim ifsho aylar ul oy ishqini,\n "
#            "Subhnung bot-bot dami andog'ki aylar mehr fosh.\n "
#            "Bo'sae qilmas muruvvat, asru qattiqdur labing,\n "
#            "Desam og'zi ichra aytur la'l ham bor nav' tosh.\n "
#            "Novaking ko'nglimga kirgach jon talashmoq bu ekin,\n"
#            " Kim qilur paykonini ko'nglum bila jonim talosh.\n "
#            "Umri jovid istasang fard o'lki, bo'ston Xizridur,\n "
#            "Sarvkim da'b ayladi ozodaliq birla maosh.\n "
#            "Qoshi ollinda Navoiy bersa jon, ayb etmangiz,\n"
#            " Gar budur mehrob, bir-bir qo'ygusidir barcha bosh.")
# file.close()
#
# file=open("orazin_yopqach.txt","r")
#
# def read_line(line,file):
#     content = file.read()
#     elements= content.split("\n")
#     if len(elements)>=line:
#
#         return elements[line-1]
#     else:
#         raise ValueError("kiritgan sonda qator yo`q")
# print(read_line(int(input('Kerakli sonni kiriting: ')),file))

