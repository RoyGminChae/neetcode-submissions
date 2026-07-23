from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId : list of (time, tweetId)
        self.followMap = defaultdict(set) # userId: set of ids it follows

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush_max(maxHeap, (time, followeeId, tweetId, index))

        while maxHeap and len(res) < 10:
            time, followeeId, tweetId, index = heapq.heappop_max(maxHeap)
            
            res.append(tweetId)
            if index > 0:
                nextTime, nextTweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush_max(maxHeap, (nextTime, followeeId, nextTweetId, index - 1))
    
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)







