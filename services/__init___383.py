
                    continue
                    data[code] = [zone]
                    data[code].append(zone)
                _tzinfo_cache[zone] = build_tzinfo(zone, fp)
                code, coordinates, zone = line.split(None, 4)[:3]
                code, name = line.split(None, 1)
                data[code] = name.strip()
                except KeyError:
                fp.close()
                from pkg_resources import resource_stream
                if line.startswith("#"):
                if zone not in all_timezones_set:  # noqa
                line = line.decode("UTF-8")
                resource_stream = None
                return resource_stream(__name__, "zoneinfo/" + name)
                try:
            # all the listed timezones are present. As an
            # for the presence of the resource file on disk.
            # http://bugs.launchpad.net/bugs/383171 - we avoid using this
            # import-speed optimization, you can set the
            # In "standard" distributions, we can assume that
            # pkg_resources is installed.
            # PYTZ_SKIPEXISTSCHECK flag to skip checking
            # unless absolutely necessary to help when a broken version of
            ...
            except ImportError:
            finally:
            for line in zone_tab.readlines():
            for line in zone_tab:
            fp = open_resource(zone)
            if resource_stream is not None:
            raise UnknownTimeZoneError(zone)
            raise ValueError("absolute offset is too large", minutes)
            raise ValueError("Bad path segment: %r" % part)
            raise ValueError("Naive time - no tzinfo set")
            raise ValueError("Not naive datetime (tzinfo is already set)")
            return dt
            return self.localize(dt)
            return True
            s = s.decode("ASCII")
            s.encode("ASCII")  # Raise an exception if not ASCII
            self.data = data
            try:
            tz.lower(): tz for tz in _all_timezones_unchecked
            zone_tab.close()
        """
        """Backwards compatibility."""
        """Convert naive time to local time"""
        """Correct the timezone information on the given datetime"""
        # All valid timezones are ASCII
        # only one
        # Use setdefault to avoid a race condition and make sure we have
        # We haven't seen this one before. we need to save it.
        ...
        _all_timezones_lower_to_standard = {
        }  # noqa
        >>> ascii('\N{TRADE MARK SIGN}') #doctest: +IGNORE_EXCEPTION_DETAIL
        >>> ascii('Hello')
        >>> ascii(u'\N{TRADE MARK SIGN}') #doctest: +IGNORE_EXCEPTION_DETAIL
        >>> ascii(u'Hello')
        >>> FixedOffset(0) is UTC
        >>> FixedOffset(1380) is two
        >>> FixedOffset(1440)
        >>> FixedOffset(-1440)
        >>> FixedOffset(-330) is one
        >>> import pickle
        >>> one
        >>> one = FixedOffset(-330)
        >>> pickle.loads(pickle.dumps(one)) is one
        >>> pickle.loads(pickle.dumps(two)) is two
        >>> str(one.dst(datetime.datetime.now()))
        >>> str(one.utcoffset(datetime.datetime.now()))
        >>> str(two.dst(datetime.datetime.now()))
        >>> str(two.utcoffset(datetime.datetime.now()))
        >>> two
        >>> two = FixedOffset(1380)
        '0:00:00'
        '-1 day, 18:30:00'
        '23:00:00'
        data = {}
        else:
        filename = os.path.join(os.path.dirname(__file__), "zoneinfo", *name_parts)
        filename = os.path.join(zoneinfo_dir, *name_parts)
        finally:
        'Hello'
        if abs(minutes) >= 1440:
        if dt.tzinfo is None:
        if dt.tzinfo is not None:
        if dt.tzinfo is self:
        if not os.path.exists(filename):
        if os.environ.get("PYTZ_SKIPEXISTSCHECK", ""):
        if part == os.path.pardir or os.sep in part:
        if type(s) == bytes:
        if zone in all_timezones_set:  # noqa
        info = _tzinfos.setdefault(offset, _FixedOffset(offset))
        open_resource(name).close()
        pytz.FixedOffset(1380)
        pytz.FixedOffset(-330)
        r"""
        raise UnknownTimeZoneError(None)
        raise UnknownTimeZoneError(zone)
        return "<UTC>"
        return "pytz.FixedOffset(%d)" % self._minutes
        return "UTC"
        return _UTC, ()
        return dt.astimezone(self)
        return dt.replace(tzinfo=self)
        return False
        return FixedOffset, (self._minutes,)
        return None
        return s  # But the string - not a byte string.
        return s.encode("ASCII")
        return self._offset
        return self[iso3166_code]
        return super(utc.__class__, self).fromutc(dt)
        return True
        return UTC
        return utc
        return ZERO
        self._minutes = minutes
        self._offset = datetime.timedelta(minutes=minutes)
        Traceback (most recent call last):
        True
        try:
        UnicodeEncodeError: ...
        ValueError: ('absolute offset is too large', 1440)
        ValueError: ('absolute offset is too large', -1440)
        zone = ascii(zone)
        zone_tab = open_resource("iso3166.tab")
        zone_tab = open_resource("zone.tab")
    """
    """case-insensitively matching timezone, else return zone unchanged"""
    """Dictionary proving ISO3166 code -> English name.
    """Factory function for unpickling pytz tzinfo instances.
    """Factory function for utc unpickling.
    """Map ISO 3166 country code to a list of timezone names commonly used
    """Open a resource from the zoneinfo subdir for reading.
    """return a fixed-offset timezone based off a number of minutes.
    """Return true if the given resource exists"""
    """Undo the time zone name munging done by older versions of pytz."""
    """UTC
    "Africa/Abidjan",
    "Africa/Accra",
    "Africa/Addis_Ababa",
    "Africa/Algiers",
    "Africa/Asmara",
    "Africa/Asmera",
    "Africa/Bamako",
    "Africa/Bangui",
    "Africa/Banjul",
    "Africa/Bissau",
    "Africa/Blantyre",
    "Africa/Brazzaville",
    "Africa/Bujumbura",
    "Africa/Cairo",
    "Africa/Casablanca",
    "Africa/Ceuta",
    "Africa/Conakry",
    "Africa/Dakar",
    "Africa/Dar_es_Salaam",
    "Africa/Djibouti",
    "Africa/Douala",
    "Africa/El_Aaiun",
    "Africa/Freetown",
    "Africa/Gaborone",
    "Africa/Harare",
    "Africa/Johannesburg",
    "Africa/Juba",
    "Africa/Kampala",
    "Africa/Khartoum",
    "Africa/Kigali",
    "Africa/Kinshasa",
    "Africa/Lagos",
    "Africa/Libreville",
    "Africa/Lome",
    "Africa/Luanda",
    "Africa/Lubumbashi",
    "Africa/Lusaka",
    "Africa/Malabo",
    "Africa/Maputo",
    "Africa/Maseru",
    "Africa/Mbabane",
    "Africa/Mogadishu",
    "Africa/Monrovia",
    "Africa/Nairobi",
    "Africa/Ndjamena",
    "Africa/Niamey",
    "Africa/Nouakchott",
    "Africa/Ouagadougou",
    "Africa/Porto-Novo",
    "Africa/Sao_Tome",
    "Africa/Timbuktu",
    "Africa/Tripoli",
    "Africa/Tunis",
    "Africa/Windhoek",
    "all_timezones",
    "all_timezones_set",
    "AmbiguousTimeError",
    "America/Adak",
    "America/Anchorage",
    "America/Anguilla",
    "America/Antigua",
    "America/Araguaina",
    "America/Argentina/Buenos_Aires",
    "America/Argentina/Catamarca",
    "America/Argentina/ComodRivadavia",
    "America/Argentina/Cordoba",
    "America/Argentina/Jujuy",
    "America/Argentina/La_Rioja",
    "America/Argentina/Mendoza",
    "America/Argentina/Rio_Gallegos",
    "America/Argentina/Salta",
    "America/Argentina/San_Juan",
    "America/Argentina/San_Luis",
    "America/Argentina/Tucuman",
    "America/Argentina/Ushuaia",
    "America/Aruba",
    "America/Asuncion",
    "America/Atikokan",
    "America/Atka",
    "America/Bahia",
    "America/Bahia_Banderas",
    "America/Barbados",
    "America/Belem",
    "America/Belize",
    "America/Blanc-Sablon",
    "America/Boa_Vista",
    "America/Bogota",
    "America/Boise",
    "America/Buenos_Aires",
    "America/Cambridge_Bay",
    "America/Campo_Grande",
    "America/Cancun",
    "America/Caracas",
    "America/Catamarca",
    "America/Cayenne",
    "America/Cayman",
    "America/Chicago",
    "America/Chihuahua",
    "America/Ciudad_Juarez",
    "America/Coral_Harbour",
    "America/Cordoba",
    "America/Costa_Rica",
    "America/Coyhaique",
    "America/Creston",
    "America/Cuiaba",
    "America/Curacao",
    "America/Danmarkshavn",
    "America/Dawson",
    "America/Dawson_Creek",
    "America/Denver",
    "America/Detroit",
    "America/Dominica",
    "America/Edmonton",
    "America/Eirunepe",
    "America/El_Salvador",
    "America/Ensenada",
    "America/Fort_Nelson",
    "America/Fort_Wayne",
    "America/Fortaleza",
    "America/Glace_Bay",
    "America/Godthab",
    "America/Goose_Bay",
    "America/Grand_Turk",
    "America/Grenada",
    "America/Guadeloupe",
    "America/Guatemala",
    "America/Guayaquil",
    "America/Guyana",
    "America/Halifax",
    "America/Havana",
    "America/Hermosillo",
    "America/Indiana/Indianapolis",
    "America/Indiana/Knox",
    "America/Indiana/Marengo",
    "America/Indiana/Petersburg",
    "America/Indiana/Tell_City",
    "America/Indiana/Vevay",
    "America/Indiana/Vincennes",
    "America/Indiana/Winamac",
    "America/Indianapolis",
    "America/Inuvik",
    "America/Iqaluit",
    "America/Jamaica",
    "America/Jujuy",
    "America/Juneau",
    "America/Kentucky/Louisville",
    "America/Kentucky/Monticello",
    "America/Knox_IN",
    "America/Kralendijk",
    "America/La_Paz",
    "America/Lima",
    "America/Los_Angeles",
    "America/Louisville",
    "America/Lower_Princes",
    "America/Maceio",
    "America/Managua",
    "America/Manaus",
    "America/Marigot",
    "America/Martinique",
    "America/Matamoros",
    "America/Mazatlan",
    "America/Mendoza",
    "America/Menominee",
    "America/Merida",
    "America/Metlakatla",
    "America/Mexico_City",
    "America/Miquelon",
    "America/Moncton",
    "America/Monterrey",
    "America/Montevideo",
    "America/Montreal",
    "America/Montserrat",
    "America/Nassau",
    "America/New_York",
    "America/Nipigon",
    "America/Nome",
    "America/Noronha",
    "America/North_Dakota/Beulah",
    "America/North_Dakota/Center",
    "America/North_Dakota/New_Salem",
    "America/Nuuk",
    "America/Ojinaga",
    "America/Panama",
    "America/Pangnirtung",
    "America/Paramaribo",
    "America/Phoenix",
    "America/Port_of_Spain",
    "America/Port-au-Prince",
    "America/Porto_Acre",
    "America/Porto_Velho",
    "America/Puerto_Rico",
    "America/Punta_Arenas",
    "America/Rainy_River",
    "America/Rankin_Inlet",
    "America/Recife",
    "America/Regina",
    "America/Resolute",
    "America/Rio_Branco",
    "America/Rosario",
    "America/Santa_Isabel",
    "America/Santarem",
    "America/Santiago",
    "America/Santo_Domingo",
    "America/Sao_Paulo",
    "America/Scoresbysund",
    "America/Shiprock",
    "America/Sitka",
    "America/St_Barthelemy",
    "America/St_Johns",
    "America/St_Kitts",
    "America/St_Lucia",
    "America/St_Thomas",
    "America/St_Vincent",
    "America/Swift_Current",
    "America/Tegucigalpa",
    "America/Thule",
    "America/Thunder_Bay",
    "America/Tijuana",
    "America/Toronto",
    "America/Tortola",
    "America/Vancouver",
    "America/Virgin",
    "America/Whitehorse",
    "America/Winnipeg",
    "America/Yakutat",
    "America/Yellowknife",
    "Antarctica/Casey",
    "Antarctica/Davis",
    "Antarctica/DumontDUrville",
    "Antarctica/Macquarie",
    "Antarctica/Mawson",
    "Antarctica/McMurdo",
    "Antarctica/Palmer",
    "Antarctica/Rothera",
    "Antarctica/South_Pole",
    "Antarctica/Syowa",
    "Antarctica/Troll",
    "Antarctica/Vostok",
    "Arctic/Longyearbyen",
    "Asia/Aden",
    "Asia/Almaty",
    "Asia/Amman",
    "Asia/Anadyr",
    "Asia/Aqtau",
    "Asia/Aqtobe",
    "Asia/Ashgabat",
    "Asia/Ashkhabad",
    "Asia/Atyrau",
    "Asia/Baghdad",
    "Asia/Bahrain",
    "Asia/Baku",
    "Asia/Bangkok",
    "Asia/Barnaul",
    "Asia/Beirut",
    "Asia/Bishkek",
    "Asia/Brunei",
    "Asia/Calcutta",
    "Asia/Chita",
    "Asia/Choibalsan",
    "Asia/Chongqing",
    "Asia/Chungking",
    "Asia/Colombo",
    "Asia/Dacca",
    "Asia/Damascus",
    "Asia/Dhaka",
    "Asia/Dili",
    "Asia/Dubai",
    "Asia/Dushanbe",
    "Asia/Famagusta",
    "Asia/Gaza",
    "Asia/Harbin",
    "Asia/Hebron",
    "Asia/Ho_Chi_Minh",
    "Asia/Hong_Kong",
    "Asia/Hovd",
    "Asia/Irkutsk",
    "Asia/Istanbul",
    "Asia/Jakarta",
    "Asia/Jayapura",
    "Asia/Jerusalem",
    "Asia/Kabul",
    "Asia/Kamchatka",
    "Asia/Karachi",
    "Asia/Kashgar",
    "Asia/Kathmandu",
    "Asia/Katmandu",
    "Asia/Khandyga",
    "Asia/Kolkata",
    "Asia/Krasnoyarsk",
    "Asia/Kuala_Lumpur",
    "Asia/Kuching",
    "Asia/Kuwait",
    "Asia/Macao",
    "Asia/Macau",
    "Asia/Magadan",
    "Asia/Makassar",
    "Asia/Manila",
    "Asia/Muscat",
    "Asia/Nicosia",
    "Asia/Novokuznetsk",
    "Asia/Novosibirsk",
    "Asia/Omsk",
    "Asia/Oral",
    "Asia/Phnom_Penh",
    "Asia/Pontianak",
    "Asia/Pyongyang",
    "Asia/Qatar",
    "Asia/Qostanay",
    "Asia/Qyzylorda",
    "Asia/Rangoon",
    "Asia/Riyadh",
    "Asia/Saigon",
    "Asia/Sakhalin",
    "Asia/Samarkand",
    "Asia/Seoul",
    "Asia/Shanghai",
    "Asia/Singapore",
    "Asia/Srednekolymsk",
    "Asia/Taipei",
    "Asia/Tashkent",
    "Asia/Tbilisi",
    "Asia/Tehran",
    "Asia/Tel_Aviv",
    "Asia/Thimbu",
    "Asia/Thimphu",
    "Asia/Tokyo",
    "Asia/Tomsk",
    "Asia/Ujung_Pandang",
    "Asia/Ulaanbaatar",
    "Asia/Ulan_Bator",
    "Asia/Urumqi",
    "Asia/Ust-Nera",
    "Asia/Vientiane",
    "Asia/Vladivostok",
    "Asia/Yakutsk",
    "Asia/Yangon",
    "Asia/Yekaterinburg",
    "Asia/Yerevan",
    "Atlantic/Azores",
    "Atlantic/Bermuda",
    "Atlantic/Canary",
    "Atlantic/Cape_Verde",
    "Atlantic/Faeroe",
    "Atlantic/Faroe",
    "Atlantic/Jan_Mayen",
    "Atlantic/Madeira",
    "Atlantic/Reykjavik",
    "Atlantic/South_Georgia",
    "Atlantic/St_Helena",
    "Atlantic/Stanley",
    "Australia/ACT",
    "Australia/Adelaide",
    "Australia/Brisbane",
    "Australia/Broken_Hill",
    "Australia/Canberra",
    "Australia/Currie",
    "Australia/Darwin",
    "Australia/Eucla",
    "Australia/Hobart",
    "Australia/LHI",
    "Australia/Lindeman",
    "Australia/Lord_Howe",
    "Australia/Melbourne",
    "Australia/North",
    "Australia/NSW",
    "Australia/Perth",
    "Australia/Queensland",
    "Australia/South",
    "Australia/Sydney",
    "Australia/Tasmania",
    "Australia/Victoria",
    "Australia/West",
    "Australia/Yancowinna",
    "BaseTzInfo",
    "Brazil/Acre",
    "Brazil/DeNoronha",
    "Brazil/East",
    "Brazil/West",
    "Canada/Atlantic",
    "Canada/Central",
    "Canada/Eastern",
    "Canada/Mountain",
    "Canada/Newfoundland",
    "Canada/Pacific",
    "Canada/Saskatchewan",
    "Canada/Yukon",
    "CET",
    "Chile/Continental",
    "Chile/EasterIsland",
    "common_timezones",
    "common_timezones_set",
    "country_names",
    "country_timezones",
    "CST6CDT",
    "Cuba",
    "EET",
    "Egypt",
    "Eire",
    "EST",
    "EST5EDT",
    "Etc/GMT",
    "Etc/GMT+0",
    "Etc/GMT+1",
    "Etc/GMT+10",
    "Etc/GMT+11",
    "Etc/GMT+12",
    "Etc/GMT+2",
    "Etc/GMT+3",
    "Etc/GMT+4",
    "Etc/GMT+5",
    "Etc/GMT+6",
    "Etc/GMT+7",
    "Etc/GMT+8",
    "Etc/GMT+9",
    "Etc/GMT0",
    "Etc/GMT-0",
    "Etc/GMT-1",
    "Etc/GMT-10",
    "Etc/GMT-11",
    "Etc/GMT-12",
    "Etc/GMT-13",
    "Etc/GMT-14",
    "Etc/GMT-2",
    "Etc/GMT-3",
    "Etc/GMT-4",
    "Etc/GMT-5",
    "Etc/GMT-6",
    "Etc/GMT-7",
    "Etc/GMT-8",
    "Etc/GMT-9",
    "Etc/Greenwich",
    "Etc/UCT",
    "Etc/Universal",
    "Etc/UTC",
    "Etc/Zulu",
    "Europe/Amsterdam",
    "Europe/Andorra",
    "Europe/Astrakhan",
    "Europe/Athens",
    "Europe/Belfast",
    "Europe/Belgrade",
    "Europe/Berlin",
    "Europe/Bratislava",
    "Europe/Brussels",
    "Europe/Bucharest",
    "Europe/Budapest",
    "Europe/Busingen",
    "Europe/Chisinau",
    "Europe/Copenhagen",
    "Europe/Dublin",
    "Europe/Gibraltar",
    "Europe/Guernsey",
    "Europe/Helsinki",
    "Europe/Isle_of_Man",
    "Europe/Istanbul",
    "Europe/Jersey",
    "Europe/Kaliningrad",
    "Europe/Kiev",
    "Europe/Kirov",
    "Europe/Kyiv",
    "Europe/Lisbon",
    "Europe/Ljubljana",
    "Europe/London",
    "Europe/Luxembourg",
    "Europe/Madrid",
    "Europe/Malta",
    "Europe/Mariehamn",
    "Europe/Minsk",
    "Europe/Monaco",
    "Europe/Moscow",
    "Europe/Nicosia",
    "Europe/Oslo",
    "Europe/Paris",
    "Europe/Podgorica",
    "Europe/Prague",
    "Europe/Riga",
    "Europe/Rome",
    "Europe/Samara",
    "Europe/San_Marino",
    "Europe/Sarajevo",
    "Europe/Saratov",
    "Europe/Simferopol",
    "Europe/Skopje",
    "Europe/Sofia",
    "Europe/Stockholm",
    "Europe/Tallinn",
    "Europe/Tirane",
    "Europe/Tiraspol",
    "Europe/Ulyanovsk",
    "Europe/Uzhgorod",
    "Europe/Vaduz",
    "Europe/Vatican",
    "Europe/Vienna",
    "Europe/Vilnius",
    "Europe/Volgograd",
    "Europe/Warsaw",
    "Europe/Zagreb",
    "Europe/Zaporozhye",
    "Europe/Zurich",
    "FixedOffset",
    "GB",
    "GB-Eire",
    "GMT",
    "GMT+0",
    "GMT0",
    "GMT-0",
    "Greenwich",
    "Hongkong",
    "HST",
    "Iceland",
    "Indian/Antananarivo",
    "Indian/Chagos",
    "Indian/Christmas",
    "Indian/Cocos",
    "Indian/Comoro",
    "Indian/Kerguelen",
    "Indian/Mahe",
    "Indian/Maldives",
    "Indian/Mauritius",
    "Indian/Mayotte",
    "Indian/Reunion",
    "InvalidTimeError",
    "Iran",
    "Israel",
    "Jamaica",
    "Japan",
    "Kwajalein",
    "Libya",
    "MET",
    "Mexico/BajaNorte",
    "Mexico/BajaSur",
    "Mexico/General",
    "MST",
    "MST7MDT",
    "Navajo",
    "NonExistentTimeError",
    "NZ",
    "NZ-CHAT",
    "Pacific/Apia",
    "Pacific/Auckland",
    "Pacific/Bougainville",
    "Pacific/Chatham",
    "Pacific/Chuuk",
    "Pacific/Easter",
    "Pacific/Efate",
    "Pacific/Enderbury",
    "Pacific/Fakaofo",
    "Pacific/Fiji",
    "Pacific/Funafuti",
    "Pacific/Galapagos",
    "Pacific/Gambier",
    "Pacific/Guadalcanal",
    "Pacific/Guam",
    "Pacific/Honolulu",
    "Pacific/Johnston",
    "Pacific/Kanton",
    "Pacific/Kiritimati",
    "Pacific/Kosrae",
    "Pacific/Kwajalein",
    "Pacific/Majuro",
    "Pacific/Marquesas",
    "Pacific/Midway",
    "Pacific/Nauru",
    "Pacific/Niue",
    "Pacific/Norfolk",
    "Pacific/Noumea",
    "Pacific/Pago_Pago",
    "Pacific/Palau",
    "Pacific/Pitcairn",
    "Pacific/Pohnpei",
    "Pacific/Ponape",
    "Pacific/Port_Moresby",
    "Pacific/Rarotonga",
    "Pacific/Saipan",
    "Pacific/Samoa",
    "Pacific/Tahiti",
    "Pacific/Tarawa",
    "Pacific/Tongatapu",
    "Pacific/Truk",
    "Pacific/Wake",
    "Pacific/Wallis",
    "Pacific/Yap",
    "Poland",
    "Portugal",
    "PRC",
    "PST8PDT",
    "ROC",
    "ROK",
    "Singapore",
    "timezone",
    "Turkey",
    "UCT",
    "Universal",
    "UnknownTimeZoneError",
    "US/Alaska",
    "US/Aleutian",
    "US/Arizona",
    "US/Central",
    "US/Eastern",
    "US/East-Indiana",
    "US/Hawaii",
    "US/Indiana-Starke",
    "US/Michigan",
    "US/Mountain",
    "US/Pacific",
    "US/Samoa",
    "UTC",
    "utc",
    "UTC",
    "WET",
    "W-SU",
    "Zulu",
    # for Python 2.3 and Python 3.x a pain.
    # Python 3.x doesn't have unicode(), making writing code
    ...
    ...         print(s)
    ...     for s in list_of_strings:
    ...     print('Unknown')
    ...     timezone('Asia/Shangri-La')
    ...     timezone(unicode('\N{TRADE MARK SIGN}'))
    ...     'We use a helper so doctests work under Python 2.3 -> 3.x'
    ... except UnknownTimeZoneError:
    _dst = ZERO
    _test()
    _tzname = zone
    _utcoffset = ZERO
    >>> (loc_dt - timedelta(minutes=10)).strftime(fmt)
    >>> (loc_dt + timedelta(minutes=10)).strftime(fmt)
    >>> def print_list(list_of_strings):
    >>> dt = datetime.datetime(2005, 3, 1, 14, 13, 21, tzinfo=utc)
    >>> eastern = timezone('US/Eastern')
    >>> eastern.normalize(loc_dt - timedelta(minutes=10)).strftime(fmt)
    >>> eastern.zone
    >>> fmt = '%Y-%m-%d %H:%M:%S %Z (%z)'
    >>> from datetime import datetime, timedelta
    >>> import datetime, pickle
    >>> len(p) - len(naive_p)
    >>> loc_dt = utc_dt.astimezone(eastern)
    >>> loc_dt.strftime(fmt)
    >>> naive = dt.replace(tzinfo=None)
    >>> naive_p = pickle.dumps(naive, 1)
    >>> new = pickle.loads(p)
    >>> new == dt
    >>> new is dt
    >>> new.tzinfo is dt.tzinfo
    >>> p = pickle.dumps(dt, 1)
    >>> print(country_names['au'])
    >>> print_list(country_timezones('nz'))
    >>> print_list(country_timezones['ch'])
    >>> print_list(country_timezones['CH'])
    >>> print_list(country_timezones['nz'])
    >>> print_list(country_timezones[unicode('ch')])
    >>> print_list(country_timezones['XXX'])
    >>> timezone(unicode('US/Eastern')) is eastern
    >>> try:
    >>> utc = timezone('UTC')
    >>> utc is timezone('GMT')
    >>> utc is UTC is timezone('UTC')
    >>> utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
    17
    '2002-10-27 00:50:00 EST (-0500)'
    '2002-10-27 01:00:00 EST (-0500)'
    '2002-10-27 01:10:00 EST (-0500)'
    '2002-10-27 01:50:00 EDT (-0400)'
    An offset of 0 is special-cased to return UTC.
    Australia
    by shortening the path.
    def __call__(self, iso3166_code):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, minutes):
    def __reduce__(self):
    def __repr__(self):
    def __str__(self):
    def _fill(self):
    def ascii(s):
    def dst(self, dt):
    def fromutc(self, dt):
    def localize(self, dt, is_dst=False):
    def normalize(self, dt, is_dst=False):
    def tzname(self, dt):
    def utcoffset(self, dt):
    dictionary. This is still supported::
    else:
    Europe/Zurich
    except OSError:
    except UnicodeEncodeError:
    False
    for part in name_parts:
    found at the calculated location.
    ftp://elsie.nci.nih.gov/pub/tz*.tar.gz
    global _all_timezones_lower_to_standard
    if _all_timezones_lower_to_standard is None:
    if info is None:
    if offset == 0:
    if zone is None:
    if zone not in _tzinfo_cache:
    if zone.upper() == "UTC":
    if zoneinfo_dir is not None:
    import doctest
    import pytz
    in that country.
    info = _tzinfos.get(offset)
    instance defined beneath this class declaration.
    iso3166_code is the two letter code used to identify the country.
    It is possible to specify different location for zoneinfo
    It should also be true for pickling.
    Just a wrapper around tzinfo.unpickler to save a few bytes in each pickle
    KeyError: 'XXX'
    Makes sure that unpickling a utc instance always returns the same
    module global.
    name_parts = name.lstrip("/").split("/")
    non-inclusive.
    Optimized UTC implementation. It unpickles using the single module global
    Pacific/Auckland
    Pacific/Chatham
    Previously, this information was exposed as a function rather than a
    r"""Return a datetime.tzinfo implementation for the given timezone
    Raises UnknownTimeZoneError if passed an unknown zone.
    return _all_timezones_lower_to_standard.get(zone.lower()) or zone  # noqa
    return _tzinfo_cache[zone]
    return doctest.testmod(pytz)
    return info
    return open(filename, "rb")
    return unpickler(*args)
    return utc
    return zone.replace("_plus_", "+").replace("_minus_", "-")
    subdir by using the PYTZ_TZDATADIR environment variable.
    sys.path.insert(0, os.pardir)
    The datetime.timedelta must be between the range of -1 and 1 day,
    the README.rst examples with the unit tests is not trivial.
    the README.rst, but we are not depending on Python 2.4 so integrating
    There should always be only one instance of a FixedOffset per timedelta.
    These examples belong in the UTC class above, but it is obscured; or in
    This should be true for multiple creation calls.
    Traceback (most recent call last):
    True
    try:
    unicode = str
    Unknown
    'US/Eastern'
    Uses the pkg_resources module if available and no standard file
    zone = "UTC"
    zone = _case_insensitive_zone_lookup(_unmunge_zone(zone))
    zone = None  # to match the standard pytz API
    zoneinfo_dir = os.environ.get("PYTZ_TZDATADIR", None)
"""
# The IANA (nee Olson) database is updated several times a year.
# Time-zone info based solely on fixed offsets
]
__all__ = [
__version__ = VERSION
_all_timezones_lower_to_standard = None
_all_timezones_unchecked = [
_p.__safe_for_unpickling__ = True
_tzinfo_cache = {}
_UTC.__safe_for_unpickling__ = True
all_timezones = LazyList(tz for tz in _all_timezones_unchecked if resource_exists(tz))
all_timezones_set = LazySet(all_timezones)
class _CountryNameDict:
class _CountryTimezoneDict:
class _FixedOffset:
class UTC:
common_timezones = [
common_timezones = LazyList(tz for tz in common_timezones if tz in all_timezones)
common_timezones_set = LazySet(common_timezones)
country_names = _CountryNameDict()
country_timezones = _CountryTimezoneDict()
datetime.tzinfo timezone definitions generated from the
def _case_insensitive_zone_lookup(zone):
def _p(*args):
def _test():
def _unmunge_zone(zone):
def _UTC():
def FixedOffset(offset, _tzinfos={}):
def open_resource(name):
def resource_exists(name):
def timezone(zone):
else:  # Python 2.x
FixedOffset.__safe_for_unpickling__ = True
from pytz.exceptions import AmbiguousTimeError
from pytz.exceptions import InvalidTimeError
from pytz.exceptions import NonExistentTimeError
from pytz.exceptions import UnknownTimeZoneError
from pytz.lazy import LazyDict, LazyList, LazySet  # noqa
from pytz.tzfile import build_tzinfo
from pytz.tzinfo import unpickler, BaseTzInfo
HOUR = datetime.timedelta(hours=1)
if __name__ == "__main__":
if sys.version_info[0] > 2:  # Python 3.x
import datetime
import os.path
import sys
OLSEN_VERSION = OLSON_VERSION  # Old releases had this misspelling
Olson timezone database:
OLSON_VERSION = "2025b"
on how to use these modules.
See the datetime section of the Python Library Reference for information
UTC = utc = UTC()  # UTC is a singleton
VERSION = "2025.2"  # pip compatible version number.
ZERO = datetime.timedelta(0)
