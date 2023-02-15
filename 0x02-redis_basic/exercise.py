#!/usr/bin/env python3
""" Redis module that declares methods and class"""

from typing import Callable, Union
from uuid import uuid4
import redis


class Cache:
    """declares a class Cache"""
    def __init__(self) -> None:
        """Instantiate redit client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
