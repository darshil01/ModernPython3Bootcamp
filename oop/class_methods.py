# import pdb

class User:
    
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
        
    @classmethod
    def data_from_str(cls, str_data):
        first, last, age = str_data.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age=21):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return self.first

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, Birthday {self.first}"

# user1 = User("Joe", "Smith")
# user2 = User("Jim", "Jones", 123)
# user3 = User("Bob", "Thompson", 23)
# print(User.display_active_users())

tom = User.data_from_str("Tom,Jones,34")
print(tom.first)
print(tom.full_name())
print(tom)

