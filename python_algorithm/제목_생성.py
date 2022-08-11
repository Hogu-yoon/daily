
file = open("test.txt", "r", encoding='utf-8')
title = []
pure_title = []
k = 1
while True:
    f_read = file.readline()
    if not f_read:
        break
    pure_title.append(f_read.strip())
    f_read = f'{k}_{f_read.strip().replace(" ","_")}.py'
    # 전각문자 한자 ㄱ + 9
    f_read = f_read.replace("?","？")

    title.append(f_read)
    k += 1
file.close()

add = []
with open("add.txt","r") as f:
    while True:
        f_read = f.readline().strip()
        if not f_read:
            break
        add.append(f_read)
date = []
with open("date.txt","r") as f:
    while True:
        f_read = f.readline().strip()
        if not f_read:
            break
        date.append(f_read)

for x in zip(title,add,date,pure_title):
    f = open(x[0], "w", encoding="utf-8")
    f.write(f"\"\"\"\n 제목 : {x[3]}\n문제 주소 : {x[1]},\n작성일 : {x[2]}\n\"\"\"")
    f.close()

