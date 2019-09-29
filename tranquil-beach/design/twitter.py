from collections import defaultdict
import time

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(set) # userId -> followeeIds
        self.posts = defaultdict(list) # userId -> posts, posts = (timestamp, postId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        ts = time.time()
        self.posts[userId].append((ts, tweetId))

    def getNewsFeed(self, userId: int) -> 'List[int]':
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = [v for v in self.posts[userId]]
        for id in self.users[userId]:
            news += self.posts[id]
        return [id for _, id in sorted(news, reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.users[followerId].discard(followeeId)