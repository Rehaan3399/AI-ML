"""#case 1-if the file is not present
f=open("Mohammad","W")
f.write("Hello world")
f.close()


#writing multiple line string
f=open("Sample.txt", 'w')
f.write("hello world")
f.write("\n how are you")
f.close()

#case 2 if the file is already present
f=open("Sample.text", 'w')
f.write("Salman khan")
f.close()

f=open('Sample.txt','a')
f.write('I am fine')
f.close()


#write lines
L=['helo\n', 'hi\n','how are you\n','I am the best\n']
f=open('Sample.txt','w')
f.writelines(L)
f.close()

#reading from files #read()
f=open("Sample.txt",'r')
s=f.read()
print(s)
f.close()


f=open("Sample.txt",'r')
print(f.readline(), end=" ")
print(f.readline()),  end="")
f.close()


#reading entire using readline
f=open('sample.txt','r')
while True:
    data=f.readline()
    if data=="":
        break
    else:
        print(data,end='')
f.close()   

#using Context Manager(With) #better instead of write close()
with open('Sample.txt','w') as f:
    f.write("Selmon bhai")


#Trying f.read() now
with open('Sample.txt', 'r') as f:
    print(f.read())"""

"""
#to laod a big file in memory
big_L=["hello world" for i in range(1000)]
with open('big.txt','w')as f:
    f.writelines(big_L)
"""

#Serialization
import json
student_data={#dictonary
    'name':'nitish',
    'age':33,
    'gender':'male'
}
#SERIALIZATION
with open('demo.json', "w") as f:
    json.dump(student_data, f)
#DESERIALIZATION
with open("demo.json", "r") as f:
    data=json.load(f) 
    print(data)
    print(type(data))
   



#Pickling  example
import pickle:
class Person:
    def display(self):
        print("Hello I am a python objcet i have powers")
#creating object for above class
p1=Person()
#pickling (storing object in binary file)
with open("my_object.pk1", "wb") as f:
    pickle.dump(p1,f)
#unpickling (taking object from file)
with open("my_object.pk1", "rb") as f:
    loaded_obj=pickle.load(f)
    loaded_obj.display()
          













