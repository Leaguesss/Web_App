import sqlite3
from datetime import datetime

from bottle import request

import random
import string

import hashlib

# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call 
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self, database_arg="mydb.db"):
        self.conn = sqlite3.connect(database_arg, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.secret_key = "secret-key-abcabc"


    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------
    
    # Sets up the database
    # Default admin password
    def database_setup(self, admin_password='iamnotadmin!1221'):


        # Create the users table
        self.execute( """ 
            CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            username char(500) NOT NULL,  
            email char(500) NOT NULL, 
            password char(500) NOT NULL, 
            admin INTEGER DEFAULT 0,
            status INTEGER DEFAULT 0,
            salt char(30) NOT NULL,
            loginErrorCount INTEGER DEFAULT 0
            )""")
    
        self.commit()

        self.execute (
            """
            CREATE TABLE IF NOT EXISTS user_session (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            token char(50) NOT NULL,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id))
        """
        )
        self.commit()

        # Table that contain all user's message
        self.execute (
            """
            CREATE TABLE IF NOT EXISTS message_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            message char(500) NOT NULL,
            receiver char(500),
            sender char(500),
            send_time TimeStamp NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        self.commit()

        #Table contain all comment 
        #bottle:0 css: 1 flask:2 http:3 java:4 javascript:5 osi: 6 python:7 tcpip:8
        self.execute (
            """
            CREATE TABLE IF NOT EXISTS page_comment (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            message char(500) NOT NULL,
            sender char(500),
            page INTEGER
            );
        """
        )
        self.commit()


        # Add our admin user
        adminstatus = self.fetch_email_username('adminisgood','adminisgood@email.com')
        if not adminstatus:
            self.add_user(username = 'adminisgood', email = "adminisgood@email.com",password = admin_password, admin=1, status = 0)

    
    #-----------------------------------------------------------------------------
    # loginErrorCount Check
    #-----------------------------------------------------------------------------
    def loginErrorCount(self,email):

        sql_accountstatus = """SELECT loginErrorCount from users  where email = '{email}' """.format(email = email)
        self.execute(sql_accountstatus)
        user_accountstatus = self.cur.fetchone()

        return user_accountstatus



    
    
    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    #Random generater
    def random(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        char = ""
        for i in range(0,10):
            char += str(random.choice(alphabet))
        return char


    # Add a user to the database
    def add_user(self, username, email, password,admin=0,status = 0,salt=0):
        salt = self.random()

        salt_pass = str(salt) + password
        hashed_saltpass = hashlib.md5(salt_pass.encode()).hexdigest()

        sql_cmd = """
                INSERT INTO users (username, email ,password, admin, status,salt)
                VALUES('{username}', '{email}','{password}',{admin},{status},'{salt}')
            """

        sql_cmd = sql_cmd.format(username=username, email = email, password=hashed_saltpass, admin=admin,status = status,salt=salt)
        self.execute(sql_cmd)
        self.commit()

        return True

    #-----------------------------------------------------------------------------

    # Check login credentials

    def adjust_errorplusone(self,email):
        #loginErrorCount INTEGER DEFAULT 0,

        sql_cmd = """
                UPDATE users
                SET loginErrorCount = loginErrorCount + 1
                WHERE email = '{email}' """.format(email = email)
                
        self.execute(sql_cmd)
        self.commit()
        
        return True


    def adjust_loginErrorCount(self,email):
        sql_cmd = """
                UPDATE users
                SET loginErrorCount = 0
                WHERE email = '{email}' """.format(email = email)
        self.execute(sql_cmd)
        self.commit()
        return True

    


    def check_credentials(self, email, password):
        sql_query = """SELECT * FROM users WHERE email = '{ema}' """.format(ema = email)
        

        self.execute(sql_query)
        # If our query returns
        user_information = self.cur.fetchone()

        if user_information: # if user exists
            user_accountstatus = self.loginErrorCount(email)
            print(user_accountstatus)

            if user_accountstatus[0] >= 10: #account lock
                return False, "User Account Permanently Locked, and Please Contact Us to Unlock Your Account:("
            else:
                salt = user_information[6]
                salt_pass = salt + password
                hashed_saltpass = hashlib.md5(salt_pass.encode()).hexdigest()
                if hashed_saltpass == user_information[3]:
                    self.adjust_loginErrorCount(email)
                    return True,user_information
 
                #wrong password
                else:
                    self.adjust_errorplusone(email)
                    return False,"Password Error, Waring!!! Your account will Permanently Lock, reamaning times {times}".format(times = int(9-user_accountstatus[0]))

        else: 
            return False,"User Not Exists"

    #-----------------------------------------------------------------------------

    # fetch email
    def fetch_email_username(self,username,email):
        sql_query = """
                    Select 1 
                    from users 
                    where email = '{email}' or username = '{username}' """.format(email=email,username = username)

        self.execute(sql_query)

        # If our query returns
        if self.cur.fetchone():
            return True
        else:
            return False

    #-----------------------------------------------------------------------------
    def check_user_existence(self, username):
        sql_query = """
        SELECT *
        FROM USERS
        WHERE username = '{username}'""".format(username = username)
        self.execute(sql_query)

        #check return 
        if self.cur.fetchone():
            return True
        return False

    #----------------------------------------------------------------
    def add_message(self, message, receiver, sender):
        sql_query = """
        INSERT INTO message_content (message, receiver, sender)
        VALUES('{message}','{receiver}','{sender}');
        """.format(message = message, receiver = receiver, sender = sender)
        self.execute(sql_query)
        self.commit()



# this function is for testing
    def show_message(self):
        sql_query = """
        SELECT * FROM message_content
        """
        self.execute(sql_query)
        user_information = self.cur.fetchall()
        return user_information


    def insert_comment(self,get_message, username, page):
        sql_query = """
        INSERT INTO page_comment (message, sender, page)
        VALUES('{get_message}', '{username}', {page})
        """.format(get_message = get_message, username = username, page = page)
        self.execute(sql_query)
        self.commit()
        return True

    def get_comment(self, page ):
        sql_query = """
        SELECT sender,message
        FROM page_comment 
        WHERE page = {page}
        """.format(page = page)
        self.execute(sql_query)
        res = self.cur.fetchall()
        return res

    def remove_user(self, id):
        sql_cmd = """
                DELETE FROM users
                WHERE users.id={id}""".format(id = id)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    #mute of unmute user
    def change_users_status(self, id):
        sql_cmd = """
                UPDATE users
                SET status = case
                            when status = 1 then 0
                            else 1
                            end
                WHERE users.id = {id}""".format(id = id)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    #add user session token
    def add_user_session(self,token,user_id):
        sql_cmd = """
                INSERT INTO user_session (token, user_id)
                VALUES('{token}', {user_id})
            """.format(token = token, user_id = user_id)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    #delete user session token
    def delete_user_session(self,token):
        sql_cmd = """
                DELETE FROM user_session where token = '{token}'
            """.format(token = token)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    #get user token information
    def token_userinfo(self):
        token = request.get_cookie('my_token',secret = self.secret_key)
        self.cur.execute("""
                SELECT users.id,username,email,admin,status FROM users 
                JOIN user_session ON user_session.user_id = users.id 
                WHERE token= (?) """,(token,))
        user_information = self.cur.fetchone()

        return user_information

    #-----------------------------------------------------------------------------
    #get all users information
    def get_all_user_info(self):
        sql_cmd = "SELECT id, username, email, status FROM users"
        self.execute(sql_cmd)
        all_users = self.cur.fetchall()
        
        return all_users
        
    
    #-----------------------------------------------------------------------------
    #get the max id
    def get_max_id(self):
        sql_cmd = "SELECT max(id) FROM users"
        self.execute(sql_cmd)
        max_id = self.cur.fetchone()
        return max_id

