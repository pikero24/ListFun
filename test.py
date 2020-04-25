#Libraries
import tweepy
import time
import copy
#External Files
import twitter_credentials

def print_tweets(api):
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print(tweet.text)

def checkKey(dict,key):
	if key in dict:
		return True
	else:
		return False

def printDict(dict):
	for element in dict:
		print(dict[element])

if __name__ == "__main__":
	auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

	#print_tweets(api)
	user = api.get_user("JCTecklenburg")
	# user = api.friends_ids("JCTecklenburg")
	# print(user.followers_count)
	userLists = api.lists_all(user.name)

	#initialize list
	listRef = []
	for i in range(len(userLists)):
		listRef.append(False)
	#Followers["user.id"] = [user.id, user.name, user.screen_name,[booleans of list membership]]
	followers = {}

	print("GETTING FOLLOWERs")


	for page in tweepy.Cursor(api.friends).pages():
		for follow in page:
			# print(follow.name, follow.screen_name, follow.id)
			followers[follow.id] = [follow.id, follow.name, follow.screen_name,copy.deepcopy(listRef)]
			# print(followers[follow.id])
		# print(".", end = '')
		print(len(followers))
		time.sleep(10)
	print(len(followers))


	#Get Lists, then print out members
	# userLists = api.lists_all(user.name)
	print("GETTING LISTs")
	listID = 0
	for tList in userLists:
		print(" ")
		print (tList.id, tList.name,tList.slug)
		# print("---------------------------------------------")
		# members = []
		for member in tweepy.Cursor(api.list_members, 'JCTecklenburg', tList.slug).items():
			if(checkKey(followers,member.id)):
				followers[member.id][3][listID] = True
			# members.append(member.name)
			print(".", end = '')
		# print(members)
		listID += 1
	print(" ")
	
	# printDict(followers)

	for userInfo in followers:
		noList = True;
		# print(followers[userInfo][2] , " ", followers[userInfo][3])
		for listCheck in followers[userInfo][3]:
			# print(listCheck, followers[userInfo][3][listCheck])
			if listCheck:
				# print(True) 
				noList = False
				continue
		if noList == True:
			print("https://twitter.com/" + followers[userInfo][2] + " " , followers[userInfo][3])

