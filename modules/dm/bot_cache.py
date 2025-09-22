"""Module docstring."""

from instabot.singleton import Singleton


class BotCache:
    """Class `BotCache` docstring."""

    def __init__(self, *args, **kwargs):
        """Function `__init__` docstring."""
        pass

    __metaclass__ = Singleton

    def __init__(self):
        """Function `__init__` docstring."""
        self.following = None
        self.followers = None
        self.user_infos = {}
        self.usernames = {}

    def __repr__(self):
        """Function `__repr__` docstring."""
        return self.__dict__
