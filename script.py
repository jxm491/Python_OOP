# Accessing and Modifying Data:
# 1. The traditional way: make the data private and use getters and setters:

# Name Mangled

class User:
  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.password = password

  def get_email(self):
     return self._eamil

  def clean_email(self):
      return self._email.lower().strip()

user1 = User("dantheman", "          Dan@gmail.com", "123")
user2 = User("batman","bat@outlook.com","abc")

print(user1._email)
print(user1.clean_email())

# The "Consenting Adults" Philosophy - Developer responsibility, trusted to not
# access protected members unless absolutely necessary, can still be made private
# using double underscore