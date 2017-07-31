from steem import Steem
import random

#create steem instance
s = Steem()

#set your username
user = '<your steemit username>'
#set the link to your post
postLink = '<permlink to post>'

#get all voters on a post
voters = s.get_active_votes(user, postLink)
#create a list of all the voters
voterList = [user['voter'] for user in voters]
#get a list of all the people who reblogged the post
reblogs = s.get_reblogged_by(user, postLink)
#get of all your followers
followers = s.get_followers(user, 0, 'blog', <your follower count or greater>)
#create a list of all your followers
followerList = [follower['follower'] for follower in followers]
#create a list of all the people who voted, reblogged and followed you
potentialWinnerList = []

for potentialWinner in voterList:
    if potentialWinner in reblogs and potentialWinner in followerList:
        #user is following us and reblogged our post so lets add them to the list
        potentialWinnerList.append(potentialWinner)

#pick a random winner from the list
winner = random.choice(potentialWinnerList)
print("yaaay " + winner + " won the competition!!!")
