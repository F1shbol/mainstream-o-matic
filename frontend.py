from datetime import datetime

current_timestamp = int(datetime.now().timestamp())
lastWeek = current_timestamp - 864000

def welcome():
    print("Welcome to the Mainstream-O-Matic!\n\nTo get started, follow these steps:\n"\
            "1) Open your browser and go to htpps://mainstream.ghan.nl/export.html\n" \
            "2) Enter the last.fm username of the user you want to score\n"\
            "3) Select \"Scrobbles\" from the first dropdown and \"csv\" from the second\n"\
            "4) Enter this number in the \"Previous timestamp\" box:", lastWeek, "\n"\
            "5) Click go to download the file, then move it into the same directory as this program\n\n"\
            "Have you completed the above steps?\n1. Yes, run the program\n2. No, I'm not ready")

    ans = input()
    if (ans == "1"):
        return True
    else:
        return False