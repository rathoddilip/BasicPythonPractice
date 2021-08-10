# dictionary nothing but kay value pair
myDict = {"subject": "python",
          "marks": [20],
          "teacher": "Ashish Ogale",
          "anotherDic": {"grade": "A+"}
          }
print("Subject: ", myDict["subject"])
print("Teacher Name: ", myDict["teacher"])
# dictionary within dictionary
print("Grade: ", myDict["anotherDic"]["grade"])

# methods
print("keys: ", myDict.keys())
print("Values: ", myDict.values())
print("items: ", myDict.items())
# typecast dictionary to list
print("type cast dic to list:", list(myDict.keys()))

# add new value to dictionary

updateDict = {
    "university": "pune",
}
myDict.update(updateDict)
print("updated dictionary: ", myDict)

# get particular value based on keys using get method

print(myDict.get("subject"))

favLang = {}
stud1 = input("enter your favorite lang Dilip\n")
stud2 = input("enter your favorite lang Sandip\n")
stud3 = input("enter your favorite lang Arjun\n")
stud4 = input("enter your favorite lang Ranjit\n")

favLang["dilip"] = stud1
favLang["sandip"] = stud2
favLang["arjun"] = stud3
favLang["ranjit"] = stud4

print(favLang)
