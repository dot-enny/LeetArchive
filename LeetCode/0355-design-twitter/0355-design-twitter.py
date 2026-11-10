class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                for t_count, tweetId in self.tweets[followeeId]:
                    heapq.heappush(min_heap, (t_count, tweetId))
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

