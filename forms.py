from flask_wtf import FlaskForm
from wtforms import StringField,DateField
from wtforms.fields.html5 import EmailField, TelField, IntegerField # can be accessed under the wtforms.fields.html5 namespace

class LoginForm(FlaskForm):
    #Step 1: Ensure LoginForm instances have the attributes necessary to establish Heirarchy.
    # Next, we make sure the UI can record these details.

    #User Details
    name = StringField('First Name:', id='name')
    middle_name = StringField('Middle Name:', id='name')
    last_name = StringField('Last Name:', id='name')
    date_of_birth = StringField('Date of Birth:', id='name') #This is a mistake, for analytics, this needs to be a DateField-Both on the form and on SQL.
    village = StringField('Village:', id='name')
    district = StringField('District:', id='name')
    state = StringField('State:', id='name')
    postoffice = StringField('Post Office:', id='name')
    pincode = IntegerField('Pincode:', id='name')

    #Family Details
    father_name = StringField('Father\'s Name:', id='name')
    father_aadhaar = IntegerField('Father\'s Aadhaar ID', id='name')
    mother_name = StringField('Mother\'s Name:', id='name')
    grandfather_name = StringField('Grandfather\'s Name:', id='name')
    grandfather_aadhaar = IntegerField('Grandfather\'s Aadhaar ID', id='name')
    grandmother_name = StringField('Grandmother\'s Name:', id='name')


