# modules/core/__init__.py


# from .parking_lot import ParkingLot
# from .checkpoint import checkpoint_if_cancelled, checkpoint
# from .task import current_task, spawn_system_task
# from .errors import WouldBlock, RunFinishedError
class ParkingLot:
    def park(self):
        pass


def checkpoint_if_cancelled():
    pass


class WouldBlock(Exception):
    pass
