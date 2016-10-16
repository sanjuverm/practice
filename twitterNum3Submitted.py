# Complete the function below.
# followGraph_edges is a list of tuples (userId, userId)
# likeGraph_edges is also a list of tuples (userId, tweetId)

"""
Logic: of the people you follow, and for each of those people, iterate through the tweets that they like. then increment a count for each tweet in the dictionary and check which ones exceed the threshold
"""
""""- create a follows dictionary, create a recommendedTweets list

- Iterate over followGraph edges, inserting each of the users targetUserId follows in to the follows dictionary

- Iterate over likeGraph edges, inserting all tweets that a user that targetUser follows has liked (use the follows dictionary to check if they are a follower)

- If tweet already exists in recommendedTweets list, increment count by 1

- map, then filter out tweets in recommendedTweets list that are not over the minThreshhold

- return recommendedTweets"""

#s = sys.stdin.read()
#print(s)
import operator

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    follows = []
    rec_tweets = {}

    for i, k in followGraph_edges:
        if i == targetUser:
            follows.append(k)

    for i, k in likeGraph_edges:
        if i in follows:
            if k in rec_tweets:
                rec_tweets[k] += 1
            else:
                rec_tweets[k] = 1

    #print (rec_tweets)

    rec_tweets = {k:v for k, v in list(rec_tweets.items()) if v >= minLikeThreshold}

    #print(sorted(rec_tweets.items(), key=operator.itemgetter(1)))
    rec_tweets = dict(sorted(rec_tweets.items(), key=operator.itemgetter(1)))
    return rec_tweets.keys()
    

