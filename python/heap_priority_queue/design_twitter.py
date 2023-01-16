from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.timeStamp = 0
        self.follows = {}
        self.userToTweets = {}
        
    def __init_user(self,userId:int):
        self.follows[userId] = [userId]
        self.userToTweets[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userToTweets:
            self.__init_user(userId)
        self.userToTweets[userId].append((tweetId,self.timeStamp))
        self.timeStamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follows:
            self.__init_user(userId)
        timeStamps = []
        timeStampToTweet = {}
        for followee in self.follows[userId]:
            for id,timestamp in self.userToTweets[followee]:
                timeStamps.append(-timestamp)
                timeStampToTweet[-timestamp] = id
        heapq.heapify(timeStamps)
        feed = []
        for i in range(10):
            if not timeStamps:
                return feed
            feed.append(timeStampToTweet[heapq.heappop(timeStamps)])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.__init_user(followerId)
        if followeeId not in self.follows:
            self.__init_user(followeeId)
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId not in self.follows:
            return
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1,1)
    twitter.getNewsFeed(1)
    twitter.follow(2,1)
    print(twitter.getNewsFeed(2))
    twitter.unfollow(2,1)
    twitter.getNewsFeed(2)