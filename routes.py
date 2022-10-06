from flask import render_template, request, redirect, url_for
import forms

""" 
Generate the login form (using flask) for the index.html page, where you will 
enter a new user. The form itself is created in forms.py. 
The index() route method is called from app.py
"""
def index():
    form = forms.LoginForm()
    return render_template('index.html', form=form)

""" 
Retrieve all the rows from the database and return them.
All the data will be displayed on entire_database.html file.
The view_database() route method is called from app.py
"""
def view_database():
    from app import get_all_rows_from_table
    rows = get_all_rows_from_table()
    
    return render_template('entire_database.html', rows=rows)

def modify_database(the_id ,modified_category):
    if request.method == 'POST':
        from app import modify_data
        # Get data from the form on database page
        user_input = request.form[modified_category]
        # modify the row from the database
        modify_data(the_id, modified_category, user_input)
        # redirect back to the database page
        return redirect(url_for('view_database'))
    return redirect(url_for('index'))

def delete(the_id):
    if request.method == 'POST':
        from app import delete_data
        # if the checkbox was selected (for deleting entire row)
        if 'remove' in request.form:
            delete_data(the_id)
    return redirect(url_for('view_database'))

def submitted():
    #Step 4: Adjust these routes here, once they are done, they will be successfully inserted into the 'info.db' database.
    #Then adjust the contents of entire_database.html to visualize the db on the UI.
    from app import insert_data
    if request.method == 'POST':
        name = request.form['name']
        midname = request.form['middle_name']
        lastname = request.form['last_name']
        dob = request.form['date_of_birth']
        village = request.form['village']
        district = request.form['district']
        state = request.form['state']
        postoffice = request.form['postoffice']
        pincode = request.form['pincode']

        fathname = request.form['father_name']
        mothname = request.form['mother_name']
        grandmothname = request.form ['grandmother_name']
        grandfathname = request.form['grandfather_name']
        fath_aadhaar = request.form['father_aadhaar']
        grandfath_aadhar = request.form['grandfather_aadhaar']



        # insert data into database
        insert_data(name, midname, lastname, dob,village,district,state,postoffice,pincode,fathname,mothname,grandmothname,grandfathname,fath_aadhaar,grandfath_aadhar)

    return render_template('submitted.html')