#This program converts a decimal number up to 128 into its binary equivalent

decimal = int(input("Enter Decimal Number : "))
d = decimal
l = []

if(decimal>0 and decimal<=128):
	while(decimal>0):
		binary = decimal%2
		binary = str(binary)
		# print(binary)
		l.append(binary)
		decimal = decimal//2
	while(len(l)!=8):
		l.append('0')
	v = l[::-1]
	print("The binary for "+str(d)+" is "+''.join(v))

elif(decimal>128):
	print("Sorry!! Can't convert numbers beyond 128")
else:
	print("Sorry!! Can't convert negative numbers")