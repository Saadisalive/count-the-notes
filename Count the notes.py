#taking total amount from user
Amount =int(input("please enter the amount for Withraw"))
 
 #calculating the number of notes of different denominations
note__1 = Amount//100
note__2 = (Amount%100)//50
note__3 = ((Amount%100)%50)//10

print("notes of 100 rupee",note__1)
print("notes of 50 rupee",note__2)
print("notes of 10 rupee",note__3)