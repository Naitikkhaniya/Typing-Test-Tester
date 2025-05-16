import os
import random
import time
from datetime import datetime

class Choice:

    def before_login(self):
        
        new_game = User()

        print("\n1. New User \n2. Registered User \n3. Exit")
        choice = int(input("\nEnter Your Choice :- "))
        try:
                
            if choice == 1 :
                new_game.registration()
            
            elif choice == 2 :
                new_game.login()
            
            elif choice == 3 :
                exit()
            
            else :
                print("\n===============")
                print("nInvalid Value")
                self.before_login()
        
        except ValueError:

            print("\n==========================================")
            print("======== Please Enter Valid Value ========")
            print("==========================================")
        
        self.before_login()
    
    def after_login(self, username):
        
        hist = History(username)
        play = Play(username)

        print("\n1. For Play \n2. For Show History \n3. Log Out")
        choice = int(input("\nEnter Your Choice :- "))
        
        if choice == 1:
            play.play(hist)
            
        elif choice == 2:
            hist.show()

        elif choice == 3:
            print("\n============================================")
            print("======== Thank You For Your Support ========")
            print("============================================\n")
            exit()


class User :

    user_data = {}
    
    def registration(self):
        
        file = open('UserData.txt','a+')
        for line in file:
            string = line.split(" :- ")
            
            f_name = string[0]
            l_name = string[1][:len(string[1])-1]

            User.user_data[f_name] = l_name

        name = input("Create User Name :- ")
        password = input("Create Your Password :- ")

        if name.isdigit() :
            print("\n---Please Enter String Also---\n")

        else :
            User.user_data[name] = password
            print(f"\n{name} is Registered Successfully\n")
            
            for key, value in User.user_data.items():
                file.write(f"{key} :- {value}\n")
            
            flag = False

        file.close()
        self.login()
    
    def login(self):
        
        file = open('UserData.txt','r')

        for line in file:
            string = line.split(" :- ")
            
            f_name = string[0]
            l_name = string[1][:len(string[1])-1]

            User.user_data[f_name] = l_name
       
        choice = Choice()
        
        username = input("Enter Your Username :- ")
        password = input("Enter Your Password :- ")

        if username in User.user_data and User.user_data[username] == password :
            
            print("\n===========================")
            print("==== Login Successfull ====")
            print("===========================\n")
            print(f"Welcome {username}")
            
            choice.after_login(username)

        else :
            print("==============================================")
            print("======== Invalid Username Or Password ========")
            print("==============================================")
            
            choice.before_login()

class Play :

    def __init__(self, username):
        self.username = username
        self.file_exist()

    def file_exist(self):

        if os.path.exists(self.username + ".txt"):
            return
        
        else:
            file = open(self.username+'.txt', 'w')
            file.close()

    
    def play(self, hist):
        
        random_number = random.randint(0,15)
        self.get_sentence(random_number, hist)
    
    
    def get_sentence(self, random_number, hist):
    
        file = open('Sentance.txt','r')
        texts = file.readlines()
        line = texts[random_number]
        file.close()
    
        self.main(line, hist)

    def main(self, line, hist):
    
        choice = Choice()
    
        print("Type The Following Text \n")
        print(f"{line} \n")
        
        start = time.time()
        
        print("Press Enter To Start Typing")
        user_input = input()
        
        end = time.time()
        
        difference = ((end - start) / 60).__round__(2)
        
        total_chars = len(user_input)
        wpm = round((total_chars/difference),2)
        

        correct_chars = 0

        for i in range(min(len(line), len(user_input))):

            if line[i] == user_input[i]:
                correct_chars += 1


        accuracy = (correct_chars / len(line)) * 100

        print(f"Time :- {difference} Second")
        print(f"Word Per Minute :- {wpm} W/M")
        print(f"Accuracy: {round(accuracy,2)} %")

        hist.add(wpm, accuracy)

class History:

    choice = Choice()
    
    def __init__(self, username):
        self.username = username 
    
    def add(self, wpm, accuracy):
        name = self.username + ".txt"
        
        file = open(name, 'a')
        file.write(f"{self.username} | {wpm} | {accuracy} | {datetime.now()}\n")
        file.close()

        History.choice.after_login(self.username)

    def show(self):
        string = self.username + '.txt'

        file = open(string, 'r') 
        content = file.read().strip()
        
        if content:
            print("\n=========================")
            print("======== History ========")
            print("=========================\n")
            print('\n --Name-- | --WPM-- | --Accuracy-- | --Date--\n')
            print(content)
        else:
            print("No History Available")

        file.close()

        History.choice.after_login(self.username)



print("\n=========================")
print("======== Welcome ========")
print("=========================")
obj = Choice()
obj.before_login()