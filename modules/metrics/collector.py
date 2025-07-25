
                                   have this set to False, for example.
                                   should be cached. PyPI index urls should
                    "application/vnd.pypi.simple.v1+html; q=0.1",
                    "application/vnd.pypi.simple.v1+json",
                    "text/html; q=0.01",
                ",".join(redact_auth_from_url(url) for url in index_urls),
                "Ignoring indexes: %s",
                [
                ]
                cache_link_parsing=False,
                cache_link_parsing=True,
                candidates_from_page=candidates_from_page,
                continue
                expand_dir=False,
                expand_dir=True,
                f"* {s.link}"
                f"{len(lines)} location(s) to search "
                f"for versions of {project_name}:"
                for s in itertools.chain(find_links_sources, index_url_sources)
                if s is not None and s.link is not None
                loc,
                page_validator=self.session.is_secure_origin,
                project_name=project_name,
                return value
                self.base_url = href
            "Accept": ", ".join(
            "application/vnd.pypi.simple.v1+html",
            "application/vnd.pypi.simple.v1+html, and text/html",
            "application/vnd.pypi.simple.v1+json",
            "be checked by a HTTP HEAD request.",
            "Cache-Control": "max-age=0",
            "Cannot look at %s URL %s because it does not support lookup as web pages.",
            "Skipping page %s because it looks like an archive, and cannot "
            "Skipping page %s because the %s request got Content-Type: %s. "
            "text/html",
            "The only supported Content-Types are application/vnd.pypi.simple.v1+json, "
            # /simple/, because authors generally expecting that
            # blindly use any cached data, however the benefit of
            # changed at all, we will just always incur the round
            # For more information, please see pypa/pip#5670.
            # it won't. Thus by setting this to zero we will not
            # minimize traffic sent in cases where the page hasn't
            # once per 10 minutes.
            # still support conditional requests, so we will still
            # they've done a pip install in the last ~10 minutes
            # trip for the conditional GET now instead of only
            # twine upload && pip install will function, but if
            # using max-age=0 instead of no-cache, is that we will
            # We don't want to blindly returned cached data for
            )
            ),
            ]
            ] + lines
            build_source(
            continue
            exc.content_type,
            exc.request_desc,
            find_links=find_links,
            find_links=list(find_links_sources),
            for loc in self.find_links
            for loc in self.search_scope.get_index_urls_locations(project_name)
            href = self.get_href(attrs)
            if href is not None:
            if link is None:
            if name == "href":
            index_urls = []
            index_urls=index_urls,
            index_urls=list(index_url_sources),
            lines = [
            link = Link.from_json(file, page.url)
            link,
            logger.debug(
            logger.debug("\n".join(lines))
            no_index=options.no_index,
            return scheme
            return str(charset)
            return wrapper(CacheablePageContent(page))
            search_scope=search_scope,
            self.anchors.append(dict(attrs))
            session=session,
            url += "/"
            vcs_scheme,
            when constructing the SearchScope object.
            yield link
        """
        "Fetched page %s as %s",
        #       so we'll need to come up with something on our own.
        #       standard file extension for application/vnd.pypi.simple.v1+json
        #       style responses in the file:// URLs, however there's no
        # add trailing slash if not present so urljoin doesn't trim
        # final segment
        # Make sure find_links is a list before passing to create().
        # The OrderedDict calls deduplicate sources by URL.
        # TODO: In the future, it would be nice if pip supported PEP 691
        (
        )
        ).values()
        :param cache_link_parsing: whether links parsed from this page's url
        :param encoding: the encoding to decode the given content.
        :param session: The Session to use to make requests.
        :param suppress_no_index: Whether to ignore the --no-index option
        :param url: the URL from which the HTML was downloaded.
        _ensure_api_response(url, session=session)
        _handle_get_simple_fail(link, "timed out")
        _handle_get_simple_fail(link, exc)
        _handle_get_simple_fail(link, f"connection error: {exc}")
        _handle_get_simple_fail(link, reason, meth=logger.info)
        },
        assert page.cache_link_parsing
        cache_link_parsing: bool = True,
        cache_link_parsing=cache_link_parsing,
        candidates_from_page: CandidatesFromPage,
        charset = m.get_param("charset")
        cls,
        content: bytes,
        content_type: str,
        data = json.loads(page.content)
        elif tag == "a":
        encoding: Optional[str],
        encoding=encoding,
        Fetch an HTML page containing package links.
        find_links = options.find_links or []
        find_links_sources = collections.OrderedDict(
        for file in data.get("files", []):
        for name, value in attrs:
        headers={
        if charset:
        if link is None:
        if logger.isEnabledFor(logging.DEBUG):
        if not url.endswith("/"):
        if options.no_index and not suppress_no_index:
        if page.cache_link_parsing:
        if tag == "base" and self.base_url is None:
        if url.lower().startswith(scheme) and url[len(scheme)] in "+:":
        index_url_sources = collections.OrderedDict(
        index_urls = [options.index_url] + options.extra_index_urls
        link = Link.from_element(anchor, page_url=url, base_url=base_url)
        link_collector = LinkCollector(
        logger.debug(" file: URL is directory, getting %s", url)
        logger.warning(
        m = email.message.Message()
        m["content-type"] = headers["Content-Type"]
        meth = logger.debug
        options: Values,
        project_name: str,
        raise _NotHTTP()
        reason += str(exc)
        reason = "There was a problem confirming the ssl certificate: "
        redact_auth_from_url(url),
        resp = _get_simple_response(url, session=session)
        resp.headers.get("Content-Type", "Unknown"),
        response.content,
        response.headers["Content-Type"],
        return
        return _get_index_content(location, session=self.session)
        return _make_index_content(resp, cache_link_parsing=link.cache_link_parsing)
        return CollectedSources(
        return hash(self.page.url)
        return isinstance(other, type(self)) and self.page.url == other.page.url
        return link_collector
        return list(fn(cacheable_page.page))
        return list(fn(page))
        return None
        return redact_auth_from_url(self.url)
        return self.search_scope.find_links
        search_scope = SearchScope.create(
        search_scope: SearchScope,
        self,
        self.anchors: List[Dict[str, Optional[str]]] = []
        self.base_url: Optional[str] = None
        self.cache_link_parsing = cache_link_parsing
        self.content = content
        self.content_type = content_type
        self.encoding = encoding
        self.page = page
        self.request_desc = request_desc
        self.search_scope = search_scope
        self.session = session
        self.url = url
        self.url: str = url
        session: PipSession,
        super().__init__(content_type, request_desc)
        super().__init__(convert_charrefs=True)
        suppress_no_index: bool = False,
        url = urllib.parse.urljoin(url, "index.html")
        url,
        url: str,
        url=response.url,
        yield link
       `_NotAPIContent` if it is not HTML or a Simple API.
       and raise `_NotAPIContent` otherwise.
       check the Content-Type is HTML or Simple API, to avoid downloading a
       large file. Raise `_NotHTTP` if the content type cannot be determined, or
    """
    """Access an Simple API response with GET, and return the response.
    """Determine if we have any encoding information in our headers."""
    """Look for VCS schemes in the URL.
    """Represents one response (or page), along with its URL"""
    # Check for VCS schemes that do not support lookup as web pages.
    # downloaded it.
    # requirement of an url. Unless we issue a HEAD request on every
    # Simple API response or not. However we can check after we've
    # something that looks like an archive. However that is not a
    # Tack index.html onto file:// URLs that point to directories
    # The check for archives above only works if the url ends with
    # url we cannot know ahead of time for sure if something is a
    )
    ) -> "LinkCollector":
    ) -> CollectedSources:
    ) -> None:
    ):
    @classmethod
    @functools.lru_cache(maxsize=None)
    @functools.wraps(fn)
    @property
    _ensure_api_header(resp)
    `_NotAPIContent` if the content type is not a valid content type.
    `page` has `page.cache_link_parsing == False`.
    1. If the URL looks suspiciously like an archive, send a HEAD first to
    2. Actually perform the request. Raise HTTP exceptions on network failures.
    3. Check the Content-Type header to make sure we got a Simple API response,
    API Response.
    base_url = parser.base_url or url
    Callable,
    Check the Content-Type header to ensure the response contains a Simple
    content_type = response.headers.get("Content-Type", "Unknown")
    content_type_l = content_type.lower()
    content_type_l = page.content_type.lower()
    def __call__(self, page: "IndexContent") -> Iterable[Link]: ...
    def __eq__(self, other: object) -> bool:
    def __hash__(self) -> int:
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def __init__(self, content_type: str, request_desc: str) -> None:
    def __init__(self, page: "IndexContent") -> None:
    def __init__(self, url: str) -> None:
    def __str__(self) -> str:
    def collect_sources(
    def create(
    def fetch_response(self, location: Link) -> Optional[IndexContent]:
    def find_links(self) -> List[str]:
    def get_href(self, attrs: List[Tuple[str, Optional[str]]]) -> Optional[str]:
    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
    def wrapper(cacheable_page: CacheablePageContent) -> List[Link]:
    def wrapper_wrapper(page: "IndexContent") -> List[Link]:
    Dict,
    elements' attributes.
    else:
    encoding = _get_encoding_from_headers(response.headers)
    encoding = page.encoding or "utf-8"
    except _NotAPIContent as exc:
    except _NotHTTP:
    except NetworkConnectionError as exc:
    except requests.ConnectionError as exc:
    except requests.Timeout:
    except RetryError as exc:
    except SSLError as exc:
    find_links: Sequence[Optional[LinkSource]]
    for anchor in parser.anchors:
    for scheme in vcs.schemes:
    from typing import Protocol
    function's result (keyed by CacheablePageContent), unless the IndexContent
    Given a function that parses an Iterable[Link] from an IndexContent, cache the
    HTMLParser that keeps the first base HREF and a list of all anchor
    if content_type_l.startswith(
    if content_type_l.startswith("application/vnd.pypi.simple.v1+json"):
    if headers and "Content-Type" in headers:
    if is_archive_file(Link(url).filename):
    if meth is None:
    if scheme == "file" and os.path.isdir(urllib.request.url2pathname(path)):
    if scheme not in {"http", "https"}:
    if vcs_scheme:
    index_urls: Sequence[Optional[LinkSource]]
    Iterable,
    link: Link,
    List,
    logger.debug(
    logger.debug("Getting page %s", redact_auth_from_url(url))
    making network requests as needed.
    meth("Could not fetch URL %s: %s - skipping", link, reason)
    meth: Optional[Callable[..., None]] = None,
    MutableMapping,
    Optional,
    Parse a Simple API's Index Content, and yield its anchor elements as Link objects.
    parser = HTMLLinkParser(page.url)
    parser.feed(page.content.decode(encoding))
    Protocol = object
    raise _NotAPIContent(content_type, response.request.method)
    raise_for_status(resp)
    Raises `_NotAPIContent` if the content type is not a valid content-type.
    Raises `_NotHTTP` if the URL is not available for a HEAD request, or
    reason: Union[str, Exception],
    resp = session.get(
    resp = session.head(url, allow_redirects=True)
    response: Response, cache_link_parsing: bool = True
    Responsible for collecting Link objects from all configured locations,
    return IndexContent(
    return None
    return resp
    return wrapper_wrapper
    Returns the matched VCS scheme, or None if there's no match.
    scheme, _, path, _, _, _ = urllib.parse.urlparse(url)
    scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
    Send a HEAD request to the URL, and ensure the response contains a simple
    Sequence,
    The class's main method is its collect_sources() method.
    This consists of three parts:
    try:
    Tuple,
    TYPE_CHECKING,
    Union,
    url = link.url.split("#", 1)[0]
    url = page.url
    vcs_scheme = _match_vcs_scheme(url)
"""
# -*- coding: utf-8 -*-
)
) -> IndexContent:
) -> None:
@with_cached_index_content
class _NotAPIContent:
class _NotHTTP:
class CacheablePageContent:
class CollectedSources:
class HTMLLinkParser:
class IndexContent:
class LinkCollector:
class ParseLinks:
def _ensure_api_header(response: Response) -> None:
def _ensure_api_response(url: str, session: PipSession) -> None:
def _get_encoding_from_headers(headers: ResponseHeaders) -> Optional[str]:
def _get_index_content(link: Link, *, session: PipSession) -> Optional["IndexContent"]:
def _get_simple_response(url: str, session: PipSession) -> Response:
def _handle_get_simple_fail(
def _make_index_content(
def _match_vcs_scheme(url: str) -> Optional[str]:
def parse_links(page: "IndexContent") -> Iterable[Link]:
def with_cached_index_content(fn: ParseLinks) -> ParseLinks:
else:
from .sources import CandidatesFromPage, LinkSource, build_source
from optparse import Values
from pip._internal.exceptions import NetworkConnectionError
from pip._internal.models.link import Link
from pip._internal.models.search_scope import SearchScope
from pip._internal.network.session import PipSession
from pip._internal.network.utils import raise_for_status
from pip._internal.utils.filetypes import is_archive_file
from pip._internal.utils.misc import redact_auth_from_url
from pip._internal.vcs import vcs
from pip._vendor import requests
from pip._vendor.requests import Response
from pip._vendor.requests.exceptions import RetryError, SSLError
from typing import (
if TYPE_CHECKING:
import collections
import email.message
import functools
import itertools
import json
import logging
import os
import urllib.parse
import urllib.request
logger = logging.getLogger(__name__)
ResponseHeaders = MutableMapping[str, str]
The main purpose of this module is to expose LinkCollector.collect_sources().
