import os
import re
import datetime
import random
import socket
import time
from dotenv import load_dotenv
from typing import Optional, Tuple, List, Union

from future.backports.email._parseaddr import AddressList as _AddressList
from future.backports.email._parseaddr import (_parsedate_tz, mktime_tz,
                                               parsedate, parsedate_tz, quote)
from future.backports.email.charset import Charset
from future.backports.urllib.parse import quote as url_quote
from future.backports.urllib.parse import unquote as url_unquote
from future.builtins import bytes, int, str

# .env 로드 및 기본 경로 설정
load_dotenv()
BASE_PATH = os.getenv("BASE_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
if not os.path.exists(BASE_PATH):
    raise FileNotFoundError(f"⚠️ BASE_PATH 경로 없음: {BASE_PATH}")
print(f"✅ BASE_PATH 로드 완료: {BASE_PATH}")

__all__ = [
    "collapse_rfc2231_value", "decode_params", "decode_rfc2231", "encode_rfc2231",
    "format_datetime", "formataddr", "formatdate", "getaddresses", "make_msgid",
    "mktime_tz", "parseaddr", "parsedate", "parsedate_to_datetime", "parsedate_tz", "unquote"
]

# 정규식 및 상수 정의
CRLF = "\r\n"
COMMASPACE = ", "
EMPTYSTRING = ""
UEMPTYSTRING = ""
TICK = "'"
rfc2231_continuation = re.compile(r"^(?P<name>\w+)\*((?P<num>[0-9]+)\*?)?$", re.ASCII)
specialsre = re.compile(r'[][\\()<>@,:;".]')
escapesre = re.compile(r'[\\"]')
ecre = re.compile("([^\ud800-\udbff]|\\A)[\udc00-\udfff]([^\udc00-\udfff]|\\Z)")

def _sanitize(string: str) -> str:
    return string.replace("\\", "\\\\").replace('"', '\\"')

def _format_timetuple_and_zone(timetuple, zone) -> str:
    return "%s, %02d %s %04d %02d:%02d:%02d %s" % (
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][timetuple[6]],
        timetuple[2],
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][timetuple[1] - 1],
        timetuple[0], timetuple[3], timetuple[4], timetuple[5], zone
    )

def collapse_rfc2231_value(value: Union[str, Tuple[str, str, str]],
                            errors="replace", fallback_charset="us-ascii") -> str:
    if not isinstance(value, tuple) or len(value) != 3:
        return value
    charset, language, text = value
    if not charset and not language:
        return text
    try:
        rawbytes = bytes(text, "raw-unicode-escape")
        return str(rawbytes, charset, errors)
    except (LookupError, UnicodeError):
        return str(rawbytes, fallback_charset, errors)

def decode_rfc2231(s: str) -> Tuple[str, str, str]:
    parts = s.split(TICK, 2)
    if len(parts) != 3:
        return '', '', s
    return parts[0], parts[1], unquote(parts[2])

def decode_params(params: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    new_params = []
    rfc2231_params = {}
    params = params[:]
    while params:
        name, value = params.pop(0)
        mo = rfc2231_continuation.match(name)
        if mo:
            name, num = mo.group("name", "num")
            if name.endswith("*"):
                name = name[:-1]
                encoded = True
            else:
                encoded = False
            if num is not None:
                num = int(num)
                rfc2231_params.setdefault(name, []).append((num, value, encoded))
                continue
        new_params.append((name, value))
    for name, continuations in rfc2231_params.items():
        continuations.sort()
        value = []
        charset = language = None
        extended = False
        for num, s, encoded in continuations:
            if encoded:
                extended = True
                s = url_unquote(s, encoding="latin-1")
            value.append(s)
        if extended:
            charset, language, value = decode_rfc2231(''.join(value))
        else:
            value = ''.join(value)
        if extended:
            new_params.append((name, (charset, language, value)))
        else:
            new_params.append((name, value))
    return new_params

def encode_rfc2231(s: str, charset: Optional[str] = None, language: Optional[str] = None) -> str:
    s = url_quote(s, safe="", encoding=charset or "ascii")
    return "{}'{}'{}".format(charset or '', language or '', s)

def format_datetime(dt: datetime.datetime, usegmt=False) -> str:
    if usegmt:
        if dt.tzinfo is None or dt.tzinfo != datetime.timezone.utc:
            raise ValueError("usegmt option requires a UTC datetime")
        zone = "GMT"
    else:
        if dt.tzinfo is None:
            dt = dt.astimezone()
        zone = dt.strftime("%z")
    return _format_timetuple_and_zone(dt.timetuple(), zone)

def formataddr(pair: Tuple[str, str], charset="utf-8") -> str:
    name, address = pair
    if not name:
        return address
    try:
        address.encode("ascii")
    except UnicodeEncodeError:
        return '"%s" <%s>' % (_sanitize(name), address)
    try:
        name.encode("ascii")
    except UnicodeEncodeError:
        charset = Charset(charset)
        name = charset.header_encode(name)
        return "%s <%s>" % (name, address)
    if specialsre.search(name):
        return '"%s" <%s>' % (name, address)
    return "%s <%s>" % (name, address)

def formatdate(timeval: Optional[float] = None,
               localtime: bool = False, usegmt: bool = False) -> str:
    if timeval is None:
        timeval = time.time()
    now = time.gmtime(timeval) if not localtime else time.localtime(timeval)
    zone = "GMT" if usegmt else time.strftime("%z", now)
    return _format_timetuple_and_zone(now, zone)

def getaddresses(fieldvalues: List[str]) -> List[Tuple[str, str]]:
    all = COMMASPACE.join(fieldvalues)
    a = _AddressList(all)
    return a.addresslist

def make_msgid(idstring: Optional[str] = None, domain: Optional[str] = None) -> str:
    timeval = time.time()
    utcdate = time.strftime("%Y%m%d%H%M%S", time.gmtime(timeval))
    pid = os.getpid()
    randint = random.randrange(100000)
    if domain is None:
        domain = socket.getfqdn()
    if idstring is not None:
        idstring = "." + idstring
    else:
        idstring = ""
    msgid = "<{}.{}.{}{}@{}>".format(utcdate, pid, randint, idstring, domain)
    return msgid

def parseaddr(addr: str) -> Tuple[str, str]:
    return _AddressList(addr).addresslist[0] if _AddressList(addr).addresslist else ("", "")

def parsedate_to_datetime(data: str) -> Optional[datetime.datetime]:
    t = _parsedate_tz(data)
    if t is None:
        return None
    dt = datetime.datetime(*t[:6])
    if t[9] is None:
        return dt
    return dt.replace(tzinfo=datetime.timezone(datetime.timedelta(seconds=t[9])))

def unquote(text: str) -> str:
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1].replace("\\\\", "\\").replace('\\"', '"')
    return text

def localtime(dt: Optional[datetime.datetime] = None, isdst: int = -1) -> datetime.datetime:
    if dt is None:
        dt = datetime.datetime.now(datetime.timezone.utc).astimezone()
    elif dt.tzinfo is None:
        tm = dt.timetuple()[:-1] + (isdst,)
        seconds = time.mktime(tm)
        localtm = time.localtime(seconds)
        delta = datetime.timedelta(seconds=localtm.tm_gmtoff)
        tz = datetime.timezone(delta, localtm.tm_zone)
        dt = dt.replace(tzinfo=tz)
    else:
        dt = dt.astimezone()
    return dt

def mktime_tz(dtuple: Tuple[int, ...]) -> float:
    if len(dtuple) != 10:
        raise ValueError("dtuple must be a 10-tuple")
    *dt, tz = dtuple
    return time.mktime(dt) - tz

if __name__ == "__main__":
    print("✅ utils.py 모듈 테스트용 진입점")
