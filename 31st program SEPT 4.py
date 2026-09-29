#Multiple Inheritance

class Hospital:                                        #hospital

    def __init__(self):
        self.hsptl_name=input("Enter Hospital Name :")
        self.location=input("Enter Location :")
        self.phone=int(input("Enter Phone no. :"))

    def display_hospital(self):
        print("Hospital Name :",self.hsptl_name,"\nLocation :",self.location,"\nPhone no. :",self.phone)

class Department:
    def __init__(self):
        self.dept_name = input("Enter Department Name :")
        self.doctor_name = input("Enter Doctor Name :")


    def display_department(self):
        print("Department Name :", self.dept_name, "\nDoctor Name :", self.doctor_name)

class Patient(Hospital,Department):
    def __init__(self):

        Hospital.__init__(self)                   #has multiple parents so instead of super()
        Department.__init__(self)                 # this is used.


        self.patient_name = input("Enter Patient Name :")
        self.age = int(input("Enter Age :"))
        self.gender = input("Enter Gender :")
        self.admission_date = input("Enter Admission Date :")
        self.bed = int(input("Enter Bed no. :"))
        self.discharge_date=""


    def full_summary(self):

        Hospital.display_hospital(self)
        Department.display_department(self)

        print("Patient Name :",self.patient_name,"\nAge :",self.age,"\nGender :",self.gender,"\nAdmission Date :",self.admission_date)
        print("Bed no. :",self.bed,)
        if self.discharge_date == "":        # new admission has no discharge date
            print("Not yet discharged")
        else:
            print("Discharged Date :", self.discharge_date)

    def set_discharge(self):
        self.discharge_date = input("Enter Discharge Date :")


p=Patient()
p.set_discharge()
p.full_summary()
