def fun1():
    fun2()
    print('This is first function')

def fun2():
    fun3()
    print('this is second function ')


    while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print("After reverse : %d" %reverse) 


while(i < n):
			# Pick a random index
			# from 0 to i.
			j = random.randrange(i+1);
			
			# If the randomly picked
			# index is smaller than k,
			# then replace the element
			# present at the index
			# with new element from stream
			if(j < k):
				reservoir[j] = stream[i];
			i+=1;
		
		print("Following are k randomly selected items");
		printArray(reservoir, k);