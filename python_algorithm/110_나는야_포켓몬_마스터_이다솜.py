"""
제목 : 나는야 포켓몬 마스터 이다솜
문제 주소 : https://www.acmicpc.net/problem/1620
작성일 : 2022/08/16
"""

"""
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
"""

"""
Pikachu
26
Venusaur
16
14
"""

n, m = map(int, input().split())

dict_list = {}
quiz_list = []
for i in range(n + m):
    if i < n:
        dict_list[i + 1] = input()
    else:
        quiz_list.append(input())

dict_list_v = {}
for x, y in dict_list.items():
    dict_list_v[y] = x

for x in quiz_list:
    if x.isdigit():
        print(dict_list.get(int(x)))
    else:
        print(dict_list_v.get(x))

