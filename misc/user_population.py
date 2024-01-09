class Username:
    population=0
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        Username.population+=1
    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

    @classmethod
    def user_population(cls):
        print(f"{cls.population} users in the program")

    @staticmethod
    def validate_age(age):
        is_valid = True
        if age <18:
            is_valid = False
        return is_valid
    
james = Username("James", "Fern", 29) 
dog = Username("dog", "dog", 10)
Username.user_population()

