#Libraries
import tweepy
import time
#External Files
import twitter_credentials

def print_tweets(api):
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print(tweet.text)

if __name__ == "__main__":
	auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	#print_tweets(api)
	user = api.get_user("JCTecklenburg")
	# user = api.friends_ids("JCTecklenburg")
	# print(user.followers_count)
	userLists = api.lists_all(user.name)

	#List to reference in the followers dict
	listRef = []
	for i in range(len(userLists)):
		#initialize list
		listRef.append(False)
	#Followers["user.id"] = [user.id, user.name, user.screen_name,[booleans of list membership]]
	followers = {}

	for page in tweepy.Cursor(api.friends).pages(3):
		for follow in page:
			# print(follow.name, follow.screen_name, follow.id)
			followers[follow.id] = [follow.id, follow.name, follow.screen_name,listRef]
			print(followers[follow.id])
		print("__________")
		time.sleep(2)


	#Get Lists, then print out members
	# userLists = api.lists_all(user.name)
	# listID = 0
	# for tList in userLists:
	# 	print (tList.id, tList.name,tList.slug)
	# 	print("---------------------------------------------")
	# 	members = []
	# 	for member in tweepy.Cursor(api.list_members, 'JCTecklenburg', tList.slug).items():
	# 		members.append(member.name)
	# 	print(members)
	# 	listID = listID + 1
	


	# 	memmbers = api.list_members(tList.id)
		# print(api.get_list(tList.id))


	# 	for tList in userLists:
	# 		if 

	# print( user.friends()[3] )

	