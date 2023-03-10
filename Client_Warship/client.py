import time
import os
import json
import requests

baseUrl = "http://127.0.0.1:8000/HttpMethods/"

create_url = baseUrl + "create_board/"
join_url = baseUrl + "join_board/"
check_url = baseUrl + "send_status/"
choice_url = baseUrl + "send_choice/"

name = ''
board = ''

def get_input():
    global name, board
    name = input("What's your name?: ")
    cb = input("Do you want to create a new game or join an existing game? \n1. create board\n2. join board \n3. connect to board (when disconnect to the board)\n")
    while (cb not in ["1", "2", "3"]):
        print("Invalid input")
        cb = input("Do you want to create a new game or join an existing game? \n1. create board\n2. join board \n3. connect to board (when disconnect to the board)\n")
    if cb == "1":
        #send a data of name to server to create a new game
        #response a room code from server then wait for another player to join
        while True:
            try:          
                response = requests.post(create_url, data={'name': name})
                break
            except:
                print("Can't connect to server, try again in 3 second(s)")
                time.sleep(1)
                os.system('clear')
                print("Can't connect to server, try again in 2 second(s)")
                time.sleep(1)
                os.system('clear')
                print("Can't connect to server, try again in 1 second(s)")
                time.sleep(1)
                os.system('clear')
        obj = json.loads(response.text)
        # while obj["status"] != "Ok":
        #     obj = json.loads(requests.post(create_url, data={'name': name}).text)
        board = obj["board"]
    elif cb == "2":
        #send a data of name and room code to server to join an existing game
        #response a message from server to tell if the room code is valid or not
        board = input("What's the room code?: ")
        while True:
            try:
                obj = json.loads(requests.post(join_url, data={'name': name, "board": board}).text)
                break
            except:
                print("Can't connect to server, try again in 3 second(s)")
                time.sleep(1)
                os.system('clear')
                print("Can't connect to server, try again in 2 second(s)")
                time.sleep(1)
                os.system('clear')
                print("Can't connect to server, try again in 1 second(s)")
                time.sleep(1)
                os.system('clear')
        # while obj["status"] != "Ok":
        #     obj = json.loads(requests.post(join_url, data={'name': name, "board": board}).text)
    elif cb == "3":
        board = input("What's the room code?: ")
        
def play():
    #send http to server to get the status and who start first
    #if its player's turn then ask for input 
    #if its not player's turn then get every 1 second to check if its player's turn
    while True:
        try:
            obj = json.loads(requests.post(check_url, data={'name': name, "board": board}).text)
            break
        except:
            print("Disconnected from server. Trying to reconnect.")
            time.sleep(0.33)
            os.system("clear")
            print("Disconnected from server. Trying to reconnect..")
            time.sleep(0.33)
            os.system("clear")
            print("Disconnected from server. Trying to reconnect...")
            time.sleep(0.33)
            os.system("clear")
    while obj["status"] == "Wait":
        os.system("clear")
        print("Room code: " + str(board) + "\n" + "Waiting for another player to join.")
        time.sleep(0.33)
        os.system("clear")
        print("Room code: " + str(board) + "\n" + "Waiting for another player to join..")
        time.sleep(0.33)
        os.system("clear")
        print("Room code: " + str(board) + "\n" + "Waiting for another player to join...")
        time.sleep(0.33)
        while True:
            try:
                obj = json.loads(requests.post(check_url, data={'name': name, "board": board}).text)
                break
            except:
                print("Disconnected from server. Trying to reconnect.")
                time.sleep(0.33)
                os.system("clear")
                print("Disconnected from server. Trying to reconnect..")
                time.sleep(0.33)
                os.system("clear")
                print("Disconnected from server. Trying to reconnect...")
                time.sleep(0.33)
                os.system("clear")
    os.system("clear")
    
    while obj["your_turn"] != -1:
        print(obj["announce"])
        commands = obj["commands"]
        can_front = obj["can_front"] 
        if obj["your_turn"] == 1:
            action = input()
            while action not in commands:
                print("Invalid command")
                action = input()
            temp = "0"
            if action == "3":
                temp = int(input("which ship do you want to set at front?: "))
                while temp not in can_front:
                    print("That Ship can't be set at front")
                    temp = int(input("which ship do you want to set at front?: "))
            while True:
                try:
                    requests.post(choice_url, data={'name': name, "board": board, "action": action, "temp": temp})
                    break
                except:
                    print("Disconnected from server. Trying to reconnect.")
                    time.sleep(0.33)
                    os.system("clear")
                    print("Disconnected from server. Trying to reconnect..")
                    time.sleep(0.33)
                    os.system("clear")
                    print("Disconnected from server. Trying to reconnect...")
                    time.sleep(0.33)
                    os.system("clear")
        else:
            time.sleep(1)
        os.system("clear")
        
        #Is Server still alive?
        while True:
            try: 
                obj = json.loads(requests.post(check_url, data={'name': name, "board": board}).text)
                break
            except: 
                print("Disconnected from server. Trying to reconnect.")
                time.sleep(0.33)
                os.system("clear")
                print("Disconnected from server. Trying to reconnect..")
                time.sleep(0.33)
                os.system("clear")
                print("Disconnected from server. Trying to reconnect...")
                time.sleep(0.33)
                os.system("clear")
    print(obj["announce"])

    


get_input()
play()
        