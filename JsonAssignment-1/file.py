# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.
import json
python_dict={'employee 1':{'Name':'Saikuamar Konakanchi',
                           'DOB':'21/09/2002',
                           'Height':'6ft',
                           'City':'Hyderabad',
                           'State':'Telanagana'},
            'employee 2':{'Name':'Praneeth',
                          'DOB':'21/09/2002',
                          'Height':'6ft',
                          'City':'DilsukhNagar',
                          'State':'Telanagana'},
            'employee 3':{'Name':'Vyshnav',
                          'DOB':'21/09/2002',
                          'Height':'6ft',
                          'City':'Khammam',
                          'State':'Telanagana'},
            'employee 4':{'Name':'Kripal',
                          'DOB':'21/09/2002',
                          'Height':'6ft',
                          'City':'Secunderabad',
                          'State':'Telanagana'},
            'employee 5':{'Name':'Hithesh-Programmer',
                          'DOB':'21/09/2002',
                          'Height':'6ft',
                          'City':'LB_Nagar',
                          'State':'Telanagana'}}
with open('employee.json','w') as f:
    x=json.dump(python_dict,f,indent=10)
print()

#Expected Output:
# {
#           "employee 1": {
#                     "Name": "Saikuamar Konakanchi",
#                     "DOB": "21/09/2002",
#                     "Height": "6ft",
#                     "City": "Hyderabad",
#                     "State": "Telanagana"
#           },
#           "employee 2": {
#                     "Name": "Praneeth",
#                     "DOB": "21/09/2002",
#                     "Height": "6ft",
#                     "City": "DilsukhNagar",
#                     "State": "Telanagana"
#           },
#           "employee 3": {
#                     "Name": "Vyshnav",
#                     "DOB": "21/09/2002",
#                     "Height": "6ft",
#                     "City": "Khammam",
#                     "State": "Telanagana"
#           },
#           "employee 4": {
#                     "Name": "Kripal",
#                     "DOB": "21/09/2002",
#                     "Height": "6ft",
#                     "City": "Secunderabad",
#                     "State": "Telanagana"
#           },
#           "employee 5": {
#                     "Name": "Hithesh-Programmer",
#                     "DOB": "21/09/2002",
#                     "Height": "6ft",
#                     "City": "LB_Nagar",
#                     "State": "Telanagana"
#           }
# }



class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name=name
        self.dob=dob
        self.height=height
        self.city=city
        self.state=state

    def __str__(self):
        return f'Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}'
    
def main():
    employee_list=[]
    with open('employee.json','r') as f:
        employee_data=json.load(f)
    for emp_id, emp_info in employee_data.items():
        employee = Employee(emp_info['Name'], emp_info['DOB'], emp_info['Height'], emp_info['City'], emp_info['State'])
        employee_list.append(employee)

    for employee in employee_list:
        print(employee)
main()

#Expected Output:
# Name: Saikuamar Konakanchi, DOB: 21/09/2002, Height: 6ft, City: Hyderabad, State: Telanagana
# Name: Praneeth, DOB: 21/09/2002, Height: 6ft, City: DilsukhNagar, State: Telanagana
# Name: Vyshnav, DOB: 21/09/2002, Height: 6ft, City: Khammam, State: Telanagana
# Name: Kripal, DOB: 21/09/2002, Height: 6ft, City: Secunderabad, State: Telanagana
# Name: Hithesh-Programmer, DOB: 21/09/2002, Height: 6ft, City: LB_Nagar, State: Telanagana  



# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

seven_states={'Telanagana':'Hyderabad','AndhraPradesh':'Amaravathi','UtterPradesh':'Noida','Gujarat':'GandhiNagar','HimachalPradesh':'Shimla','Haryana':'Chandighar','Jammu_Kashmir':'Srinagar'}
with open('seven_states.json','w') as f:
    x=json.dump(seven_states,f,indent=5)

#Expected Output:
# {
#      "Telanagana": "Hyderabad",
#      "AndhraPradesh": "Amaravathi",
#      "UtterPradesh": "Noida",
#      "Gujarat": "GandhiNagar",
#      "HimachalPradesh": "Shimla",
#      "Haryana": "Chandighar",
#      "Jammu_Kashmir": "Srinagar"
# }