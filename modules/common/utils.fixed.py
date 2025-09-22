
# collapse_rfc2231_value treats this as an octet sequence.
                    # Decode as "latin-1", so the characters in s directly
                    # represent the percent-encoded octet values.
                    extended = True
                    s = url_unquote(s, encoding="latin-1")
                charset = Charset(charset)
                charset, language, value = decode_rfc2231(value)
                if encoded:
                new_params.append((name, '"%s"' % value))
                new_params.append((name, (charset, language, '"%s"' % value)))
                num = int(num)
                quotes = '"'
                value.append(s)
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
            "Sep",
            # %-encodings for the encoded segments.  If any of the
            # And now append all values in numerical order, converting
            # continuation names ends in a *, then the entire string, after
            # decoding segments and concatenating, must have the charset and
            # language specifiers at the beginning of the string.
            # Sort by number
            continuations.sort()
            else:
            encoded = False
            encoded = True
            encoded_name = charset.header_encode(name)
            extended = False
            for num, s, encoded in continuations:
            if extended:
            if isinstance(charset, str):
            if num is not None:
            if specialsre.search(name):
            name = escapesre.sub(r"\\\g<0>", name)
            name, num = mo.group("name", "num")
            name.encode("ascii")
            new_params.append((name, '"%s"' % quote(value)))
            offset = time.altzone
            offset = time.timezone
            quotes = ""
            raise ValueError("usegmt option requires a UTC datetime")
            return "{} <{}>".format(encoded_name, address)
            return "{}{}{} <{}>".format(quotes, name, quotes, address)
            return str[1:-1]
            return str[1:-1].replace("\\\\", "\\").replace('\\"', '"')
            rfc2231_params.setdefault(name, []).append((num, value, encoded))
            sign = "-"
            sign = "+"
            tz = datetime.timezone(delta)
            tz = datetime.timezone(delta, time.tzname[dst])
            value = []
            value = quote(EMPTYSTRING.join(value))
            zone = "-0000"
            zone = "GMT"
        # Calculate timezone offset, based on whether the local zone has
        # charset is not a known codec.
        # Compute UTC offset and compare with the value implied by tm_isdst.
        # daylight savings time, and whether DST is in effect.
        # If the values match, use the zone name implied by tm_isdst.
        # minutes east of UTC, so the signs differ.
        # Remember offset is in seconds west of UTC, but the timezone is in
        # Timezone offset is always -0000
        *dtuple[:6], tzinfo=datetime.timezone(datetime.timedelta(seconds=tz))
        [
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][timetuple[6]],
        ][timetuple[1] - 1],
        _3to2list[:-1]
        delta = datetime.timedelta(seconds=localtm.tm_gmtoff)
        delta = dt - datetime.datetime(*time.gmtime(seconds)[:6])
        domain = socket.getfqdn()
        dst = time.daylight and localtm.tm_isdst > 0
        dtuple,
        else:
        except UnicodeEncodeError:
        for name, continuations in rfc2231_params.items():
        gmtoff = -(time.altzone if dst else time.timezone)
        hours, minutes = divmod(abs(offset), 3600)
        idstring = ""
        idstring = "." + idstring
        if delta == datetime.timedelta(seconds=gmtoff):
        if dt.tzinfo is None or dt.tzinfo != datetime.timezone.utc:
        if mo:
        if name.endswith("*"):
        if offset > 0:
        if str.startswith('"') and str.endswith('"'):
        if str.startswith("<") and str.endswith(">"):
        if time.daylight and now[-1]:
        if usegmt:
        language = ""
        mo = rfc2231_continuation.match(name)
        name, value = params.pop(0)
        now = time.gmtime(timeval)
        now = time.localtime(timeval)
        return "", ""
        return datetime.datetime(*dtuple[:6])
        return datetime.datetime.now(datetime.timezone.utc).astimezone()
        return dt.astimezone()
        return None, None, s
        return s
        return str(rawbytes, charset, errors)
        return unquote(text)
        return unquote(value)
        timetuple[0],
        timetuple[2],
        timetuple[3],
        timetuple[4],
        timetuple[5],
        timeval = time.time()
        try:
        tz = datetime.timezone(delta, localtm.tm_zone)
        tz,
        value = unquote(value)
        zone = "%s%02d%02d" % (sign, hours, minutes // 60)
        zone = "-0000"
        zone = "GMT"
        zone = dt.strftime("%z")
        zone,
    """
    """Decode parameters list according to RFC 2231.
    """Decode string according to RFC 2231"""
    """Encode string according to RFC 2231.
    """Remove quotes from a string."""
    """Return a list of (REALNAME, EMAIL) for each fieldvalue."""
    """Return local time as an aware datetime object.
    """Returns a date string as specified by RFC 2822, e.g.:
    """Returns a string suitable for RFC 2822 compliant Message-ID, e.g:
    """The inverse of parseaddr(), this takes a 2-tuple of the form
    """Turn a datetime into a date string as specified in RFC 2822.
    "([^\ud800-\udbff]|\\A)[\udc00-\udfff]([^\udc00-\udfff]|\\Z)"
    "collapse_rfc2231_value",
    "decode_params",
    "decode_rfc2231",
    "encode_rfc2231",
    "format_datetime",
    "formataddr",
    "formatdate",
    "getaddresses",
    "make_msgid",
    "mktime_tz",
    "parseaddr",
    "parsedate",
    "parsedate_to_datetime",
    "parsedate_tz",
    "unquote",
    # 2822 requires that day and month names be the English abbreviations.
    # 3-tuple of the continuation number, the string value, and a flag
    # Copy params so we don't mess with the original
    # interpretation of the string as character bytes.
    # Map parameter's name to a list of continuations.  The values are a
    # Note: we cannot use strftime() because that honors the locale and RFC
    # object.  We do not want bytes() normal utf-8 decoder, we want a straight
    # seconds since epoch.
    # specifying whether a particular segment is %-encoded.
    # system mktime together with the isdst hint.  System mktime will return
    # The address MUST (per RFC) be ascii, so raise an UnicodeError if it isn't.
    # Turn any escaped bytes into unicode 'unknown' char.
    # We have a naive datetime.  Convert to a (localtime) timetuple and pass to
    # While value comes to us as a unicode string, we need it to be a bytes
    (
    (realname, email_address) and returns the string value suitable
    )
    ) = [
    ] + _3to2list[-1:]
    _3to2list = list(_parsedate_tz(data))
    <20020201195627.33539.96671@nightshade.la.mastaler.com>
    a = _AddressList(all)
    a Charset-like object which has a header_encode method.  Default is
    address.encode("ascii")
    addrs = _AddressList(addr).addresslist
    all = COMMASPACE.join(fieldvalues)
    an ascii string, not numeric one (so "GMT" instead of "+0000"). This
    argument should be a datetime instance, and it is converted to the
    charset is given but not language, the string is encoded using the empty
    charset, language, text = value
    defined hostname.
    elif dt.tzinfo is None:
    else:
    except AttributeError:
    except LookupError:
    for an RFC 2822 From, To or Cc header.
    Fri, 09 Nov 2001 01:08:47 -0000
    gmtime() and localtime(), otherwise the current time is used.
    If called without arguments, return current time.  Otherwise *dt*
    if charset is None and language is None:
    if domain is None:
    if dt is None:
    if dt.tzinfo is not None:
    if idstring is None:
    if language is None:
    if len(parts) <= 2:
    if len(str) > 1:
    if localtime:
    if name:
    If neither charset nor language is given, then s is returned as-is.  If
    if not addrs:
    if not isinstance(value, tuple) or len(value) != 3:
    if rfc2231_params:
    If the first element of pair is false, then the second element is
    if timeval is None:
    if tz is None:
    If usegmt is True, dt must be an aware datetime with an offset of zero.  In
    if usegmt:
    In this case, a positive or zero value for *isdst* causes localtime to
    is needed for HTTP, and is only used when localtime==False.
    is or is not (respectively) in effect for the specified time.  A
    local time zone according to the system time zone database.  If *dt* is
    localtm = time.localtime(seconds)
    msgid = "<{}.{}.{}{}@{}>".format(utcdate, pid, randint, idstring, domain)
    naive (that is, dt.tzinfo is None), it is assumed to be in local time.
    name, address = pair
    name, value = params.pop(0)
    negative value for *isdst* causes the localtime() function to attempt
    new_params = []
    new_params.append((name, value))
    now = dt.timetuple()
    Optional argument usegmt means that the timezone is written out as
    Optional charset if given is the character set that is used to encode
    Optional idstring if given is a string used to strengthen the
    Optional localtime is a flag that when True, interprets timeval, and
    Optional timeval if given is a floating point time value as accepted by
    original_bytes = string.encode("ascii", "surrogateescape")
    params = params[:]
    params is a sequence of 2-tuples containing (param name, string value).
    parts = s.split(TICK, 2)
    pid = os.getpid()
    portion of the message id after the '@'.  It defaults to the locally
    presume initially that summer time (for example, Daylight Saving Time)
    r"""
    randint = random.randrange(100000)
    rawbytes = bytes(text, "raw-unicode-escape")
    re.ASCII = 0
    re.VERBOSE | re.IGNORECASE,
    realname in case realname is not ASCII safe.  Can be an instance of str or
    return "%s, %02d %s %04d %02d:%02d:%02d %s" % (
    return "{}'{}'{}".format(charset, language, s)
    return _format_timetuple_and_zone(now, zone)
    return a.addresslist
    return address
    return addrs[0]
    return datetime.datetime(
    return dt.replace(tzinfo=tz)
    return msgid
    return new_params
    return original_bytes.decode("ascii", "replace")
    return parts
    return str
    returned unmodified.
    returns a date relative to the local timezone instead of UTC, properly
    rfc2231_params = {}
    RFC2822.  This is to support HTTP headers involving date stamps.
    s = url_quote(s, safe="", encoding=charset or "ascii")
    seconds = time.mktime(tm)
    string for language.
    taking daylight savings time into account.
    this case 'GMT' will be rendered instead of the normal +0000 required by
    timeval = time.time()
    tm = dt.timetuple()[:-1] + (isdst,)
    to divine whether summer time is in effect for the specified time.
    try:
    uniqueness of the message id.  Optional domain if given provides the
    utcdate = time.strftime("%Y%m%d%H%M%S", time.gmtime(timeval))
    'utf-8'.
    while params:
  """,
  (?P<atom>.*?)         # non-greedy up to the next ?= is the atom
  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset
  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive
  \?                    # literal ?
  \?=                   # literal ?=
  =\?                   # literal =?
"""Miscellaneous utilities."""
#
# adapted from the patch in issue 9527.  This may not be perfect, but it is
# application through the 'normal' interface.
# Author: Barry Warsaw
# better than not having it.
# Contact: email-sig@python.org
# Copyright (C) 2001-2010 Python Software Foundation
# datetime doesn't provide a localtime function yet, so provide one.  Code
# Helpers
# How to deal with a string containing bytes before handing it to the
# How to figure out if we are processing strings that come from a byte
# Intrapackage imports
# RFC2231-related functions - parameter encoding and decoding
# rfc822.unquote() doesn't properly de-backslash-ify in Python pre-2.3.
# source with undecodable characters.
)
).search
]
__all__ = [
_has_surrogates = re.compile(
COMMASPACE = ", "
CRLF = "\r\n"
def _format_timetuple_and_zone(timetuple, zone):
def _sanitize(string):
def collapse_rfc2231_value(value, errors="replace", fallback_charset="us-ascii"):
def decode_params(params):
def decode_rfc2231(s):
def encode_rfc2231(s, charset=None, language=None):
def format_datetime(dt, usegmt=False):
def formataddr(pair, charset="utf-8"):
def formatdate(timeval=None, localtime=False, usegmt=False):
def getaddresses(fieldvalues):
def localtime(dt=None, isdst=-1):
def make_msgid(idstring=None, domain=None):
def parseaddr(addr):
def parsedate_to_datetime(data):
def unquote(str):
ecre = re.compile(
EMPTYSTRING = ""
escapesre = re.compile(r'[\\"]')
from future import utils
from future.backports.email._parseaddr import AddressList as _AddressList
from future.backports.email._parseaddr import (_parsedate_tz, mktime_tz,
                                               parsedate, parsedate_tz, quote)
from future.backports.email.charset import Charset
from future.backports.urllib.parse import quote as url_quote
from future.backports.urllib.parse import unquote as url_unquote
from future.builtins import bytes, int, str

if utils.PY2:
import datetime
import os
import random
import re
import socket
import time

rfc2231_continuation = re.compile(r"^(?P<name>\w+)\*((?P<num>[0-9]+)\*?)?$", re.ASCII)
specialsre = re.compile(r'[][\\()<>@,:;".]')
TICK = "'"
UEMPTYSTRING = ""

pass
