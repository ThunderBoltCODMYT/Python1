#Write to check if a person is buying oranges for 100rs and then later selling it for 120rs did he make a profit or loss?

B=int(input("Enter your buying price: "))
S=int(input("Enter your selling price: "))
if B>S:
    print("You made a loss of", B-S,"Rs")
elif S>B:
    print("You made a profit of", S-B,"Rs")