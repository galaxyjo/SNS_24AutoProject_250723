
                ~Literal(",")
                + ~LineEnd()
                + Opt(White(" \t") + ~FollowedBy(LineEnd() | ","))
                + Word(printables, exclude_chars=",")
                raise ParseException(s, l, str(ve))
                raise ParseException(ss, ll, str(ve))
                return datetime.strptime(t[0], fmt)
                return datetime.strptime(tt[0], fmt).date()
            "IPv6 address"
            # any int or real number, returned as float
            # any int or real number, returned as the appropriate type
            # fractions
            # hex numbers
            # mixed fractions
            # strip HTML links from normal text
            # uuid
            )
            ''')
            [datetime.date(1999, 12, 31)]
            [datetime.datetime(1999, 12, 31, 23, 59, 59, 999000)]
            +100
            1
            1/2
            100
            -100
            12345678-1234-5678-1234-567812345678
            1-3/4
            1e-12
            3.14159
            -3/4
            6.02e23
            date_expr = pyparsing_common.iso8601_date.copy()
            date_expr.set_parse_action(pyparsing_common.convert_to_date())
            dt_expr = pyparsing_common.iso8601_datetime.copy()
            dt_expr.set_parse_action(pyparsing_common.convert_to_datetime())
            except ValueError as ve:
            FF
            More info at the pyparsing wiki page
            OneOrMore(
            print(date_expr.parse_string("1999-12-31"))
            print(dt_expr.parse_string("1999-12-31T23:59:59.999"))
            print(table_text.parse_string(text).body)
            table_text = td + SkipTo(td_end).set_parse_action(pyparsing_common.strip_html_tags)("body") + td_end
            td, td_end = make_html_tags("TD")
            text = '<td>More info at the <a href="https://github.com/pyparsing/pyparsing/wiki">pyparsing</a> wiki page</td>'
            try:
        - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%d"``)
        - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%dT%H:%M:%S.%f"``)
        """
        """Helper to create a parse action for converting parsed
        """Parse action to remove HTML tags from web page HTML source
        "full IPv6 address"
        # (?![-_])(?:[-\w\u00a1-\uffff]{0,63}[^-_]\.)+
        # (first & last IP address of each class)
        # any int or real number, returned as float
        # any int or real number, returned as the appropriate type
        # can be replaced by a shortest alternative
        # excludes loopback network 0.0.0.0
        # excludes network & broadcast addresses
        # excludes reserved space >= 224.0.0.0
        # fractions
        # fragment (optional)
        # hex numbers
        # host & domain names, may end with dot
        # https://gist.github.com/dperini/729294
        # https://mathiasbynens.be/demo/url-regex
        # IP address dotted notation octets
        # IP address exclusion
        # mixed fractions
        # port number (optional)
        # private & local networks
        # protocol identifier (optional)
        # query string (optional)
        # resource path (optional)
        # short syntax // still required
        # TLD identifier name, may end with dot
        # user:pass BasicAuth (optional)
        # uuid
        (_full_ipv6_address | _mixed_ipv6_address | _short_ipv6_address).set_name(
        )
        .set_name("commaItem")
        .set_name("fnumber")
        .set_name("real number with scientific notation")
        .set_name("real number")
        .set_name("signed integer")
        .set_parse_action(convert_to_float)
        .set_parse_action(convert_to_integer)
        .streamline()
        [0.5]
        [-0.75]
        [1.75]
        [1]
        [100.0]
        [-100.0]
        [100]
        [-100]
        [1e-12]
        [255]
        [256]
        [3.14159]
        [6.02e+23]
        [UUID('12345678-1234-5678-1234-567812345678')]
        + "/"
        + "::"
        + Opt(_ipv6_part + (":" + _ipv6_part) * (0, 6))
        + signed_integer().set_parse_action(convert_to_float)
        +100
        1
        1/2
        100
        -100
        12345678-1234-5678-1234-567812345678
        1-3/4
        1e-12
        3.14159
        -3/4
        6.02e23
        Combine(
        datetime string to Python datetime.datetime
        def cvt_fn(s, l, t):
        def cvt_fn(ss, ll, tt):
        Example::
        FF
        fraction | signed_integer + Opt(Opt("-").suppress() + fraction)
        Helper to create a parse action for converting parsed date string to Python datetime.date
        import uuid
        lambda t: sum(1 for tt in t if pyparsing_common._ipv6_part.matches(tt)) < 8
        Opt(_ipv6_part + (":" + _ipv6_part) * (0, 6))
        Opt(quoted_string.copy() | _commasepitem, default="")
        Params -
        Prints::
        prints::
        pyparsing_common.fnumber.run_tests('''
        pyparsing_common.fraction.run_tests('''
        pyparsing_common.hex_integer.run_tests('''
        pyparsing_common.mixed_integer.run_tests('''
        pyparsing_common.number.run_tests('''
        pyparsing_common.uuid.run_tests('''
        pyparsing_common.uuid.set_parse_action(token_map(uuid.UUID))
        r"(#(?P<fragment>\S*))?" +
        r"(:(?P<port>\d{2,5}))?" +
        r"(?!(?:10|127)(?:\.\d{1,3}){3})" +
        r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})" +
        r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})" +
        r"(?:" +
        r"(?:(?:(?P<scheme>https?|ftp):)?\/\/)" +
        r"(?:(?P<auth>\S+(?::\S*)?)@)?" +
        r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])" +
        r"(?:[a-z\u00a1-\uffff]{2,}\.?)" +
        r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))" +
        r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}" +
        r"(?P<host>" +
        r"(?P<path>\/[^?# ]*)?" +
        r"(?P<url>" +
        r"(?P<year>\d{4})(?:-(?P<month>\d\d)(?:-(?P<day>\d\d))?)?"
        r"(?P<year>\d{4})-(?P<month>\d\d)-(?P<day>\d\d)[T ](?P<hour>\d\d):(?P<minute>\d\d)(:(?P<second>\d\d(\.\d*)?)?)?(?P<tz>Z|[+-]\d\d:?\d\d)?"
        r"(\?(?P<query>[^#]*))?" +
        r"(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}"
        r")"
        r")" +
        r")?" +
        r")+" +
        r"[0-9a-fA-F]{2}([:.-])[0-9a-fA-F]{2}(?:\1[0-9a-fA-F]{2}){4}"
        r"[a-z0-9\u00a1-\uffff]" +
        r"[a-z0-9\u00a1-\uffff]\." +
        r"[a-z0-9\u00a1-\uffff_-]{0,62}" +
        r"|" +
        Regex(r"[+-]?(?:\d+(?:[eE][+-]?\d+)|(?:\d+\.\d*|\.\d+)(?:[eE][+-]?\d+)?)")
        Regex(r"[+-]?(?:\d+\.\d*|\.\d+)")
        Regex(r"[+-]?\d+")
        Regex(r"[+-]?\d+\.?\d*([eE][+-]?\d+)?")
        return cvt_fn
        return pyparsing_common._html_stripper.transform_string(tokens[0])
        signed_integer().set_parse_action(convert_to_float)
        Word(hexnums).set_name("hex integer").set_parse_action(token_map(int, 16))
      :class:`datetime<iso8601_datetime>`
      :class:`IPv4<ipv4_address>`, :class:`IPv6<ipv6_address>`)
      :class:`scientific notation<sci_real>`)
    - :class:`comma-separated list<comma_separated_list>`
    - :class:`convert_to_date`
    - :class:`convert_to_datetime`
    - :class:`convert_to_float`
    - :class:`convert_to_integer`
    - :class:`downcase_tokens`
    - :class:`strip_html_tags`
    - :class:`upcase_tokens`
    - :class:`url`
    - :class:`UUID<uuid>`
    - common :class:`programming identifiers<identifier>`
    - ISO8601 :class:`dates<iso8601_date>` and
    - network addresses (:class:`MAC<mac_address>`,
    - numeric forms (:class:`integers<integer>`, :class:`reals<real>`,
    """
    """any int or real number, returned as float"""
    """any numeric expression, returns the corresponding Python type"""
    """Deprecated - use :class:`convert_to_date`"""
    """Deprecated - use :class:`convert_to_datetime`"""
    """Deprecated - use :class:`convert_to_float`"""
    """Deprecated - use :class:`convert_to_integer`"""
    """Deprecated - use :class:`downcase_tokens`"""
    """Deprecated - use :class:`strip_html_tags`"""
    """Deprecated - use :class:`upcase_tokens`"""
    """expression that parses a floating point number and returns a float"""
    """expression that parses a floating point number with optional
    """expression that parses a hexadecimal integer, returns an int"""
    """expression that parses an integer with optional leading sign, returns an int"""
    """expression that parses an unsigned integer, returns an int"""
    """fractional expression of an integer divided by an integer, returns a float"""
    """Here are some common low-level expressions that may be useful in
    """mixed integer of the form 'integer - fraction', with optional leading integer, returns float"""
    """Parse action to convert tokens to lower case."""
    """Parse action to convert tokens to upper case."""
    """Predefined expression of 1 or more printable words or quoted strings, separated by commas."""
    """typical code identifier (leading alpha or '_', followed by 0 or more alphas, nums, or '_')"""
    """URL (http/https/ftp scheme)"""
    "IPv4 address (``0.0.0.0 - 255.255.255.255``)"
    "IPv6 address (long, short, or mixed form)"
    "ISO8601 date (``yyyy-mm-dd``)"
    "ISO8601 datetime (``yyyy-mm-ddThh:mm:ss.s(Z|+-00:00)``) - trailing seconds, milliseconds, and timezone optional; accepts separating ``'T'`` or ``' '``"
    "MAC address xx:xx:xx:xx:xx (may also have '-' or '.' delimiters)"
    "UUID (``xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx``)"
    # fmt: off
    # fmt: on
    # pre-PEP8 compatibility names
    # streamlining this expression makes the docs nicer-looking
    )
    ).set_name("comma separated list")
    ).set_name("fraction or mixed integer-fraction")
    ).set_name("fraction")
    ).set_name("IPv4 address")
    ).set_name("IPv6 address")
    ).set_name("ISO8601 date")
    ).set_name("ISO8601 datetime")
    ).set_name("MAC address")
    ).set_name("short IPv6 address")
    ).set_name("url")
    @staticmethod
    _commasepitem = (
    _full_ipv6_address = (_ipv6_part + (":" + _ipv6_part) * 7).set_name(
    _html_stripper = any_open_tag.suppress() | any_close_tag.suppress()
    _ipv6_part = Regex(r"[0-9a-fA-F]{1,4}").set_name("hex_integer")
    _mixed_ipv6_address = ("::ffff:" + ipv4_address).set_name("mixed IPv6 address")
    _short_ipv6_address = (
    _short_ipv6_address.add_condition(
    comma_separated_list = DelimitedList(
    convert_to_float = token_map(float)
    convert_to_integer = token_map(int)
    convertToDate = convert_to_date
    convertToDatetime = convert_to_datetime
    convertToFloat = convert_to_float
    convertToInteger = convert_to_integer
    def convert_to_date(fmt: str = "%Y-%m-%d"):
    def convert_to_datetime(fmt: str = "%Y-%m-%dT%H:%M:%S.%f"):
    def strip_html_tags(s: str, l: int, tokens: ParseResults):
    downcase_tokens = staticmethod(token_map(lambda t: t.lower()))
    downcaseTokens = downcase_tokens
    Example::
    fnumber = (
    fraction = (
    fraction.add_parse_action(lambda tt: tt[0] / tt[-1])
    hex_integer = (
    identifier = Word(identchars, identbodychars).set_name("identifier")
    integer = Word(nums).set_name("integer").set_parse_action(convert_to_integer)
    ipv4_address = Regex(
    ipv6_address = Combine(
    iso8601_date = Regex(
    iso8601_datetime = Regex(
    jump-starting parser development:
    mac_address = Regex(
    mixed_integer = (
    mixed_integer.add_parse_action(sum)
    number = (sci_real | real | signed_integer).setName("number").streamline()
    Parse action for converting parsed integers to Python int
    Parse action for converting parsed numbers to Python float
    Parse actions:
    prints::
    real = (
    sci_real = (
    scientific notation and returns a float"""
    signed_integer = (
    stripHTMLTags = strip_html_tags
    upcase_tokens = staticmethod(token_map(lambda t: t.upper()))
    upcaseTokens = upcase_tokens
    url = Regex(
    uuid = Regex(r"[0-9a-fA-F]{8}(-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}").set_name("UUID")
    v for v in vars(pyparsing_common).values() if isinstance(v, ParserElement)
# common.py
# some other useful expressions - using lower-case class name since we are really using this as a namespace
]
_builtin_exprs = [
class pyparsing_common:
from .core import *
from .helpers import DelimitedList, any_open_tag, any_close_tag
from datetime import datetime
