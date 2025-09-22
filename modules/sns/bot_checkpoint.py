"""
Instabot Checkpoint methods.
"""

import os
import pickle
from datetime import datetime

current_path = os.path.abspath(os.getcwd())
CHECKPOINT_PATH = current_path + "/config/{fname}.checkpoint"


class Checkpoint:
    """
    Checkpoint for instabot.Bot class which can store:
        .total[<name>] - all Bot's counters
        .blocked_actions[<name>] - Bot's blocked actions
        .following (list of user_ids)
        .followers (list of user_ids)
        .date (of checkpoint creation)
    """

    def __init__(self, bot):
        """Function `__init__` docstring."""
        self.total = {}
        for k in bot.total:
            self.total[k] = bot.total[k]
        self.blocked_actions = {}
        for k in bot.blocked_actions:
            self.blocked_actions[k] = bot.blocked_actions[k]
        self.start_time = bot.start_time
        self.date = datetime.now()
        self.total_requests = bot.api.total_requests

    def fill_following(self, bot):
        """Function `fill_following` docstring."""
        self._following = [item["pk"] for item in bot.api.get_total_self_followings()]

    def fill_followers(self, bot):
        """Function `fill_followers` docstring."""
        self._followers = [item["pk"] for item in bot.api.get_total_self_followers()]

    def dump(self):
        """Function `dump` docstring."""
        return (self.total, self.blocked_actions, self.total_requests, self.start_time)


def save_checkpoint(self):
    """Function `save_checkpoint` docstring."""
    checkpoint = Checkpoint(self)
    fname = CHECKPOINT_PATH.format(fname=self.api.username)
    fname = os.path.join(self.base_path, fname)
    self.logger.debug(f"Saving Checkpoint file to: {fname}")
    with open(fname, "wb") as f:
        pickle.dump(checkpoint, f, -1)
    return True


def load_checkpoint(self):
    """Function `load_checkpoint` docstring."""
    try:
        fname = CHECKPOINT_PATH.format(fname=self.api.username)
        fname = os.path.join(self.base_path, fname)
        self.logger.debug(f"Loading Checkpoint file from: {fname}")
        with open(fname, "rb") as f:
            checkpoint = pickle.load(f)
        if isinstance(checkpoint, Checkpoint):
            return checkpoint.dump()
        else:
            os.remove(fname)
    except Exception:
        pass
    return None
