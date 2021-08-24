import praw
import config
import time
import os
import random
print()
def randomTime():
    randomText1 = random.randint(150,321)
    return  randomText1
def randomLine():
    textim = random.choice(list(open('readme.txt')))
    return textim

def bot_login():
	print ("Logging in...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "replay bot by u/Accountfinders")
	print ("Logged in!")

	return r

def run_bot(subreddit1, comments_replied_to):
	print ("Searching last 1,000 comments")
   

	for submission in subreddit1.new(limit=1):
		if submission.id not in comments_replied_to :
			print ("String with \"sample user comment\" found in comment " + submission.id)
     
			submission.reply(randomLine()+" ->> [MEGA FOLDER](https://l24.im/sOc)")    
			print ("Replied to comment " + submission.id)

			comments_replied_to.append(submission.id)
          
			with open ("comments_replied_to.txt", "a") as f:
				f.write(submission.id + "\n")

	print ("Search Completed.")

	print (comments_replied_to)
    
	print ("Sleeping for seconds...",time.sleep(randomTime()))
    
   
	#Sleep for 100 seconds...		

def get_saved_comments():

	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
subreddit1 = r.subreddit('WorldPacks+xxxycelebs+JizzedToThiss+nsfw_gifs+Megnutt02_+knockmeup+youngporn+gothsluts')
comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
	run_bot(subreddit1, comments_replied_to)