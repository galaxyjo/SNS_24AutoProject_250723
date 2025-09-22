# modules/queue/_wakeup_socketpair.py

import socket
import threading


class WakeupSocketpair:
    """Cross-thread notification using socketpair (for event loop integration)."""

    def __init__(self) -> None:
        self._r, self._w = socket.socketpair()
        self._r.setblocking(False)
        self._w.setblocking(False)
        self._lock = threading.Lock()

    def wakeup_thread_and_signal_safe(self) -> None:
        with self._lock:
            try:
                self._w.send(b"x")
            except OSError:
                pass  # already woken

    def wait_woken(self) -> None:
        try:
            while self._r.recv(1):
                pass
        except BlockingIOError:
            pass

    def close(self) -> None:
        self._r.close()
        self._w.close()
