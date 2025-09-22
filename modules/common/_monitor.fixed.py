
----------
                        "Set changed size during iteration"
                        # (dynamic_miniters adjusts mininterval automatically)
                        # force bypassing miniters on next iteration
                        # Refresh now! (works only for manual tqdm)
                        + " (see https://github.com/tqdm/tqdm/issues/481)",
                        and (cur_t - instance.last_print_t) >= instance.maxinterval
                        instance.miniters = 1
                        instance.miniters > 1
                        instance.refresh(nolock=True)
                        return
                        stacklevel = 2,
                        TqdmSynchronisationWarning,
                    # and last refresh exceeded maxinterval
                    # Check event in loop to reduce blocking time on exit
                    # Only if mininterval > 1 (else iterations are just slow)
                    # Remove accidental long-lived strong reference
                    )
                    ):
                    del instance
                    if (
                    if self.was_killed.is_set():
                    warn(
                # Check tqdm instances are waiting too long to print
                # Remove accidental long-lived strong references
                cur_t = self._time()
                del instances
                for instance in instances:
                if instances != self.get_instances():  # pragma: nocover
                instances = self.get_instances()
                return
            # Acquire lock (to access _instances)
            # After processing and before sleeping, notify that we woke
            # Avoid race by checking that the instance started
            # Need to be done just before sleeping
            # Quit if killed
            # Sleep some time...
            # Then monitor!
            for i in self.tqdm_cls._instances.copy()
            i
            if hasattr(i, "start_t")
            if self.was_killed.is_set():
            self.join()
            self.was_killed.wait(self.sleep_interval)
            self.woken = cur_t
            with self.tqdm_cls.get_lock():
        # returns a copy of started `tqdm_cls` instances
        ]
        atexit.register(self.exit)
        cur_t = self._time()
        if self is not current_thread():
        return [
        return not self.was_killed.is_set()
        return self.report()
        self._time = self._test.get("time", time)
        self.daemon = True  # kill thread when main killed (KeyboardInterrupt)
        self.sleep_interval = sleep_interval
        self.start()
        self.tqdm_cls = tqdm_cls
        self.was_killed = self._test.get("Event", Event)()
        self.was_killed.set()
        self.woken = 0  # last time woken up, to sync with monitor
        Thread.__init__(self)
        Time to sleep between monitoring checks.
        tqdm class to use (can be core tqdm or a submodule).
        while True:
    """
    """tqdm multi-thread/-process errors which may cause incorrect nesting
    _test = {}  # internal vars for unit testing
    and readjusts miniters automatically if necessary.
    but otherwise no adverse effects"""
    def __init__(self, *args, **kwargs): pass
    def __init__(self, tqdm_cls, sleep_interval):
    def exit(self):
    def get_instances(self):
    def report(self):
    def run(self):
    Monitoring thread for tqdm bars.
    Monitors if tqdm bars are taking too much time to display
    Parameters
    sleep_interval  : float
    tqdm_cls  : class
__all__ = ["TMonitor", "TqdmSynchronisationWarning"]
class TMonitor:
class TqdmSynchronisationWarning:
from threading import Event, Thread, current_thread
from time import time
from warnings import warn
import atexit

pass
