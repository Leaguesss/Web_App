'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''

from bottle import get, post, error, request, static_file
from app import app
from app import model





#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@app.route('/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='app/static/img/')

#-----------------------------------------------------------------------------

# Allow CSS
@app.route('/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='app/static/css/')

#-----------------------------------------------------------------------------

# Allow javascript
@app.route('/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='app/static/js/')

#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to login
@app.route('/',method = ['GET'])
@app.route('/home',method = ['GET'])
def get_index():
    '''
        get_index
        
        Serves the index page
    '''
    return model.index()

#-----------------------------------------------------------------------------

# Display the login page
@app.route('/login',method = ['GET'])
def get_login_controller():
    '''
        get_login
        
        Serves the login page
    '''
    return model.login_form()

#-----------------------------------------------------------------------------

# Attempt the login and register
@app.route('/login',method = ['POST'])
def post_login():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'email' and 'password' fields
    '''

    # Handle the form processing
    #login
    email = request.forms.get('email')
    password = request.forms.get('password')

    
    #sign up 
    signup_username = request.forms.get('signup-username')
    signup_email= request.forms.get('signup-email')
    signup_password = request.forms.get('signup-password')
    signup_confirmpass = request.forms.get('signup-confirmpass')

    if email == None and password == None:
        # call the appropriate method sign up
        return model.signup_check(signup_username.lower(), signup_email.lower(), signup_password,signup_confirmpass)
    # Call the appropriate method
    return model.login_check(email.lower(), password)




#-----------------------------------------------------------------------------

@app.route('/logout',method = ['GET'])
def get_logout_controller():
    return model.logout_check()


#-----------------------------------------------------------------------------
@app.route('/add_user', method = ['POST','GET'])
def add_user():
    new_name = request.forms.get('new_name')
    new_email = request.forms.get('new_email')
    new_password = request.forms.get('new_password')
    return model.add_user_check(new_name, new_email, new_password)


#-----------------------------------------------------------------------------

@app.route('/mute',method = ['POST'])
def mute_user():

    return model.muteUser()


@app.route('/admin',method = ['POST'])
def remove_user(deleted_email):
    return model.remove_user(deleted_email)


@app.route('/admin',method = ['POST'])
def change_status(email):
    return model.change_users_status(email)
#-----------------------------------------------------------------------------

# Display the admin page
@app.route('/admin',method = ['GET'])
def get_admin_controller():
    '''
        get_admin
        
        Serves the admin page
    '''
    return model.admin_form()
    
#-----------------------------------------------------------------------------

# Display the Message page
@app.route('/message',method = ['GET'])
def get_message_controller():
    '''
        get_message
        
        Serves the message page
    '''
    mes = model.get_messages()
    return model.message_form(content = mes)
#-----------------------------------------------------------------------------
# Post the content from Message page
@app.route('/message',method = ['POST'])
def post_message():
    '''

        get_message
        
        Serves the message page
    '''
    # Receive username from user
    send_to_user = request.forms.get('username')

    message_sent = request.forms.get('message')
    return model.send_message(send_to_user, message_sent)







@app.route('/about',method = ['GET'])
def get_about():
    '''
        get_about
        
        Serves the about page
    '''
    return model.about()
#-----------------------------------------------------------------------------

@app.route('/contact',method = ['GET'])
def get_contact():
    '''
        get_contact
        
        Serves the contact page
    '''
    return model.contact()


#-----------------------------------------------------------------------------
@app.route('/bottle',method = ['GET'])
def get_bottle():
    '''
            get_bottle page
        
    '''
    comment = model.get_comment(0)
    return model.bottle_page(comment)


@app.route('/bottle',method = ['POST'])
def post_bottle():

    '''


        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,0)

@app.route('/css',method = ['POST'])
def post_css():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,1)

@app.route('/flask',method = ['POST'])
def post_flask():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,2)

@app.route('/http',method = ['POST'])
def post_http():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,3)


@app.route('/java',method = ['POST'])
def post_java():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,4)

@app.route('/javascript',method = ['POST'])
def post_javascript():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,5)

@app.route('/OSI_layers',method = ['POST'])
def post_OSI_layers():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,6)

@app.route('/python',method = ['POST'])
def post_python():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,7)

@app.route('/TCP_IP',method = ['POST'])
def post_TCP_IP():

    '''
    

        post comment to other page

    '''

    get_message = request.forms.get('comment')
    return model.add_new_comment(get_message,8)

#-----------------------------------------------------------------------------
@app.route('/flask',method = ['GET'])
def get_flask():
    '''
            get_flask page
        
    '''
    
    comment = model.get_comment(2)
    return model.flask_page(comment)

#-----------------------------------------------------------------------------
@app.route('/http',method = ['GET'])
def get_http():
    '''
            get_http page
        
    '''
    comment = model.get_comment(3)
    return model.http_page(comment)

#-----------------------------------------------------------------------------
@app.route('/java',method = ['GET'])
def get_java():
    '''
            get_java page
        
    '''
    comment = model.get_comment(4)
    return model.java_page(comment)

#-----------------------------------------------------------------------------
@app.route('/OSI_layers',method = ['GET'])
def get_OSI_layers():
    '''
            get_OSI_layers page
        
    '''
    comment = model.get_comment(6)
    return model.OSI_layers_page(comment)

#-----------------------------------------------------------------------------
@app.route('/python',method = ['GET'])
def get_python():
    '''
            get_python page
        
    '''
    comment = model.get_comment(7)
    return model.python_page(comment)

#-----------------------------------------------------------------------------
@app.route('/TCP_IP',method = ['GET'])
def get_TCP_IP():
    '''
            get_TCP_IP page
        
    '''
    comment = model.get_comment(8)
    return model.TCP_IP_page(comment)

#-----------------------------------------------------------------------------
@app.route('/css',method = ['GET'])
def get_css():
    '''
            get_css page
        
    '''
    comment = model.get_comment(1)
    return model.css_page(comment)

#-----------------------------------------------------------------------------
@app.route('/javascript',method = ['GET'])
def get_javascript():
    '''
            get_javascript page
        
    '''
    comment = model.get_comment(5)
    return model.javascript_page(comment)

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors
@app.error(404)
def error(error): 
    return model.handle_errors(error)


