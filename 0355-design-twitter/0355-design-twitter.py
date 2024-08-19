class Twitter:

    def __init__(self):
        self.posts = []
        self.followList = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [userId, tweetId]
        self.posts.append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for i in range(len(self.posts) - 1, -1, -1):
            if self.posts[i][0] == userId:
                feed.append(self.posts[i][1])
            else:
                if userId in self.followList:
                    if self.posts[i][0] in self.followList[userId]:
                        feed.append(self.posts[i][1])
            if len(feed) == 10:
                return feed
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followList:
            self.followList[followerId] = [followeeId]
        else:
            if followeeId not in self.followList[followerId]:
                self.followList[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followList:
            if followeeId in self.followList[followerId]:
                self.followList[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)