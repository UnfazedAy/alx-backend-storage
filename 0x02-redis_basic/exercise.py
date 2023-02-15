#!/usr/bin/env python3
""" Redis module that declares methods and class"""

from typing import Callable, Union, Optional
from uuid import uuid4
from functools import wraps
import redis

def count_calls(method: Callable) -> Callable:
    '''count how many times methods of Cache class are called'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated function and return the wrapper'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """declares a class Cache"""
    def __init__(self) -> None:
        """Instantiate redit client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates and returns a random key string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, float, bytes, int]:
        """Converts data back into any format"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Parametrize Cache.get with the correct conversion(str)"""
        return self._redis.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Parametrize Cache.get with the correct conversion(int)"""
        return self._redis.get(key, lambda x: int(x))
