import sys
print("OPTIONS")
print("1.Add items to dictionary")
print("2.Sort them in Ascending Order")
print("3.Sort them in Descending Order")
print("4.Exit")
print("give choice in numbers like 1,2,3,4 etc")
dictionary1 = {}
while True:
            inp = input("Enter Your Choice")
            if inp=='1':
               key=input("insert Key")
               value=int(input("insert value"))
               dictionary1.update( {key : value} )
               print(dictionary1)
            elif inp=='2':

              print (sorted(dictionary1.items(),key=lambda kv:kv[1]))
            elif inp=='3':
                print(sorted(dictionary1.items(), key=lambda kv: kv[1], reverse=True))
            elif inp=='4':
               sys.exit()
            elif inp=='5':
                key=input("Enter the key you want to delete from dictionary ")
                result = dictionary1.pop(key,None)
                print("Deleted item's value = ", result)
                print("Updated Dictionary :", dictionary1)
            else:
                print("Enter valid choice")
