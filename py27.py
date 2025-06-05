for i in range(1,21,3):
    if i == 10:
        break
    print(i)
print("*********************")
for i in range(1,21,3):
    if i%2 == 0:
        continue
    print(i)