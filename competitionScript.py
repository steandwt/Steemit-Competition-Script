from steem import Steem
import random

#create steem instance
s = Steem()

#set your username
#my username as example
user = 'benniebanana' 
#set the link to your post
#my previous post for example
postLink = 'getting-started-with-steem-python-upvote-and-comment-bot-examples-linux' 

#get all the people who voted on the post
voters = s.get_active_votes(user, postLink)
#create a list of all the voters
voterList = [user['voter'] for user in voters]
#get a list of all the people who reblogged the post
reblogs = s.get_reblogged_by(user, postLink)
#get of your follower count 
followerCount = s.get_follow_count(user)['follower_count']
#retrieve all your followers names
followers = s.get_followers(user, 0, 'blog',  followerCount)
#create a list of all your followers
followerList = [follower['follower'] for follower in followers]
#create a list of all the people who voted, reblogged and followed you
potentialWinnerList = []

for potentialWinner in voterList:
    if potentialWinner in reblogs and potentialWinner in followerList:
        #user is following us and reblogged our post so lets add them to the list
        potentialWinnerList.append(potentialWinner)

#pick a random winner from the list
#check if our list is empty
if not potentialWinnerList: 
#our list is empty :(
    print("No winners :( The list is empty")
else:
#we have some potential winners so lets pick a random one
    winner = random.choice(potentialWinnerList)
    print("yaaay "+winner+" won the competition!!!")
