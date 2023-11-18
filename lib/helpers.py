from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def getDepartmentsOrEmployees(cls):
    if (cls == Department or cls == Employee):
        return cls.get_all();
    else: raise Exception("the class was not of the correct type!");

def listDepartmentsOrEmployees(cls):
    if (cls == Department or cls == Employee):
        deporemps = cls.get_all()
        for depemp in deporemps: print(depemp);
    else: raise Exception("the class was not of the correct type!");

def list_departments(): listDepartmentsOrEmployees(Department);

def list_employees(): listDepartmentsOrEmployees(Employee);


def getTypeString(cls):
    if (cls == Department or cls == Employee):
        if (cls == Department): return "department";
        else: return "employee";
    else: raise Exception("the class was not of the correct type!");

def findDepartmentOrEmployeeByName(cls):
    if (cls == Department or cls == Employee):
        typestr = getTypeString(cls);
        name = input(f"Enter the {typestr}'s name: ");
        deporemp = cls.find_by_name(name);
        print(deporemp) if deporemp else print(f'{typestr.capitalize()} {name} not found');
    else: raise Exception("the class was not of the correct type!");

def find_department_by_name(): findDepartmentOrEmployeeByName(Department);

def find_employee_by_name(): findDepartmentOrEmployeeByName(Employee);

def getDepartmentOrEmployeeById(cls, mid):
    if (cls == Department or cls == Employee):
        #use a trailing underscore not to override the built-in id function
        #id_ = ...
        return cls.find_by_id(mid);
    else: raise Exception("the class was not of the correct type!");

def findDepartmentOrEmployeeById(cls):
    if (cls == Department or cls == Employee):
        #use a trailing underscore not to override the built-in id function
        #id_ = ...
        typestr = getTypeString(cls);
        mid = int(input(f"Enter the {typestr}'s id: "));
        deporemp = getDepartmentOrEmployeeById(cls, mid);
        print(deporemp) if deporemp else print(f'{typestr.capitalize()} {mid} not found');
    else: raise Exception("the class was not of the correct type!");

def find_department_by_id(): findDepartmentOrEmployeeById(Department);

def find_employee_by_id(): findDepartmentOrEmployeeById(Employee);


def getInputsForDepartmentOrEmployee(cls, dscstr=""):
    if (cls == Department or cls == Employee):
        #in additon to name, employee has job_title, and department_id in the constructor
        #the location is like job title
        if (type(dscstr) == str): pass;
        else: raise Exception("description string must be a string!");
        typestr = getTypeString(cls);
        mstrs = [];
        mstrs.append(input(f"Enter the {typestr}'s {dscstr}name: "));
        locjobstr = "";
        if (typestr == "department"): locjobstr = "location";
        else: locjobstr = "job title";
        mstrs.append(input(f"Enter the {typestr}'s {dscstr}{locjobstr}: "));
        if (typestr == "department"): pass;
        else: mstrs.append(input(f"Enter the employee's {dscstr}department id: "));
        return mstrs;
    else: raise Exception("the class was not of the correct type!");

def createDepartmentOrEmployee(cls):
    if (cls == Department or cls == Employee):
        #in additon to name, employee has job_title, and department_id in the constructor
        #the location is like job title
        typestr = getTypeString(cls);
        inputsarr = getInputsForDepartmentOrEmployee(cls, "");
        try:
            if (typestr == "employee"): depemp = cls.create(inputsarr[0], inputsarr[1], int(inputsarr[2]));
            else: depemp = cls.create(inputsarr[0], inputsarr[1]);
            print(f'Success: {depemp}');
        except Exception as exc:
            print(f"Error creating {typestr}: ", exc)
    else: raise Exception("the class was not of the correct type!");

def create_department(): createDepartmentOrEmployee(Department);

def create_employee(): createDepartmentOrEmployee(Employee);


def updateDepartmentOrEmployee(cls):
    if (cls == Department or cls == Employee):
        typestr = getTypeString(cls);
        mid = int(input(f"Enter the {typestr}'s id: "));
        if deporemp:= cls.find_by_id(mid):
            try:
                inputsarr = getInputsForDepartmentOrEmployee(cls, "new ");
                deporemp.name = inputsarr[0];
                deporemp.location = inputsarr[1];
                if (typestr == "employee"): deporemp.department_id = int(inputsarr[2]);

                deporemp.update();
                print(f'Success: {deporemp}');
            except Exception as exc:
                print(f"Error updating {typestr}: ", exc);
        else:
            print(f'{typestr.capitalize()} {mid} not found');
    else: raise Exception("the class was not of the correct type!");

def update_department(): updateDepartmentOrEmployee(Department);

def update_employee(): updateDepartmentOrEmployee(Employee);


def delDepartmentOrEmployee(cls):
    if (cls == Department or cls == Employee):
        typestr = getTypeString(cls);
        mid = int(input(f"Enter the {typestr}'s id: "));
        if deporemp := cls.find_by_id(mid):
            deporemp.delete()
            print(f'{typestr.capitalize()} {mid} deleted')
        else:
            print(f'{typestr.capitalize()} {mid} not found')
    else: raise Exception("the class was not of the correct type!");

def delete_department(): delDepartmentOrEmployee(Department);

def delete_employee(): delDepartmentOrEmployee(Employee);

# You'll implement the employee functions in the lab

def list_department_employees():
    #if we got the department id, we could at least select the department
    #we can list all employees or all departments from above
    #first get the department
    #get a list of all of the employees,
    #then take the list of employees and filter by department
    cls = Department;
    typestr = getTypeString(cls);
    mid = int(input(f"Enter the {typestr}'s id: "));
    dep = getDepartmentOrEmployeeById(cls, mid);
    if (dep):
        emps = getDepartmentsOrEmployees(Employee);
        for emp in emps:
            if (emp.department_id == int(mid)): print(emp);
    else: print(f'{typestr.capitalize()} {mid} not found');
