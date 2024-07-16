t = int(input())
s = int(input())
sot1 = t // 100
des1 = t // 10 % 10
ed1 = t % 10
sot2 = s // 100
des2 = s // 10 % 10
ed2 = s % 10
per1 = sot1 * 10 + sot2
per2 = des1 * 10 + des2
per3 = ed1 * 10 + ed2
sum = per1 + per2 + per3
kor = sum ** 0.5
print(kor)

