import json
import praw
import requests


with open("/home/haboussi/streak.txt", 'r') as f:
        lines = f.readlines()
        write_streak = int(lines[0].split('=')[1])
        speak_streak = int(lines[1].split('=')[1])

writesub = 'WriteStreakGerman'
speaksub = 'SpeakStreakDeutsch'
credentials = 'clients_secrets1.json'
 
with open(credentials) as f:
    creds = json.load(f)
 
reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])
                     

flair_id_verbesser_mich = None
for template in reddit.subreddit('WriteStreakGerman').flair.link_templates:
    if template['text'] == 'Verbesser mich!':
        flair_id_verbesser_mich = template['id']
        break


if flair_id_verbesser_mich is None:
    print("Error: Flair ID for 'Verbesser mich!' not found.")
    exit(1)


flair_id_nicht_korrigieren  = None
for template in reddit.subreddit('WriteStreakGerman').flair.link_templates:
    if template['text'] == 'Nicht korrigieren!':
        flair_id_nicht_korrigieren = template['id']
        break


if flair_id_nicht_korrigieren  is None:
    print("Error: Flair ID für 'Nicht Korrigieren!' nicht gefunden.")
    exit(1)

pause_or_not=input("Pause ? j/n")
if pause_or_not.lower()=="n":

	title = f'Streak {write_streak}'
	body = input("write text: ")
	write_subreddit = reddit.subreddit(writesub)
	write_subreddit.submit(title, selftext=body, flair_id=flair_id_verbesser_mich)

	speak_title = f'Streak {speak_streak}'
	speak_body = input("Vocaroo link: ")
	speak_subreddit = reddit.subreddit(speaksub)
	speak_subreddit.submit(speak_title, selftext=speak_body)
else:
	title2 = f'Streak {write_streak} - Pause'
	body2 = "bis morgen InchAllah"
	write_subreddit2 = reddit.subreddit(writesub)
	write_subreddit2.submit(title2, selftext=body2, flair_id=flair_id_nicht_korrigieren)

	speak_title2 = f'Streak {speak_streak} - Pause'
	speak_body2 = "bis morgen InchAllah"
	speak_subreddit2 = reddit.subreddit(speaksub)
	speak_subreddit2.submit(speak_title2, selftext=speak_body2)



write_streak += 1
speak_streak += 1
with open("/home/haboussi/streak.txt", "w") as f:
        f.write(f"WriteStreakGerman_streak={write_streak}\n")
        f.write(f"SpeakStreakDeutsch={speak_streak}\n")


