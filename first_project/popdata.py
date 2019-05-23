import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
# Import settings
django.setup()

from first_app.models import Employee
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        # Create Fake Data for entry
        fake_name = fakegen.name()
        fake_email = fakegen.email()

        # Create new Webpage Entry
        Employee.objects.get_or_create(empname=fake_name,empemail=fake_email)

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')