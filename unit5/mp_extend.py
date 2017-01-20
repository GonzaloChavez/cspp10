#Worked With Andres

original = [100,200,300]
extension = [400,500,600]

def extend(original, extension):
    for element in extension:
        original.append(element)
        
extend(original,extension)    

print(original)