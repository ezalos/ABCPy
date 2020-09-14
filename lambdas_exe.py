lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

lst_2=sorted(lst, key=lambda x: x[1][-1])

print(lst_2)

def lambda_to_gen(index=0):
    return lambda x: x[1][index]

index = int(input("Choose your index: "))
lst_2=sorted(lst, key=lambda_to_gen(index))
print(lst_2)

