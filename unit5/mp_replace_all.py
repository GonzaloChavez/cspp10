#Worked With Andres
original = [1,2,1,4,1]
to_replace = 1
replace_with = "Andres is God and Gonzalo is Jesus"
def replace_all(original,to_replace,replace_with):
    for index in range(len(original)):
	    if original[index] == to_replace:
	        original[index] = replace_with
    
        
replace_all(original,to_replace,replace_with)
print(original)
