while True:
    import random
    print ("\n*** Password *** ")
    g=input("Do you want to create random passwords? (y or n)=")
    if(g=="y" or g=="Y" or  g=="yes"):
    	a="1234567890"
    	b1="abcdefghijklmnopqrstuvwxyz"
    	b2=b1.upper()
    	c="*&^%$#@!`~"
    	z=a+b2+c+b1
    
    	n=int(input("\n Enter the length of password you want : "))
    	m=""
    	for i in range(0,n):
    		y=random.choice(z)
    		m+=y
    	print("\n"+ m)
    elif(g=="n" or g=="N" or g=="no"):
        print("OK.....THANK YOU")
        break 