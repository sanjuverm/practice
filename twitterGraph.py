""""- create a follows dictionary, create a recommendedTweets list

- Iterate over followGraph edges, inserting each of the users targetUserId follows in to the follows dictionary

- Iterate over likeGraph edges, inserting all tweets that a user that targetUser follows has liked (use the follows dictionary to check if they are a follower)

- If tweet already exists in recommendedTweets list, increment count by 1

- map, then filter out tweets in recommendedTweets list that are not over the minThreshhold

- return recommendedTweets"""

import operator

def main():
    print "Working"
    followGraph_edges = [(1, 2), (1, 3), (1, 4)]
    targetUser = 1
    minLikeThreshold = 3
    likeGraph_edges = [(2, 10), (3, 10), (4, 10), (2, 11), (3, 12), (4, 11)]
    temp = getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold)
    print ("temp: ")
    print(temp)


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

if __name__ == "__main__": main()

