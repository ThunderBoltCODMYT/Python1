#diamond pattern
# diamond pattern
r = int(input("Enter the number of rows: "))
if r % 2 == 0:
    m = r // 2
else:
    m = r // 2 + 1

# Upper part
for i in range(1, m + 1):
    print(" " * (m - i), end="")
    num = 1
    for j in range(1, 2 * i):
        print(num, end="")
        num += 1
    print()

# Lower part
for i in range(m - 1, 0, -1):
    print(" " * (m - i), end="")
    num = 1
    for j in range(1, 2 * i):
        print(num, end="")
        num += 1
    print()