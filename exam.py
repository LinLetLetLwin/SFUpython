x = int(input("Please enter exam result"))


if x < 101 and x > 89 or x == 100:
	print("A")
elif x < 89 and x > 79:
	print("B")
elif x < 79 and x > 59 or x == 80:
	print("C")
elif x < 59 and x > 49 or x == 60:
	print("D")
elif x < 49 and x > 0 or x == 0 or x == 49:
	print("F")
else:
	print("Check again")
100 -90  A
90 - 80  B
80 - 60  C
60 - 50  D
50 <     F