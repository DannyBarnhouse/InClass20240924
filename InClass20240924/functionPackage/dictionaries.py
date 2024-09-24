# dictionaries.py

def demo():
    """
    Demonstrate basic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
       
    # iterate by key/value
    for item in myDictionary.items():
        print(item)
        
    # iterate by value
    for value in myDictionary.values():
        print(value)
        
    # add a key value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"  
    
    print(len(myDictionary))
    
    # cause an exception. add try/except logic
    try:
        print(myDictionary["Ohio State"])
    except :
        print("Failed")
        
    # remove Xavier bby key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # create another dictionary called newTeams
    # add several key/value pairs
    # combine thaat with my Dictionary and print the results
    newTeams = {"Alabama":"Crimson Tide","Georgia":"Bulldogs","Notre Dame":"Fighting Irish","Kentucky":"Wildcats"}
    myDictionary.update(newTeams)
    print(myDictionary)

    