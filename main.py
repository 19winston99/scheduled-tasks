# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

# import os and use it to get the Github repository secrets
import smtplib
import datetime as dt
import random
import os

quotes = []
EMAIL = "hasaroberto99@gmail.com" | os.environ.get("MY_EMAIL")
PASSWORD = "hzqsyhckgmmhdlrv" | os.environ.get("PWD")
EMAIL_RECIP = "schiesaro.giada@gmail.com" | os.environ.get("EMAIL_RECIP")

with open("quotes.txt") as file:
    quotes = file.readlines()

msg_body = f"Subject:Lucky Charm\n\n{random.choice(quotes)}"

today = dt.datetime.now()

if today.weekday() == 0:
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL_RECIP,
                msg=msg_body.encode("utf-8"))
    except Exception:
        raise
