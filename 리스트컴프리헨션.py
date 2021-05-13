# r1 = ['a', 'b']
# r2 = ['c', 'd', 'e']
# r3 = []

# for i in r1:
#   for j in r2:
#       r3.append(i + j)
# -> 리스트 컴프리헨션을 이용해 간단히 표현 ^^



r1 = ['a', 'b']
r2 = ['c', 'd', 'e']

r3 = [x + y for x in r1 for y in r2]
print(r3)