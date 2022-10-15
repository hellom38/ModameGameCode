from DatabaseHandling import *
import wx 
import wx.html2 
import tkinter as tk
from os import system
from tkinter import ttk
from functools import partial
import hashlib
def Hash1(Word):

    Word = hashlib.sha256(str.encode(Word)).hexdigest()
    return Word
def buyMultipliers(Multi,Money,List):
  for i in List:
    if List[(i)] < 5:
      pass
 
def Login3(Logins):

    while Logins < 6:
        def validateLogin(user,password,Logins):
            password = password.get()
            user = user.get()
            
            Finder = Get_DB(LoginDB,user,Hash1(password),Login_Cur,"LoginDetails","User","Pass",False)
            if Finder != True:

                print('Welcome back')
                system("cls")
                transportationZone(user)

            else:
                
                print(Logins)
                Logins = Logins + 1
                print('Password or/and user does not match')
                system("cls")
                Login3(Logins)
        tkWindow = Tk()  
        tkWindow.geometry('400x150')  
        tkWindow.title('Modame Menu')

        #username label and text entry box
        usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  
            
            #password label and password entry box
        passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(tkWindow, textvariable=password, show='x').grid(row=1, column=1)  
            
        validateLogin = partial(validateLogin, username, password,Logins)
            
            #login button
        loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
            
        tkWindow.mainloop()      


  
    checkIfRobot()
      
def TEST1():
  print("TESTING")
def MultipliersZone(UserM):
  List = {{"permanent x2 multiplier" : 1000} : 1,{"+1 heart" : 50} : 2}
  ListUser = UserM[3]
  Multipliers = ListUser.split(" ")
  print(Multipliers)
  transportationMultiplier = input("[1] Buy\n[2] Use\n[3] Amount\n[4] Exit")
  if 1 in transportationMultiplier:
    buyMultipliers(Multipliers,UserM[1],List)
  
    


def Game1():
    quiz = {
    1 : {
        "question" : "What is the first name of Iron Man?",
        "answer" : "Tony"
    },
    2 : {
        "question" : "Who is called the god of lightning in Avengers?",
        "answer" : "Thor"
    },
    3 : {
        "question" : "Who carries a shield of American flag theme in Avengers?",
        "answer" : "Captain America"
    },
    4 : {
        "question" : "Which avenger is green in color?",
        "answer" : "Hulk"
    },
    5 : {
        "question" : "Which avenger can change it's size?",
        "answer" : "AntMan"
    },
    6 : {
        "question" : "Which Avenger is red in color and has mind stone?",
        "answer" : "Vision"
    }
    }



    def check_ans(question, ans, attempts, score):
        """
        Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the quiz is not case sensitive.
        """
        if quiz[question]['answer'].lower() == ans.lower():
            print(f"Correct Answer! \nYour score is {score + 1}!")
            return True
        else:
            print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
            return False


    def print_dictionary():
        for question_id, ques_answer in quiz.items():
            for key in ques_answer:
                print(key + ':', ques_answer[key])


    def intro_message():
        print("Welcome to this fun food quiz! \nAre you ready to test your knowledge about food?")
        print("There are a total of 20 questions, you can skip a question anytime by typing 'skip'")
        input("Press any key to start the fun ;) ")
        return True


    # python project.py
    intro = intro_message()
    while True:
        score = 0
        for question in quiz:
            attempts = 3
            while attempts > 0:
                print(quiz[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":
                    break
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

    print(f"Your final score is {score}!\n\n")
    print("Want to know the correct answers? Please see them below! ;)\n")
    print_dictionary()
    print("Thanks for playing! 💜")

def Register2():
  print("hh")
def Start2():
  root = tk.Tk()
  root.title("Modame Game")

  Message = tk.Label(root, text="Welcome to modame Game")
  Message.pack()
  Login = ttk.Button(root,text="Login")
  Login.grid(column="2",row=0)
  Login.configure(command=Login3(0))
  Register = tk.Button(root,text="Register",command=Register2)
  root.mainloop()



class MyBrowser(wx.Dialog): 
  def __init__(self, *args, **kwds): 
    wx.Dialog.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) 
    self.browser = wx.html2.WebView.New(self) 
    sizer.Add(self.browser, 1, wx.EXPAND, 10) 
    self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.OnWebViewLoaded, self.browser)
    self.SetSizer(sizer) 
    self.SetSize((700, 700))

  def OnWebViewLoaded(self, evt):
    # The full document has loaded
    self.browser.RunScript('alert("hello");')

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1) 
  dialog.browser.LoadURL("http://www.google.com") 
  dialog.Show() 
  app.MainLoop() 



users = {'hellom38': 'bdbbe1ad7ff12fbddba4fc1a8ae89ba841e1d7bf3fd09c9d1030b373b4a2312c', 'TEST' : '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4' \
,'soldadoborjarex' : 'b791cfcc64506a6dbb27345fa3a154eb800b2e54928add85284d7bf13e137314'}
User_money = {'hellom38' : 100, 'TEST' : 300,'soldadoborjarex' : 200}
Pmoney = {'hellom38' : 0, 'TEST' : 20, 'soldadoborjarex' : 100}
bonuses = {'hellom38' : 12,'TEST' : 1,'soldadoborjarex' : 2}

import random
def StartPlay(Username):
    
    print('welcome to 9 lives')
    clue = []
    words = ['shirt', 'otter', 'rocks', 'plane', 'teeth', 'fairy', 'pizza', 'gorilla', 'cheese', 'parrot', 'hippopotamus', 'mississippi', 'giraffe', 'orange']
    secret_word = random.choice(words)
    lives = 0
    difficulty = input('what difficulty\n easy, press \"1\" \n medium, press \"2\" \n difficult, press \"3\"')
    if difficulty == '3':
            lives = 4
    elif difficulty == '2':
            lives = 6
    elif difficulty == '1':
        lives = 9
    else:
        print('Incorrect, Restarting game')


    heart_symbol = "L "
    guessed_word_correctly = False

    index = 0
    while index < len(secret_word):
        clue.append('?')
        index = index + 1


    def check_word(guessed_letter, clue, secret_word):
        index = 0
        while index < len(secret_word):
            if guessed_letter.lower() == secret_word[index].lower():
                clue[index] = guessed_letter
            index = index + 1


    while lives > 0:
        print(clue)
        print('lives left: ' + heart_symbol * lives)
        guess = input("guess the letter or the whole word: ")


        if guess == secret_word:
            print("correct")
            guessed_word_correctly = True
            if difficulty == '3':
                Pmoney[Username] = Pmoney[Username] + 20
                StartPlay(Username)
            elif difficulty == '2':
                Pmoney[Username] = Pmoney[Username] + 13
                StartPlay(Username)
            elif difficulty == '1':
                Pmoney[Username] = Pmoney[Username] + 8
                StartPlay(Username)

         
            


        if guess in secret_word:
            check_word(guess, clue, secret_word)
            
        else:
            print('Incorrect, you lose a life')
            lives = lives - 1

    if lives == 0:
        print("you lost, the answer was: " + secret_word)
        
        StartPlay(Username)
        
        
        
