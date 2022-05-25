from threading import current_thread
import time
import keyboard
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyautogui
from PyDictionary import PyDictionary
import subprocess
import screen_brightness_control as sbc
from word2number import w2n
from email.mime import image
import cv2
import winsound
import psutil
from translate import Translator
from tkinter import HIDDEN, NORMAL, Tk, Canvas
import pyjokes
from termcolor import colored

lol = False
MASTER = "Neeraj"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Speak function will pronounce the string which is passed to it
def speak(text):
	engine.say(text)
	engine.runAndWait()


def wishMe():
	hour = int(datetime.datetime.now().hour)

	if 0 <= hour < 12:
		speak('Good Morning' + MASTER)

	elif 12 <= hour < 18:
		speak('Good Afternoon' + MASTER)

	else:
		speak('Good evening' + MASTER)

	print("what can I do for you sir!")
	speak("what can I do for you sir!")


# This func will take query from the microphone
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print(colored("Listening...", "green"))
		speak('Tell me!')
		r.adjust_for_ambient_noise(source, duration=0.8)
		# r.energy_threshold = 1
		# audio = r.listen(source, phrase_time_limit=5)
		audio = r.listen(source)
		speak('Got it')

	try:
		print(colored("Recognizing...\n", "red"))
		speak("Recognizing")
		query = r.recognize_google(audio, language='en-In')
		print(f"user said: {query}\n")

	except Exception as e:
		query = ""
	return query


def takeCommand_ToStart():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.adjust_for_ambient_noise(source, duration=0.8)
		audio = r.listen(source)

	try:
		print("Recognizing...\n")
		query = r.recognize_google(audio, language='en-In')
		print(f"user said: {query}\n")

	except Exception as e:
		query = " "
	return query


def sendEmail(to, content):
	server = smtplib.SMTP('SMTP.gmail.com', 587)
	server.ehlo()
	server.starttls()
	speak("please login to your account, see on the screen!")
	email_here = input("email: ")
	password = input("password: ")
	server.login(email_here, password)
	server.sendmail(email_here, to, content)
	server.close()



def ToRunFriday():
	while True:
		command = takeCommand_ToStart()
		if 'friday' in command.lower():
			lol = False
			break
		
		else:
			lol = True



def Game():
	def toggle_eyes():
		current_color = c.itemcget(eye_left, 'fill')
		new_color = c.body_color if current_color == 'white' else 'white'
		current_state = c.itemcget(pupil_left, 'state')
		new_state = NORMAL if current_state == HIDDEN else HIDDEN
		c.itemconfigure(pupil_left, state=new_state)
		c.itemconfigure(pupil_right, state=new_state)
		c.itemconfigure(eye_left, fill=new_color)
		c.itemconfigure(eye_right, fill=new_color)

	def blink():
		toggle_eyes()
		root.after(250, toggle_eyes)
		root.after(3000, blink)

	def toggle_pupils():
		if not c.eyes_crossed:
			c.move(pupil_left, 10, -5)
			c.move(pupil_right, -10, -5)
			c.eyes_crossed = True
		else:
			c.move(pupil_left, -10, 5)
			c.move(pupil_right, 10, 5)
			c.eyes_crossed = False

	def toggle_tongue():
		if not c.tongue_out:
			c.itemconfigure(tongue_tip, state=NORMAL)
			c.itemconfigure(tongue_main, state=NORMAL)
			c.tongue_out = True
		else:
			c.itemconfigure(tongue_tip, state=HIDDEN)
			c.itemconfigure(tongue_main, state=HIDDEN)
			c.tongue_out = False

	def cheeky(event):
		toggle_tongue()
		toggle_pupils()
		hide_happy(event)
		root.after(1000, toggle_tongue)
		root.after(1000, toggle_pupils)
		return

	def show_happy(event):
		if (20 <= event.x and event.x <= 350) and (20 <= event.y and event.y <= 350):
			c.itemconfigure(cheek_left, state=NORMAL)
			c.itemconfigure(cheek_right, state=NORMAL)
			c.itemconfigure(mouth_happy, state=NORMAL)
			c.itemconfigure(mouth_normal, state=HIDDEN)
			c.itemconfigure(mouth_sad, state=HIDDEN)
			c.happy_level = 10
		return

	def hide_happy(event):
		c.itemconfigure(cheek_left, state=HIDDEN)
		c.itemconfigure(cheek_right, state=HIDDEN)
		c.itemconfigure(mouth_happy, state=HIDDEN)
		c.itemconfigure(mouth_normal, state=NORMAL)
		c.itemconfigure(mouth_sad, state=HIDDEN)
		return

	def sad():
		if c.happy_level == 0:
			c.itemconfigure(mouth_happy, state=HIDDEN)
			c.itemconfigure(mouth_normal, state=HIDDEN)
			c.itemconfigure(mouth_sad, state=NORMAL)
		else:
			c.happy_level -= 1
		root.after(5000, sad)

	root = Tk()
	root.title("Screen pet")
	c = Canvas(root, width=400, height=400)
	c.configure(bg='dark blue', highlightthickness=0)
	c.body_color = 'SkyBlue1'

	body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
	ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
	ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
	foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
	foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

	eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
	pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
	eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
	pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

	mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
	mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
	mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
	tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
	tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

	cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
	cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

	c.pack()
	c.bind('<Motion>', show_happy)
	c.bind('<Leave>', hide_happy)
	c.bind('<Double-1>', cheeky)

	c.happy_level = 10
	c.eyes_crossed = False
	c.tongue_out = False

	root.after(1000, blink)
	root.after(5000, sad)
	root.mainloop()


def Jokes():
	jokes = pyjokes.get_joke()
	print(jokes)
	speak(jokes)
	time.sleep(2)
	print("would you like to hear one more joke?")
	speak("would you like to hear one more joke?")
	userAns = takeCommand().lower()
	if 'yes' in userAns:
		Jokes()
	else:
		pass


# Main program starts here
print("Initializing Friday\n")
speak('Initializing Friday...')
print(colored(
	"<<<<<------THIS IS PROJECT FRIDAY------>>>>>", "red"))

print(colored("----SAY FRIDAY IN YOUR SENTENCE TO AWAKE ME----\n", "green"))
print(
	"\n1.You can ask me anything available on the internet"
	"\n2.I can do some of your basic tasks:-\n"
	)
print(
	"    a. clicking a picture\n"
	"    b. opening an application\n"
	"    c. playing songs on youtube\n"
	"    d. taking screenshot\n"
	"    e. email\n"
	"    f. jokes\n"
	"    g. chats\n"
	"    h. controlling brightness\n"
	"    i. shutdown and restarting your pc\n"
	"    j. sending a whatsapp message\n"
	"    k. asking date and time\n"
	"    l. asking your battery percentage\n"
	"    m. opening a site\n"
	"    n. translation\n"
	"    o. meaning of a word\n"
	"    p. wikipedia\n"
	"    q. And many more random things... try to ask them out\n"
	)
print("starting in")
time.sleep(1)
print("3...",end = "")
time.sleep(1)
print("2...",end = "")
time.sleep(1)
print("1...",end = "\n")
time.sleep(1)


if __name__ == '__main__':
	ToRunFriday()
	wishMe()

	while lol == False:
		query = takeCommand().lower()
		# query = query.replace("can you please", "")

		if query == "":
			print("I didn't get it say that again please, maybe you are away from mic")
			speak("I didn't get it say that again please, maybe you are away from mic")
			query = takeCommand().lower()

		# TO STOP FRIDAY
		elif (('sleep' in query) and ('friday' in query)) or ("go sleep" in query) or (
				(query == "no") or (query == "nope") or (query == "nah") or (query == "nahi")):
			print("okay, should I go offline now?")
			speak("okay, should I go offline now?")
			inp = takeCommand().lower()
			if (("yes" in query) and ("offline" in query)) or ("go" in query):
				speak(
					"I am going in hybernation mode, just say Friday in your sentence and I will be here again to help you.")
				ToRunFriday()
			else:
				pass
		# <------------------------------CHAT FEATURES STARTS HERE------------------------------->

		# KEY WORD FOR INTRODUCTION
		elif (query == "friday") or (query == "hey") or (query == "hey friday") or (query == "hello") or (
				query == "hi") or (query == "hello friday"):
			print(f"Hello {MASTER}. how may I help you")
			speak(f"Hello {MASTER}. how may I help you")

		# WHO ARE YOU TYPE
		elif ('what can you do' in query) or (('what' and 'your name') in query) or (
				(('tera' in query) or ('aapka' in query) or ('tumhara' in query) or ('tumao' in query)) and (
				('name' in query) or ('naam' in query))):
			print(
				"I am Friday, I can try to answer your questions and if you need anything just ask to me, your wish is my command.")
			speak(
				"I am Friday, I can try to answer your questions and if you need anything just ask to me, your wish is my command.")


		# WHAT ARE YOU DOING TYPE
		elif (("how" in query)) and (("doing" in query) or ("going" in query)):
			print("I'm great, and talking to you. Let me know if I can do something for you")
			speak("I'm great, and talking to you. Let me know if I can do something for you")
			ans = takeCommand().lower()
			if ans != None:
				print("That's good")
				speak("That's good")
			else:
				pass

		# What's HAPPENING TYPE
		elif ((("what's" in query) or ("what is" in query) or ("what are you")) and (
				("going" in query) or ("happening" in query) or ("doing" in query))):
			print("Nothing, How is your day going?")
			speak("Nothing, How is your day going?")
			ans = takeCommand().lower()
			if ans != None:
				print("That's great")
				speak("That's great")
			else:
				pass


		# WHO MADE YOU OR FAMILY TYPE QUESTION
		elif ('who made you' in query) or (
				'your' in query and ('father' or 'mother' or 'brother' or 'sister' or 'boss' or 'creator') in query):
			print(
				"I am not a human, but I can tell you that Neeraj created me by doing a lengthy code. I am so proud of him")
			speak(
				"I am not a human, but I can tell you that Neeraj created me by doing a lengthy code. I am so proud of him")
			speak("anything else?")

		# TO ASK THE NAME
		elif ('what is my name' in query) or ('who am I' in query) or ('call my name' in query):
			print(f'Your name is {MASTER}')
			speak(f'Your name is {MASTER}')
			speak("anything else?")

		# TO CHANGE THE NAME
		elif ("no my name is" in query) or ("not my name" in query) or ("set my name" in query) or ("change my name" in query) or ("my name is" in query):
			print("okay, what should I call you?")
			speak("okay, what should I call you?")
			name = takeCommand()
			print(f'do you want that I will call you {name}?')
			speak(f'do you want that I will call you {name}?')
			confirmation = takeCommand().lower()
			if 'yes' in confirmation.lower():
				MASTER = MASTER.replace(MASTER, name)
				print(f"From now I will call you {MASTER}")
				speak(f"From now I will call you {MASTER}")

			else:
				print("I've made no changes in your name")

			speak("anything else?")

		# TO ASK TIME
		elif ('the time' in query) or ('what is the time' in query):
			# strTime = datetime.datetime.now().strftime("%H:%M:%S")
			current_date = datetime.datetime.now()
			print(f"Time : {current_date.strftime('%I : %M : %S %p')}")
			speak(f"{MASTER} the time is {current_date.strftime('%I : %M : %S %p')}")

		# TO ASK DATE
		elif ('the date' in query) or ('what is the date' in query) or (('day' in query) and ('today' in query)):
			current_date = datetime.datetime.now()
			print(f"Date : {current_date.strftime('%A, %B %d, %Y')}")
			speak(f"{MASTER} the date is {current_date.strftime('%A, %B %d, %Y')}")

		# REPLY FOR COMPLIMENT
		elif ("well done" in query) or ("Thank you" in query) or ("I am happy" in query) or ("thanks" in query):
			print("Its my pleasure sir, you are always welcome")
			speak("Its my pleasure sir, you are always welcome")

		# SOME JOKES
		elif ("joke" in query) or ("jokes" in query):
			Jokes()
			speak("anything else sir?")


		# <------------------------------LIGHT TASKS, NON OS TYPE------------------------------->

		# TO ASK MEANING OF A WORD
		elif (('what is' in query) and ('meaning of' in query)) or ('meaning of') in query:
			try:
				dict = PyDictionary()
				query = query.replace('what is the meaning of', '')
				query = query.replace('hey Friday what is the meaning of', '')
				query = query.replace('hey what is the meaning of', '')
				query = query.replace('meaning of', '')
				query = query.replace('friday', '')
				query = query.replace('the', '')
				query = query.replace('hi', '')
				query = query.replace('please', '')
				query = query.replace('tell me', '')
				query = query.replace('hey', '')
				query = query.replace('hello', '')
				query = query.replace(' ', '')
				word = query
				meaning_dict = dict.meaning(word)
				meaning_list = next(iter(meaning_dict.values()))
				meaning_str = meaning_list[0]
				print(f"{query} : {meaning_str}")
				speak(f"Meaning of {word}. {meaning_str}")
			except Exception as e:
				print("try to ask meaning of a single word or you can google it")
				speak("please try to ask meaning of a single word or you can google it")

		# WIKIPEDIA SEARCH
		elif ((('who' in query) or ('what' in query)) and 'is' in query) or 'wikipedia' in query:
			print(query)
			print('Wikipedia Search')
			query = query.replace("wikipedia", "")
			info = wikipedia.summary(query, sentences=3)
			print(info)
			speak(info)

		# GOOGLE SEARCH
		elif (('search google for') in query) or (('search' in query) and ('on google' in query)) or (
				("search" in query) and ("google" in query)) or ("google it" in query):
			print('Google Search')
			speak('searching on google')
			query = query.replace('search google for', '')
			query = query.replace('search', '')
			query = query.replace('on google', '')
			query = query.replace('search google', '')
			query = query.replace('do google', '')
			query = query.replace(' ', '+')
			pywhatkit.search(query)

		# TO OPEN YOUTUBE
		elif ('open youtube' in query) or ('youtube khol' in query):
			url = "youtube.com"
			# chrome_path = 'C:/Program Files (×86)/Google/Chrome/Application/chrome.exe %s'
			# webbrowser.get(chrome_path).open(url) comment
			webbrowser.open(url)
			speak("Haa haa opening na wait!")

		# TO WRITE AN EMAIL
		elif (('write' in query) or ('send')) and ('email' in query):
			try:
				speak("whom should I write?")
				to = input("write the email address of reciever: ")
				print("what should I write in it?")
				speak("what should I write in it?")
				content = takeCommand().lower()
				content = content.replace("friday write", "")
				sendEmail(to, content)
				print("Email has been sent")
				speak("Email has been sent")
			except Exception as e:
				print(e)
				speak("Sorry sir, I am not able to send this email!")

		# TO OPEN GOOGLE
		elif 'open google' in query:
			url = "google.com"
			print("opening google!")
			speak("opening google!")
			webbrowser.open(url)


		# TO SEND WHATSAPP message
		elif ((("send" in query) and ("message" in query)) or (("write" in query) and ("message" in query))) or ((("send" in query) and ("messege" in query)) or (("write" in query) and ("messege" in query))) or (query=='whatsapp'):
			current_date = datetime.datetime.now()
			hour = current_date.strftime('%H')
			minute = current_date.strftime('%M')
			hour = int(hour)
			minute = int(minute)
			minute = minute + 2
			# print(f"{hour} : {minute}")
			speak("type the number please")
			number = "+91" + (input("enter mobile number: "))
			print("what should I write in message?")
			speak("what should I write in message?")
			msg_command = takeCommand().lower()
			msg_command = msg_command.replace("friday write", " ")
			pywhatkit.sendwhatmsg(number, msg_command, hour, minute)
			time.sleep(5)
			print(f"Your message : {msg_command}")
			print("message will be sent")
			speak("message will be sent")
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# TO WRITE INTO NOTEPAD USING VOICE COMMAND
		elif (("write" in query) and ("notepad" in query)) or ("save this information" in query) or (
				("write" in query) and ("notepad" in query)):

			flag_it = False
			while flag_it == False:
				speak("okay")
				print("tell me the name of file")
				speak("tell me the name of text file")
				file_name = takeCommand().lower()
				if file_name != None:
					file = open(file_name + ".txt", "w")
					print("what should I note down?")
					speak("what should I note down?")
					file_command = takeCommand().lower()
					file.write(file_command)
					file.close()
					print(f"noted, saved as {file_name}")
					speak("noted")
					break

				else:
					flag_it = False
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# TO TRANSLATE INTO ANY LANGUAGE
		elif (("translate" in query)) or ("meaning in" in query):
			print("<<<<<----TRANSLATOR---->>>>>")
			query = query.replace("meaning in", "")
			query = query.replace("friday", "")
			query = query.replace("hey", "")
			query = query.replace("hello", "")
			query = query.replace("please", "")
			query = query.replace("hi", "")
			query = query.replace("of", "")
			query = query.replace("to", "")
			query = query.replace("in", "")
			query = query.replace("what", "")
			query = query.replace("translate", "")
			query = query.replace("into", "")

			try:
				speak("see the translation on the screen, it's hard for me to pronounce it")
				if "hindi" in query:
					query = query.replace("hindi", "")
					translator = Translator(to_lang="hi")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "bengali" in query:
					query = query.replace("bengali", "")
					translator = Translator(to_lang="bengali")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "german" in query:
					query = query.replace("German", "")
					translator = Translator(to_lang="German")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "greek" in query:
					query = query.replace("Greek", "")
					translator = Translator(to_lang="Greek")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "japanese" in query:
					query = query.replace("japanese", "")
					translator = Translator(to_lang="japanese")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "gujarati" in query:
					query = query.replace("Gujarati", "")
					translator = Translator(to_lang="Gujarati")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "russian" in query:
					query = query.replace("Russian", "")
					translator = Translator(to_lang="Russian")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "chinese" in query:
					query = query.replace("Chinese", "")
					translator = Translator(to_lang="Chinese")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "urdu" in query:
					query = query.replace("Urdu", "")
					translator = Translator(to_lang="Urdu")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "ukrainian" in query:
					query = query.replace("Ukrainian", "")
					translator = Translator(to_lang="Ukrainian")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "arabic" in query:
					query = query.replace("Arabic", "")
					translator = Translator(to_lang="Arabic")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				elif "english" in query:
					query = query.replace("english", "")
					translator = Translator(to_lang="english")
					translation = translator.translate(query)
					print(f"Translation of {query} : {translation}")

				else:
					print("Sorry, I am unable to translate into that language")
					speak("Sorry, I am unable to translate into that language")

			except Exception as e:
				print("Sorry, I am unable to translate into that language try after some time.")
				speak("Sorry, I am unable to translate into that language try after some time.")
				speak("Anything else to do?")





		# ********************************************SYSTEM TASKS**************************************************

		# TO OPEN VS CODE
		elif ('open' in query) and ('code' in query):
			codePath = "C:\\Users\\NEERAJ KUMAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)
			speak("opening your workspace sir")
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# TO PLAY MUSIC PRESENT IN SYSTEM
		elif (('play' in query) and ('music' in query)) or ("play music" in query):
			try:
				# musicPath = "C:\\Users\\NEERAJ KUMAR\\Desktop\\Resso.lnk"
				os.startfile(musicPath)
				speak("Playing music sir")

			except Exception as e:
				speak("Playing music sir")
				url = "https://youtu.be/99XF71Fpjl8"
				webbrowser.open(url)

		# TO OPEN ANY WEB URL
		elif ("open" in query) and (("website" in query) or ("url")):
			print("if you want to open a site, just tell me the name of the site")
			speak("if you want to open a site, just tell me the name of the site")

			try:
				urlquery = takeCommand()
				urlquery = urlquery.replace("open", "")
				urlquery = urlquery.replace("friday", "")
				urlquery = urlquery.replace("website", "")
				urlquery = urlquery.replace("site", "")
				urlquery = urlquery.replace("please", "")
				urlquery = urlquery.replace("please", "")
				urlquery = urlquery.replace("dot", ".")
				print("opening web url")
				speak("opening web url")
				url = urlquery
				webbrowser.open(url)

			except Exception as e:
				print("site can't be reached")
				speak("site can't be reached")
				speak("try again")


		# To return home
		elif ('return' in query) and ('home' in query):
			speak('returning to home')
			keyboard.press_and_release('win + d')


		# Bore statement
		elif ((('I') and (('bored') or ('bore'))) in query) or ("boring" in query):
			print("oho..., don't worry I  am here to entertain you")
			speak("oho..., don't worry I  am here to entertain you")
			print("Do you want to play a game?")
			speak("Do you want to play a game?")
			print("Or would you like to hear some music")
			speak("Or would you like to hear some music")
			some_random_command = takeCommand().lower()

			if ('music' in some_random_command):
				print("playing music")
				speak("playing music")
				pathformusic = "C:\\Users\\NEERAJ KUMAR\\Music\\Playlists\\mix.zpl"
				os.startfile(pathformusic)
				break

			elif ('game' in some_random_command):
				Game()

			else:
				print("I didn't understand, try again")
				speak("I didn't understand, try again")
				some_random_command = takeCommand().lower()

		# TO PLAY ANIME
		elif (('watch' and 'anime') in query) or ('play anime' in query) or ('i want to watch an anime' in query):
			speak("Alright! Let's watch it, which one do you wanna see?")
			anime = takeCommand()
			if 'plastic memories' in anime:
				anime_path = "C:\\Users\\NEERAJ KUMAR\\Videos\\Plastic Memories\\Plastic Memories EP(1).mp4"
				os.startfile(anime_path)
				print('playing Plastic Memories')
				speak('playing Plastic Memories')
				break

			else:
				print("Anime not in system, playing Hyouka")
				speak("Anime not in system, playing Hyouka")
				anime_path = "C:\\Users\\NEERAJ KUMAR\\Videos\\Hyouka\Hyouka - 01 [720p] [Dual] %40Anime_Gallery.mkv"
				os.startfile(anime_path)
				speak('playing Hyouka')
				break

		# FILE EXPLORER
		elif ('open' in query) and ('file explorer' in query):
			speak('opening file explorer')
			keyboard.press_and_release('win + e')
			break

		# OPEN CMD
		elif (('open' and 'cmd') in query) or (('start' and 'cmd') in query) or (('run' and 'cmd') in query) or (
				('play' and 'cmd') in query):
			speak('opening CMD sir')
			subprocess.call(["cmd.exe"])
		# lol = True


		elif ((('windows' or 'window') and ('update' or 'updates')) in query) or (
				('system' and ('update' or 'updates')) in query) or (
				(('update' or 'updates') and ('pc' or 'computer' or 'laptop')) in query):
			speak('opening windows update settings.')
			print('...')
			print('...')
			print('...')
			keyboard.press_and_release('win')
			keyboard.write('update')
			keyboard.press_and_release('enter')
		# lol=True

		# To stop the program execution
		elif ('exit' in query) or (('stop' in query) and ('friday' in query)):
			speak("exiting")
			lol = True

		# To close current running software
		elif ('close this app' in query) or ('close it' in query):
			print("closing this software")
			speak("closing this software")
			keyboard.press_and_release('alt + f4')


		# TO SHUTDOWN PC
		elif ('shut down' in query) or ('shutdown' in query):
			flag = False
			while flag == False:
				print('please tell me the password to shutdown your device')
				speak('please tell me the password to shutdown your device')
				pass_input = takeCommand().lower()

				conditionToPass = (pass_input == '99') or (pass_input == 'ninety nine') or (pass_input == 'ninetynine')

				if conditionToPass:
					print("shutting down")
					print("GoodBye")
					speak("shutting down, GoodBye")
					os.system("shutdown /s /t 1")

				elif not conditionToPass:
					print("The password is not correct, pc is not shutting down. Do you want to try again?")
					speak("The password is not correct, pc is NOT shutting down. Do you want to try again?")
					pass_command = takeCommand().lower()

					if 'yes' not in pass_command:
						print('ok, anything else?')
						speak('ok, anything else?')
						flag = True

					else:
						flag = False
			lol = True

		# TO RESTART PC
		elif ('restart my pc' in query) or ('restart' and ('computer' or 'device')) in query:
			flag = False
			while flag == False:
				print('please tell me the password to restart your device')
				speak('please tell me the password to restart your device')
				pass_input = takeCommand().lower()

				conditionToPass = (pass_input == '99') or (pass_input == 'ninety nine') or (pass_input == 'ninetynine')

				if conditionToPass:
					print("restarting")
					print("Meet you soon")
					speak("Meet you soon")
					os.system("shutdown /r /t 1")

				elif not conditionToPass:
					print("The password is not correct, pc is not restarting down. Do you want to try again?")
					speak("The password is not correct, pc is NOT restarting down. Do you want to try again?")
					pass_command = takeCommand().lower()

					if 'yes' not in pass_command:
						print('ok, anything else?')
						speak('ok, anything else?')
						flag = True

					else:
						flag = False
			lol = True

		# TO START ANY SOFTWARE IN THE SYSTEM
		elif (('I want to' in query) and (('start' in query) or ('run' in query) or ('open' in query))) or (
				('start' in query) and ('software' in query)):
			print("If you want to open any software")
			speak("If you want to open any software")
			print("then say the name of that file or software")
			speak("then say the name of that file or software")
			file_name = takeCommand().lower()
			keyboard.press_and_release('win')
			keyboard.write(file_name, 0.30)
			keyboard.press_and_release('enter')
			print("Okay, anything else?")
			speak("Okay, anything else?")

		elif (('open' and 'calculator') in query) or (('start' and 'calculator') in query) or (
				('run' and 'calculator') in query) or (('play' and 'calculator') in query):
			speak("starting calculator")
			subprocess.call(["calc.exe"])
			# lol = True
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# IF IT GeTS A BAD FEEDBACK
		elif (('you' in query) and (
				('idiot' in query) or ('bad' in query) or ('useless' in query) or ('crap') in query)):
			print('sorry sir, I am still learning')
			speak('sorry sir, I am still learning')
			speak("Try asking about something else in the world. Or let's watch something on youtube")
			query = takeCommand().lower()

		# Brightness control
		elif ('control brightness' in query) or (((('increase') or '(decrease')) and ('brightness' in query)):
			print("tell me the brightness percentage")
			speak("tell me the brightness percentage")
			brightness_command = takeCommand()
			current_brightness = sbc.get_brightness()
			print(f"current brightness {current_brightness}")

			brightness_command = brightness_command.replace('increase brightness to', ' ')
			brightness_command = brightness_command.replace('increase to', ' ')
			brightness_command = brightness_command.replace('percent', ' ')
			brightness_command = brightness_command.replace('%', ' ')

			print(f"increasing brightness to {brightness_command}")
			speak(f"increasing brightness to {brightness_command}")
			word_to_num = brightness_command
			res = w2n.word_to_num(word_to_num)
			sbc.fade_brightness(res)
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# TO CLICK PICTURE
		elif (('click' in query) and ('picture' in query)):
			speak("opening camera")
			camera = cv2.VideoCapture(0)
			print("3....2....1")
			speak("here you go")
			speak("say cheeeese")
			return_value, image = camera.read()
			cv2.imwrite('your pic' + '.png', image)
			del (camera)
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# TO CHECK BATTERY PERCENTAGE
		elif (("what" in query) and ("battery percentage" in query)) or (("how" in query) and ("battery" in query)) or (
				"battery percentage" in query):
			battery = psutil.sensors_battery()
			print(f"{battery.percent} % battery left")
			speak(f"{battery.percent} % battery left")
			print("Okay, anything else?")
			speak("Okay, anything else?")

		# TO TAKE A SCREENSHOT
		elif (("take" in query) and ("screenshot" in query)):
			print("Tell me the name of screenshot to save as")
			speak("please Tell me the name of screenshot to save as")
			name = takeCommand().lower()
			print("please hold a sec, i am taking screenshot")
			speak("please hold a sec, i am taking screenshot")
			time.sleep(2)
			img = pyautogui.screenshot()
			img.save(f"{name}.png")
			print(f"i am done, the screenshot is saved as {name}.png")
			speak(f"i am done, the screenshot is saved as {name}.png")
			print("Okay, anything else?")
			speak("Okay, anything else?")

		elif ('play' in query) and ('game' in query):
			speak("starting game")
			Game()

		# TO PLAY ANYTHING ON YOUTUBE
		elif ('play' in query):
			query = query.replace('play', ' ')
			query = query.replace('hey', ' ')
			query = query.replace('hello', ' ')
			query = query.replace('hey there', ' ')
			query = query.replace('please', ' ')
			query = query.replace('friday', ' ')
			query = query.replace(' ', '')
			query = query.replace('youtube', '')
			print(f"playing {query}")
			speak(f"playing {query}")
			pywhatkit.playonyt(query)
		# lol = True


		# IF HER KNOWLEDGE LACKS
		else:
			print("I don't know what you are saying, would you like to google it?")
			speak("I don't know what you are saying, would you like to google it?")
			answer = takeCommand().lower()
			try:
				if ('yes' in answer) or ('yeah' in answer):
					print('Google Search')
					speak('searching on google')
					query = query.replace('search google for', '')
					query = query.replace('search', '')
					query = query.replace('on google', '')
					query = query.replace(' ', '')
					pywhatkit.search(query)

				else:
					print("anything else?")
					speak("okay, anything else?")
					query = takeCommand().lower()

			except Exception as e:
				print(':)')
