from modules.task_queue_mgr import TaskQueueManager


def test_enqueue_and_dequeue():
    queue = TaskQueueManager()
    queue.enqueue("job1")
    queue.enqueue("job2")
    assert queue.dequeue() == "job1"
    assert queue.dequeue() == "job2"
    assert queue.dequeue() is None


def test_queue_empty_and_size():
    queue = TaskQueueManager()
    assert queue.is_empty() is True
    assert queue.size() == 0
    queue.enqueue("x")
    assert queue.is_empty() is False
    assert queue.size() == 1


def test_clear_queue():
    queue = TaskQueueManager()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.clear()
    assert queue.is_empty() is True
    assert queue.size() == 0
    assert queue.dequeue() is None
