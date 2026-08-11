"""
Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and is able to see the 10 most recent
tweets in the user's news feed.

Implement the Twitter class:

Twitter()
    Initializes your twitter object.

void postTweet(int userId, int tweetId)
    Composes a new tweet with ID tweetId by the user userId.
    Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId)
    Retrieves the 10 most recent tweet IDs in the user's news feed.
    Each item in the news feed must be posted by users who the user
    followed or by the user themself. Tweets must be ordered from most
    recent to least recent.

void follow(int followerId, int followeeId)
    The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId)
    The user with ID followerId started unfollowing the user with ID followeeId.
"""

import heapq
import sys
from collections import defaultdict
from itertools import count

class Twitter:
    """
    Approach: min heap to collect the most recent tweets

    Use a globally decrementing timestamp so the heap can pop
    the most recent tweets (i.e., those with a smaller timestamp)

    getNewsFeed(userId):
        T: O(F*log(F) + limit*log(F))
        S: O(F + limit)

        where F = total followees of userId

    For all other methods, time is O(1)
    """

    _id: count  # global timestamp; lower = more recent
    tweetMap:  defaultdict[int, list[tuple[int, int]]]  # {userId: [(_id, tweetId) ...]}
    followMap: defaultdict[int, set]                    # {followerId: {followeeId, ...}}
    
    def __init__(self):
        self._id = count(start=sys.maxsize, step=-1)
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int):
        self.tweetMap[userId].append((next(self._id), tweetId))

    def getNewsFeed(self, userId: int, limit: int = 10) -> list[int]:
        heap = []  # heap of (_id, tweetId, followeeId, nextIndex)

        self.follow(userId, userId)  # ensure self is included in the feed
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1

                heapq.heappush(heap, (
                    *self.tweetMap[followeeId][index],
                    followeeId,
                    index - 1
                ))
        self.unfollow(userId, userId)  # unfollow self

        res = []  # most recent tweets in this user's feed
        while heap and len(res) < limit:
            _, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            # add the next most recent tweet from the followee if there exists one
            if index >= 0:
                heapq.heappush(heap, (
                    *self.tweetMap[followeeId][index],
                    followeeId,
                    index -  1
                ))

        return res

    def follow(self, followerId: int, followeeId: int):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        self.followMap[followerId].discard(followeeId)
