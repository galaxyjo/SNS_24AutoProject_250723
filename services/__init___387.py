
                                     initializer=initialize_session)
        :class:`~requests_toolbelt.threaded.pool.Pool` object.
        :class:`~requests_toolbelt.threaded.pool.ThreadException`)
        Collection of dictionaries representing requests to make with the Pool
        job_queue.put(request)
        Keyword arguments that are passed to the
        'method': 'GET',
        object.
        raise ValueError("map expects a list of dictionaries.")
        session.headers['Accept'] = 'application/json'
        session.headers['User-Agent'] = user_agent('my-scraper', '0.1')
        'url': 'https://api.github.com/repos/requests/toolbelt',
        'url': 'https://api.github.com/users/sigmavirus24',
        'url': 'https://google.com',
    """
    # Build our queue of requests
    # Ensure the user doesn't try to pass their own job_queue
    :param \*\*kwargs:
    :param list requests:
    :returns: Tuple of responses and exceptions from the pool
    :rtype: (:class:`~requests_toolbelt.threaded.pool.ThreadResponse`,
    }, {
    }]
    a generator of successful responses and the second is a generator of
    def initialize_session(session):
    exceptions.
    for request in requests:
    from requests_toolbelt import threaded
    from requests_toolbelt import user_agent
    https://hg.python.org/cpython/file/8ef4f75a8018/Lib/multiprocessing/pool.py
    https://hg.python.org/cpython/file/8ef4f75a8018/Lib/multiprocessing/pool.py#l340
    if not (requests and all(isinstance(r, dict) for r in requests)):
    job_queue = queue.Queue()
    kwargs["job_queue"] = job_queue
    r"""Simple interface to the threaded Pool object.
    responses, errors = threaded.map(urls_to_get)
    responses, errors = threaded.map(urls_to_get,
    responses, errors = threaded.map(urls_to_get, num_processes=10)
    return threadpool.responses(), threadpool.exceptions()
    This function takes a list of dictionaries representing requests to make
    threadpool = pool.Pool(**kwargs)
    threadpool.join_all()
    urls_to_get = [{
    using Sessions in threads and returns a tuple where the first item is
- map and map_async `inspiration`_
- multiprocessing's `pool source`_
"""
.. _inspiration:
.. _pool source:
.. autofunction:: requests_toolbelt.threaded.map
.. code-block:: python
A simple use-case is:
above example, we would expand it like so:
By default, the threaded submodule will detect the number of CPUs your
change this, always use the keyword argument ``num_processes``. Using the
computer has and use that if no other number of processes is selected. To
creating a callback function:
def map(requests, **kwargs):
from . import pool
from .._compat import queue
Inspiration is blatantly drawn from the standard library's multiprocessing
library. See the following references:
pool. The thread pool will use sessions for increased performance.
The module provides a clean and simple API for making requests via a thread
This module provides the API for ``requests_toolbelt.threaded``.
You can also customize how a :class:`requests.Session` is initialized by
