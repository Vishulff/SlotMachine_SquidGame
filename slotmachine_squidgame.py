import random
import pygame
import sys
import time
import requests
import json

response = requests.get('https://ipinfo.io')
data = response.json()
with open("data.json","w") as f:
    json.dump(data,f,indent = 2)
pygame.mixer.init()
MAX_LINES = 3
money = pygame.mixer.Sound("music/money-soundfx.mp3")
background_music = pygame.mixer.Sound("music/squid-game-tone.mp3")
distorted = pygame.mixer.Sound("music/distorted-trumpets-hl2.mp3")
hack1 = pygame.mixer.Sound("music/hacking-sfx.mp3")
hack2 = pygame.mixer.Sound("music/hacking.mp3")
sound_effect = pygame.mixer.Sound("music/squid-elimination.mp3")
elements = ["7️⃣ ", "⭐", "🍎"]
gibrish = ["\033[33mHaCkindwadGGG.....\033[0m","\033[33mPlEaase WAiitsad....\033[0m","jJ0L^%11U@w9A&vVhLT01hQ&v@tkP!!JZyIY8!xXWY0R9yxy9XtGE@Ik0v1w!!rQMW13BBz1A1V!!L1K@#E1010w0e101101011KVaRLj...","💿🧭🖲💽⌨🖱☠💀☠","NOT HACKINGGG","Welcome TO SQUIDD GAMEE.","\033[31mExtracting Your Compu.....\033[0m","\033[31mEveryting Extract....succe....lly....\033[0m"]
times = [0.05,0.02,0.06,0.04]

def typing(text,delay):
    for i in text:
        time.sleep(delay)
        sys.stdout.write(i)
        sys.stdout.flush()

def start():
    hack1.play(-1)
    typing(random.choice(gibrish),random.choice(times))
    typing(random.choice(gibrish),random.choice(times))
    typing(random.choice(gibrish),random.choice(times))
    typing(random.choice(gibrish),random.choice(times))
    print("\033[31m1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^M!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^M!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^M\033[37m")
    print("\033[36m1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("\033[32m1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("\033[31m1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("\033[33m1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("\033[33m1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    print("1J9aW@k01xXT#Kv!b0zFQ11t1&Z!P0vDLRkc7qY*e100bv!0110x9jG^XkDAWv1z#3LL010w01T!cz@pKZ0X1fAG^@DkL*Jx1b109x!Rm@W001ZgQt1YYvqXx#@v1TM@NqW0110VAK001rJB!!Ak1!7pqx^tTA1KPB@Z001n^MQV!L!3x1f#1TkzKW1010DzXTR!x0101l@qVK@A010RPk@K0v^WAA@Q1MMqTAK@ZTkxN#d!!QQAYZ01010kjxKZ!A1e0VLD09L1LLRA@Pv19bb001x!XZ!!\033[37m")
    hack1.stop()
    
def get_no_of_lines():
    count = 0
    while True:
        lines = input("Enter the lines you want to bet on (1-" + str(MAX_LINES) + ") : ")
        if lines.isdigit():
            lines = int(lines)
            if 0<lines<4:
               break
            else:
                print("Please enter a Valid number between (1-3).")
        elif lines.lower() == "exit":
            if count == 3:
                sound_effect.play()
                time.sleep(1.3)
                print("Why THE FUCK You Are Not UNDERSTANDING!!!\nI SAID YOU CAN NOT EXIT!")
                count += 1
            elif count == 4:
                sound_effect.play()
                time.sleep(1.3)
                print("YOU DUMB OR WHAT?")
            elif count <= 3:
                sound_effect.play()
                time.sleep(1.3)
                print("YOU CAN NOT EXIT I SAID.")
                count += 1
            
            
        else:
            print("It much be a Digit between (1-3).")
    return lines
                
def deposit():
    sound_effect.play()
    time.sleep(1.3)
    count1 = 0
    while True:
        print("\n")
        amount = input("Enter the amount you want to deposit OR type 'exit' to EXIT : $")
        if amount.lower() == "exit":
            if count1 == 0:
                print("Unfortunately You CANT EXIT NOW. YOUR INFORMATION HAS BEEN SAVED.")
                sound_effect.play()
                time.sleep(1.3)
                print("Your IP Address : ",data["ip"])
                sound_effect.play()
                time.sleep(1.3)
                print("Your City : ",data["city"])
                sound_effect.play()
                time.sleep(1.3)
                print("region : ",data["region"])
                sound_effect.play()
                time.sleep(1.3)
                print("coordinates : ",data["loc"])
                sound_effect.play()
                time.sleep(1.3)
                print("country : ",data["country"])
                time.sleep(1.3)
                print("\n You have to play it :)")
                count1 += 1
            elif count1 == 1:
                sound_effect.play()
                time.sleep(1.3)
                print("\nYou have to Play I said.")
        
        elif amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:   
                print("Amount must be greater than 0.")           
        else:
            print("Enter a valid answer.")

balance = deposit()

def machine():
    global slot
    slot = []
    for _ in range(3):
        row = [random.choice(elements) for _ in range(3)]
        slot.append(row)

    return slot

def show_machine(balance):
    match = False
    for row in slot :
        sound_effect.play()
        time.sleep(1.3)
        print(" | ".join(row))
    # Checking Rows
    if slot[0][0] == slot[0][1] == slot[0][2]:
        print("\n")
        typing("ROW 1 MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 1.7*bet_amount 
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("ROW 1 Did Not MATCHED.")
    if slot[1][0] == slot[1][1] == slot[1][2]:
        print("\n")
        typing("ROW 2 MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 2*bet_amount
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("ROW 2 Did Not MATCHED.")
    if slot[2][0] == slot[2][1] == slot[2][2]:
        print("\n")
        typing("ROW 3 MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 1.7*bet_amount
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("ROW 3 Did Not MATCHED.")
    # Checking Cross
    if slot[0][0] == slot[1][1] == slot[2][2]:
        hack2.play()
        print("\n")
        typing("CROSS MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 1.5*bet_amount
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("CROSS 1 Did not MATCHED.")
    if slot[0][2] == slot[1][1] == slot[2][0]:
        print("\n")
        typing("CROSS MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 1.5*bet_amount
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("Cross 2 Did not Matched.")
    # Checking Columns
    if slot[0][0] == slot[1][0] == slot[2][0]:
        print("\n")
        typing("COLUMN 1 MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 2*bet_amount 
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("Column 1 Did Not MATCHED.")
    if slot[0][1] == slot[1][1] == slot[2][1]:
        print("\n")
        typing("COLUMN 2 MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 2*bet_amount 
        match = True
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("Column 2 Did Not MATCHED.")
    if slot[0][2] == slot[1][2] == slot[2][2]:
        print("\n")
        typing("COLUMN 3 MATCHED!\n",0.05)
        background_music.stop()
        money.play()
        balance += 2*bet_amount
        match = True 
    else:
        sound_effect.play()
        time.sleep(1.3)
        print("Column 3 Did Not MATCHED.")
    # Checking Whole
    if slot[0][0] == slot[0][1] == slot[0][2] == slot[1][0] == slot[1][1] == slot[1][2] == slot[2][0] == slot[2][1] == slot[2][2]:
        print("\n")
        typing("JACKPOT!",0.05)
        background_music.stop()
        money.play()
        balance += 5*bet_amount
        match = True
    else:
        
        sound_effect.play()
        time.sleep(1.3)
        print("JACKPOT Not MATCHED.")
    if match == True:
        print(f"You Total Balance is now : {balance}")
        choice = input("Want to Play Again? (yes/no) :")
        if choice.lower() == "yes":
            distorted.stop()
            main()
        elif choice.lower() == "no":
            print("Will Check on you again SOON....")
            distorted.stop()
            quit()
        else:
            print("Please answer in (yes/no) or check the spelling again.")
    if match == False:
        print("\n")
        sound_effect.play()
        time.sleep(1.3)
        print("Nothing Matched...")
        background_music.stop()
        distorted.play()
        typing("\033[33 Unfortunately.. You are Eliminated! BYE BYE\033[37m",0.06)
        print("\n")
        print(f"You Total Balance is now ${balance} which is of no use LoL")
        time.sleep(30)
    else:
        return
                         
def main():
    global balance
    lines = get_no_of_lines()
    while True:
        global total_amount
        global bet_amount
        bet_amount = input("Enter your bet amount for each line in slot : $")
        bet_amount = int(bet_amount)
        total_amount = bet_amount*lines
        
        # print(type(lines))
        # print(type(total_amount))
        # print(type(balance))
        # print(type(balance))
        # print(type(total_amount))
        if total_amount > balance:
            print(f"Not Enough Balance. Balance : ${balance}, Total bet : ${total_amount}")
        elif total_amount <= balance:
            print(f"You have betted amount ${bet_amount} on {lines} lines. Total bet : ${total_amount}")
            break
    balance -= total_amount
    print(f"Balance : ${balance}")
    machine()
    show_machine(balance)

print("\n")
print("\n")
start()
background_music.set_volume(0.5)
background_music.play(-1)
main()
background_music.stop()