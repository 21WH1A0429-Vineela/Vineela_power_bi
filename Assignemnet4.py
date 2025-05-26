class Department:
    department_count = 0 
    def __init__(self,deptname, deptid, loc, hodname):
        self.deptname = deptname
        self.deptid = deptid
        self.loc = loc
        self.hodname = hodname
        Department.department_count += 1 
    def display_department_info(self):
        print("Department Information: ")
        print("........................")
        print(f"Department Name : {self.deptname}")
        print(f"Department Id : {self.deptid}")
        print(f"location : {self.loc}")
        print(f"HOD Name : {self.hodname}")
    
    @classmethod
    def get_total_departments(cls):
        return cls.department_count


no_of_dept = int(input("Enter no.of dept: "))
departments = {}

for i in range(no_of_dept):
    print(f"Enter details for Department")
    name = input("Enter Department Name: ")
    dept_id = int(input("Enter Department ID: "))
    location = input("Enter Location: ")
    hod = input("Enter HOD name: ")
    dept = Department(name, dept_id, location, hod)
    departments[name] = dept
    
for dept in departments.values():
    dept.display_department_info()
    
    
search_name = input("Enter deprtment name: ")
if search_name in departments:
    print("Found")
else:
    print("Not Present")

print(f"Total Department: {Department.get_total_departments()}")
        