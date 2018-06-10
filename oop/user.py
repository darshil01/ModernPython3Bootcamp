# import pdb

class User:
    
    active_users = 0

    def __init__(self, first, last, age=21):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

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

user1 = User("Joe", "Smith")
user2 = User("Jim", "Jones", 123)
user3 = User("Bob", "Thompson", 23)

# print(user1.is_senior())
# print(user2.initials())
# print(user3.likes("Ice Cream"))
# print(user2.birthday())

print(User.active_users)
print(user2.logout())
print(User.active_users)