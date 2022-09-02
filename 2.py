dog={}
#here created dictionary
dog={'name':[],'color':[],'breed':[],'legs':[],'age':[]}
#add name,color and other 
print(dog)
#printing dog
student={'first_name':[],'last_name':[],'gender':[],'age':[],'martial status':[],'skills':[],'country':[],'city':[],'address':[]}
#created another dictionary
print(student)
print(len(student))
#to print the length of the student
print(student['skills'])
print(type(student['skills']))
#here to know type of class
student['skills']+=['running','singing']
#adding two skills
print(student.keys()) 
print(student.values())