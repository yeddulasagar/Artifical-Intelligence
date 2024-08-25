import time
import speech_recognition as sr
import os
import webbrowser
import win32com.client
import datetime
import pyautogui      #for volume
import psutil         #for battery
import speedtest
from twilio.rest import Client

speaker = win32com.client.Dispatch("SAPI.SPvoice")

speaker.speak("Welcome to Arsalan A I")

chatStr = ""
from gui import play_gif
play_gif

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Arsalan AI"

if __name__ == '__main__':
    print('Welcome to Arsalan A.I')
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            speaker.speak(f"Sir time is {hour} hour  {min} minutes and {sec} seconds")


        elif "play music" in query:
            music_dir = "C:\\Users\\arsla\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif "increase volume" in query:
            pyautogui.press("volumeup")
            speaker.speak("increasing the volume sir")

        elif "decrease volume" in query:
            speaker.speak("Decreasing the volume sir")
            pyautogui.press("volumedown")

        elif "mute the volume" in query or "mute" in query:
            speaker.speak("Now the volume is mute sir")
            pyautogui.press("volumemute")

        elif "open visual" in query:
            speaker.speak("Opening the visual sir")
            codepath = "C:\\Users\\arsla\\AppData\\Local\\Programs\\Microsoft VS Code\\code"
            os.startfile(codepath)

        elif "open photo" in query:
            speaker.speak("Searching for best photo that present in your pc  wait ")
            R_dir = "E:\R"
            photo = os.listdir(R_dir)
            print(photo)
            os.startfile(os.path.join(R_dir, photo[17]))


        elif "open camera" in query:
            speaker.speak("Opening the Camera sir")
            camerapath = "C:\\Users\\arsla\\OneDrive\\Desktop\\Camera"
            os.startfile(camerapath)

        elif "open profile" in query:
            speaker.speak("Enter usser name to find profile")
            name = input("Enter ussername here : ")
            speaker.speak("Opening instagram profile sir")
            webbrowser.open(f"www.instagram.com/{name}")

        elif "take screenshot" in query:
            speaker.speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speaker.speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speaker.speak("i am done sir, the screenshot is saved in your main folder.")

        elif "how much battery we have" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speaker.speak(f"Sir our system have {percentage} percent battery")

        elif "internet speed" in query:
            st = speedtest.Speedtest()
            d1 = st.download()
            up = st.upload()
            speaker.speak(f"sir we have {d1} bit per second downloading speed and {up} bit per second uploading speed")

        elif "send message" in query:
            speaker.speak("Sir what should i say")
            msz = takeCommand()

            account_sid = 'AC99067dae939fea64a3ca0936af8dfbd7'
            auth_token = '485e65779386d9632a14eb49f3431156'

            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=msz,
                from_='+14099040695',
                to='+917420068814'
            )
            print(message.sid)
            speaker.speak("sir, message has been send")

        elif "edit my image" in query:
            from PIL import Image, ImageEnhance
            import os

            speaker.speak("plzz wait we are working on your image")
            img = Image.open('Arsalan shaikh.jpg')
            speaker.speak("Adding some sharpness into image")
            enhancer = ImageEnhance.Sharpness(img)
            enhancer.enhance(15)
                # 0 : blurry
                # 1: original image
                # 2 : image with increased sharpness

            speaker.speak("Now adding some colour into it")
            enhancer = ImageEnhance.Color(img)
            enhancer.enhance(5)

            speaker.speak("Adding some brightness into it")
            enhancer = ImageEnhance.Brightness(img)
            enhancer.enhance(30)

            speaker.speak("Adding some contrat into it")
            enhancer = ImageEnhance.Contrast(img)
            enhancer.enhance(1.5)

            speaker.speak("Your image is edited successfully and saving your image into your main folder with name edit image")
            img.save('edit_image.jpg')

        elif "make bill" in query:
            import os
            import datetime
            import ctypes

            itemname = []
            amount = []
            qty = []
            rate = []
            ch = 'y'

            d_date = datetime.datetime.now()
            reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Bill Generator\t\t\t\t\t  %I:%M:%S %p")
            print(
                '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(reg_format_date)
            print(
                '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


            def show():
                # Get the current date and time
                current_time = datetime.datetime.now()
                # Format the current date and time as a string
                timestamp_str = current_time.strftime("%Y-%m-%d-%H-%M-%S")
                # Use the timestamp string as part of the filename
                speaker.speak("Enter name to save the bill")
                filename = input("Enter name to save the bill: ") + timestamp_str + '.txt'

                with open(filename, 'w') as f:
                    f.write('\nItemname\t\t\t\t' + '\tRate\t' + 'Qty\t' + '\tAmount\n')
                    for i in range(0, len(itemname)):
                        f.write('{0}\t\t\t\t\t{1}\t\t{2}\t\t{3}\n'.format(itemname[i], rate[i], qty[i], amount[i]))
                    f.write('\nTotal amount:\t\t\t\t\t\t\t{0}\n'.format(sum(amount)))

            def errorhand(tempvalue):
                try:
                    ctypes.windll.user32.MessageBoxA(0, "Please insert number", "Oops", 0)
                    tempvalue = float(input('Input again: '))
                except:
                    errorhand(tempvalue)
                return tempvalue


            while ch == 'y' or ch == 'Y':
                speaker.speak("Enter item name ")
                tempitemname = str(input('\nEnter item name : '))
                tempitemname = tempitemname[0:15]
                if len(tempitemname) < 8:
                    tempitemname = tempitemname + '        '
                itemname.append(tempitemname)
                tempamount = 0
                tempqty = 0
                tempa = 0
                tempq = 0

                try:
                    speaker.speak("Enter rate of the item ")
                    tempamount = float(input('Enter rate: '))
                    tempa = int(tempamount)

                except:
                    tempa = errorhand(tempamount)

                try:
                    speaker.speak("Enter quantity of the item")
                    tempqty = input('Enter quantity: ')
                    tempq = int(tempqty)
                except:
                    tempq = int(errorhand(tempqty))

                amount.append(tempq * tempa)
                qty.append(tempq)
                rate.append(tempa)
                speaker.speak("Bill generated successfully")
                speaker.speak("if you want to add another item press y either press n")
                ch = input('\nDo you want to add more(y for yes and n for no): ')
                if ch == 'n' or ch == 'N':
                    show()


        elif "make quick response code" in query:
            import qrcode as qr

            speaker.speak("Enter url to generate the qr code ")
            img = qr.make(input("Enter url to generate the qr code : "))
            speaker.speak("Enter a file name to store qrcode with extension ")
            img.save(input("Enter a file name to store qrcode with extension : "))
            speaker.speak("QR code generated successfully")

        elif "generate WhatsApp message" in query:
            import pywhatkit as pwk

            try:
                # sending message in Whatsapp in India so using Indian dial code (+91)
                speaker.speak("Enter a number to send msg")
                number = input("Enter a number to send msg :")

                speaker.speak("Enter a msg what you have to send")
                msg = input("Enter a msg what you have to send: ")

                speaker.speak("Enter the hour to send msg")
                hour = int(input("Enter the hour to send msg : "))

                speaker.speak("Enter the min to send msg")
                min = int(input("Enter the min to send msg : "))

                pwk.sendwhatmsg("+91" + number, msg, hour, min)
                print("Message Sent!")
                speaker.speak("message sent successfully")

            except:
                print("Error in sending the message")
                speaker.speak("Error in sending message")

        elif "tic-tac-toe game" in query:
            from tic_tak_game import checkWin, printBoard, sum
            xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            turn = 1  # 1 for X and 0 for O
            speaker.speak("Welcome to Tic Tac Toe game ")
            print("Welcome to Tic Tac Toe")
            while (True):
                printBoard(xState, zState)
                if (turn == 1):
                    speaker.speak("X's Chance")
                    print("X's Chance")
                    speaker.speak("Please enter a value ")
                    value = int(input("Please enter a value: "))
                    xState[value] = 1
                else:
                    speaker.speak("0's Chance")
                    print("O's Chance")
                    speaker.speak("Please enter a value ")
                    value = int(input("Please enter a value: "))
                    zState[value] = 1
                cwin = checkWin(xState, zState)
                if (cwin != -1):
                    speaker.speak("Match over")
                    print("Match over")
                    break
                turn = 1 - turn

        elif "quiz game" in query:
            questions = ("How many elements are in the periodic table?: ",
                         "Which animal lays the largest eggs?: ",
                         "What is the most abundant gas in Earth's atmosphere?: ",
                         "How many bones are in the human body?: ",
                         "Which planet in the solar system is the hottest?: ")

            options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                       ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                       ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                       ("A. 206", "B. 207", "C. 208", "D. 209"),
                       ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

            answers = ("C", "D", "A", "A", "B")
            guesses = []
            score = 0
            question_num = 0

            for question in questions:
                print("----------------------")
                speaker.speak(question)
                print(question)
                for option in options[question_num]:
                    speaker.speak(option)
                    print(option)

                guess = input("Enter (A, B, C, D): ").upper()
                guesses.append(guess)
                if guess == answers[question_num]:
                    score += 1
                    speaker.speak("CORRECT")
                    print("CORRECT!")
                else:
                    speaker.speak("INCORRECT")
                    print("INCORRECT!")
                    print(f"{answers[question_num]} is the correct answer")
                question_num += 1

            print("----------------------")
            print("       RESULTS        ")
            print("----------------------")

            print("answers: ", end="")
            for answer in answers:
                print(answer, end=" ")
            print()

            print("guesses: ", end="")
            for guess in guesses:
                print(guess, end=" ")
            print()

            score = int(score / len(questions) * 100)
            speaker.speak(f"Your score is: {score}%")
            print(f"Your score is: {score}%")

        elif "exit" in query:
            speaker.speak("Good by")
            exit()





