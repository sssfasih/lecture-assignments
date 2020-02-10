'''
Design an application in which you print all the names of your
friends whom you are calling on your graduation ceremony
(use iteration logic). If name of your friend starts with vowels
then print ”Oh my lovely friend” in the start otherwise it
would be ”name of friend, I would like you to come on my
graduation ceremony”.

'''
friends = ["ali","sara","usman","faisal","yumnah","ibad"]
message = "I would like you to come on my graduation ceremony"
for friend in friends :
    if friend[0] == "a" or friend[0] == "e" or friend[0] == "i" or friend[0] == "o" or friend[0] == "u" or friend[0] == "A" or friend[0] == "E" or friend[0] == "I" or friend[0] == "O" or friend[0] == "U" :
        friend = friend.title()
        print("Oh my lovely friend",friend,message)