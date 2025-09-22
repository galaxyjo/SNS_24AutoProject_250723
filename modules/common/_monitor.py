# modules/common/_monitor.py
# ✅ manualfixed: tqdm 모니터링 쓰레드 안정화 / 파서 오류 제거 / 구조 정리

import atexit
from threading import Event, Thread, current_thread
from time import time
from warnings import warn


__all__ = ["TMonitor", "TqdmSynchronisationWarning"]


class TqdmSynchronisationWarning(Warning):
    """Raised when tqdm bars may be out of sync between threads."""


class TMonitor(Thread):
    """
    Monitoring thread for tqdm bars.
    Monitors if tqdm bars are taking too much time to display
    and readjusts miniters automatically if necessary.

    Parameters:
    - tqdm_cls: tqdm class to use (can be core tqdm or a submodule).
    - sleep_interval: float, time to sleep between monitoring checks.
    """

    _test = {}  # internal vars for unit testing

    def __init__(self, tqdm_cls, sleep_interval: float):
        super().__init__()
        self.daemon = True  # kill thread when main killed (KeyboardInterrupt)
        self.tqdm_cls = tqdm_cls
        self.sleep_interval = sleep_interval
        self._time = self._test.get("time", time)
        self.was_killed = self._test.get("Event", Event)()
        self.woken = 0  # last time woken up, to sync with monitor
        atexit.register(self.exit)
        self.start()

    def exit(self):
        """Mark the thread as killed so it stops on the next loop."""
        self.was_killed.set()

    def get_instances(self):
        """Returns a copy of started `tqdm_cls` instances."""
        with self.tqdm_cls.get_lock():
            return list(self.tqdm_cls._instances)

    def run(self):
        """Main monitoring loop."""
        while not self.was_killed.is_set():
            cur_t = self._time()
            instances = self.get_instances()
            for instance in instances:
                if not hasattr(instance, "start_t"):
                    continue
                if self.was_killed.is_set():
                    break
                if instance.miniters > 1:
                    if (cur_t - getattr(instance, "last_print_t", 0)) >= instance.maxinterval:
                        warn(
                            f"{instance.desc or ''} (tqdm progress bar may be stuck)"
                            " (see https://github.com/tqdm/tqdm/issues/481)",
                            TqdmSynchronisationWarning,
                            stacklevel=2,
                        )
                        instance.miniters = 1  # force refresh
                        instance.refresh(nolock=True)
            self.woken = cur_t
            self.was_killed.wait(self.sleep_interval)
