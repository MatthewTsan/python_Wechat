import itchat

def friend_proportion_gender():
    friends_list = itchat.get_friends(update=True)

    male = famale = other = 0

    for item in friends_list[1:]:
        sex = item['Sex']

        if sex == 1:
            male += 1
        elif sex == 2:
            famale += 1
        else:
            other += 1

    total = len(friends_list[1:])

    print("male: %.2f%%" % (float(male) /total * 100))
    print("famale: %.2f%%" % (float(famale) /total * 100))
    print("other: %.2f%%" % (float(other) /total * 100))

if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=False)

    group_list = itchat.get_chatrooms()
