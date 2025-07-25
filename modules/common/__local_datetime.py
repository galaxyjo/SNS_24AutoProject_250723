
                                    offset = -offset
                                    sign = "-"
                                    y.s = z.s by #2
                                # strftime is going to have at this: escape %
                                assert not m % timedelta(minutes=1), "whole minute"
                                h, m = divmod(offset, timedelta(hours=1))
                                if offset.days < 0:
                                m //= timedelta(minutes=1)
                                sign = "+"
                                zreplace = "%c%02d%02d" % (sign, h, m)
                                Zreplace = s.replace("%", "%%")
                            if offset is not None:
                            if s is not None:
                            offset = object.utcoffset()
                            s = object.tzname()
                        -1,
                        freplace = "%06d" % getattr(object, "microsecond", 0)
                        if hasattr(object, "tzname"):
                        if hasattr(object, "utcoffset"):
                        self.day,
                        self.hour,
                        self.minute,
                        self.month,
                        self.second,
                        self.year,
                        zreplace = ""
                        Zreplace = ""
                    "fromutc(): dt.dst gave inconsistent " "results; cannot convert"
                    (
                    )
                    assert "%" not in zreplace
                    if freplace is None:
                    if Zreplace is None:
                    if zreplace is None:
                    newformat.append(freplace)
                    newformat.append(Zreplace)
                    newformat.append(zreplace)
                    other._day,
                    other._hour,
                    other._microsecond,
                    other._minute,
                    other._month,
                    other._second,
                    other._year,
                    push("%")
                    push(ch)
                    self._day,
                    self._hour,
                    self._microsecond,
                    self._minute,
                    self._month,
                    self._second,
                    self._year,
                    tz = timezone(delta)
                    tz = timezone(delta, _time.tzname[dst])
                " strictly between -timedelta(hours=24) and"
                " timedelta(hours=24)."
                "datetime." + self.__class__.__name__,
                "datetime." + self.__class__.__name__, self._offset
                "offset must be a timedelta"
                "offset must be a timedelta" " representing a whole number of minutes"
                # by tm_isdst.  If the values match, use the zone name
                # Compute UTC offset and compare with the value implied
                # Extract TZ data if available
                # implied by tm_isdst.
                (
                (other._hour, other._minute, other._second, other._microsecond),
                (self._hour, self._minute, self._second, self._microsecond),
                )
                ),
                _time.mktime(
                + self.microsecond / 1e6
                ch = format[i]
                date.fromordinal(delta.days),
                delta = local - datetime(*_time.gmtime(ts)[:6])
                dst = _time.daylight and localtm.tm_isdst > 0
                elif ch == "Z":
                elif ch == "z":
                else:
                gmtoff = -(_time.altzone if dst else _time.timezone)
                gmtoff = localtm.tm_gmtoff
                i += 1
                if ch == "f":
                if delta == timedelta(seconds=gmtoff):
                name = name.decode()
                off = -off
                push("%")
                raise TypeError("cannot compare naive and aware datetimes")
                raise TypeError("cannot compare naive and aware times")
                raise TypeError("name must be a string")
                raise ValueError(
                raise ValueError("astimezone() requires an aware datetime")
                raise ValueError("fromutc: dt.tzinfo " "is not self")
                return 2  # arbitrary non-zero value
                return cls.utc
                return date.fromordinal(o)
                return n, abs(n) != 1 and "s" or ""
                return self + -other
                return self._name_from_offset(self._offset)
                self._day,
                self._days - other._days,
                self._days * other, self._seconds * other, self._microseconds * other
                self._days + other._days,
                self._days,
                self._hour,
                self._microseconds - other._microseconds,
                self._microseconds + other._microseconds,
                self._microseconds,
                self._minute,
                self._month,
                self._second,
                self._seconds - other._seconds,
                self._seconds + other._seconds,
                self._seconds,
                sign = "-"
                sign = "+"
                time(hour, minute, second, delta.microseconds, tzinfo=self._tzinfo),
                tz = timezone(timedelta(seconds=gmtoff), zone)
                us1,
                us2,
                us3,
                week = 0
                year += 1
                yhi,
                ylo,
                zone = localtm.tm_zone
            - z.n + z.n - z.o + z'.o =              cancel z.n
            - z.o + z'.o =                      #1 twice
            " -timedelta(hours=24) and timedelta(hours=24)" % (name, offset)
            "%s()=%s, must be must be strictly between"
            "datetime." + self.__class__.__name__,
            "of minutes, got %s" % (name, offset)
            "or timedelta, not '%s'" % (name, type(offset))
            "tzinfo.%s() must return a whole number "
            "tzinfo.%s() must return None "
            "tzinfo.tzname() must return None or string, " "not '%s'" % type(name)
            # for CPython compatibility, we cannot use
            # For Python-Future:
            # our __class__ here, but need a real timedelta
            # Pickle support
            ###
            (myhhmm, self._second, self._microsecond),
            (othhmm, other._second, other._microsecond),
            )
            [
            ]
            _cmperror(self, other)
            _DAYNAMES[weekday],
            _MONTHNAMES[self._month],
            a, b = other.as_integer_ratio()
            and 1 <= year[2] <= 12
            and len(year) == 4
            and month is None
            args = ()
            args = getinitargs()
            assert 0 <= hh < 24
            assert abs(s) <= 3 * 24 * 3600
            assert abs(secondsfrac) <= 2.0
            assert days == int(days)
            assert daysecondswhole == int(daysecondswhole)  # can't overflow
            assert isinstance(s, int)
            assert microseconds == int(microseconds)
            assert not mm % timedelta(minutes=1), "whole minute"
            assert s[-1:] == ")"
            assert seconds == int(seconds)
            base_compare = myoff == otoff
            base_compare = True
            d += days
            d += int(days)
            d = days
            d = int(days)
            date.day,
            date.month,
            date.year,
            day = self._day
            day = self.day
            dayfrac, days = _math.modf(days)
            days, seconds = divmod(seconds, 24 * 3600)
            days, seconds = divmod(seconds, 24.0 * 3600.0)
            days1 - days2, secs1 - secs2, self._microsecond - other._microsecond
            days1 = self.toordinal()
            days2 = other.toordinal()
            daysecondsfrac = 0.0
            daysecondsfrac, daysecondswhole = _math.modf(dayfrac * (24.0 * 3600.0))
            def plural(n):
            del L[-1]
            delta = -delta
            dst = 0
            dst = 1
            dst = -1
            dt += delta
            dtdst = dt.dst()
            else:
            except AttributeError:
            hh, mm = divmod(off, timedelta(hours=1))
            hour = self.hour
            hours=self._hour,
            if 0 < o <= _MAXORDINAL:
            if allow_mixed:
            if dt.tzinfo is not self:
            if dtdst is None:
            if i < n:
            if isinstance(other, timedelta):
            if not offset:
            if off.days < 0:
            if PY2 and isinstance(name, native_str):
            if self._name is None:
            if self.tzinfo is None:
            if today >= _isoweek1monday(year + 1):
            isinstance(year, bytes)
            local = datetime(*localtm[:6])
            localtm = _time.localtime(ts)
            microsecond = self.microsecond
            microseconds += usdouble
            microseconds = float(microseconds)
            microseconds = round(microseconds, 0)
            microseconds=self._microsecond,
            minute = self.minute
            minutes=self._minute,
            mm //= timedelta(minutes=1)
            month = self._month
            month = self.month
            myoff = self.utcoffset()
            name = None
            o = self.toordinal() + other.days
            off = "%s%02d%s%02d" % (sign, hh, sep, mm)
            otoff = other.utcoffset()
            push(ch)
            q, r = divmod(self._to_microseconds(), other._to_microseconds())
            r = self._to_microseconds() % other._to_microseconds()
            raise OverflowError("result out of range")
            raise OverflowError("timedelta # of days is too large: %d" % d)
            raise TypeError("an integer is required")
            raise TypeError("bad tzinfo state arg %r" % tzinfo)
            raise TypeError("cannot mix naive and timezone-aware time")
            raise TypeError("date argument must be a date instance")
            raise TypeError("fromutc() requires a datetime argument")
            raise TypeError("not enough arguments")
            raise TypeError("offset must be a timedelta")
            raise TypeError("time argument must be a time instance")
            raise TypeError("tz argument must be an instance of tzinfo")
            raise ValueError(
            raise ValueError("astimezone() requires an aware datetime")
            raise ValueError("dt.tzinfo is not self")
            raise ValueError("fromutc() requires a non-None dst() result")
            raise ValueError("fromutc() requires a non-None utcoffset() " "result")
            result = tz.fromutc(result)
            return "%s(%d, %d)" % (
            return "%s(%d, %d, %d)" % (
            return "{}({!r})".format(
            return "datetime.timezone.utc"
            return (
            return (basestate, self._tzinfo)
            return (basestate,)
            return (self - _EPOCH).total_seconds()
            return (self.__class__, args)
            return (self.__class__, args, state)
            return (self._offset,)
            return _cmp(
            return -1
            return base
            return datetime.combine(
            return dt + self._offset
            return False
            return hash(self._getstate()[0])
            return hash(time(h, m, self.second, self.microsecond))
            return None
            return NotImplemented
            return q, timedelta(0, 0, r)
            return self
            return -self
            return self * a / b
            return -self + other
            return self + timedelta(-other.days)
            return self._cmp(other) != 0
            return self._cmp(other) < 0
            return self._cmp(other) <= 0
            return self._cmp(other) == 0
            return self._cmp(other) > 0
            return self._cmp(other) >= 0
            return self._cmp(other, allow_mixed=True) != 0
            return self._cmp(other, allow_mixed=True) == 0
            return self._name
            return self._offset
            return self.strftime(fmt)
            return timedelta(
            return timedelta(0, 0, b * usec / a)
            return timedelta(0, 0, r)
            return timedelta(0, 0, usec / other)
            return timedelta(0, 0, usec // other)
            return timedelta(days1 - days2)
            return True
            return usec / other._to_microseconds()
            return usec // other._to_microseconds()
            s += "%s%02d:%02d" % (sign, hh, mm)
            s += int(seconds)  # can't overflow
            s += tz
            s = ""
            s = ", %d" % self._second
            s = ", %d, %d" % (self._second, self._microsecond)
            s = ("%d day%s, " % plural(self._days)) + s
            s = int(daysecondswhole)
            s = s + ".%06d" % self._microseconds
            s = s[:-1] + ", tzinfo=%r" % self._tzinfo + ")"
            s,
            second = self.second
            seconds = int(seconds)
            seconds, microseconds = divmod(microseconds, 1000000)
            seconds, microseconds = divmod(microseconds, 1e6)
            seconds=self._second,
            secondsfrac += daysecondsfrac
            secondsfrac = daysecondsfrac
            secondsfrac, seconds = _math.modf(seconds)
            self = date.__new__(cls, year[:4])
            self = object.__new__(cls)
            self -= offset
            self.__setstate(hour, minute or None)
            self.__setstate(year)
            self.__setstate(year, month)
            self._day,
            self._day,  # These are never zero
            self._hour,
            self._microsecond,
            self._minute,
            self._month,
            self._name,
            self._offset,
            self._second,
            self._tzinfo = tzinfo
            self._year,
            self.toordinal(),
            self.year, self.month, self.day, self.hour, self.minute, self.second, dst
            sep,
            sign = "-"
            sign = "+"
            state = getattr(self, "__dict__", None) or None
            state = getstate()
            t += 1
            time.hour,
            time.microsecond,
            time.minute,
            time.second,
            time.tzinfo,
            timedelta(hours=self.hour, minutes=self.minute) - tzoff, timedelta(hours=1)
            try:
            ts = (self - _EPOCH) // timedelta(seconds=1)
            tzinfo = self.tzinfo
            us = 0
            us1,
            us2,
            us3,
            week, day = divmod(today - week1monday, 7)
            week1monday = _isoweek1monday(year)
            x.n  - (z.n + diff - z'.o) =    replacing diff via [6]
            x.n - (z.n + x.n - (z.n - z.o) - z'.o) =
            x.n - z.n - x.n + z.n - z.o + z'.o =    cancel x.n
            year -= 1
            year = self._year
            year = self.year
            yhi,
            ylo,
            z'.d - z.d
            -z.s - z.d + z'.s + z'.d =          z and z' have same tzinfo
          return None
        - http://www.cl.cam.ac.uk/~mgk25/iso-time.html
        - http://www.w3.org/TR/NOTE-datetime
        """
        """Construct a date from a proleptic Gregorian ordinal.
        """Construct a datetime from a POSIX timestamp (like time.time()).
        """Constructor.
        """Convert to formal string, for repr().
        """Convert to formal string, for repr()."""
        """datetime -> DST offset in minutes east of UTC.
        """day (1-31)"""
        """days"""
        """Format using strftime().  The date part of the timestamp passed
        """Hash."""
        """hour (0-23)"""
        """microsecond (0-999999)"""
        """microseconds"""
        """minute (0-59)"""
        """month (1-12)"""
        """pickle support"""
        """Return 0 if DST is not in effect, or the DST offset (in minutes
        """Return a 3-tuple containing ISO year, week number, and weekday.
        """Return a new date with new values for the specified fields."""
        """Return a new datetime with new values for the specified fields."""
        """Return a new time with new values for the specified fields."""
        """Return formatted timezone offset (+xx:xx) or None."""
        """Return proleptic Gregorian ordinal for the year, month and day.
        """Return the date formatted according to ISO.
        """Return the time formatted according to ISO.
        """Return the timezone name.
        """Return the timezone offset in minutes east of UTC (negative west of
        """second (0-59)"""
        """seconds"""
        """Subtract two dates, or a date and a timedelta."""
        """timezone info object"""
        """Total seconds in the duration."""
        """year (1-9999)"""
        "_hour",
        "_microsecond",
        "_minute",
        "_second",
        "_tzinfo",
        "-5:00", "EDT", "US/Eastern", "America/New York" are all valid replies.
        "Add a date to a timedelta."
        "Add a datetime and a timedelta."
        "can't compare '{}' to '{}'".format(type(x).__name__, type(y).__name__)
        "Construct a date from a POSIX timestamp (like time.time())."
        "Construct a date from time.time()."
        "Construct a datetime from a given date and a given time."
        "Construct a datetime from time.time() and optional time zone info."
        "Construct a UTC datetime from a POSIX timestamp (like time.time())."
        "Construct a UTC datetime from time.time()."
        "Convert to string, for str()."
        "datetime -> minutes east of UTC (negative for west of UTC)"
        "datetime -> string name of time zone."
        "datetime in UTC -> datetime in local time."
        "datetime.timezone(datetime.timedelta(-1, 68400), 'EST')"
        "Format using strftime()."
        "Hash."
        "Return ctime() style string."
        "Return day of the week, where Monday == 0 ... Sunday == 6."
        "Return day of the week, where Monday == 1 ... Sunday == 7."
        "Return local time tuple compatible with time.localtime()."
        "Return POSIX timestamp as float"
        "Return the date part."
        "Return the time part, with same tzinfo."
        "Return the time part, with tzinfo None."
        "Return UTC time tuple compatible with time.gmtime()."
        "string, format -> new datetime parsed from a string (like time.strptime())."
        "Subtract two datetimes, or a datetime and a timedelta."
        # 1-Jan-0001 is a Monday
        # and error-prone, due to ubiquitous overflow possibilities, and that
        # by the constructor.
        # C double doesn't have enough bits of precision to represent
        # can raise a bogus exception.
        # Convert from UTC to tz's local time.
        # Convert self to UTC, and attach the new time zone object.
        # days isn't referenced again before redefinition
        # daysecondsfrac isn't referenced again
        # Doing this efficiently and accurately in C is going to be difficult
        # explanation of this algorithm.
        # explicit where go-fast assumptions can be relied on, in order to
        # Final values, all integer.
        # for CPython compatibility, we cannot use
        # full second, us can be rounded up to 1000000.  In this case,
        # Get rid of all fractions, and normalize s and us.
        # guide the C implementation; it's way more convoluted than speed-
        # If timestamp is less than one microsecond smaller than a
        # ignoring auto-overflow-to-long idiomatic Python could be.
        # Internally, week and day have origin 0
        # Just a little bit of carrying possible for microseconds and seconds.
        # microseconds over 10K years faithfully.  The code here tries to make
        # Normalize everything to days, seconds, microseconds.
        # our __class__ here, but need a real timedelta
        # roll over to seconds, otherwise, ValueError is raised
        # s and us fit in 32-bit signed ints; d isn't bounded.
        # seconds isn't referenced again before redefinition
        # secondsfrac isn't referenced again
        # See the long comment block at the end of this file for an
        # Take a deep breath <wink>.
        # The year must be >= 1000 else Python's strftime implementation
        # XXX Check that all inputs are ints or floats.
        # XXX What follows could be done more efficiently...
        (
        (self._hour, self._minute, self._second, us1, us2, us3) = string
        )
        ) + _format_time(self._hour, self._minute, self._second, self._microsecond)
        ) = string
        ):  # Month is sane
        ]
        _build_struct_time,
        _call_tzinfo_method,
        _check_date_fields(year, month, day)
        _check_date_fields,
        _check_time_fields(hour, minute, second, microsecond)
        _check_time_fields,
        _check_tzinfo_arg(tz)
        _check_tzinfo_arg(tzinfo)
        _check_tzinfo_arg,
        _check_tzname(name)
        _check_tzname,
        _check_utc_offset("dst", offset)
        _check_utc_offset("utcoffset", offset)
        _check_utc_offset,
        _cmp,
        _cmperror,
        _date_class,
        _DAYNAMES,
        _DAYS_BEFORE_MONTH,
        _days_before_month,
        _days_before_year,
        _DAYS_IN_MONTH,
        _days_in_month,
        _DI100Y,
        _DI400Y,
        _DI4Y,
        _format_time,
        _is_leap,
        _isoweek1monday,
        _math,
        _MAXORDINAL,
        _MONTHNAMES,
        _ord2ymd,
        _time,
        _time_class,
        _tzinfo_class,
        _wrap_strftime,
        _ymd2ord,
        >>> dt = datetime(2010, 1, 1)
        >>> dt = datetime(2010, 1, 1, tzinfo=timezone.utc)
        >>> repr(dt)
        >>> repr(tz)
        >>> tz = timezone(timedelta(hours=-5), 'EST')
        >>> tz = timezone.utc
        A timezone info object may be passed in as well.
        Arguments:
        assert abs(daysecondsfrac) <= 1.0
        assert abs(microseconds) < 3.1e6
        assert abs(s) <= 2 * 24 * 3600
        assert abs(s) <= 24 * 3600
        assert abs(s) <= 3 * 24 * 3600
        assert abs(secondsfrac) <= 2.0
        assert abs(usdouble) < 2.1e6  # exact value not critical
        assert int(microseconds) == microseconds
        assert isinstance(d, int)
        assert isinstance(daysecondsfrac, float)
        assert isinstance(microseconds, float)
        assert isinstance(other, date)
        assert isinstance(other, datetime)
        assert isinstance(other, time)
        assert isinstance(other, timedelta)
        assert isinstance(s, int)
        assert isinstance(s, int) and 0 <= s < 24 * 3600
        assert isinstance(seconds, int)
        assert isinstance(secondsfrac, float)
        assert isinstance(us, int) and 0 <= us < 1000000
        assert n == 0
        assert not m % timedelta(minutes=1), "whole minute"
        base = timedelta(
        basestate = bytes(
        basestate = bytes([self._hour, self._minute, self._second, us1, us2, us3])
        ch = format[i]
        cls,
        containing the year's first Thursday; everything else derives
        contribute to the result.
        converter = _time.localtime if tz is None else _time.gmtime
        d += days
        d = s = us = 0
        'datetime.datetime(2010, 1, 1, 0, 0)'
        'datetime.datetime(2010, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)'
        'datetime.timezone.utc'
        day=None,
        days += weeks * 7
        days = _ymd2ord(self.year, self.month, self.day)
        days, s = divmod(s, 24 * 3600)
        days, seconds = divmod(seconds, 24 * 3600)
        days=0,
        days1 = self.toordinal()
        days2 = other.toordinal()
        delta += other
        delta = dtoff - dtdst
        delta = timedelta(
        diff = self - other  # this will take offsets into account
        dst = self.dst()
        dtdst = dt.dst()
        dtoff = dt.utcoffset()
        eastward) if DST is in effect.
        elif dst:
        elif not isinstance(name, str):
        elif not isinstance(other, date):
        elif not isinstance(tz, tzinfo):
        elif self._second != 0:
        elif week >= 52:
        else:
        from that.
        getinitargs = getattr(self, "__getinitargs__", None)
        getstate = getattr(self, "__getstate__", None)
        h, m = divmod(
        hh, mm = divmod(mm, 60)
        hh, mm, ss = self.hour, self.minute, self.second
        hour, minute (required)
        hour, rem = divmod(delta.seconds, 3600)
        hour=0,
        hour=None,
        hours, rest = divmod(delta, timedelta(hours=1))
        hours=0,
        http://www.phys.uu.nl/~vgent/calendar/isocalendar.htm
        i += 1
        if (
        if 0 < delta.days <= _MAXORDINAL:
        if 0 <= h < 24:
        if abs(d) > 999999999:
        if base_compare:
        if ch == "%":
        if day is None:
        if delta < timedelta(0):
        if delta:
        if diff.days < 0:
        if dst is None:
        if dt.tzinfo is not self:
        if dtdst is None:
        if dtoff is None:
        if getinitargs:
        if getstate:
        if hour is None:
        if isinstance(days, float):
        if isinstance(dt, datetime) or dt is None:
        if isinstance(dt, datetime):
        if isinstance(hour, bytes) and len(hour) == 6:
        if isinstance(microseconds, float):
        if isinstance(other, date):
        if isinstance(other, datetime):
        if isinstance(other, float):
        if isinstance(other, int):
        if isinstance(other, time):
        if isinstance(other, timedelta):
        if isinstance(seconds, float):
        if isinstance(year, bytes) and len(year) == 10:
        if L[-1] == 0:
        if len(fmt) != 0:
        if len(string) != 4 or not (1 <= string[2] <= 12):
        if len(string) != 6 or string[0] >= 24:
        if microsecond is None:
        if minute is None:
        if month is None:
        if myoff == otoff:
        if myoff is None or otoff is None:
        if myoffset is None:
        if mytz is None:
        if mytz is ottz:
        if name is cls._Omitted:
        if not cls._minoffset <= offset <= cls._maxoffset:
        if not isinstance(date, _date_class):
        if not isinstance(dt, datetime):
        if not isinstance(offset, timedelta):
        if not isinstance(other, (int, float, timedelta)):
        if not isinstance(other, (int, timedelta)):
        if not isinstance(other, datetime):
        if not isinstance(other, timedelta):
        if not isinstance(time, _time_class):
        if not tzoff:  # zero or None
        if off is not None:
        if offset.microseconds != 0 or offset.seconds % 60 != 0:
        if offset:
        if second is None:
        if self is self.utc:
        if self._days < 0:
        if self._days:
        if self._microsecond != 0:
        if self._microseconds:
        if self._name is None:
        if self._seconds:
        if self._tzinfo is None:
        if self._tzinfo is not None:
        if self._tzinfo is other._tzinfo:
        if self.second or self.microsecond:
        If self.tzinfo is not None, the UTC offset is also attached, giving
        if state is None:
        if type(other) != timezone:
        if tz is mytz:
        if tz is None:
        if tz is not None:
        if tz:
        if tzinfo is None or isinstance(tzinfo, _tzinfo_class):
        if tzinfo is True:
        if tzoff is None:
        if us == 1000000:
        if week < 0:
        if year is None:
        import _strptime
        info.
        ISO calendar algorithm taken from
        it mean anything in particular. For example, "GMT", "UTC", "-500",
        January 1 of year 1 is day 1.  Only the year, month and day are
        January 1 of year 1 is day 1.  Only the year, month and day values
        L = [
        m //= timedelta(minutes=1)
        microsecond=0,
        microsecond=None,
        microseconds += milliseconds * 1000
        microseconds=0,
        milliseconds=0,
        minute, second = divmod(rem, 60)
        minute=0,
        minute=None,
        minutes = rest // timedelta(minutes=1)
        minutes=0,
        mm, ss = divmod(self._seconds, 60)
        month -= 1
        month=None,
        myhhmm = self._hour * 60 + self._minute - myoff // timedelta(minutes=1)
        myoff = otoff = None
        myoff = self.utcoffset()
        myoffset = self.utcoffset()
        mytz = self._tzinfo
        mytz = self.tzinfo
        name = _call_tzinfo_method(self._tzinfo, "tzname", self)
        name = self._tzinfo.tzname(None)
        need to consult dst() unless you're interested in displaying the DST
        non-zero in the result.
        Note that the name is 100% informational -- there's no requirement that
        off = self.utcoffset()
        offset = self._tzinfo.dst(None)
        offset = self._tzinfo.dst(self)
        offset = self._tzinfo.utcoffset(None)
        offset = self._tzinfo.utcoffset(self)
        offset = self.utcoffset()
        offset = self.utcoffset() or timedelta(0)
        offset.
        Optional argument sep specifies the separator between date and
        othhmm = other._hour * 60 + other._minute - otoff // timedelta(minutes=1)
        otoff = other.utcoffset()
        ottz = other._tzinfo
        preceding -= _DAYS_IN_MONTH[month] + (month == 2 and leapyear)
        raise NotImplementedError("tzinfo subclass must override dst()")
        raise NotImplementedError("tzinfo subclass must override tzname()")
        raise NotImplementedError("tzinfo subclass must override utcoffset()")
        raise OverflowError("result out of range")
        raise TypeError(
        raise TypeError("dst() argument must be a datetime instance" " or None")
        raise TypeError("fromutc() argument must be a datetime instance" " or None")
        raise TypeError("int expected")
        raise TypeError("tzinfo argument must be None or of a tzinfo subclass")
        raise TypeError("tzname() argument must be a datetime instance" " or None")
        raise TypeError("utcoffset() argument must be a datetime instance" " or None")
        raise ValueError(
        raise ValueError("day must be in 1..%d" % dim, day)
        raise ValueError("hour must be in 0..23", hour)
        raise ValueError("microsecond must be in 0..999999", microsecond)
        raise ValueError("minute must be in 0..59", minute)
        raise ValueError("month must be in 1..12", month)
        raise ValueError("second must be in 0..59", second)
        raise ValueError("year must be in %d..%d" % (MINYEAR, MAXYEAR), year)
        References:
        result += ".%06d" % us
        result = cls(y, m, d, hh, mm, ss, us, tz)
        return
        return "%04d-%02d-%02d" % (self._year, self._month, self._day)
        return "%s %s %2d %02d:%02d:%02d %04d" % (
        return "%s %s %2d 00:00:00 %04d" % (
        return "%s(%d)" % ("datetime." + self.__class__.__name__, self._days)
        return "%s(%d, %d, %d)" % (
        return "{}({!r}, {!r})".format(
        return "UTC{}{:02d}:{:02d}".format(sign, hours, minutes)
        return ((self.days * 86400 + self.seconds) * 10**6 + self.microseconds) / 10**6
        return (bytes([yhi, ylo, self._month, self._day]),)
        return (self.__class__, self._getstate())
        return (self._days * (24 * 3600) + self._seconds) * 1000000 + self._microseconds
        return (self._days, self._seconds, self._microseconds)
        return (self._offset, self._name)
        return (self.toordinal() + 6) % 7
        return (time, self._getstate())
        return _build_struct_time(
        return _build_struct_time(self._year, self._month, self._day, 0, 0, 0, -1)
        return _build_struct_time(y, m, d, hh, mm, ss, 0)
        return _cmp(
        return _cmp((y, m, d), (y2, m2, d2))
        return _cmp(self._getstate(), other._getstate())
        return _strptime._strptime_datetime(cls, date_string, format)
        return _wrap_strftime(self, fmt, self.timetuple())
        return _wrap_strftime(self, fmt, timetuple)
        return _ymd2ord(self._year, self._month, self._day)
        Return 0 if DST not in effect.  utcoffset() must include the DST
        return 29
        return base + otoff - myoff
        return cls(
        return cls(y, m, d)
        return cls(y, m, d, hh, mm, ss, us)
        return cls._create(offset, name)
        return cls.fromtimestamp(t)
        return cls.fromtimestamp(t, tz)
        return cls.utcfromtimestamp(t)
        return date(self._year, self._month, self._day)
        return date(year, month, day)
        return datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
        return diff and 1 or 0
        return dt + dtdst
        return hash((h, m, self.second, self.microsecond))
        return hash(self._getstate())
        return hash(self._offset)
        return hash(timedelta(days, seconds, self.microsecond) - tzoff)
        return name
        return None
        return NotImplemented
        return off
        return offset
        return result
        return s
        return self
        return self._day
        return self._days
        return self._days != 0 or self._seconds != 0 or self._microseconds != 0
        return self._hour
        return self._microsecond
        return self._microseconds
        return self._minute
        return self._month
        return self._offset == other._offset
        return self._second
        return self._seconds
        return self._tzinfo
        return self._year
        return self.isoformat(sep=" ")
        return self.toordinal() % 7 or 7
        return self.tzname(None)
        return str(self)
        return time(hour, minute, second, microsecond, tzinfo)
        return time(self.hour, self.minute, self.second, self.microsecond)
        return time(self.hour, self.minute, self.second, self.microsecond, self._tzinfo)
        return timedelta(hours=self.hour, minutes=self.minute) != offset
        return timedelta(-self._days, -self._seconds, -self._microseconds)
        return tz.fromutc(utc)
        return year - 1, 12, 31
        return year, week + 1, day + 1
        s += int(seconds)  # can't overflow
        s += seconds  # cant't overflow
        s = "%04d-%02d-%02d%c" % (
        s = "%d:%02d:%02d" % (hh, mm, ss)
        s = "%s(%d, %d%s)" % (
        s = ", ".join(map(str, L))
        s = "{}({})".format("datetime." + self.__class__.__name__, s)
        s = _format_time(self._hour, self._minute, self._second, self._microsecond)
        second, microsecond (default to zero)
        second=0,
        second=None,
        seconds += minutes * 60 + hours * 3600
        seconds = self.hour * 3600 + self.minute * 60 + self.second
        seconds, us = divmod(us, 1000000)
        seconds=0,
        secs1 = self._second + self._minute * 60 + self._hour * 3600
        secs2 = other._second + other._minute * 60 + other._hour * 3600
        self = date.__new__(cls, year, month, day)
        self = object.__new__(cls)
        self = tzinfo.__new__(cls)
        self,
        self, hour=None, minute=None, second=None, microsecond=None, tzinfo=True
        self._day = day
        self._days = d
        self._hour = hour
        self._microsecond = (((us1 << 8) | us2) << 8) | us3
        self._microsecond = microsecond
        self._microseconds = us
        self._minute = minute
        self._month = month
        self._name = name
        self._offset = offset
        self._second = second
        self._seconds = s
        self._tzinfo = tzinfo
        self._year = year
        self._year = yhi * 256 + ylo
        self.microsecond == 0.
        ss = min(ss, 59)  # clamp out leap seconds if the platform has them
        t = _time.time()
        t, frac = divmod(t, 1.0)
        The first ISO week of the year is the (Mon-Sun) week
        The first week is 1; Monday is 1 ... Sunday is 7.
        the UTC offset returned by utcoffset() if applicable, so there's no
        This is 'HH:MM:SS.mmmmmm+zz:zz', or 'HH:MM:SS+zz:zz' if
        This is purely informational; the DST offset has already been added to
        This is 'YYYY-MM-DD HH:MM:SS.mmmmmm', or 'YYYY-MM-DD HH:MM:SS' if
        This is 'YYYY-MM-DD'.
        time, default 'T'.
        timetuple = (1900, 1, 1, self._hour, self._minute, self._second, 0, 1, -1)
        to underlying strftime should not be used.
        today = _ymd2ord(self._year, self._month, self._day)
        tz = self._tzstr()
        tzinfo (default to None)
        tzinfo=None,
        tzinfo=True,
        tzoff = self.utcoffset()
        us = int(frac * 1e6)
        us = int(microseconds)
        us1, us2 = divmod(us2, 256)
        us2, us3 = divmod(self._microsecond, 256)
        usdouble = secondsfrac * 1e6
        usec = self._to_microseconds()
        utc = (self - myoffset).replace(tzinfo=tz)
        UTC)."""
        week, day = divmod(today - week1monday, 7)
        week1monday += 7
        week1monday = _isoweek1monday(year)
        weekday = self.toordinal() % 7 or 7
        weeks=0,
        y, m, d = _ord2ymd(n)
        y, m, d = self._year, self._month, self._day
        y, m, d = self.year, self.month, self.day
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.gmtime(t)
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        y, m, d, hh, mm, ss, weekday, jday, dst = converter(t)
        y2, m2, d2 = other._year, other._month, other._day
        year = self._year
        year,
        year, month, day (required, base 1)
        year=None,
        yhi, ylo = divmod(self._year, 256)
        yhi, ylo, self._month, self._day = string
        'YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM' or 'YYYY-MM-DD HH:MM:SS+HH:MM'.
    - add, subtract timedelta
    - compare to timedelta
    - multiply, divide by int
    - unary plus, minus, abs
    - z.s + z.o =                   by #2
    """
    """Abstract base class for time zone info classes.
    """Concrete date type.
    """datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    """Represent the difference between two datetime objects.
    """Time with time zone.
    "Apr",
    "Aug",
    "Dec",
    "Feb",
    "Jan",
    "Jul",
    "Jun",
    "Mar",
    "May",
    "Nov",
    "Oct",
    "ordinal -> (year, month, day), considering 01-Jan-0001 as day 1."
    "Sep",
    "year -> 1 if leap year, else 0."
    "year -> number of days before January 1st of year."
    "year, month -> number of days in that month in that year."
    "year, month -> number of days in year preceding first day of month."
    "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
    #
    #     -- --- ----        ----------     ----------------
    #      1 Jan  001         1              0            400-year boundary
    #      1 Jan  401         _DI400Y +1     _DI400Y      400-year boundary
    #      1 Jan -399         -_DI400Y +1   -_DI400Y      400-year boundary
    #      2 Jan  001         2              1
    #      3 Jan  001         3              2
    #     ...
    #     30 Dec  000        -1             -2
    #     31 Dec  000         0             -1
    #     31 Dec  400         _DI400Y        _DI400Y -1
    #     31 Dec -400        -_DI400Y       -_DI400Y -1
    #     D  M   Y            n              n-1
    # 100-year cycles precede the desired day, which implies the desired
    # Additional constructors
    # And now how many single years.  Again n1 can be 4, and again meaning
    # appropriate to maintain a single module level docstring and
    # Clean up unused names
    # clips the usable dates to [1970 .. 2038).  At least ctime() is
    # closest 400-year boundary at or before n, then work with the offset
    # Comparisons of date objects with other.
    # Comparisons of datetime objects with other.
    # Comparisons of time objects with other.
    # Comparisons of timedelta objects with other.
    # Computations
    # Conversion to string
    # Conversions to string
    # day is December 31 at the end of a 400-year cycle.
    # Day-of-the-week and week-of-the-year, according to ISO
    # docstring does not get overwritten. In the future, it may be
    # Don't call utcoffset() or tzname() unless actually needed.
    # easily done without using strftime() -- that's better too because
    # from that boundary to n.  Life is much clearer if we subtract 1 from
    # Helper to calculate the day number of the Monday starting week 1
    # n first -- then the values of n at 400-year boundaries are exactly
    # n is a 1-based index, starting at 1-Jan-1.  The pattern of leap years
    # Note that it's possible for n100 to equal 4!  In that case 4 full
    # Now compute how many 4-year cycles precede it.
    # Now n is the (non-negative) offset, in days, from January 1 of year, to
    # Now the year and month are correct, and n is the offset from the
    # Now the year is correct, and n is the offset from January 1.  We find
    # Pickle support.
    # Read-only field accessors
    # remove the following line.
    # repeats exactly every 400 years.  The basic strategy is to find the
    # Scan format for %z and %Z escapes, replacing as needed.
    # Sentinel value to disallow None
    # Skip trailing microseconds when us==0.
    # Standard conversions, __cmp__, __hash__ (and helpers)
    # Standard conversions, __hash__ (and helpers)
    # start of that month:  we're done!
    # strftime("%c", ...) is locale specific.
    # that the desired day is December 31 at the end of the 4-year cycle.
    # the desired date.  Now compute how many 100-year cycles precede n.
    # the month via an estimate that's either exact or one too large.
    # those divisible by _DI400Y:
    # Timezone functions
    # Ways to produce a string.
    # XXX across the implementations.
    # XXX available from Python.  So now() may return different results
    # XXX if the platform supports a more accurate way.  The C implementation
    # XXX Since import * above excludes names that start with _,
    # XXX These shouldn't depend on time.localtime(), because that
    # XXX This could be done more efficiently
    # XXX This is supposed to do better than we *can* do by using time.time(),
    # XXX uses gettimeofday on platforms that have it, but that isn't
    (y + y.s).n =               by #5
    )
    ):
    @classmethod
    @property
    @staticmethod
    __add__, __radd__, __sub__ (add/radd only with timedelta arg)
    __cmp__, __hash__
    __new__()
    __radd__ = __add__
    __repr__, __str__
    __rmul__ = __mul__
    __slots__ = "_days", "_seconds", "_microseconds"
    __slots__ = "_offset", "_name"
    __slots__ = "_year", "_month", "_day"
    __slots__ = ()
    __slots__ = date.__slots__ + (
    __str__ = isoformat
    _DAYS_BEFORE_MONTH.append(dbm)
    _maxoffset = timedelta(hours=23, minutes=59)
    _minoffset = -_maxoffset
    _Omitted = object()
    and a timedelta giving a datetime.
    assert 0 <= n < _days_in_month(year, month)
    assert 1 <= day <= dim, "day must be in 1..%d" % dim
    assert 1 <= month <= 12, "month must be in 1..12"
    assert 1 <= month <= 12, month
    assert leapyear == _is_leap(year)
    assert name in ("utcoffset", "dst")
    Constructors:
    ctime()
    days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999
    dbm += dim
    def __abs__(self):
    def __add__(self, other):
    def __bool__(self):
    def __divmod__(self, other):
    def __eq__(self, other):
    def __floordiv__(self, other):
    def __format__(self, fmt):
    def __ge__(self, other):
    def __getinitargs__(self):
    def __gt__(self, other):
    def __hash__(self):
    def __init__(self, *args, **kwargs): pass
    def __le__(self, other):
    def __lt__(self, other):
    def __mod__(self, other):
    def __mul__(self, other):
    def __ne__(self, other):
    def __neg__(self):
    def __new__(
    def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
    def __new__(cls, offset, name=_Omitted):
    def __new__(cls, year, month=None, day=None):
    def __pos__(self):
    def __reduce__(self):
    def __repr__(self):
    def __rsub__(self, other):
    def __setstate(self, string):
    def __setstate(self, string, tzinfo):
    def __str__(self):
    def __sub__(self, other):
    def __truediv__(self, other):
    def _cmp(self, other):
    def _cmp(self, other, allow_mixed=False):
    def _create(cls, offset, name=None):
    def _getstate(self):
    def _name_from_offset(delta):
    def _to_microseconds(self):
    def _tzstr(self, sep=":"):
    def astimezone(self, tz=None):
    def combine(cls, date, time):
    def ctime(self):
    def date(self):
    def day(self):
    def days(self):
    def dst(self):
    def dst(self, dt):
    def fromordinal(cls, n):
    def fromtimestamp(cls, t):
    def fromtimestamp(cls, t, tz=None):
    def fromutc(self, dt):
    def hour(self):
    def isocalendar(self):
    def isoformat(self):
    def isoformat(self, sep="T"):
    def isoweekday(self):
    def microsecond(self):
    def microseconds(self):
    def minute(self):
    def month(self):
    def now(cls, tz=None):
    def replace(
    def replace(self, year=None, month=None, day=None):
    def second(self):
    def seconds(self):
    def strftime(self, fmt):
    def strptime(cls, date_string, format):
    def time(self):
    def timestamp(self):
    def timetuple(self):
    def timetz(self):
    def today(cls):
    def toordinal(self):
    def total_seconds(self):
    def tzinfo(self):
    def tzname(self):
    def tzname(self, dt):
    def utcfromtimestamp(cls, t):
    def utcnow(cls):
    def utcoffset(self):
    def utcoffset(self, dt):
    def utctimetuple(self):
    def weekday(self):
    def year(self):
    del (
    diff =
    diff = x.n - (z.n - z.o)                    [6]
    diff' = x.n - (z'.n - z'.o) =           replacing z'.n via [7]
    dim = _days_in_month(year, month)
    dnum = _days_before_month(y, m) + d
    dst()
    felt like it.
    firstday = _ymd2ord(year, 1, 1)
    firstweekday = (firstday + 6) % 7  # See weekday() above
    freplace = None  # the string to use for %f
    from _datetime import *
    fromordinal()
    fromtimestamp()
    hour, minute, second, microsecond, tzinfo
    i, n = 0, len(format)
    if firstweekday > THURSDAY:
    if month == 2 and _is_leap(year):
    if n1 == 4 or n100 == 4:
    if name is not None and not isinstance(name, str):
    if not 0 <= hour <= 23:
    if not 0 <= microsecond <= 999999:
    if not 0 <= minute <= 59:
    if not 0 <= second <= 59:
    if not 1 <= day <= dim:
    if not 1 <= month <= 12:
    if not isinstance(hour, int):
    if not isinstance(offset, timedelta):
    if not isinstance(year, int):
    if not MINYEAR <= year <= MAXYEAR:
    if not -timedelta(1) < offset < timedelta(1):
    if offset % timedelta(minutes=1) or offset.microseconds:
    if offset is None:
    if preceding > n:  # estimate is too large
    if tz is not None and not isinstance(tz, tzinfo):
    if tzinfo is None:
    if us:
    In addition, datetime supports subtraction of two datetime objects
    instance of a tzinfo subclass. The remaining arguments may be ints.
    isoformat()
    isoweekday(), isocalendar(), isoformat()
    leapyear = n1 == 3 and (n4 != 24 or n100 == 3)
    Methods:
    month = (n + 50) >> 5
    n -= 1
    n -= preceding
    n1, n = divmod(n, 365)
    n100, n = divmod(n, _DI100Y)
    n4, n = divmod(n, _DI4Y)
    n400, n = divmod(n, _DI400Y)
    newformat = "".join(newformat)
    newformat = []
    None,
    Operators:
    pass
    preceding = _DAYS_BEFORE_MONTH[month] + (month > 2 and leapyear)
    Properties (readonly):
    push = newformat.append
    raise TypeError(
    Representation: (days, seconds, microseconds).  Why?  Because I
    result = "%02d:%02d:%02d" % (hh, mm, ss)
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))
    return _days_before_year(year) + _days_before_month(year, month) + day
    return _DAYS_IN_MONTH[month]
    return _time.strftime(newformat, timetuple)
    return _time.struct_time((y, m, d, hh, mm, ss, wday, dnum, dstflag))
    return 0 if x == y else 1 if x > y else -1
    return getattr(tzinfo, methname)(tzinfoarg)
    return result
    return week1monday
    return y * 365 + y // 4 - y // 100 + y // 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return year, month, n + 1
    returning a timedelta, and addition or subtraction of a datetime
    strftime()
    Subclasses must override the name(), utcoffset() and dst() methods.
    Supported operators:
    The year, month and day arguments are required. tzinfo may be None, or an
    THURSDAY = 3
    timetuple()
    today()
    toordinal()
    tzname()
    utcoffset()
    wday = (_ymd2ord(y, m, d) + 6) % 7
    week1monday = firstday - firstweekday
    weekday()
    while i < n:
    x.d = x.dst(), and assuming that doesn't raise an exception or
    x.n - ((x.n + z.s) - z.o) =     expanding
    x.n - x.n - z.s + z.o =         cancelling
    x.n + y.s =                 since z and y are have the same tzinfo member,
    x.n + z.s
    x.n = x stripped of its timezone -- its naive time.
    x.o = x.utcoffset(), and assuming that doesn't raise an exception or
    x.s = x's standard offset, x.o - x.d
    y = year - 1
    y.n - y.o = x.n                             [1]
    y.n + y.s =                 since y.n = x.n
    year += n100 * 100 + n4 * 4 + n1
    year = n400 * 400 + 1  # ..., -399, 1, 401, ...
    year, month, day
    z = y + y.s                                 [4]
    z' = z + z.d = z + diff                     [7]
    z.d
    z.n - z.o = x.n                             [5]
    z'.n - z'.o = x.n                           [8]
    z.n =                       by [4]
    zreplace = None  # the string to use for %z
    Zreplace = None  # the string to use for %Z
   (y+k).n - ((y+k).s + (y+k).d) = x.n          [3]
   (y+k).n - (y+k).o = x.n                      [2]
   a region decides to change its base offset from UTC.
   Again follows from how arithmetic is defined.
   enough to say.
   k - (y+k).s - (y+k).d = 0; rearranging,
   k = (y+k).s - (y+k).d; by #4, (y+k).s == y.s, so
   k = y.s - (y+k).d
   sane tzinfo classes.
   the analysis gives up a step too early.  I haven't thought about that
   This follows from #2, and that datimetimetz+timedelta preserves tzinfo.
   This follows from the definition of x.s.
   This is actually a requirement, an assumption we need to make about
   This is again a requirement for a sane tzinfo class.
   time zone.  This isn't true if, for political reasons or continental drift,
   x.n + k - (y+k).s - (y+k).d = x.n; the x.n terms cancel, leaving
"""
"""Concrete date/time and related types.
"almost all" time zones:  so long as the standard offset is invariant, it
# A 4-year cycle has an extra leap day over what we'd get from pasting
# also assumes the current Gregorian calendar indefinitely extended in
# and Reingold's "Calendrical Calculations", where it's the base calendar
# both directions.  Difference:  Dates.py calls January 1 of year 0 day
# Correctly substitute for %z and %Z escapes in strftime formats.
# Else offset is checked for being in range, and a whole # of minutes.
# for all computations.  See the book for algorithms for converting between
# If it is, its integer value is returned.  Else ValueError is raised.
# If offset is None, returns None.
# If offset isn't None or timedelta, raises TypeError.
# Just raise TypeError if the arg isn't None or a string.
# Month and day names.  For localized versions, see the calendar module.
# name is the offset-producing method, "utcoffset" or "dst".
# number 1.  The code here calls January 1 of year 1 day number 1.  This is
# offset is what it returned.
# OTOH, a 100-year cycle has one fewer leap day than we'd get from
# pasting together 25 4-year cycles.
# pasting together 4 100-year cycles.
# proleptic Gregorian ordinals and many other calendar systems.
# Similarly, a 400-year cycle has an extra leap day over what we'd get from
# to match the definition of the "proleptic Gregorian" calendar in Dershowitz
# together 4 single years.
# Utility functions, adapted from Python's Demo/classes/Dates.py, which
(correctly) concludes that z' is not UTC-equivalent to x.
(meaning that the various tzinfo methods exist, and don't blow up or return
)
]
_date_class = date  # so functions w/ args named "date" can get at the class
_DAYNAMES = [None, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_DAYS_BEFORE_MONTH = [None]
_DAYS_IN_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_DI100Y = _days_before_year(101)  # "    "   "   " 100   "
_DI400Y = _days_before_year(401)  # number of days in 400 years
_DI4Y = _days_before_year(5)  # "    "   "   "   4   "
_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
_MAXORDINAL = 3652059  # date.max.toordinal()
_MONTHNAMES = [
_time_class = time  # so functions w/ args named "time" can get at the class
_tzinfo_class = tzinfo
1) [2] effectively says that y.s is invariant across all y belong to a given
1. x.o = x.s + x.d
2) There may be versions of "double daylight" time where the tail end of
2. If x and y have the same tzinfo member, x.s = y.s.
3. The naive UTC time corresponding to x is x.n - x.o.
4. (x+k).s = x.s
5. (x+k).n = x.n + k
a dst() offset, and starting *from* a time already in DST (we know z.d != 0),
a little further into it takes us out of DST.
add to z (in effect, z is in tz's standard time, and we need to shift the
already):
and we can again ask whether
and we have stopped then), and there are only 2 possible values dst() can
approximate k by ignoring the (y+k).d term at first.  Note that k can't be
assert _DI100Y == 25 * _DI4Y - 1
assert _DI400Y == 4 * _DI100Y + 1
assert _DI4Y == 4 * 365 + 1
assumptions we've made.  This also requires a bit of proof.  As before, let's
at the start of daylight time.  Picture US Eastern for concreteness.  The wall
At this point, if
be 0, so ignoring it has no consequence then.
be EDT (because it's "after 2"), which is a redundant spelling of 1:MM EST
Because we know z.d said z was in daylight time (else [5] would have held and
becomes true; in effect, we want to solve [2] for k:
but that takes a bit of proof.  We first prove a stronger result.  What's the
but the reasoning doesn't depend on the example -- it depends on there being
By #1, this is the same as
By #3, we want
By #5, (y+k).n = y.n + k, which equals x.n + k because x.n=y.n at the start.
class date:
class datetime:
class time:
class timedelta:
class timezone:
class tzinfo:
clock jumps from 1:59 back to 1:00 again, and repeats the 1:MM hour in
clock repeats an hour" behavior when mapping the "unspellable" UTC hour into
compute the difference between the LHS and RHS of [8] (and skipping some of
concerned (because it takes z' as being in standard time rather than the
date.max = date(9999, 12, 31)
date.min = date(1, 1, 1)
date.resolution = timedelta(days=1)
datetime.max = datetime(9999, 12, 31, 23, 59, 59, 999999)
datetime.min = datetime(1, 1, 1)
datetime.resolution = timedelta(microseconds=1)
daylight time we intend here), but returning it gives the real-life "local
dbm = 0
def _build_struct_time(y, m, d, hh, mm, ss, dstflag):
def _call_tzinfo_method(tzinfo, methname, tzinfoarg):
def _check_date_fields(year, month, day):
def _check_time_fields(hour, minute, second, microsecond):
def _check_tzinfo_arg(tz):
def _check_tzname(name):
def _check_utc_offset(name, offset):
def _cmp(x, y):
def _cmperror(x, y):
def _days_before_month(year, month):
def _days_before_year(year):
def _days_in_month(year, month):
def _format_time(hh, mm, ss, us):
def _is_leap(year):
def _isoweek1monday(year):
def _ord2ymd(n):
def _wrap_strftime(object, format, timetuple):
def _ymd2ord(year, month, day):
del dbm, dim
difference between the LHS and RHS of [5]?  Let
doesn't matter if daylight time transition points change from year to year, or
else:
except ImportError:
for dim in _DAYS_IN_MONTH[1:]:
from future.builtins import bytes
from future.builtins import int
from future.builtins import map
from future.builtins import object
from future.builtins import round
from future.builtins import str
from future.utils import native_str, PY2
How could z.d and z'd differ?  z' = z + z.d [7], so merely moving z' by
If [5] is not true now, diff = z.d != 0, and z.d is the offset we need to
If [5] is true now, diff = 0, so z.d = 0 too, and we have the standard-time
if daylight time is skipped in some years; it doesn't matter how large or
If so, we're done.  If not, the tzinfo class is insane, according to the
if z.d = 0, then we have a UTC equivalent, and are also done.
import math as _math
import time as _time
In any case, it's clear that the default fromutc() is strong enough to handle
In any case, the new value is
In fact, if [5] holds at this point, we do have the standard-time spelling,
in local time, but so it goes -- it's the way the local clock works.
It's helpful to step back at look at [4] from a higher level:  it's simply
less than 24 hours.  For that reason, if y is firmly in std time, (y+k).d must
Let
local clock into tz's daylight time).
mapping from UTC to tz's standard time.
MAXYEAR = 9999
MINYEAR = 1
None when called).
Note again that z' is not UTC-equivalent as far as the hybrid tzinfo class is
Now
Now some derived rules, where k is a duration (timedelta).
Now we can explain tz.fromutc(x).  Let's assume it's an interesting case
on the day DST starts.  We want to return the 1:MM EST spelling because that's
On the RHS, (y+k).d can't be computed directly, but y.s can be, and we
perverse time zone returns a negative dst()).  So a breaking case must be
Plugging that back into [6] gives
possibilities:
pretty bizarre, and a tzinfo subclass can override fromutc() if it is.
return in Eastern, it follows that z'.d must be 0 (which it is in the example,
return z', not bothering to compute z'.d.
See http://www.iana.org/time-zones/repository/tz-link.html for
sense then.  The docs ask that an Eastern tzinfo class consider such a time to
small dst() may get within its bounds; and it doesn't even matter if some
So diff = z.d.
So how can this break?  One of the assumptions must be violated.  Two
So z' is UTC-equivalent to x iff z'.d = z.d at this point.  If they are equal,
so z=0:MM.  z.d=60 (minutes) then, so [5] doesn't hold and we keep going.
Some time zone algebra.  For a datetime x, let
spelling we wanted in the endcase described above.  We're done.  Contrarily,
standard time.  Since that's what the local clock *does*, we want to map both
Substituting that into [3],
that hour, on an Eastern clock 1:MM is taken as being in standard time (6:MM
the 1:MM standard time spelling we want.
The algorithm starts by attaching tz to x.n, and calling that y.  So
the end of DST, where there's an hour in UTC with no spelling in a hybrid
The function wants to return a datetime y with timezone tz, equivalent to x.
the justifications for the kinds of substitutions we've done several times
the only spelling that makes sense on the local wall clock.
There isn't a sane case where this can happen.  The closest it gets is at
time (4:MM UTC).  There is no local time mapping to 5:MM UTC.  The local
time jumps from 1:59 to 3:00, and wall hours of the form 2:MM don't make good
time zone and DST data sources.
time.max = time(23, 59, 59, 999999)
time.min = time(0, 0, 0)
time.resolution = timedelta(microseconds=1)
timedelta.max = timedelta(
timedelta.min = timedelta(-999999999)
timedelta.resolution = timedelta(microseconds=1)
timezone.max = timezone._create(timezone._maxoffset)
timezone.min = timezone._create(timezone._minoffset)
timezone.utc = timezone._create(timedelta(0))
try:
two possible dst() outcomes, one zero and the other non-zero).  Therefore
tz.
tzinfo class.  In US Eastern, that's 5:MM UTC = 0:MM EST = 1:MM EDT.  During
UTC hours 5:MM and 6:MM to 1:MM Eastern.  The result is ambiguous
UTC) because the docs insist on that, but 0:MM is taken as being in daylight
very large, since all offset-returning methods return a duration of magnitude
we have an equivalent time, and are almost done.  The insecurity here is
we would have stopped then), and we know z.d != z'.d (else [8] would have held
we've found the UTC-equivalent so are done.  In fact, we stop with [7] and
When the input is 6:MM, z=1:MM and z.d=0, and we stop at once, again with
When x = 5:MM UTC is the input to this algorithm, x.o=0, y.o=-5 and y.d=0,
would have to change the result dst() returns:  we start in DST, and moving
x is already in UTC.
x.n = y.n at the start.  Then it wants to add a duration k to y, so that [1]
z' = z + z.d = 1:MM then, and z'.d=0, and z'.d - z.d = -60 != 0 so [8]
z' must be in standard time, and is the spelling we want in this case.
