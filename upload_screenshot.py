import instabot
import glob
import os

try:
    # this part was added to remove ds_user error which was some cookie problem
    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])

except IndexError:
    pass

finally:

    bot = instabot.Bot()


    def upload(path):
        bot.upload_photo(path, caption="answer it please")


    def login():
        uname = "william_as_a_human"
        passwd = "9thang10ngay"
        bot.login(username=uname, password=passwd)

    '''login()
    upload(str(input("Enter the path")))'''
