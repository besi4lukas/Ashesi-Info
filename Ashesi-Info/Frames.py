from tkinter import *
from verticalScrollFrame import*
fontStyle = "Times New Roman"
class StartPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width of 750 and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller

          #Label for heading
          heading=Label(self,text="Ashesi Info",bg="white",fg="maroon",font=("Times New Roman",60))
          heading.place(relx=.5, rely=0.2, anchor="center")

          #Label with ashesi logo
          self.img = PhotoImage(file = "ashesilogo.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.4, anchor="center")
     
          #Sign in Button
          button1 = Button(self,text="Sign In", bg = 'maroon', fg = "white",font=("Times New Roman",25),
                           command =  lambda: controller.show_SignInPageFrame("StartPage"))
          button1.place(relx=0.6, rely=0.8 ,anchor="center")
          
          #Sign up button
          button2 = Button(self,text="Sign Up", bg = "maroon", fg = "white",font=("Times New Roman",25),
                           command =  lambda: controller.show_SignUpPageFrame("StartPage"))
          button2.place(relx=0.4, rely=0.8 ,anchor="center")



class SignUpPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller

          #Label for heading
          heading=Label(self,text="Ashesi Info",bg="white",fg="maroon",font=("Times New Roman",60))
          heading.place(relx=.5, rely=0.2, anchor="center")

          #Label with ashesi logo
          self.img = PhotoImage(file = "ashesilogo.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.4, anchor="center")

          # Sign as student Button 
          button1 = Button(self,text="Sign Up as student", bg = 'maroon',fg="white", font=("Times New Roman",25),
                           command =  lambda: controller.show_SignUpStdPageFrame("SignUpPage"))
          button1.place(relx=0.5, rely=0.65 ,anchor="center")

          # Sign Up as alumni Button           
          button2 = Button(self,text="Sign Up as alumni", bg = 'maroon', fg="white", font=("Times New Roman",25),
                           command =  lambda: controller.show_SignUpAlumPageFrame("SignUpPage"))
          button2.place(relx=0.5, rely=0.8 ,anchor="center")

          # Back to Start Page Button 
          button = Button(self, text = "Back to Start Page", bg = "maroon", fg = "white", font = ('Times New Roman', 13),
                          command = lambda: controller.show_frame("StartPage"))
          button.place(relx=0.5, rely=0.94 ,anchor="center")
          

class SignInPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller

          #Label for heading
          heading=Label(self,text="Ashesi Info",bg="white",fg="maroon",font=("Times New Roman",60))
          heading.place(relx=.5, rely=0.2, anchor="center")

          #Label with ashesi logo
          self.img = PhotoImage(file = "ashesilogo.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.4, anchor="center")

          # Sign In as student Button 
          button1 = Button(self,text="Sign In as student", bg = 'maroon', fg="white", font=("Times New Roman",25),
                           command =  lambda: controller.show_SignInStdPageFrame("SignInPage"))
          button1.place(relx=0.5, rely=0.65 ,anchor="center")

          # Sign In as alumni Button          
          button2 = Button(self,text="Sign In as alumini", bg = 'maroon', fg="white", font=("Times New Roman",25),
                           command =  lambda: controller.show_SignInAlumPageFrame("SignInPage"))
          button2.place(relx=0.5, rely=0.8 ,anchor="center")

          # Back to Start Page Button 
          button = Button(self, text = "Back to Start Page", bg = "maroon", fg = "white", font = ('Times New Roman', 13),
                          command = lambda: controller.show_frame("StartPage"))
          button.place(relx=0.5, rely=0.94 ,anchor="center")

class StdSignInPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Label with ashesi logo
          self.img = PhotoImage(file = "ashesilogo.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.13, anchor="center")

          #Label for heading          
          labelUsrname = Label(self, text = "Sign In ", bg = "white", fg = "maroon", font = (fontStyle,45))
          labelUsrname.place(relx = 0.5 , rely = 0.35, anchor = "center")

            
          #Label and text entry for student username
          labelUsrname = Label(self, text = "Student Name: ", bg = "white", fg = "maroon", font = (fontStyle,12))
          labelUsrname.place(relx = 0.2 , rely = 0.51, anchor = "center")
          Usrentry = Entry(self, bg = "white", selectforeground = "black", selectbackground = "maroon", width = 50)
          Usrentry.place(relx = 0.3,rely = 0.5)


          #Label and text entry for student username
          labelUsrpasswrd = Label(self, text = "Password: ", bg = "white", fg = "maroon", font = (fontStyle,12))
          labelUsrpasswrd.place(relx = 0.2 , rely = 0.59, anchor = "center")
          Passentry = Entry(self, bg = "white", selectforeground = "black", selectbackground = "maroon", width = 25)
          Passentry.place(relx = 0.3,rely = 0.58)


          #button for student signin
          buttonSignIn = Button(self, text = "Submit", bg = "maroon", fg = "white", font = (fontStyle,12),
                                command = lambda: controller.show_HomeFromSignInFrame("StdSignInPage",Usrentry,Passentry))
          buttonSignIn.place(relx = 0.5,rely = 0.68, anchor = "center")

          # Back to Sign In Page Button 
          button = Button(self, text = "Back to Sign In page",bg = "maroon", fg = "white", font = ('Times New Roman', 13),
                          command = lambda: controller.show_SignInPageFrame("StartPage"))
          button.place(relx=0.5, rely=0.94 ,anchor="center")




class AlumSignInPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Label with ashesi logo
          self.img = PhotoImage(file = "ashesilogo.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.13, anchor="center")

          #Label for heading 
          labelUsr = Label(self, text = "Sign In ", bg = "white", fg = "maroon", font = (fontStyle,45))
          labelUsr.place(relx = 0.5 , rely = 0.35, anchor = "center")

          #Label and text entry for student username
          labelUsrname = Label(self, text = "Alumni Name: ", bg = "white", fg = "maroon", font = (fontStyle,12))
          labelUsrname.place(relx = 0.2 , rely = 0.51, anchor = "center")
          Usrentry = Entry(self, bg = "white", selectforeground = "black", selectbackground = "maroon", width = 50)
          Usrentry.place(relx = 0.3,rely = 0.5)


          #Label and text entry for student username
          labelUsrpasswrd = Label(self, text = "Password: ", bg = "white", fg = "maroon", font = (fontStyle,12))
          labelUsrpasswrd.place(relx = 0.2 , rely = 0.59, anchor = "center")
          Passentry = Entry(self, bg = "white", selectforeground = "black", selectbackground = "maroon", width = 25)
          Passentry.place(relx = 0.3,rely = 0.58)


          #button for student signin
          buttonSignIn = Button(self, text = "Submit", bg = "maroon", fg = "white", font = (fontStyle,12),
                                command = lambda: controller.show_HomeFromSignInFrame("AlumSignInPage",Usrentry,Passentry))
          buttonSignIn.place(relx = 0.5,rely = 0.68, anchor = "center")

          # Back to Sign In Page Button 
          button = Button(self, text = "Back to Sign In page",bg = "maroon", fg = "white", font = ('Times New Roman', 13),
                          command = lambda: controller.show_SignInPageFrame("StartPage"))
          button.place(relx=0.5, rely=0.94 ,anchor="center")


class NoResultsPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller, pseudoPar):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          self.oldHomePage = 0

          #Label for heading 
          labelNoRlts = Label(self, text = "No Results", bg = "white", fg = "maroon", font = (fontStyle,45))
          labelNoRlts.place(relx = 0.5 , rely = 0.13, anchor = "center")

          #Labels containing error message and hint for user
          labelTips = Label(self, text = "Hints: ", bg = "white", fg = "maroon", font = (fontStyle,25))
          labelTips.place(relx = 0.3 , rely = 0.3, anchor = "center")
          labelTips = Label(self, text = "Check your spelling", bg = "white", fg = "maroon", font = (fontStyle,11))
          labelTips.place(relx = 0.5 , rely = 0.35, anchor = "center")
          labelTips = Label(self, text = "User is probably not a Student or Alumni of Ashesi", bg = "white", fg = "maroon", font = (fontStyle,11))
          labelTips.place(relx = 0.5 , rely = 0.4, anchor = "center")


          #button for going back to homepage
          button = Button(self, text = "Back to Home Page", font = ('Helvetica', 13),
                          command = lambda: controller.show_ShowHomeFromSearchResults("SearchResultPage", self.oldHomePage))
          button.place(relx=0.5, rely=0.94 ,anchor="center")



class StudentSignUp(Frame):
     
     def __init__(self, parent, controller):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller

          #Label with heading "Student Sign Up"
          heading = Label(self, text = "Student Sign Up", bg = "white", fg = "maroon", font = ('Times New Roman', 20))
          heading.place(relx = .5, rely = .05, anchor = "center")

          #Label and entry widget for student's full name
          nameLabel = Label(self, text = "Full Name:", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          nameLabel.place(relx = .2, rely = .13, anchor = "center")
          nameEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          nameEntry.place(relx = .46, rely = .13, anchor = "center")

          #Label and entry widget for student's password
          passwordLabel = Label(self, text = "Password:", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          passwordLabel.place(relx = .2, rely = .22, anchor = "center")
          passwordEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          passwordEntry.place(relx = .46, rely = .22, anchor = "center")

          #Label and entry widget for student's year group
          classLabel = Label(self, text = "Year Group: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          classLabel.place(relx = .2, rely = .31, anchor = "center")
          classEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          classEntry.place(relx = .46, rely = .31, anchor = "center")

          #Label and entry widget for student's Id
          idLabel = Label(self, text = "Student ID: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          idLabel.place(relx = .2, rely = .4, anchor = "center")
          idEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          idEntry.place(relx = .46, rely = .4, anchor = "center")

          #Label and entry widget for student's interests
          interestsLabel = Label(self, text = "Interests: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          interestsLabel.place(relx = .2, rely = .49, anchor = "center")
          interestsEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon", width = 15)
          interestsEntry.place(relx = .46, rely = .49, anchor = "center")

          #Label and entry widget for student's major
          majorLabel = Label(self, text = "Major: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          majorLabel.place(relx = .2, rely = .58, anchor = "center")
          majorEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          majorEntry.place(relx = .46, rely = .58, anchor = "center")

          #Label and entry widget for student's phone number
          phoneLabel = Label(self, text = "Phone: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          phoneLabel.place(relx = .2, rely = .67, anchor = "center")
          phoneEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          phoneEntry.place(relx = .46, rely = .67, anchor = "center")

          #Label and entry widget for student's email address
          emailLabel = Label(self, text = "email: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          emailLabel.place(relx = .2, rely = .76, anchor = "center")
          emailEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          emailEntry.place(relx = .46, rely = .76, anchor = "center")

          #Button to show the next frame 
          button = Button(self, text = "Sign Up",
                          command = lambda: controller.show_HomeFromStdSignUpFrame("StudentSignUp",nameEntry,
                                                                                   passwordEntry,classEntry,idEntry,
                                                                                   interestsEntry,majorEntry,phoneEntry,emailEntry))
          button.place(relx=0.5, rely=0.94 ,anchor="center")

          #Button to go back to old frame
          button = Button(self, text = "Back to SignUp page",bg = "maroon", fg = "white",
                          command = lambda: controller.show_SignUpPageFrame("StartPage"))
          button.place(relx=0.35, rely=0.94 ,anchor="center")

          
class AlumniSignUp(Frame):
     
     def __init__(self, parent, controller):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller

          #Label with heading "Alumni Sign Up"
          heading = Label(self, text = "Alumni Sign Up", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          heading.place(relx = .5, rely = .05, anchor = "center")

          #Label and entry widget for alumni's full name
          nameLabel = Label(self, text = "Full Name:", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          nameLabel.place(relx = .2, rely = .15, anchor = "center")
          nameEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          nameEntry.place(relx = .46, rely = .15, anchor = "center")

          #Label and entry widget for alumni's password
          passwordLabel = Label(self, text = "Password: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          passwordLabel.place(relx = .2, rely = .24, anchor = "center")
          passwordEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          passwordEntry.place(relx = .46, rely = .24, anchor = "center")

          #Label and entry widget for alumni's year group
          classLabel = Label(self, text = "Year Group: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          classLabel.place(relx = .2, rely = .33, anchor = "center")
          classEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          classEntry.place(relx = .46, rely = .33, anchor = "center")

          #Label and entry widget for alumni's interests
          interestsLabel = Label(self, text = "Interests: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          interestsLabel.place(relx = .2, rely = .42, anchor = "center")
          interestsEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          interestsEntry.place(relx = .46, rely = .42, anchor = "center")

          #Label and entry widget for alumni's career
          careerLabel = Label(self, text = "Career: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          careerLabel.place(relx = .2, rely = .51, anchor = "center")
          careerEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          careerEntry.place(relx = .46, rely = .51, anchor = "center")

          #Label and entry widget for alumni's phone number
          phoneLabel = Label(self, text = "Phone: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          phoneLabel.place(relx = .2, rely = .6, anchor = "center")
          phoneEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          phoneEntry.place(relx = .46, rely = .6, anchor = "center")

          #Label and entry widget for alumni's email address
          emailLabel = Label(self, text = "email: ", bg = "white", fg = "maroon", font = ('Times New Roman', 15))
          emailLabel.place(relx = .2, rely = .69, anchor = "center")
          emailEntry = Entry(self, bg = 'white', fg = "black", selectbackground = "white", selectforeground = "maroon")
          emailEntry.place(relx = .46, rely = .69, anchor = "center")

          #Button to show the next frame           
          button = Button(self, text = "Sign Up",
                          command = lambda: controller.show_HomeFromAlmSignUpFrame("AlumniSignUp",nameEntry,
                                  passwordEntry,classEntry,interestsEntry,careerEntry,phoneEntry,emailEntry))
          button.place(relx=0.5, rely=0.94 ,anchor="center")

          #Button to go back to old frame
          button = Button(self, text = "Back to SignUp page",bg = "maroon", fg = "white",
                          command = lambda: controller.show_SignUpPageFrame("StartPage"))
          button.place(relx=0.35, rely=0.94 ,anchor="center")



class SearchResultPage(Frame):
     
     def __init__(self, parent, controller, pseudoPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller
          self.oldHomePage = 0

          #Label of the name of person that was searched for
          label = Label(self, text = pseudoPar["fullName"], bg = "white", fg = "maroon", font = (fontStyle,40))
          label.place(relx = 0.5,rely = 0.13, anchor = "center")

          #Label of the year group of person that was searched for
          label2 = Label(self, text = "Member of " + pseudoPar["yearGroup"] + " Year Group", bg = "white", fg = "maroon", font = (fontStyle,20))
          label2.place(relx = 0.5,rely = 0.3, anchor = "center")

          #Label of the career/major of person that was searched for
          labelStory = Label(self, text = "Career/Major: " + pseudoPar["career"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelStory.place(relx = 0.4,rely = 0.45, anchor = "center")

          #Label of the interests of person that was searched for
          labelInterest = Label(self, text = "Interest: "+pseudoPar["interests"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelInterest.place(relx = 0.4,rely = 0.6, anchor = "center")

          #Label of the number of person that was searched for
          labelNum = Label(self, text = pseudoPar["phone"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelNum.place(relx = 0.5,rely = 0.8, anchor = "center")

          #Label of the email of person that was searched for
          labelMail = Label(self, text = pseudoPar["email"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelMail.place(relx = 0.5, rely = 0.85 , anchor = "center")

          #Button to go back to old frame          
          button = Button(self, text = "Back to Home Page", font = ('Helvetica', 13),
                          command = lambda: controller.show_ShowHomeFromSearchResults("SearchResultPage", self.oldHomePage))
          button.place(relx=0.5, rely=0.94 ,anchor="center")


class HomePage(Frame):
     
     def __init__(self, parent, controller, pseudoPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller
          
          # Entry acting as search bar
          entry = Entry(self, bg = "grey", selectforeground = "maroon", selectbackground = "white", width = 50)
          entry.place(relx = 0.5, rely = 0.1, anchor = "center")

          #Search button
          buttonSearch = Button(self, text = "Search", bg = "maroon", fg = "white", font = (fontStyle, 12),
                                command = lambda: controller.show_SearchResultsFrame("HomePage", entry, pseudoPar))
          buttonSearch.place(relx = 0.8, rely = 0.1, anchor = "center")

          #Label of the name of user
          label = Label(self, text = pseudoPar["fullName"], bg = "white", fg = "maroon", font = (fontStyle,30))
          label.place(relx = 0.5,rely = 0.2, anchor = "center")

          #Label of the year group of user
          label2 = Label(self, text = "Member of " + pseudoPar["yearGroup"] + " Year Group", bg = "white", fg = "maroon", font = (fontStyle,20))
          label2.place(relx = 0.5,rely = 0.34, anchor = "center")

          #Label of the career/major of user
          labelcareer = Label(self, text = "Career/Major: " + pseudoPar["career"], bg = "white", fg = "maroon", width = 50,
                              font = (fontStyle,18))
          labelcareer.place(relx = 0.4,rely = 0.45, anchor = "center")

          #Label of the interest of user
          labelInterest = Label(self, text = "Interest: "+ pseudoPar["interests"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelInterest.place(relx = 0.4,rely = 0.6, anchor = "center")

          #Label of the phone of user
          labelphone = Label(self, text = pseudoPar["phone"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelphone.place(relx = 0.5,rely = 0.8, anchor = "center")

          #Label of the email of user
          labelMail = Label(self, text = pseudoPar["email"], bg = "white", fg = "maroon", font = (fontStyle,18))
          labelMail.place(relx = 0.5, rely = 0.85 , anchor = "center")

          #Log out button
          button = Button(self, text = "Log out", font = ('Helvetica', 13),
                          command = lambda: controller.show_frame("StartPage"))
          button.place(relx=0.5, rely=0.94 ,anchor="center")
          




class YearBookPage(Frame):
     def __init__(self, parent, controller,pseudoPar, passPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 650, width = 700)
          self.controller = controller

          #Instance variable to hold previous homepage frame
          self.oldHomePage = 0

          #Object of VerticalScrolledFrame class which is placed in the yearbook frame
          self.frame = VerticalScrolledFrame(parent, controller)
          self.frame.place(relx = 0.5,rely = 0.7, anchor = "center")

          #Button to go back to home page
          button = Button(self, text = "Back to Home Page", font = ('Helvetica', 13),
                          command = lambda: controller.show_ShowHomeFromSearchResults("SearchResultPage", self.oldHomePage))
          button.place(relx=0.5, rely=0.13 ,anchor="center")

          #Label for heading
          label = Label(self, text = "Class  List for year group", bg = "white", fg = "maroon", font = ('Times New Roman',20))
          label.place(relx = 0.5,rely = 0.2, anchor = "center")

          #Place names of students of the year group in scroll frame.
          labels = []
          if pseudoPar != 0:
               for i in range(len(pseudoPar)):
                     labels.append(Label(self.frame.interior, text = pseudoPar[i], bg = "white", fg = "maroon", font = ('Times New Roman',15)))
                     labels[-1].pack()


class Graph:
     #Initialize graph
     def __init__(self):
          self.data = {}

     #Add vertices to graph
     def add(self, key, Vertices):
          self.data[key] = Vertices

     #Get vertices from graph
     def get(self, key):
          return self.data[key]

    # Special method to use python's get functionality
     def __getitem__(self,key):
        return self.get(key)

    # Special method to use python's get functionality
     def __setitem__(self,key,data):
        self.add(key,data)

