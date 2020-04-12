n=5
L=[]
for values in range(n):
        character=input("Enter Character :")
        L.append(character)
print("THE ARRAY IS :",L)
L.reverse()
print("REVERSE ARRAY IS :",L)
L.sort(reverse=True)
print("DESCENDNG ORDER IS :",L)