#Worked With Andres
original = [1,2,1,4,1]
target = 1
original.count(1)

def remove_all(original, target):
   for x in range(original.count(target)):
       original.remove(target)
	        
remove_all(original, target) 
print(original)