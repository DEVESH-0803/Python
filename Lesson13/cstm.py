from random import choice

name = 'Devesh'

profession = 'Software Trainer'

age = 26

def skills():
   language = ['Python', 'Java', 'HTML', 'CSS', 'JavaScript', 'SQL']

   index = choice("012345")
   print(language[int(index)])


# Prevents code from running automatically when module is imported
# if __name__ == "__main__":
#    skills()