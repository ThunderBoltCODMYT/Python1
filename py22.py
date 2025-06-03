#default argument
def vol_cube(L):
    V=L*L*L
    return V

def vol_cuboid(L=10,B=5,H=7):
    V=L*B*H
    return V

L1=int(input("Enter length of cube: "))
print(vol_cube(L1))
L2=int(input("Enter length of cuboid: "))
B2=int(input("Enter width of cuboid: "))
H2=int(input("Enter height of cuboid: "))
print(vol_cuboid(L2,B2,H2))