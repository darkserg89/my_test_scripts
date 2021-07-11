from faker import Faker
from random import choice

def gen_pass():
    '''This function generate password based on user name and date'''
    lst_pass = []
    fake = Faker()
    lst_pass = [fake.first_name()+fake.last_name()+fake.year() for i in range(100)]
    return choice(lst_pass)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print([gen_pass() for i in range(10)])

