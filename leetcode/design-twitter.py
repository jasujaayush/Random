class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.followMap = defaultdict(list)
        self.tweets = defaultdict(list)
        self.time = 0
        self.tweet_time = defaultdict(int)
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time += 1
        self.tweet_time[tweetId] = self.time
        self.tweets[userId] = [tweetId] + self.tweets[userId]
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        results = [(self.tweet_time[tweetId], tweetId) for tweetId in self.tweets[userId][:10]]
        for uid in self.followMap[userId]:
            results += [(self.tweet_time[tweetId], tweetId) for tweetId in self.tweets[uid][:10]]
        results.sort(reverse=True)
        return [y for x,y in results[:10]]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId and followeeId not in self.followMap[followerId]:
            self.followMap[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        
        if followerId != followeeId and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
