
    -------
    --------
    ----------
        -------
        ----------
                        "Argument 'match_querystring' is deprecated. "
                        "'responses.matchers.query_string_matcher'"
                        "Use 'responses.matchers.query_param_matcher' or "
                        else request_url.startswith(p)
                        if isinstance(p, Pattern)
                        p.match(request_url)
                    " Using the `content_type` kwarg is recommended."
                    """
                    """Since we call 'retries.increment()' by ourselves, we always set "error"
                    "You cannot define both `content_type` and `headers[Content-Type]`."
                    # not all kwargs are required
                    (
                    )
                    ),
                    [(match.method, match.url) for match in not_called]
                    177dd90f18a8f4dc79a7d2049f0a3f4fcc5932a0/requests/adapters.py#L549
                    argument equal to None, thus, MaxRetryError exception will be raised with
                    branch found at:
                    DeprecationWarning,
                    error_msg += f"- {p}\n"
                    for p in self.passthru_prefixes
                    Here we're emulating the `if isinstance(e.reason, ResponseError):`
                    https://github.com/psf/requests/blob/
                    kwargs["cert"] = args[3]
                    kwargs["proxies"] = args[4]
                    kwargs["stream"] = args[0]
                    kwargs["timeout"] = args[1]
                    kwargs["verify"] = args[2]
                    m.method, m.url, match_failed_reasons[i]
                    method=response.request.method,  # type: ignore[misc]
                    pass
                    raise RetryError(e, request=request)
                    request, match.get_response(request)
                    response=response.raw,  # type: ignore[misc]
                    ResponseError as a 'reason'.
                    url=response.url,  # type: ignore[misc]
                "Available matches:\n"
                "Cannot replace Registry, current registry has responses.\n"
                "Connection refused by Responses - the call doesn't "
                "match any registered mock.\n\n"
                "Not all requests have been executed {!r}".format(
                "Request: \n"
                "Run 'responses.registry.reset()' first"
                "stream argument is deprecated. Use stream parameter in request directly",
                # `requests` implementation does it always with kwargs
                # close but return False to mock like is still opened
                # function since we still apply the value on 'responses.mock' object
                # It is fully legit to send positional args from adapter, although,
                # Mock automatically unsets to avoid leakage to another decorated
                # See for more info: https://github.com/getsentry/responses/issues/642
                # set 'assert_all_requests_are_fired' temporarily for a single run.
                # that probably means that the request was sent from the custom adapter
                # type: ignore[arg-type]
                )
                [
                [h for h in r_headers if h and h[0].lower() == "content-type"]
                ]
                _query_string_matcher(urlsplit(self.url).query),
                1
                assert_all_requests_are_fired=assert_all_requests_are_fired,
                auto_calculate_content_length=rsp["auto_calculate_content_length"],
                body=rsp["body"],
                call = Call(request, response)
                callback=callback,
                content_type = "application/json"
                content_type = "text/plain"
                content_type = "text/plain; charset=utf-8"
                content_type=content_type,
                content_type=rsp["content_type"],
                content_type=self.content_type,
                d = "xn--" + d.encode("punycode").decode("ascii")
                data.close()
                DeprecationWarning,
                domains[i] = d
                error_msg += "- {} {} {}\n".format(
                error_msg += "Passthru prefixes:\n"
                except IndexError:
                f"- {request.method} {request_url}\n\n"
                f"Expected URL '{url}' to be called {count} times. Called {call_count} times."
                for call in self.calls
                for p in self.passthru_prefixes:
                function,
                headers=json_module.dumps(self.headers),
                headers=rsp["headers"] if "headers" in rsp else None,
                if call.request.url == _ensure_url_default_path(url)
                if retries.raise_on_status:
                logger.info("request.allowed-passthru", extra={"url": request_url})
                match.calls.add_call(call)
                match_querystring=match_querystring,
                match=match,
                method=method,
                method=rsp["method"],
                raise
                raise RuntimeError(
                registry=registry,
                response = adapter.build_response(  # type: ignore[assignment]
                responses._set_registry(registry)
                retries = retries.increment(
                return await func(*args, **kwargs)
                return False
                return False, reason
                return func(*args, **kwargs)
                return response
                return self._on_request(adapter, request, retries=retries, **kwargs)
                return self._real_send(adapter, request, **kwargs)  # type: ignore
                self,
                self._calls.add_call(call)
                status=rsp["status"],
                status=self.status,
                try:
                url = _clean_unicode(url)
                url=rsp["url"],
                url=self.url,
                url=url,
                values = values[0]  # type: ignore[assignment]
                warn(
            "<Response(url='{url}' status={status} "
            "content_type" in kwargs
            "content_type='{content_type}' headers='{headers}')>".format(
            # another decorated function
            # fresh patcher on self.start()
            # if there is more bytes to read then keep open, but return pointer
            # once patcher is stopped, clean it. This is required to create a new
            # only if file really closed (by us) return True
            # prevent stopping unstarted patchers
            # the old default from <= 0.9.0
            # this prevents issues when one decorated function is called from
            # type: ignore[misc]
            # we must not override value of the _patcher if already applied
            (list) list with reasons why other matches don't match
            (Response) found match. If multiple found, then remove & return the first match.
            )
            ):
            **kwargs: Any,
            *args: Any,
            [
            ["PreparedRequest"],
            ]
            adapter: "HTTPAdapter",
            and "Content-Length" not in headers
            and "headers" in kwargs
            and isinstance(body, BytesIO)
            and kwargs["headers"] is not None
            assert isinstance(method_or_response, str)
            assert not body
            assert url is not None
            body = json_module.dumps(json)
            bool,
            CallbackResponse(
            chars[i] = quote(x)
            Class reference of the registry that should be set, eg OrderedRegistry
            content_length = len(body.getvalue())
            Current registry instance with responses.
            data = yaml.safe_load(file)
            data.seek(-1, 1)
            DeprecationWarning,
            else:
            err_msg = (
            error_msg = (
            except BaseException as response:
            except MaxRetryError as e:
            f"{name} is deprecated. Please use 'responses.mock.{name}",
            for i, m in enumerate(self.registered()):
            has_content_type = any(
            has_content_type = True
            header_keys = [header.lower() for header in kwargs["headers"]]
            headers.extend(self.headers)
            headers.pop("Content-Type", None)
            headers["Content-Length"] = str(content_length)
            headers["Content-Type"] = self.content_type
            HTTPAdapter,
            if "content-type" in header_keys:
            if _has_unicode(d):
            if _has_unicode(url):
            if any(
            if args:
            if content_type is _UNSET:
            if isinstance(body, str) and _has_unicode(body):
            if len(values) == 1:
            if not data.closed:
            if not isinstance(match_querystring_argument, FalseBool):
            if not valid:
            if registry is not None:
            if self.passthru_prefixes:
            kwargs.setdefault("headers", adding_headers)
            logger.info("request.passthrough-response", extra={"url": request_url})
            match = tuple(match) + (
            method=response.request.method, status_code=response.status_code
            not self.headers or "Content-Type" not in self.headers
            Optional[Mapping[str, str]],
            params[key] = values
            prefix = _clean_unicode(prefix)
            PreparedRequest,
            raise AssertionError(
            raise AttributeError(err_msg)
            raise body
            raise response
            raise result
            raise self.body
            Reference URL or Pattern to compare.
            request.path_url)  # type: ignore[attr-defined]
            request: "PreparedRequest",
            response = BaseResponse(method=method_or_response, url=url)
            response = ConnectionError(error_msg)
            response = method_or_response
            response = resp_callback(response)  # type: ignore[misc]
            response = Response(method=method_or_response, url=url, body=body, **kwargs)
            response = self._real_send(adapter, request, **kwargs)  # type: ignore
            response.request = request
            return
            return _get_url_and_path(url) == _get_url_and_path(other)
            return body
            return body.read()
            return False
            return False, "Method does not match"
            return False, "URL does not match"
            return False, reason
            return get_wrapped(
            return get_wrapped(func, self)
            return match_querystring_argument
            return self._on_request(adapter, request, **kwargs)
            return self._registry.add(method)
            return self._registry.find(request)
            return self.add(method_or_response, url, body, *args, **kwargs)
            return self.replace(method_or_response, url, body, *args, **kwargs)
            return True
            rsp = rsp["response"]
            self._calls.add(request, response)
            self._patcher = None
            self._patcher.stop()
            self.add(
            self.auto_calculate_content_length
            self.reset()
            self.stop(allow_assert=success)
            setattr(self.body, "request", request)
            True, if URLs are identical or 'other' matches the pattern.
            try:
            Union[bool, str],
            Union[bytes, str, Tuple[Union[bytes, str], Union[bytes, str]], None],
            Union[Exception, Tuple[int, Mapping[str, str], "_Body"]],
            Union[float, Tuple[float, float], Tuple[float, None], None],
            url = urlunsplit(url_parts)
            URl that should be compared.
            url_parts[2] = "/"
            valid, reason = matcher(request)
            values = list(map(lambda x: x[1], val))
            warn(
            with assert_mock, responses:
        """
        """Compares two URLs.
        """Overload for scenario when
        """Overload for scenario when 'responses.activate' is used."""
        """Replaces current registry with `new_registry`.
        """Resets registry (including type), calls, passthru_prefixes to default values."""
        """Returns current registry instance with responses.
        "Function is deprecated. Use 'from responses.matchers import json_params_matcher'",
        "Function is deprecated. Use 'from responses.matchers import urlencoded_params_matcher'",
        # add attributes params and req_kwargs to 'request' object for further match comparison
        # Add Content-Type if it exists and is not already in headers
        # Based on
        # Can't simply do an equality check on the objects directly here since __eq__ isn't
        # content type values.
        # ensure the url has a default path set if the url is a string
        # Extend headers if they exist
        # first validate that current request is eligible to be retried.
        # https://github.com/urllib3/urllib3/blob/abbfbcb1dd274fc54b4f0a7785fd04d59b634195/src/urllib3/util/request.py#L220
        # If the callback set a content-type remove the one
        # if we were passed a `json` argument,
        # implemented for regex. It might seem to work as regex is using a cache to return
        # in the call list and allow the user to compare against the data that was in the
        # original request object does not have these attributes
        # override the body and content_type
        # Read from the file if it's a file-like object to avoid storing a closed file
        # request.
        # Requests/urllib support multiple types of body, including file-like objects.
        # See ``urllib3.util.retry.Retry`` documentation.
        # See GH #719
        # set asynchronous wrapper if requestor function is asynchronous
        # set in add_callback() so that we don't have multiple
        # the same regex instances, but it doesn't in all cases.
        )
        ) -> "models.Response":
        ):
        **kwargs: Any,
        *,
        *args: Any,
        :param request: (PreparedRequest), request object
        :return:
        @wraps(func)
        [
        [url_parsed.scheme, url_parsed.netloc, url_parsed.path, None, None, None]
        ],
        ``BaseResponse`` interface:
        ``method`` and ``url``. Removes all matching responses.
        `Response` body
        >>>     headers={'X-Header': 'foo'},
        >>>     json={'foo': 'bar'},
        >>>     method='GET',
        >>>     url='http://example.com',
        >>> )
        >>> import re
        >>> import responses
        >>> responses.add(
        >>> responses.add(Response(...))
        >>> responses.add(responses.GET, 'http://example.com')
        >>> responses.add(responses.GET, 'http://example.org')
        >>> responses.add(responses.GET, 'http://example.org', json={'data': 1})
        >>> responses.add_passthru('https://example.com')
        >>> responses.add_passthru(re.compile('https://example.com/\\w+'))
        >>> responses.remove(responses.GET, 'http://example.org')
        >>> responses.replace(responses.GET, 'http://example.org', json={'data': 2})
        >>> responses.upsert(responses.GET, 'http://example.org', json={'data': 2})
        A basic request:
        A JSON payload:
        adapter: "HTTPAdapter",
        adapter: HTTPAdapter,
        adding_headers: "_HeaderSet" = None,
        and ``url``, and the first matching response is replaced.
        assert isinstance(method, str)
        assert not isinstance(self.body, (Response, BaseException))
        assert url is not None
        assert_all_requests_are_fired: bool = ...,
        assert_all_requests_are_fired: bool = False,
        assert_all_requests_are_fired: bool = True,
        async def wrapper(*args: Any, **kwargs: Any) -> Any:  # type: ignore[misc]
        attribute="assert_all_requests_are_fired",
        auto_calculate_content_length: bool = False,
        body = _handle_body(body)
        body = _handle_body(self.body)
        body = body.encode("utf-8")
        body: "_Body" = "",
        body=body,
        body=data,  # required to avoid "ValueError: Unable to determine whether fp is closed."
        bool
        call = Call(request, response)  # type: ignore[misc]
        call_count = len(
        callback: Callable[
        callback: Callable[[Any], Any],
        Cleaned URL
        Compares only scheme, netloc and path. If 'url' is a re.Pattern, then checks that
        content to consume and the file-like object is still opened
        content_type: Optional[str] = "text/plain",
        content_type: Union[str, object] = _UNSET,
        Custom headers:
        Custom registry that should be applied. See ``responses.registries``
        data = self._parse_response_file(file_path)
        def deco_activate(function: "_F") -> Callable[..., Any]:
        def send(
        def wrapper(*args: Any, **kwargs: Any) -> Any:  # type: ignore[misc]
        DeprecationWarning,
        domains = netloc.split(".")
        either by a response object inheriting ``BaseResponse`` or
        elif isinstance(r_headers, list):
        elif isinstance(url, Pattern) and url.match(other):
        else:
        except ValueError:
        finally:
        FirstMatchRegistry
        For example, to allow any request to 'https://example.com', but require
        for i, d in enumerate(domains):
        for key, val in groupby(parse_qsl(urlsplit(url).query), lambda kv: kv[0]):
        for matcher in match:
        for rsp in data["responses"]:
        func: Optional["_F"] = None,
        Function to wrap.
        has_content_type = False
        headers = HTTPHeaderDict()  # Duplicate headers are legal
        headers = self.get_headers()
        headers.extend(r_headers)
        headers: Optional[Mapping[str, str]] = None,
        headers=headers,
        https://github.com/getsentry/responses/issues/394
        https://github.com/getsentry/responses/issues/438
        if (
        if adding_headers is not None:
        if call_count == count:
        if content_type is _UNSET:
        if func is not None:
        if has_content_type:
        if hasattr(body, "read") or isinstance(body, BufferedReader):
        if isinstance(body, Exception):
        if isinstance(body, str) or isinstance(body, bytes) or body is None:
        if isinstance(method, BaseResponse):
        if isinstance(method_or_response, BaseResponse):
        if isinstance(r_headers, dict) and "Content-Type" in r_headers:
        if isinstance(result, Exception):
        if isinstance(self.url, Pattern):
        if isinstance(url, str):
        if json is not None:
        if match is None:
        if match.passthrough:
        if match_querystring_argument is not None:
        if no response exists.  Responses are matched using ``method``and ``url``.
        if not allow_assert:
        if not data.closed and data.read(1):
        if not isinstance(other, BaseResponse):
        if not isinstance(prefix, Pattern) and _has_unicode(prefix):
        if not self._url_matches(self.url, str(request.url)):
        if not self.assert_all_requests_are_fired:
        if not valid:
        if not_called:
        if ord(x) > 128:
        if request.method != self.method:
        if resp_callback:
        if retries.is_retry(
        if self._patcher:
        if self._should_match_querystring(match_querystring):
        if self.body and isinstance(self.body, Exception):
        if self.content_type and (
        if self.headers:
        if self.method != other.method:
        if self.registered():
        if stream is not None:
        if url_parts[2] == "":
        Input data to generate `Response` body.
        is identical to ``add()``. The response is identified using ``method``
        Iterates through all available matches and validates if any of them matches the request
        json: Optional[Any] = None,
        match, match_failed_reasons = self._find_match(request)
        match.calls.add_call(call)
        match: "_MatcherIterable" = (),
        match: "_MatcherIterable", request: "PreparedRequest"
        match_querystring: Union[bool, FalseBool] = FalseBool(),
        match_querystring: Union[bool, object] = None,
        method: "_HTTPMethodOrResponse" = None,
        method: str,
        method_or_response: "_HTTPMethodOrResponse" = None,
        Mock object that is used as context manager.
        mocks for the remainder, you would add the prefix as so:
        models.Response,
        Modified URL if str or unchanged re.Pattern
        msg=headers,  # type: ignore[arg-type]
        new_registry : Type[FirstMatchRegistry]
        new=assert_all_requests_are_fired,
        not_called = [m for m in self.registered() if m.call_count == 0]
        original_response=orig_response,  # type: ignore[arg-type]  # See comment above
        other : str
        'other' matches the pattern.
        other_url = other.url.pattern if isinstance(other.url, Pattern) else other.url
        Parameters
        params: Dict[str, Union[str, int, float, List[Any]]] = {}
        passthrough: bool = False,
        passthru_prefixes: Tuple[str, ...] = (),
        preload_content=False,
        Raise an error if not all registered responses were executed.
        raise NotImplementedError
        Real Response uses HTTPResponse as body object.
        real_adapter_send: "_HTTPAdapterSend" = _real_send,
        reason=client.responses.get(status, None),
        Regex can be used like:
        Register a URL prefix or regex to passthru any non-matching mock requests to.
        registry: Optional[Type[Any]] = None,
        registry: Type[Any] = ...,
        registry: Type[FirstMatchRegistry] = FirstMatchRegistry,
        Removes a response previously added using ``add()``, identified
        Replaces a response previously added using ``add()``, or adds the response
        Replaces a response previously added using ``add()``. The signature
        request.body = self._read_filelike_body(request.body)
        request.params = self._parse_request_params(
        request.req_kwargs = kwargs  # type: ignore[attr-defined]
        request: "PreparedRequest",
        request: PreparedRequest,
        request_method=request_method,
        request_url = str(request.url)
        resp_callback = self.response_callback
        response = Response(method=method, url=url, body=body, **kwargs)
        response_callback: Optional[Callable[[Any], Any]] = None,
        'responses.activate(registry=, assert_all_requests_are_fired=True)' is used.
        result = self.callback(request)
        retries = retries or adapter.max_retries
        retries: Optional["_Retry"] = None,
        return (
        return _form_response(body, headers, status, request.method)
        return body
        return bool(urlsplit(self.url).query)
        return data
        return deco_activate
        return False
        return globals()[f"_deprecated_{name}"]
        return headers
        return iter(self._calls)
        return len(self._calls)
        return not self.__eq__(other)
        return params
        return response
        return self
        return self._calls
        return self._calls[idx]
        return self._registry
        return self._registry.add(response)
        return self._registry.registered
        return self._registry.remove(response)
        return self._registry.replace(response)
        return self_url == other_url
        return send
        return success
        return True, ""
        Returns
        See https://github.com/getsentry/responses/pull/469 for more details
        self,
        self, body: Union[str, bytes, BufferedReader, None]
        self, file_path: "Union[str, bytes, os.PathLike[Any]]"
        self, match_querystring_argument: Union[bool, object]
        self, request: "PreparedRequest"
        self, url: str
        self._calls = []
        self._calls.add_call(call)
        self._calls.append(Call(request, response))
        self._calls.append(call)
        self._calls.reset()
        self._calls: CallList = CallList()
        self._calls: List[Call] = []
        self._patcher = std_mock.patch(target=self.target, new=self.unbound_on_send())
        self._patcher.start()
        self._patcher: Optional["_mock_patcher[Any]"] = None
        self._real_send = real_adapter_send
        self._registry = FirstMatchRegistry()
        self._registry = new_registry()
        self._registry.add(
        self._registry: FirstMatchRegistry = registry()  # call only after reset
        self._thread_lock = _ThreadingLock()
        self.assert_all_requests_are_fired: bool = assert_all_requests_are_fired
        self.auto_calculate_content_length: bool = auto_calculate_content_length
        self.body: "_Body" = ""
        self.body: "_Body" = body
        self.callback = callback
        self.content_type: Optional[str] = content_type
        self.content_type: str = content_type  # type: ignore[assignment]
        self.headers: Optional[Mapping[str, str]] = headers
        self.match: "_MatcherIterable" = match
        self.method: str = method
        self.passthrough = passthrough
        self.passthru_prefixes += (prefix,)
        self.passthru_prefixes = ()
        self.passthru_prefixes: Tuple[_URLPatternType, ...] = tuple(passthru_prefixes)
        self.reset()
        self.response_callback: Optional[Callable[[Any], Response]] = response_callback
        self.start()
        self.status: int = 200
        self.status: int = status
        self.stream: Optional[bool] = stream
        self.target: str = target
        self.url: "_URLPatternType" = _ensure_url_default_path(url)
        self_url = self.url.pattern if isinstance(self.url, Pattern) else self.url
        status = self.status
        status, r_headers, body = result
        status: int = 200,
        status=status,
        stream: Optional[bool] = None,
        success = type is None
        super().__init__(*args, passthrough=True, **kwargs)
        super().__init__(method, url, **kwargs)
        target: str = "requests.adapters.HTTPAdapter.send",
        target=responses,
        The first matching response is replaced.
        This method ensures stability to work for both:
        Thus, when method is_closed is called first to check if there is any more
        try:
        url : Union["Pattern[str]", str]
        url = urlunsplit(urllist)
        URL that should be cleaned from unicode
        URL to parse.
        URL to validate.
        URL with scheme, netloc and path
        url: "_URLPatternType",
        url: "Optional[_URLPatternType]" = None,
        url_parts = list(urlsplit(url))
        urllist[1] = ".".join(domains)
        valid, reason = self._req_attr_matches(self.match, request)
        warn(
        where file should be intentionally be left opened to continue consumption
        with open(file_path) as file:
        with self._thread_lock:
        Wrapped function
        You can also directly pass an object which implements the
    """
    """Add empty URL path '/' if doesn't exist.
    """Class to mock up built-in False boolean.
    """Clean up URLs, which use punycode to handle unicode chars.
    """Construct URL only containing scheme, netloc and path by truncating other parts.
    """Generates `Response` body.
    """Wrap provided function inside ``responses`` context manager.
    "_add_from_file",
    "_deprecated_assert_all_requests_are_fired",
    "_deprecated_passthru_prefixes",
    "_deprecated_target",
    "activate",
    "add",
    "add_callback",
    "add_passthru",
    "assert_call_count",
    "CallbackResponse",
    "calls",
    "delete",
    "DELETE",
    "GET",
    "get",
    "head",
    "HEAD",
    "http://example.com/"
    "http://example.com/path;segment"
    "OPTIONS",
    "options",
    "patch",
    "PATCH",
    "POST",
    "post",
    "PUT",
    "put",
    "registered",
    "remove",
    "replace",
    "RequestsMock",
    "reset",
    "Response",
    "response_callback",
    "start",
    "stop",
    "upsert",
    # Block of type annotations
    # Clean up path/query/params, which use url-encoding to handle unicode chars
    # Exposed by the RequestsMock class:
    # import only for linter run
    # Make the `matchers` name available under a RequestsMock instance
    )
    ) -> "Dict[str, Any]":
    ) -> "models.Response":
    ) -> BaseResponse:
    ) -> Callable[["_F"], "_F"]:
    ) -> Dict[str, Union[str, int, float, List[Optional[Union[str, int, float]]]]]:
    ) -> List[BaseResponse]:
    ) -> models.Response: ...
    ) -> None:
    ) -> Tuple[bool, str]:
    ) -> Tuple[Optional["BaseResponse"], List[str]]:
    ) -> Union[bool, object]:
    ) -> Union[Callable[["_F"], "_F"], "_F"]:
    ) -> Union[str, bytes, None]:
    *,
    @overload
    @property
    @staticmethod
    ]
    _Body = Union[str, BaseException, "Response", BufferedReader, bytes, None]
    _F = Callable[..., Any]
    _HeaderSet = Optional[Union[Mapping[str, str], List[Tuple[str, str]]]]
    _HTTPAdapterSend = Callable[
    _HTTPMethodOrResponse = Optional[Union[str, "BaseResponse"]]
    _MatcherIterable = Iterable[Callable[..., Tuple[bool, str]]]
    _URLPatternType = Union["Pattern[str]", str]
    >>> _ensure_url_default_path("http://example.com")
    >>> _get_url_and_path("http://example.com/path;segment?ab=xy&zed=qwe#test=1&foo=bar")
    a real socket to imitate the object. This may not be desired, as some users may
    Applies percent encoding to URL path and query if required.
    assert_all_requests_are_fired : bool
    assert_all_requests_are_fired: Optional[bool] = None,
    assert_mock = std_mock.patch.object(
    body : BufferedReader or BytesIO
    body : str or bytes or BufferedReader
    body: Optional[Union[bytes, BufferedReader, str]],
    body: Union[BufferedReader, BytesIO],
    Callable
    chars = list(url)
    class UnboundSend:
    content_type: Optional[str] = None
    data = BytesIO()
    data = BytesIO(body)  # type: ignore[arg-type]
    data.close()
    data.isclosed = is_closed  # type: ignore[attr-defined]
    def __bool__(self) -> bool:
    def __call__(
    def __enter__(self) -> "RequestsMock":
    def __eq__(self, other: Any) -> bool:
    def __exit__(self, type: Any, value: Any, traceback: Any) -> bool:
    def __getitem__(self, idx: "slice[int, int, Optional[int]]") -> List[Call]: ...
    def __getitem__(self, idx: int) -> Call: ...
    def __getitem__(self, idx: Union[int, slice]) -> Union[Call, List[Call]]:
    def __init__(
    def __init__(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def __init__(self, *args: Any, **kwargs: Any):
    def __iter__(self) -> Iterator[Call]:
    def __len__(self) -> int:
    def __ne__(self, other: Any) -> bool:
    def __repr__(self) -> str:
    def _add_from_file(self, file_path: "Union[str, bytes, os.PathLike[Any]]") -> None:
    def _find_match(
    def _on_request(
    def _parse_request_params(
    def _parse_response_file(
    def _read_filelike_body(
    def _req_attr_matches(
    def _set_registry(self, new_registry: Type[FirstMatchRegistry]) -> None:
    def _should_match_querystring(
    def _url_matches(self, url: "_URLPatternType", other: str) -> bool:
    def activate(
    def activate(  # type: ignore[misc]
    def activate(self, func: "_F" = ...) -> "_F":
    def add(
    def add(self, request: "PreparedRequest", response: "_Body") -> None:
    def add_call(self, call: Call) -> None:
    def add_callback(
    def add_passthru(self, prefix: "_URLPatternType") -> None:
    def assert_call_count(self, url: str, count: int) -> bool:
    def call_count(self) -> int:
    def calls(self) -> CallList:
    def get_headers(self) -> HTTPHeaderDict:
    def get_registry(self) -> FirstMatchRegistry:
    def get_response(self, request: "PreparedRequest") -> HTTPResponse:
    def is_closed() -> bool:
    def matches(self, request: "PreparedRequest") -> Tuple[bool, str]:
    def registered(self) -> List["BaseResponse"]:
    def remove(
    def replace(
    def reset(self) -> None:
    def start(self) -> None:
    def stop(self, allow_assert: bool = True) -> None:
    def unbound_on_send(self) -> "UnboundSend":
    def upsert(
    delete = partialmethod(add, DELETE)
    DELETE: Literal["DELETE"] = "DELETE"
    else:
    Examples
    for i, x in enumerate(chars):
    from requests import models
    from requests import PreparedRequest
    from responses import matchers
    from typing import Literal  # type: ignore  # pragma: no cover
    from typing import Protocol
    from typing_extensions import Literal
    from unittest.mock import _patch as _mock_patcher
    from urllib3 import Retry as _Retry
    func : Callable
    func: Callable[..., Any],
    Function to generate `urllib3.response.HTTPResponse` object.
    get = partialmethod(add, GET)
    GET: Literal["GET"] = "GET"
    having an original response object with the headers stored in the `msg` attribute.
    head = partialmethod(add, HEAD)
    HEAD: Literal["HEAD"] = "HEAD"
    headers: Optional[Mapping[str, str]] = None
    headers: Optional[Mapping[str, str]],
    https://github.com/getsentry/responses/issues/464
    if _has_unicode(netloc):
    if inspect.iscoroutinefunction(func):
    if isinstance(body, BufferedReader):
    if isinstance(body, str):
    if isinstance(url, str):
    if name in deprecated_names:
    import os
    Instead of supplying a file-like object of type `HTTPMessage` for the headers, we provide
    introduce potential errors.
    netloc = urllist[1]
    object and then rely on the library to unparse it back. These additional conversions can
    options = partialmethod(add, OPTIONS)
    OPTIONS: Literal["OPTIONS"] = "OPTIONS"
    orig_response = HTTPResponse(
    Parameters
    passthrough: bool = False
    patch = partialmethod(add, PATCH)
    PATCH: Literal["PATCH"] = "PATCH"
    post = partialmethod(add, POST)
    POST: Literal["POST"] = "POST"
    Provides a synchronous or asynchronous wrapper for the function.
    put = partialmethod(add, PUT)
    PUT: Literal["PUT"] = "PUT"
    raise AttributeError(f"module {__name__} has no attribute {name}")
    registry : FirstMatchRegistry, optional
    registry: Optional[Any] = None,
    request: "PreparedRequest"
    request_method: Optional[str],
    response: "_Body"
    Response: Type[Response] = Response
    response_callback: Optional[Callable[[Any], Any]] = None
    responses : RequestsMock
    responses: "RequestsMock",
    return "".join(chars)
    return _json_params_matcher(params)
    return _urlencoded_params_matcher(params)
    return any(ord(char) > 128 for char in s)
    return data
    return HTTPResponse(
    return parse_url(url_and_path).url
    return url
    return wrapper
    Returns
    See https://github.com/getsentry/responses/issues/691
    status: int,
    str
    stream: Optional[bool] = False
    The cookie handling functionality of the `requests` library relies on the response object
    the headers directly. This approach eliminates the need to parse the headers into a file-like
    The type `urllib3.response.HTTPResponse` is incorrect; we should
    This method complies with RFC 3986.
    url : str
    url : str or re.Pattern
    url: "_URLPatternType",
    url_and_path = urlunparse(
    url_parsed = urlsplit(url)
    urllist = list(urlsplit(url))
    use `http.client.HTTPResponse` instead. However, changing this requires opening
    Used for backwards compatibility, see
    want to completely restrict network access in their tests.
    warn(
# expose default mock namespace
# expose only methods and/or read-only methods
) -> "_URLPatternType":
) -> Callable[..., Any]:
) -> HTTPResponse:
) -> Union[BufferedReader, BytesIO]:
]
__all__ = [
_add_from_file = _default_mock._add_from_file
_deprecated_assert_all_requests_are_fired = _default_mock.assert_all_requests_are_fired
_deprecated_passthru_prefixes = _default_mock.passthru_prefixes
_deprecated_target = _default_mock.target
_real_send = HTTPAdapter.send
_UNSET = object()
activate = _default_mock.activate
add = _default_mock.add
add_callback = _default_mock.add_callback
add_passthru = _default_mock.add_passthru
assert_call_count = _default_mock.assert_call_count
calls = _default_mock.calls
class BaseResponse:
class Call:
class CallbackResponse:
class CallList:
class FalseBool:
class PassthroughResponse:
class RequestsMock:
class Response:
def __getattr__(name: str) -> Any:
def _clean_unicode(url: str) -> str:
def _ensure_url_default_path(
def _form_response(
def _get_url_and_path(url: str) -> str:
def _handle_body(
def _has_unicode(s: str) -> bool:
def get_wrapped(
def json_params_matcher(params: Optional[Dict[str, Any]]) -> Callable[..., Any]:
def urlencoded_params_matcher(params: Optional[Dict[str, str]]) -> Callable[..., Any]:
DELETE = _default_mock.DELETE
delete = _default_mock.delete
deprecated_names = ["assert_all_requests_are_fired", "passthru_prefixes", "target"]
except ImportError:  # pragma: no cover
from functools import partialmethod
from functools import wraps
from http import client
from io import BufferedReader
from io import BytesIO
from itertools import groupby
from re import Pattern
from requests.adapters import HTTPAdapter
from requests.adapters import MaxRetryError
from requests.exceptions import ConnectionError
from requests.exceptions import RetryError
from responses.matchers import json_params_matcher as _json_params_matcher
from responses.matchers import query_string_matcher as _query_string_matcher
from responses.matchers import urlencoded_params_matcher as _urlencoded_params_matcher
from responses.registries import FirstMatchRegistry
from threading import Lock as _ThreadingLock
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NamedTuple
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Sized
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
from unittest import mock as std_mock
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import urlsplit
from urllib.parse import urlunparse
from urllib.parse import urlunsplit
from urllib3.response import HTTPHeaderDict
from urllib3.response import HTTPResponse
from urllib3.util.url import parse_url
from warnings import warn
GET = _default_mock.GET
get = _default_mock.get
head = _default_mock.head
HEAD = _default_mock.HEAD
if TYPE_CHECKING:  # pragma: no cover
import inspect
import json as json_module
import logging
import yaml
logger = logging.getLogger("responses")
mock = _default_mock = RequestsMock(assert_all_requests_are_fired=False)
OPTIONS = _default_mock.OPTIONS
options = _default_mock.options
PATCH = _default_mock.PATCH
patch = _default_mock.patch
POST = _default_mock.POST
post = _default_mock.post
put = _default_mock.put
PUT = _default_mock.PUT
registered = _default_mock.registered
remove = _default_mock.remove
replace = _default_mock.replace
reset = _default_mock.reset
response_callback = _default_mock.response_callback
start = _default_mock.start
stop = _default_mock.stop
try:
upsert = _default_mock.upsert
