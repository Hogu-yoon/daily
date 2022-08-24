"""수정중"""

제목 = input("제목")
주소 = input("제목").replace(" ","_")+".py"

파일명 = 제목.replace(" ","_")+".py"




print(제목)

# for x in zip(title,add,date,pure_title):
"""
f = open(파일명, "w", encoding="utf-8")
f.write(f"\"\"\"\n 제목 : 제목\n문제 주소 : {x[1]},\n작성일 : {x[2]}\n\"\"\"")
f.close()
"""