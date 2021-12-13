
class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Name: "+self.citizen_name)
        print("Price: "+self.citizen_age)
        print("Author: "+self.citizen_dob)
        print("Book was published in: "+self.citizen_id)
        print("Book Added")
        
citizen1 = Citizen("Harry poter and the Philosopher's stone","₹1,928","J.K Rowling","1997 , 25 years ago")
citizen1.add_citizen()

citizen2 = Citizen("Diary of a Wimpy kid","₹700","Jeff Kenny","2017 , 5 years ago")
citizen2.add_citizen()

    