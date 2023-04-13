#!/usr/bin/python3
"""
caches data for faster retrieval
"""
import redis
from os import getenv


class Cache:

    def __init__(self):
        port = getenv('REDIS_PORT') or 6379
        host = getenv('REDIS_HOST') or 'localhost'
        self.__r = redis.Redis(host=host, port=port)


    def set_value(self, key, value):
        """
        cache 50 values in redis server at most
        """
        count = self.__r.dbsize()
        if count < 50:
            self.__r.set(key, value)
        else:
            oldest_key = self.__r.keys(pattern='*')[0]
            self.__r.delete(oldest_key)
            self.__r.set(key, value)
        return True


    def get_value(self, key):
        """
        checks if a value is saved in the redis
        server.
        """
        value = self.__r.get(key)

        if value is None:
            return False
        return value
