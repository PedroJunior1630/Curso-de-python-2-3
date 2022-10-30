for var in range(1,51):
    if var % 2 == 0:
        print(f"\033[1;32m{var}",end=" ")
#outra forma

for var2 in range(2,51,2):
    print(f"\n{var2}",end=" ")
