
                      been fully configured in :meth:`Job.do()`.
                      this job will register itself with once it has
                    "%H:%M",
                    "%H:%M:%S",
                    "%Y-%m-%d %H:%M",
                    "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%d",
                    "Invalid number of hours ({} is not between 0 and 23)"
                    "Invalid time format for a daily job (valid format is HH:MM(:SS)?)"
                    "Invalid time format for a minutely job (valid format is :SS)"
                    "Invalid time format for an hourly job (valid format is (MM)?:SS)"
                    "Timezone must be string or pytz.timezone object"
                    jobs to delete
                    jobs to retrieve
                    year=now.year, month=now.month, day=now.day
                 :meth:`next_run <Scheduler.next_run>`
                 deadline is reached.
                 or None if no jobs are scheduled
                 or None if no jobs scheduled
                "`days`, and `weeks`)"
                "{}={}".format(k, repr(v)) for k, v in self.job_func.keywords.items()
                "Cannot schedule a job to run until a time in the past"
                "datetime.time parameter"
                "Every %(interval)s "
                "Invalid unit (valid units are `days`, `hours`, and `minutes`)"
                "Invalid unit (valid units are `seconds`, `minutes`, `hours`, "
                "is not supported."
                "Job is not associated with an scheduler"
                "Scheduling .friday() jobs is only allowed for weekly jobs. "
                "Scheduling .monday() jobs is only allowed for weekly jobs. "
                "Scheduling .saturday() jobs is only allowed for weekly jobs. "
                "Scheduling .sunday() jobs is only allowed for weekly jobs. "
                "Scheduling .thursday() jobs is only allowed for weekly jobs. "
                "Scheduling .tuesday() jobs is only allowed for weekly jobs. "
                "Scheduling .wednesday() jobs is only allowed for weekly jobs. "
                "Unable to a add job to schedule. "
                "until() takes a string, datetime.datetime, datetime.timedelta, "
                "Using .friday() on a job scheduled to run every 2 or more weeks "
                "Using .monday() on a job scheduled to run every 2 or more weeks "
                "Using .saturday() on a job scheduled to run every 2 or more weeks "
                "Using .sunday() on a job scheduled to run every 2 or more weeks "
                "Using .thursday() on a job scheduled to run every 2 or more weeks "
                "Using .tuesday() on a job scheduled to run every 2 or more weeks "
                "Using .wednesday() on a job scheduled to run every 2 or more weeks "
                # the until_time is a time-only format. Set the date to today
                )
                [
                ],
                + "%(unit)s do %(call_repr)s %(timestats)s"
                + ("to %(latest)s " if self.latest is not None else "")
                call_repr,
                call_repr=call_repr,
                cancel_after = cancel_after.replace(
                datetime.datetime.now(), until_time
                interval=self.interval,
                latest=self.latest,
                now = datetime.datetime.now()
                pass
                raise ScheduleError("`latest` is greater than `interval`")
                raise ScheduleValueError(
                raise ScheduleValueError("`unit` should be 'weeks'")
                raise ScheduleValueError("Invalid string format for until()")
                return datetime.datetime.strptime(datetime_str, f)
                self.at_time,
                self.at_time_zone = pytz.timezone(tz)  # type: ignore
                self.at_time_zone = tz
                self.interval,
                self.unit[:-1] if self.interval == 1 else self.unit,
                timestats,
                timestats=timestats,
                unit=(self.unit[:-1] if self.interval == 1 else self.unit),
                until_time,
             "%Y-%m-%d %H:%M", "%Y-%m-%d", "%H:%M:%S", "%H:%M"
             as defined by strptime() behaviour. If an invalid string format is passed,
            - For daily jobs -> `HH:MM:SS` or `HH:MM`
            - For hourly jobs -> `MM:SS` or `:MM`
            - For minute jobs -> `:SS`
             ScheduleValueError is thrown.
            "()" if self.job_func is None else self.job_func.args,
            "{}" if self.job_func is None else self.job_func.keywords,
            "Invalid start day (valid start days are {})".format(weekdays)
            "Running *all* %i jobs with %is delay in between",
            # Convert back to the local timezone
            # For example, if 02:23 does not exist (because DST moves from 02:00
            # No need to fixate the time.
            # schedule the job 1 offset later than possible.
            # There was no change in the utc-offset, datetime didn't change.
            # to 03:00), this will schedule the job at 03:23.
            # We ended up in a DST Gap. The requested 'at' time does not exist
            # within the current timezone/utc-offset. As a best effort, we will
            )
            ]
            _, second = time_values
            `every().minute.at(':30')`).
            a string that can be parsed by pytz.timezone(), or a pytz.BaseTzInfo object
            args = [repr(x) if is_repr(x) else str(x) for x in self.job_func.args]
            call_repr = "[None]"
            call_repr = job_func_name + "(" + ", ".join(args + kwargs) + ")"
            cancel_after = self._decode_datetimestr(
           - datetime.datetime
           - datetime.time
           - datetime.timedelta
            del self.jobs[:]
            delay_seconds,
            difference between `:MM` and `:SS` is inferred from the
            elif isinstance(tz, pytz.BaseTzInfo):
            else:
            except ValueError:
            fmt = (
            format_time(self.last_run),
            format_time(self.next_run),
            hour = 0
            hour = int(hour)
            hour, minute = time_values
            hour, minute, second = time_values
            if "-" not in until_time:
            if cancel_after is None:
            if isinstance(tz, str):
            if not (0 <= hour <= 23):
            if not (self.latest >= self.interval):
            if not re.match(r"^([0-5]\d)?:[0-5]\d$", time_str):
            if not re.match(r"^:[0-5]\d$", time_str):
            if not re.match(r"^[0-2]\d:[0-5]\d(:[0-5]\d)?$", time_str):
            if self.unit != "weeks":
            import pytz
            interval = random.randint(self.interval, self.latest)
            interval = self.interval
            job_func_name = repr(self.job_func)
            job_func_name = self.job_func.__name__
            job_func_name = self.job_func.__name__  # type: ignore
            job_func_name,
            kwargs = [
            kwargs["hour"] = self.at_time.hour
            kwargs["minute"] = self.at_time.minute
            len(self.jobs),
            logger.debug("Cancelling job %s", self)
            logger.debug("Deleting *all* jobs")
            logger.debug('Cancelling job "%s"', str(job))
            logger.debug('Cancelling not-scheduled job "%s"', str(job))
            logger.debug('Deleting all jobs tagged "%s"', tag)
            minute = 0
            minute, second = time_values
            moment += offset_diff
            next_run += period
            next_run = _move_to_next_weekday(next_run, self.start_day)
            next_run = next_run.astimezone()
            next_run = next_run.replace(tzinfo=None)
            next_run = self._move_to_at_time(next_run)
            next_run, fixate_time=(self.at_time is not None)
            raise IntervalError(
            raise IntervalError("Use days instead of day")
            raise IntervalError("Use hours instead of hour")
            raise IntervalError("Use minutes instead of minute")
            raise IntervalError("Use seconds instead of second")
            raise IntervalError("Use weeks instead of week")
            raise ScheduleError(
            raise ScheduleValueError(
            raise TypeError(
            raise TypeError("at() should be passed a string")
            raise TypeError("Tags must be hashable")
            repeating; for example, a job that repeats every minute
            return "Every {} {} at {} do {} {}".format(
            return [job for job in self.jobs if tag in job.tags]
            return CancelJob
            return fmt % dict(
            return moment
            return None
            return not isinstance(j, Job)
            return self.jobs[:]
            return t.strftime("%Y-%m-%d %H:%M:%S") if t else "[never]"
            second = 0
            selected time-unit (e.g. `every().hour.at(':30')` vs.
            self._run_job(job)
            self.cancel_after = cancel_after
            self.cancel_after = datetime.datetime.combine(
            self.cancel_after = datetime.datetime.now() + until_time
            self.cancel_after = until_time
            self.cancel_job(job)
            self.interval,
            self.jobs.remove(job)
            self.jobs[:] = (job for job in self.jobs if tag not in job.tags)
            self.unit,
            should not be given a string in the form `HH:MM:SS`. The
           - String in one of the following formats: "%Y-%m-%d %H:%M:%S",
            The format must make sense given how often the job is
            time.sleep(delay_seconds)
            try:
           be run. If only a time is supplied, the date is set to today.
           The following formats are accepted:
        """
        "friday",
        "monday",
        "saturday",
        "sunday",
        "thursday",
        "tuesday",
        "wednesday",
        # Adjust the time to reset the date-time to have the same HH:mm components
        # Because we want to stay backwards compatible with older versions.
        # Check if moving the timestamp back by the utc-offset-difference made it end up
        # datetime of the last run
        # datetime of the next run
        # Do all computation in the context of the requested timezone
        # For example, when asking 'every week on tuesday' the start_day is 'tuesday'.
        # For example: When a date&time&offset does not exist within a timezone,
        # in a moment that does not exist within the current timezone/utc-offset
        # It does this while keeping the moment in time the same, by moving the
        # Normalize corrects the utc-offset to match the timezone
        # optional time at which this job runs
        # optional time of final run
        # optional time zone of the self.at_time field. Only relevant when at_time is not None
        # Target day already happened this week, move to next week
        # the normalization will change the utc-offset to where it is valid.
        # The utc-offset and time-component has changed
        # This happens when we cross into or out of daylight saving time.
        # time component opposite of the utc-change.
        # time units, e.g. 'minutes', 'hours', ...
        # To keep the api consistent with older versions, we have to set the 'next_run' to a naive timestamp in the local timezone.
        # Weekday to run the job at. Only relevant when unit is 'weeks'.
        # When we set the time elements, we might end up in a different UTC-offset than the current offset.
        )
        :param delay_seconds: A delay added between every executed job
        :param interval: A quantity of a certain time unit
        :param job: The job to be unscheduled
        :param job_func: The function to be scheduled
        :param latest: Maximum interval between randomized job runs
        :param tag: An identifier used to identify a subset of
        :param tag: Filter the next run for the given tag parameter
        :param tags: A unique list of ``Hashable`` tags.
        :param time_str: A string in one of the following formats:
        :param tz: The timezone that this timestamp refers to. Can be
        :param until_time: A moment in the future representing the latest time a job can
        :return: ``True`` if the job should be run now.
        :return: A :class:`~datetime.datetime` object
        :return: An unconfigured :class:`Job <Job>`
        :return: Number of seconds until
        :return: The invoked job instance
        :return: The return value returned by the `job_func`, or CancelJob if the job's
        A delay of `delay` seconds is added between each job. This helps
        Any additional arguments are passed on to job_func when
        assert self.next_run is not None, "must run _schedule_next_run before"
        between but only once.
        both ends. For example, `every(A).to(B).seconds` executes
        case CancelJob takes priority over any other returned value.
        Compute the instant when this job should run next.
        Datetime when the next job should run.
        days_ahead += 7
        def format_time(t):
        def is_repr(j):
        Delete a scheduled job.
        Deletes scheduled jobs marked with the given tag, or all jobs
        distribute system load generated by the jobs more evenly
        does not run missed jobs*. For example, if you've registered a job
        elif isinstance(until_time, datetime.time):
        elif isinstance(until_time, datetime.timedelta):
        elif isinstance(until_time, str):
        elif len(time_values) == 2 and self.unit == "hours" and len(time_values[0]):
        elif len(time_values) == 2 and self.unit == "minutes":
        elif self.unit == "hours":
        elif self.unit == "minutes":
        else:
        except ValueError:
        for f in formats:
        for job in self.jobs[:]:
        for job in sorted(runnable_jobs):
        functools.update_wrapper(self.job_func, job_func)
        Gets scheduled jobs marked with the given tag, or all jobs
        Given a datetime, corrects any mistakes in the utc offset.
        hour = int(hour)
        hour: Union[str, int]
        if hasattr(self.job_func, "__name__"):
        if interval != 1:
        if isinstance(ret, CancelJob) or ret is CancelJob:
        if isinstance(until_time, datetime.datetime):
        if len(time_values) == 3:
        if not all(isinstance(tag, Hashable) for tag in tags):
        if not fixate_time:
        if not isinstance(time_str, str):
        if not jobs_filtered:
        if not self.jobs:
        if not self.next_run:
        if offset_before_normalize == offset_after_normalize:
        if re_normalized_offset != offset_after_normalize:
        if self._is_overdue(datetime.datetime.now()):
        if self._is_overdue(self.next_run):
        if self.at_time is None:
        if self.at_time is not None:
        if self.at_time_zone is None:
        if self.at_time_zone is not None:
        if self.cancel_after < datetime.datetime.now():
        if self.interval != 1:
        if self.job_func is not None:
        if self.latest is not None:
        if self.scheduler is None:
        if self.start_day is not None:
        if self.unit == "days" or self.start_day is not None:
        if self.unit == "days" or self.start_day:
        if self.unit == "hours":
        if self.unit == "minutes":
        if self.unit in ["days", "hours"] or self.start_day is not None:
        if self.unit not in ("days", "hours", "minutes") and not self.start_day:
        if self.unit not in ("seconds", "minutes", "hours", "days", "weeks"):
        if tag is None:
        if tag is omitted.
        if the current time is after until_time. This latter case can happen when the
        If the job's deadline is reached (configured using .until()), the job is not
        if tz is not None:
        If until_time is a moment in the past, ScheduleValueError is thrown.
        in one hour increments then your job won't be run 60 times in
        job = Job(interval, self)
        job runs.
        job.do(decorated_function, *args, **kwargs)
        jobs_filtered = self.get_jobs(tag)
        keeping the time-component at the same hour/minute/second.
        kwargs = {"second": self.at_time.second, "microsecond": 0}
        logger.debug(
        logger.debug("Running job %s", self)
        minute = int(minute)
        minute: Union[str, int]
        moment = moment.replace(**kwargs)  # type: ignore
        moment -= offset_diff
        moment = self._correct_utc_offset(moment, fixate_time=True)
        moment = self.at_time_zone.normalize(moment)
        next run is after the until_time. The job is also canceled right before it runs,
        next_run = now
        next_run = self._correct_utc_offset(
        now = datetime.datetime.now(self.at_time_zone)
        offset_after_normalize = moment.utcoffset()
        offset_before_normalize = moment.utcoffset()
        offset_diff = offset_after_normalize - offset_before_normalize
        over time.
        period = datetime.timedelta(**{self.unit: interval})
        PeriodicJobs are sortable based on the scheduled time they
        Please note that it is *intended behavior that run_pending()
        raise ScheduleValueError(
        re_normalized_offset = self.at_time_zone.normalize(moment).utcoffset()
        ret = job.run()
        ret = self.job_func()
        return ("Job(interval={}, unit={}, do={}, args={}, kwargs={})").format(
        return (self.next_run - datetime.datetime.now()).total_seconds()
        return datetime.datetime.now() >= self.next_run
        return decorated_function
        return job
        return min(jobs_filtered).next_run
        return moment
        return None
        return ret
        return self
        return self.cancel_after is not None and when > self.cancel_after
        return self.days
        return self.hours
        return self.minutes
        return self.next_run < other.next_run
        return self.seconds
        return self.weeks
        Run all jobs regardless if they are scheduled to run or not.
        Run all jobs that are scheduled to run.
        run and CancelJob is returned immediately. If the next scheduled run exceeds
        run next.
        Run the job and immediately reschedule it.
        runnable_jobs = (job for job in self.jobs if job.should_run)
        Schedule a new periodic job.
        Schedule job to run until the specified moment.
        Schedule the job to run at an irregular (randomized) interval.
        second = int(second)
        second: Union[str, int]
        self,
        self, datetime_str: str, formats: List[str]
        self, moment: datetime.datetime, fixate_time: bool
        self, tag: Optional[Hashable] = None
        self._schedule_next_run()
        self.at_time = datetime.time(hour, minute, second)
        self.at_time: Optional[datetime.time] = None
        self.at_time_zone = None
        self.cancel_after: Optional[datetime.datetime] = None
        self.interval: int = interval  # pause interval * unit between runs
        self.job_func = functools.partial(job_func, *args, **kwargs)
        self.job_func: Optional[functools.partial] = None  # the job job_func to run
        self.jobs: List[Job] = []
        self.last_run = datetime.datetime.now()
        self.last_run: Optional[datetime.datetime] = None
        self.latest = latest
        self.latest: Optional[int] = None  # upper limit to the interval
        self.next_run = next_run
        self.next_run: Optional[datetime.datetime] = None
        self.scheduler.jobs.append(self)
        self.scheduler: Optional[Scheduler] = scheduler  # scheduler to register with
        self.start_day = "friday"
        self.start_day = "monday"
        self.start_day = "saturday"
        self.start_day = "sunday"
        self.start_day = "thursday"
        self.start_day = "tuesday"
        self.start_day = "wednesday"
        self.start_day: Optional[str] = None
        self.tags.update(tags)
        self.tags: Set[Hashable] = set()  # unique set of tags for the job
        self.unit = "days"
        self.unit = "hours"
        self.unit = "minutes"
        self.unit = "seconds"
        self.unit = "weeks"
        self.unit: Optional[str] = None
        Specifies the job_func that should be called every time the
        Specify a particular time that the job should be run at.
        Tags must be hashable. Duplicate tags are discarded.
        Tags the job with one or more unique identifiers.
        Takes a datetime and moves the time-component to the job's at_time.
        that should run every minute and you only call run_pending()
        the job function every N seconds such that A <= N <= B.
        The job is canceled whenever the next run is calculated and it turns out the
        the job runs.
        the job was scheduled to run before until_time, but runs after until_time.
        the job's deadline, CancelJob is returned after the execution. In this latter
        The job's interval will randomly vary from the value given
        This is similar to pytz' normalize, but adds the ability to attempt
        time_values = time_str.split(":")
        timestats = "(last run: {}, next run: {})".format(
        to  `every` to `latest`. The range defined is inclusive on
        try:
        until_time: Union[datetime.datetime, datetime.timedelta, datetime.time, str],
        while next_run <= now:
    - A simple to use API for scheduling jobs.
    - Excellent test coverage.
    - Tested on Python 3.7, 3.8, 3.9, 3.10, 3.11 and 3.12
    - Very lightweight and no external dependencies.
    """
    """An improper interval was used"""
    """Base schedule exception"""
    """Base schedule value error"""
    """Calls :meth:`cancel_job <Scheduler.cancel_job>` on the
    """Calls :meth:`clear <Scheduler.clear>` on the
    """Calls :meth:`every <Scheduler.every>` on the
    """Calls :meth:`get_jobs <Scheduler.get_jobs>` on the
    """Calls :meth:`idle_seconds <Scheduler.idle_seconds>` on the
    """Calls :meth:`next_run <Scheduler.next_run>` on the
    """Calls :meth:`run_all <Scheduler.run_all>` on the
    """Calls :meth:`run_pending <Scheduler.run_pending>` on the
    )
    ) -> datetime.datetime:
    ) -> Optional[datetime.datetime]:
    ):
    * a :meth:`time unit <Job.second>`
    * a quantity of `time units` defined by `interval`
    :data:`default scheduler instance <default_scheduler>`.
    :param interval: A quantity of a certain time unit
    :param job: a :class:`Jobs <Job>`
    :param scheduler: The :class:`Scheduler <Scheduler>` instance that
    @property
    >>>     print("I'm working on:", message)
    >>>     schedule.run_pending()
    >>>     time.sleep(1)
    >>> def job(message='stuff'):
    >>> import schedule
    >>> import time
    >>> schedule.every().day.at("10:30").do(job)
    >>> schedule.every().hour.do(job, message='things')
    >>> schedule.every(10).minutes.do(job)
    >>> schedule.every(5).to(10).days.do(job)
    >>> while True:
    A job is usually created and returned by :meth:`Scheduler.every`
    A periodic job as used by :class:`Scheduler`.
    Any additional arguments are passed on to the decorated function
    Can be returned from a job to unschedule itself.
    days_ahead = weekday_index - moment.weekday()
    Decorator to schedule a new periodic job.
    def __init__(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def __init__(self, interval: int, scheduler: Optional[Scheduler] = None):
    def __lt__(self, other) -> bool:
    def __repr__(self):
    def __str__(self) -> str:
    def _correct_utc_offset(
    def _decode_datetimestr(
    def _is_overdue(self, when: datetime.datetime):
    def _move_to_at_time(self, moment: datetime.datetime) -> datetime.datetime:
    def _run_job(self, job: "Job") -> None:
    def _schedule_decorator(decorated_function):
    def _schedule_next_run(self) -> None:
    def at(self, time_str: str, tz: Optional[str] = None):
    def cancel_job(self, job: "Job") -> None:
    def clear(self, tag: Optional[Hashable] = None) -> None:
    def day(self):
    def days(self):
    def do(self, job_func: Callable, *args, **kwargs):
    def every(self, interval: int = 1) -> "Job":
    def friday(self):
    def get_jobs(self, tag: Optional[Hashable] = None) -> List["Job"]:
    def get_next_run(
    def hour(self):
    def hours(self):
    def idle_seconds(self) -> Optional[float]:
    def minute(self):
    def minutes(self):
    def monday(self):
    def run(self):
    def run_all(self, delay_seconds: int = 0) -> None:
    def run_pending(self) -> None:
    def saturday(self):
    def second(self):
    def seconds(self):
    def should_run(self) -> bool:
    def sunday(self):
    def tag(self, *tags: Hashable):
    def thursday(self):
    def to(self, latest: int):
    def tuesday(self):
    def until(
    def wednesday(self):
    def week(self):
    def weeks(self):
    default_scheduler.cancel_job(job)
    default_scheduler.clear(tag)
    default_scheduler.run_all(delay_seconds=delay_seconds)
    default_scheduler.run_pending()
    Every job runs at a given fixed time interval that is defined by:
    factories to create jobs, keep record of scheduled jobs and
    handle their execution.
    if day not in weekdays:
    if days_ahead < 0:
    method, which also defines its `interval`.
    Move the given timestamp to the nearest given weekday. May be this week
    moved.
    next_run = property(get_next_run)
    Objects instantiated by the :class:`Scheduler <Scheduler>` are
    or next week. If the timestamp is already at the given weekday, it is not
    return _schedule_decorator
    return default_scheduler.every(interval)
    return default_scheduler.get_jobs(tag)
    return default_scheduler.get_next_run(tag)
    return default_scheduler.idle_seconds
    return moment + datetime.timedelta(days=days_ahead)
    return weekdays.index(day)
    weekday_index = _weekday_index(weekday)
    weekdays = (
    when the job runs.
"""
"clockwork" Ruby module [2][3].
# create a Scheduler instance:
# The following methods are shortcuts for not having to
#: Default :class:`Jobs <Job>` list
#: Default :class:`Scheduler <Scheduler>` object
[1] https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/
[2] https://github.com/Rykian/clockwork
[3] https://adam.herokuapp.com/past/2010/6/30/replace_cron_with_clockwork/
An in-process scheduler for periodic jobs that uses the builder pattern
callable) periodically at pre-determined intervals using a simple,
class CancelJob:
class IntervalError:
class Job:
class ScheduleError:
class Scheduler:
class ScheduleValueError:
def _move_to_next_weekday(moment: datetime.datetime, weekday: str):
def _weekday_index(day: str) -> int:
def cancel_job(job: Job) -> None:
def clear(tag: Optional[Hashable] = None) -> None:
def every(interval: int = 1) -> Job:
def get_jobs(tag: Optional[Hashable] = None) -> List[Job]:
def idle_seconds() -> Optional[float]:
def next_run(tag: Optional[Hashable] = None) -> Optional[datetime.datetime]:
def repeat(job, *args, **kwargs):
def run_all(delay_seconds: int = 0) -> None:
def run_pending() -> None:
default_scheduler = Scheduler()
Features:
for configuration. Schedule lets you run Python functions (or any other
from collections.abc import Hashable
from typing import Set, List, Optional, Callable, Union
github.com/dbader/schedule
human-friendly syntax.
import datetime
import functools
import logging
import random
import re
import time
Inspired by Addam Wiggins' article "Rethinking Cron" [1] and the
jobs = default_scheduler.jobs  # todo: should this be a copy, e.g. jobs()?
logger = logging.getLogger("schedule")
Python job scheduling for humans.
Usage:
