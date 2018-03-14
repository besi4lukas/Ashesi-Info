''' Final Project for Data Structures and Algorithms
 Authors: Kingsley Besidonne, Oswald Fiifi Amissah & Yaw Darfour Botwe

This program aims to bridge the gap between Ashesi students and Ashesi Alumni by
providing a platform to easily search for students or Alumni and their details.

 In this program, classes are used to represent the various frames in the app'''


from Frames import *
from InfoHashTable import*

class InfoApp:
     
     def __init__(self, master):
          ''' The container is a frame for stacking other frames.
               when we wanta frame to be visible we raise that frame above others'''
          self.master = master
          self.container = Frame(self.master)
          self.container.pack(side="top", fill="both", expand=True)
          self.container.grid_rowconfigure(0, weight=1)
          self.container.grid_columnconfigure(0, weight=1)

          #Hashtable containing fullnames as key
          self.fullnameHash = HashTable()

          #A graph to hold the current frame as a key and a list of all possible frames it
          #can lead to as a value. 
          self.frames = Graph()

          #Adding each Graph and the possible frames it can lead to, to self.frames
          self.frames.add(StartPage.__name__, [StartPage(parent=self.container, controller=self), SignUpPage(parent=self.container, controller=self), SignInPage(parent=self.container, controller=self)])
          self.frames.add(SignUpPage.__name__, [StudentSignUp(parent=self.container, controller=self), AlumniSignUp(parent=self.container, controller=self), StartPage(parent=self.container, controller=self)])
          self.frames.add(SignInPage.__name__, [StdSignInPage(parent=self.container, controller=self), AlumSignInPage(parent=self.container, controller=self), StartPage(parent=self.container, controller=self)])
          self.frames.add(StudentSignUp.__name__, [HomePage(parent=self.container, controller=self, pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                                                   SignUpPage(parent=self.container, controller=self)])
          self.frames.add(AlumniSignUp.__name__, [HomePage(parent=self.container, controller=self,pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                                                  SignUpPage(parent=self.container, controller=self)])
          self.frames.add(StdSignInPage.__name__, [HomePage(parent=self.container, controller=self,pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                          SignInPage(parent=self.container, controller=self)])
          self.frames.add(AlumSignInPage.__name__, [HomePage(parent=self.container, controller=self,pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                                                    SignInPage(parent=self.container, controller=self)])
          self.frames.add(HomePage.__name__, [SearchResultPage(parent=self.container, controller=self, pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                                              NoResultsPage(parent=self.container, controller=self, pseudoPar ={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                                              HomePage(parent=self.container, controller=self,pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             }),
                                              YearBookPage(parent=self.container, controller=self,pseudoPar = 0, passPar = 0)])

          
               
          self.frames.add(SearchResultPage.__name__, [HomePage(parent=self.container, controller=self,pseudoPar={"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             })])
          self.frames.add(NoResultsPage.__name__, [HomePage(parent=self.container, controller=self, pseudoPar = {"fullName": "Full Name",
                                                                                                             "yearGroup": "Full Name",
                                                                                                             "interests": "Full Name",
                                                                                                             "career": "Full Name",
                                                                                                              "phone": "Full Name",
                                                                                                               "email": "Full Name"
                                                                                                             })])
          
          #A dictionary containing the list of students by their year groups
          self.yearBook = {}


          #Call method for placing page at the top of the stacking order
          self.show_frame("StartPage")



     '''The following methods are used as commands for the buttons
          in the frames above'''


     def show_frame(self, page_name):
          #Show a frame for the given page name
          frame = self.frames[page_name][0]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

     def show_SignInPageFrame(self, page_name):
          #Show a frame for the given page name
          frame = self.frames[page_name][2]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

     def show_SignUpPageFrame(self, page_name):
          #Show a frame for the given page name
          frame = self.frames[page_name][1]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()
          
     def show_SignUpStdPageFrame(self, page_name):
     #Show a frame for the given page name
          frame = self.frames[page_name][0]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

     def show_SignUpAlumPageFrame(self, page_name):
     #Show a frame for the given page name
          frame = self.frames[page_name][1]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

     def show_SignInStdPageFrame(self, page_name):
          #Show a frame for the given page name
          frame = self.frames[page_name][0]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()
          
     def show_SignInAlumPageFrame(self, page_name):
          #Show a frame for the given page name
          frame = self.frames[page_name][1]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

     def show_HomeFromStdSignUpFrame(self, page_name,entry1,
                                  entry2,entry3,entry4,entry5,entry6, entry7, entry8):
       
          #dictionary for user information 
          info = {}

          #This is to get the user entries
          fullName = entry1.get()
          passwrd = entry2.get()
          yearGroup = entry3.get()
          studentID = entry4.get()
          interests = entry5.get()
          major = entry6.get()
          phone = entry7.get()
          email = entry8.get()

          #Putting entries in a dictionary
          info["fullName"] = fullName
          info["passwrd"] = passwrd
          info["yearGroup"] = yearGroup
          info["studentID"] = studentID
          info["interests"] = interests
          info["career"] = major
          info["phone"] = phone
          info["email"] = email

          #Putting the dictionary into our Hashtable with the full name of the user as our key.
          self.fullnameHash.put(fullName,info)


          #Put the name of the user into the yearBook dictionary
          if yearGroup not in self.yearBook.keys():
              self.yearBook[yearGroup] = [fullName]

          else:
            self.yearBook[yearGroup].append(fullName)



          
          #Show a frame for the given page name
          frame = self.frames[page_name][0]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

          page_name = HomePage.__name__
          frame = HomePage(parent = self.container,controller = self, pseudoPar = self.fullnameHash[fullName])
          self.frames[page_name] = frame
          frame.grid(row=0, column=0, sticky="nsew")

          

     def show_HomeFromAlmSignUpFrame(self, page_name,entry1,
                                  entry2,entry3,entry4,entry5, entry6, entry7):
       
          #dictionary for user information 
          info = {}

          #This is to get the user entries
          fullName = entry1.get()
          passwrd = entry2.get()
          yearGroup = entry3.get()
          interests = entry4.get()
          career = entry5.get()
          phone = entry6.get()
          email = entry7.get()

          #Putting entries in a dictionary
          info["fullName"] = fullName
          info["passwrd"] = passwrd
          info["yearGroup"] = yearGroup
          info["interests"] = interests
          info["career"] = career
          info["phone"] = phone
          info["email"] = email

          #Putting the dictionary into our Hashtable with the full name of the user as our key.         
          self.fullnameHash.put(fullName,info)


          #Put the name of the user into the yearBook dictionary
          if yearGroup not in self.yearBook.keys():
              self.yearBook[yearGroup] = [fullName]

          else:
            self.yearBook[yearGroup].append(fullName)          

          #Show a frame for the given page name in this case the HomePage frame
          frame = self.frames[page_name][0]
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

          page_name = HomePage.__name__
          frame = HomePage(parent = self.container,controller = self, pseudoPar = self.fullnameHash[fullName])
          self.frames[page_name] = frame
          frame.grid(row=0, column=0, sticky="nsew")


     def show_HomeFromSignInFrame(self, page_name, entry1, entry2):

          #Get user entries
          fullName = entry1.get()
          passwrd = entry2.get()

          #Check whether password matches the one in the hashtable
          if self.fullnameHash[fullName] != None:
              checkPass = self.fullnameHash[fullName]["passwrd"]
              if passwrd == checkPass:         
                  #Show a frame for the given page name           
                  frame = self.frames[page_name][0]
                  frame.grid(row=0, column=0, sticky="nsew")
                  frame.tkraise()

                  page_name = HomePage.__name__
                  frame = HomePage(parent = self.container,controller = self, pseudoPar = self.fullnameHash[fullName])
                  self.frames[page_name] = frame
                  frame.grid(row=0, column=0, sticky="nsew")
              else:
                # Error label
                error1 = Label(self.container, text = "Wrong password", fg = "red", bg = "white")
                error1.place(relx = 0.5, rely = 0.73, anchor = "center")

          else:
            # Error label
            error2 = Label(self.container, text = "Not a student or Alumni", fg = "red", bg = "white")
            error2.place(relx = 0.5, rely = 0.73, anchor = "center")

     def show_SearchResultsFrame(self, page_name, entry1, homeFrame):
          # Get entry from that search bar
          fullName = entry1.get()

          #Show results frame if entry is in Hashtable
          if self.fullnameHash[fullName] != None:
              page_name = SearchResultPage.__name__
              frame = SearchResultPage(parent = self.container, controller = self, pseudoPar = self.fullnameHash[fullName])
              self.frames[page_name] = frame
              frame.oldHomePage = homeFrame
              frame.grid(row=0, column = 0, sticky ="nsew")

          #Show year book frame if entry is in yearBook dictionary         
          elif fullName in self.yearBook.keys():
              page_name = YearBookPage.__name__
              frame = YearBookPage(parent = self.container, controller = self, pseudoPar = self.yearBook[fullName],passPar = homeFrame)
              self.frames[page_name] = frame
              frame.oldHomePage = homeFrame
              frame.grid(row=0, column = 0, sticky ="nsew")

          #Show No results frame if entry is not in both Hashtable and yearBook dictionary 
          elif fullName not in self.yearBook.keys() or self.fullnameHash[fullName] == None:
            page_name = NoResultsPage.__name__
            frame = NoResultsPage(parent = self.container,controller = self, pseudoPar = homeFrame)
            self.frames[page_name] = frame
            frame.oldHomePage = homeFrame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()
            
     def show_ShowHomeFromSearchResults(self, page_name, homepage):
          
          #Show Home page frame
          page_name = HomePage.__name__
          frame = HomePage(parent = self.container,controller = self, pseudoPar = homepage)
          self.frames[page_name] = frame
          frame.grid(row=0, column=0, sticky="nsew")
          frame.tkraise()

          
def main():
     #Create tkinter window with dimension 600x750
     # and title 'Ashesi Info'
     root = Tk()
     root.title('Ashesi Info')
     root.geometry('700x650')
     
     app = InfoApp(root)
     #To keep the tkinter window running
     root.mainloop()

main()
