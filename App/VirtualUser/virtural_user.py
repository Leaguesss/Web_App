from build_users import user_one, user_two, user_three, delete_user, close

'''
This Python class selects a virtual user at random and navigates them through the site.

The routes that each virtual user tests:
- User #1: registers and traverses through all the routes within Main Page.
- User #2: registers and traverses through all the routes within Message.
- User #3: registers and traverses through all the routes within Admin.
'''

class VirtualUser:

    def __init__(self, link):
        self.link = link

    def run(self):
        print("Virtual user has been randomly selected... Running user #1:\n")
        user_one(self.link)

        print("Virtual user has been randomly selected... Running user #2:\n")
        user_two(self.link)
        delete_user(self.link)

        print("Virtual user has been randomly selected... Running user #3:\n")
        user_three(self.link)
        delete_user(self.link)
        #print("Finished!\n")
        close()


user = VirtualUser("http://10.86.227.70/")
user.run()
