from pprint import pprint
#from the pprint module, import the pprint
#dictionaries
d = {
    #key    : value
    "name":"chen",
    "birthmonth":"August",
    "grade":16
}
pprint(d)

schedule = {
    "A": "SE11",
    "B": "SE12",
    "C": "SE13",
    "D": "SE14",
}
#add a key value pair where the key is "E"
#   and the value is "holla"
schedule['E'] = "holla"
print(schedule['E'])

#ONLY checks if it exists as a key(not as a value)
if 'E' in schedule:
    print("E is in schedule")
else:
    print("E is not in schedule")
    
#how to check if a value exists
for key in schedule:
    print(key)