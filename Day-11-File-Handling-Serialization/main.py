file = open("notes.txt", "r")
print(file.read())
file.close()

file = open("notes.txt","r")
data = file.read()
file.close()


with open("notes.txt","r") as file:
    data = file.read()
print(data)

#writing files
with open("sample.txt","w") as file:
    file.write("Hello Mohammad")


#Appending data
with open("sample.txt","a") as file:
    file.write("\nNew Line")


#save json
import json
student = {
    "name":"Mohammad",
    "marks":95
}
with open("student.json","w") as file:
    json.dump(student,file)  

#load json
import json
with open("student.json","r") as file:
    data = json.load(file)
print(data)



#Convert object to dictionary first.
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("Mohammad")
data = {
    "name": s1.name
}
json.dump(data,f)
