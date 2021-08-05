'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
from os import error
from app import view
import random

from bottle import template

from bottle import response, request, redirect

from app.sql import SQLDatabase

from datetime import datetime

import random, string

#-----------------------------------------------------------------------------
#mydatabase
#-----------------------------------------------------------------------------

SQLDatabase = SQLDatabase()
SQLDatabase.database_setup()

# Initialise our views, all arguments are defaults for the template
page_view = view.View()


#-----------------------------------------------------------------------------
#Cookie secret_key
#This method returns a string which represents random bytes suitable for cryptographic use.
#-----------------------------------------------------------------------------

secret_key = "secret-key-abcabc"


error_ = [";","#","&","'","<",">","-"]
special_error_message = " Sorry! No Special Characters Allowed ; # & ' < > - , or can not exceed 100 characters"

def user_input_sanitation(string):
    if len(string) > 100:
        return True
    for i in error_:
        if i in string: # find special characters
            return True
    return False
    

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index():
    '''
        index
        Returns the view for the index
    '''
    #check if user already logged in
    user_information = SQLDatabase.token_userinfo()
    if user_information != None:
        return page_view("index", header = "login_header")
    else:
        return page_view("index")

    

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    #check if user already logged in
    user_information = SQLDatabase.token_userinfo()
    
    #user_ already logged in
    if user_information != None:
        return page_view("invalid", header = "login_header" ,reason="You Already Logged In")
    else:
        return page_view("login")

#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(email, password):
    '''
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''
    
    if user_input_sanitation(email):
        return page_view("invalid", reason=special_error_message)

    if user_input_sanitation(password):
        return page_view("invalid", reason=special_error_message)
    isuser, information = SQLDatabase.check_credentials(email,password)

    if isuser:
        token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(24))
        SQLDatabase.add_user_session(token,information[0])
        response.set_cookie('my_token',token,secret=secret_key)
        redirect('/home')
        return
    else:
        return page_view("invalid", reason=information)



#-----------------------------------------------------------------------------
#Register
#-----------------------------------------------------------------------------
def signup_check(signup_username, signup_email, signup_password,signup_confirmpass):
    if user_input_sanitation(signup_username):
        return page_view("invalid", reason=special_error_message)
    if user_input_sanitation(signup_email):
        return page_view("invalid", reason=special_error_message)
    if user_input_sanitation(signup_password):
        return page_view("invalid", reason=special_error_message)
    if user_input_sanitation(signup_confirmpass):
        return page_view("invalid", reason=special_error_message)



    if signup_password != signup_confirmpass:
        return page_view("invalid", reason="Password does not match") 


    found =  SQLDatabase.fetch_email_username(signup_username,signup_email)

    if found:
        return page_view("invalid", reason="Email or Username already token") 
    else:
        SQLDatabase.add_user(signup_username,signup_email,signup_password)
        return page_view("login")


#-----------------------------------------------------------------------------
#Message
#-----------------------------------------------------------------------------

def message_form(content=""):

    #check if user already logged in
    user_information = SQLDatabase.token_userinfo()

    
    #user_ already logged in
    if user_information != None:
        # return template("templates/message.html", content = content)
        return page_view("message",header="login_header", content = content)
    else:
        return page_view("invalid", reason="Please Login To access this feature")




#-----------------------------------------------------------------------------
#Logout
#-----------------------------------------------------------------------------
def logout_check():
    #check if user already logged in
    user_information = SQLDatabase.token_userinfo()
    if user_information != None:
        token = request.get_cookie('my_token', secret=secret_key)
        SQLDatabase.delete_user_session(token)
        response.delete_cookie('my_token')
        return page_view("invalid",reason="Successful Loged Out, See You Next Time!")

    else:
        return page_view("invalid", reason="You Have Not Logged in")
    



    
#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

def about():
    '''
        about
        Returns the view for the about page
    '''
    user_information = SQLDatabase.token_userinfo()

    if user_information != None:
        return page_view("about", header = "login_header",garble=about_garble())
    else:
        return page_view("about",garble=about_garble())



# Returns a random string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.", 
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

#-----------------------------------------------------------------------------
# contact
#-----------------------------------------------------------------------------

def contact():
    '''
        contact
        Returns the view for the contact page
    '''
    user_information = SQLDatabase.token_userinfo()

    if user_information != None:
        return page_view("contact", header = "login_header")
    else:
        return page_view("contact")

#-----------------------------------------------------------------------------
# admin
#-----------------------------------------------------------------------------


def admin_form():
    '''
    
        Returns the view for the admin page
    '''
    user_information = SQLDatabase.token_userinfo()
        
    
    if user_information != None: #already logged in
        if user_information[3] == 1:
            all_users = SQLDatabase.get_all_user_info()

            result = "<ul>"
            id = "<h3>ID:</h3>" 
            name = "<h3>Name:</h3>" 
            email = "<h3>Email:</h3>" 
            status = "<h3>Status:</h3>" 
            
            for i in all_users:
                admin_status = "yes"
                if i[3] != 1:
                    admin_status = "no"

                result += '<li>' + id +str(i[0]) + name +str(i[1])+ email +str(i[2])+ status +admin_status+ ' <button type="submit" name = "mute'+ str(i[0]) + '"><font size="3">Mute/Unmute</font></button><button type="submit" name = "remove'+ str(i[0]) + '"><font size="3">Remove</font></button></li> '
                                
            ans =  result+"</ul>"

            return page_view("admin", header = "login_header",name=user_information[1], email=user_information[2], allusers=ans)
        else:
            return page_view("invalid", header = "login_header",reason="You are not admin")
    else:
        return page_view("invalid", reason="Please Login To access this feature")


    
#-----------------------------------------------------------------------------
# content
#-----------------------------------------------------------------------------

def bottle_page(comment):

    '''
    return bottle page
    '''
    

    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/bottle",header = "login_header",comment = comment)
    else:
        return page_view("content/bottle",comment = comment)


def flask_page(comment):
    '''
    return flask page
    '''
    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/flask",header = "login_header", comment = comment)
    else:
        return page_view("content/flask",comment = comment)


def http_page(comment):
    '''
    return http page
    '''
    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/http",header = "login_header", comment = comment)
    else:
        return page_view("content/http",comment = comment)


def java_page(comment):
    '''
    return java page
    '''
    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/java",header = "login_header", comment = comment)
    else:
        return page_view("content/java",comment = comment)


def OSI_layers_page(comment):
    '''
    return OSI_layers page
    '''

    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/OSI_layers",header = "login_header", comment = comment)
    else:
        return page_view("content/OSI_layers",comment = comment)


def python_page(comment):
    '''
    return python page
    '''
    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/python",header = "login_header", comment = comment)
    else:
        return page_view("content/python",comment = comment)


def TCP_IP_page(comment):
    '''
    return TCP_IP page
    '''

    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/TCP_IP",header = "login_header", comment = comment)
    else:
        return page_view("content/TCP_IP",comment = comment)


def css_page(comment):
    '''
    return css page
    '''
    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/css",header = "login_header", comment = comment)
    else:
        return page_view("content/css",comment = comment)


def javascript_page(comment):
    '''
    return javascript page
    '''
    user_information = SQLDatabase.token_userinfo()

    
    if user_information != None: #already logged in
        return page_view("content/javascript",header = "login_header", comment = comment)
    else:
        return page_view("content/javascript",comment = comment)


#-----------
# def get_message(username):
#     """
#     display all message in time descent order 
#     """
#     messages = SQLDatabase.get_messages(username)
#     print(messages)
#     return messages

def send_message(username, message):
    '''
    send message
    '''
    if user_input_sanitation(username):
        return page_view("invalid", header = "login_header", reason=special_error_message)

    if user_input_sanitation(message):
        return page_view("invalid", header = "login_header",reason=special_error_message)

    check_result = SQLDatabase.check_user_existence(username)
    if check_result == False:
        return page_view("invalid", header = "login_header",reason="The user you want to contact does not exist!")
    else:
        if SQLDatabase.token_userinfo()[4] == 1:
            return page_view("invalid", header = "login_header", reason="You have been blocked by admin and cannot send message!")
        elif username == SQLDatabase.token_userinfo()[1]:
            return page_view("invalid", header = "login_header", reason="You cannot send message to yourself!")
        SQLDatabase.add_message(message,username,SQLDatabase.token_userinfo()[1])
        
        return page_view("invalid", header = "login_header", reason="You have sent message successfully!")

def get_messages():

    user_information = SQLDatabase.token_userinfo()

    if user_information != None: #already logged in
        current_user = user_information[1]
        all_message = SQLDatabase.show_message()
        select_message = []
        for i in all_message:
            if i[2] == current_user and i[3] != i[2]:
                select_message.append((i[3],i[1],i[4]))

        sender = "<h3>Sender Name:</h3>" 
        message = "<h3>Message:</h3>" 
        time = "<h3>Time:</h3>" 
        total = "<ul>"

        for i,j,k in select_message:
            total += "<li>" +sender + str(i) + message + str(j) +time + str(k) + "</li>"
        
        return total + "</ul>"
    else:
        return page_view("invalid", reason="Please Login To access this feature")




def add_new_comment(get_message, page):



    pagename  = {6:"OSI_layers",8:"TCP_IP",3:"http",5:"javascript",1:"css",0:"bottle",2:"flask",4:"java",7:"python"}
    user_information = SQLDatabase.token_userinfo()
    if user_information != None:
        username  = user_information[1]
        if user_information[4] == 1:
            return page_view("invalid", header = "login_header", reason="You have been blocked by admin and cannot Comment!")
        

        if user_input_sanitation(get_message):
            return page_view("invalid", header = "login_header", reason=special_error_message)

        SQLDatabase.insert_comment(get_message, username, page)
        return page_view("invalid",header = "login_header",reason="comment successfully! ")
    else:
        return page_view("invalid", reason="Please Login To access this feature")


def get_comment(page):
    res = SQLDatabase.get_comment(page)
    sender = "<h3>User Name:</h3>" 
    comment = "<h3>Comment:</h3>"
    total = "<ul>" 
    for i,e in res:
        total += "<li>" +sender + str(i) + comment + str(e) + "</li>"

    return total + "</ul>"



    
#-----------------------------------------------------------------------------
# Admin
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Admin Add User Check
#-----------------------------------------------------------------------------
def add_user_check(username,email,password):



    user_information = SQLDatabase.token_userinfo()
    
    #already logged in
    if user_information != None: 
        
        #if the input not fill complete
        if username == None or email == None or password == None:
            return page_view("invalid",header="login_header",reason = "Sorry, You Have Not Fill All Required Information")
        else:
            username = username.lower()
            email = email.lower()

        #login user is not admin
        if user_information[3] != 1:
            return page_view("invalid",header="login_header",reason = "Premission denied, You Are not Admin")
        #login user is  admin
        elif user_information[3] == 1:
            found =  SQLDatabase.fetch_email_username(username,email)

            #Email or Username already token
            if found:
                return page_view("invalid",header="login_header" ,reason="Email or Username already token") 
            #successful
            else:
                if user_input_sanitation(username):
                    return page_view("invalid", header="login_header" ,reason=special_error_message)

                if user_input_sanitation(email):
                    return page_view("invalid", header="login_header" ,reason=special_error_message)

                if user_input_sanitation(password):
                    return page_view("invalid", header="login_header" ,reason=special_error_message)

                SQLDatabase.add_user(username,email,password)
                redirect("/admin")
                return
        #login user admin status error
        else:
            return page_view("invalid",header="login_header",reason = "Admin Type Error!") 
    #Does not Login
    else:
        return page_view("invalid",reason = "Please Login to access this feature")



#-----------------------------------------------------------------------------
# Admin Mute User 
#-----------------------------------------------------------------------------

def muteUser():
    

    user_information = SQLDatabase.token_userinfo()
    
    #already logged ina
    if user_information != None: 
                
        #login user is not admin
        if user_information[3] != 1:
            return page_view("invalid",header="login_header",reason = "Premission denied, You Are not Admin")
        #login user is  admin
        elif user_information[3] == 1:
            max_id = SQLDatabase.get_max_id()[0]
            for i in range(1,max_id+1):
                mutename = 'mute'+ str(i)
                removename = 'remove' + str(i)
                if request.forms.get(mutename) is not None:
                    if SQLDatabase.change_users_status(i):
                        redirect("/admin")
                        return
                elif request.forms.get(removename) is not None:
                        if SQLDatabase.remove_user(i):
                            redirect("/admin")
                            return
            
            return page_view("invalid",header="login_header",reason = "Random Unknow Error!") 


        #login user admin status error
        else:
            return page_view("invalid",header="login_header",reason = "Admin Type Error!") 
    #Does not Login
    else:
        return page_view("invalid",reason = "Please Login to access this feature")




#-----------------------------------------------------------------------------
# Debug
#-----------------------------------------------------------------------------

def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass


#-----------------------------------------------------------------------------
# 404
# Custom 404 error page
#-----------------------------------------------------------------------------

def handle_errors(error):
    error_type = error.status_line
    error_msg = error.body
    return page_view("error", error_type=error_type, error_msg=error_msg)
    