import praw
import model_bot as model
from time import sleep

sleeptime = 600 # Tid mellan posts i sekunder

reddit = praw.Reddit(client_id='G2wVn4hb94fhWw',
                    client_secret='XdFNEB-eCSPlwutC0bdm8YgsUUo',
                    user_agent='abbspets',
                    username='abbspets123',
                    password='qwerty123')

def makeNewPost(title, body): # Skapar post med titel och body
    reddit.subreddit("BotsParadise").submit(title, selftext=body)
    print(title, body)
    print("New post submitted")

while True:
    new_post_data = model.generate_text()
    makeNewPost(new_post_data["title"], new_post_data["body"])
    print("Sleeping...")
    sleep(sleeptime)
    print("Awake!")