import emoji
import tweepy
import io
from emojis import output

C_KEY = " "
C_SECRET = " "
A_TOKEN = " "
A_TOKEN_SECRET = " "

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(output + "️‍⃠")

L = (output + "\n")
with io.open("used.txt","a", encoding='utf8') as f:
    f.writelines(L)


print("Output: " + "️‍⃠")
