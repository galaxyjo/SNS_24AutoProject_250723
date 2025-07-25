
    -----
    ------
    -------
    --------
    ----------
                                  input if not expandable
                         or buffer
                        "Multiple files found in TAR archive. "
                        "Multiple files found in ZIP file. "
                        f"Only one file per TAR archive: {files}"
                        f"Only one file per ZIP: {zip_names}"
                    # "Union[str, BaseBuffer]", "str", "Dict[str, Any]"
                    # No overload variant of "GzipFile" matches argument types
                    )
                    **compression_args,
                    assert file is not None
                    file = handle.buffer.extractfile(files[0])
                    filename=handle,
                    fileobj=handle,  # type: ignore[call-overload]
                    fileobj=handle, **compression_args  # type: ignore[arg-type]
                    handle = file
                    handle = handle.buffer.open(zip_names.pop())
                    mode=ioargs.mode,
                    raise ValueError(
                    raise ValueError(f"Zero files found in TAR archive {path_or_buf}")
                    raise ValueError(f"Zero files found in ZIP file {path_or_buf}")
                "For no header, use header=None instead"
                "Passing negative integer to header is invalid. "
                # "GzipFile", variable has type "Union[str, BaseBuffer]")
                # don't mutate user input.
                # error: Argument "fileobj" to "_BytesTarFile" has incompatible
                # error: Incompatible types in assignment (expression has type
                # for mypy
                # Override compression based on Content-Encoding header
                # type "BaseBuffer"; expected "Union[ReadBuffer[bytes],
                # WriteBuffer[bytes], None]"
                )
                **compression_args,
                **open_args,
                assert isinstance(col, tuple)
                ClientError,
                col = col[:-1] + (f"{col[-1]}.{cur_count}",)
                col = f"{col}.{cur_count}"
                compression = {"method": "gzip"}
                elif not files:
                elif not zip_names:
                else:
                encoding=ioargs.encoding,
                errors=errors,
                filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
                files = handle.buffer.getnames()
                handle = _BytesTarFile(
                handle = _BytesTarFile(name=handle, **compression_args)
                handle = gzip.GzipFile(
                handle = gzip.GzipFile(  # type: ignore[assignment]
                handle,
                handle, ioargs.mode, **compression_args  # type: ignore[arg-type]
                handle.fileno(), 0, access=mmap.ACCESS_READ  # type: ignore[arg-type]
                handles.append(handle)
                if len(files) == 1:
                if len(zip_names) == 1:
                ioargs.mode,
                mode = f"{mode}:{suffix[1:]}"
                mode=ioargs.mode,
                newline="",
                NoCredentialsError,
                open_args = {"cctx": zstd.ZstdCompressor(**compression_args)}
                open_args = {"dctx": zstd.ZstdDecompressor(**compression_args)}
                PermissionError,
                return compression
                return filename.with_suffix("").name
                self.write_to_buffer()
                storage_options = {"anon": True}
                storage_options = dict(storage_options)
                storage_options["anon"] = True
                zip_names = handle.buffer.namelist()
              {compression arguments}, Dict[str, Any])
            "compression has no effect when passing a non-binary object as input.",
            "Expected file path name or file-like object, "
            "header=int or list-like of ints to specify "
            "Passing a bool to header is invalid. Use header=None for no header or "
            "storage_options passed with file object or non-fsspec file path"
            "the row(s) making up the column names"
            # "Union[str, BaseBuffer]", "str", "Dict[str, Any]"
            # "Union[str, BaseBuffer]"; expected "Union[Union[str, PathLike[str]],
            # already closed
            # BaseBuffer]"; expected "Optional[Union[Union[str, bytes, PathLike[str],
            # Binary mode
            # Cannot infer compression of a buffer, assume no compression
            # compression libraries do not like an explicit text-mode
            # compression libraries to use binary mode.
            # Encoding
            # error: "BaseBuffer" has no attribute "close"
            # error: Argument 1 to "_BytesZipFile" has incompatible type
            # error: Argument 1 to "LZMAFile" has incompatible type "Union[str,
            # GH 27779
            # Overload of "BZ2File" to handle pickle protocol 5
            # PathLike[bytes]], IO[bytes]], None]"
            # python-zstandard defaults to text mode, but we always expect
            # ReadBuffer[bytes], WriteBuffer[bytes]]"
            # write to buffer
            )
            ).open()
            **kwargs,
            ]
            assert isinstance(handle, _BytesTarFile)
            assert isinstance(self.handle, TextIOWrapper)
            binary_classes += (type(reader),)
            compression_args.setdefault("mode", ioargs.mode)
            compression_method = compression_args.pop("method")
            compression=compression,
            content_encoding = req.headers.get("Content-Encoding", None)
            counts[col] = cur_count + 1
            cur_count = counts[col]
            else:
            encoding=encoding,
            encoding=ioargs.encoding,
            err_types_to_retry_with_anon = [
            errors=errors,
            f"{compression} will not write the byte order mark for {encoding}",
            f"got {type(ioargs.filepath_or_buffer)} type"
            file, mode, **kwargs
            file_obj = fsspec.open(
            filename = Path(self.buffer.filename)
            fileobj=fileobj,
            filepath_or_buffer = filepath_or_buffer.replace("s3a://", "s3://")
            filepath_or_buffer = filepath_or_buffer.replace("s3n://", "s3://")
            filepath_or_buffer, str
            filepath_or_buffer=_expand_user(filepath_or_buffer),
            filepath_or_buffer=file_obj,
            filepath_or_buffer=reader,
            from botocore.exceptions import (
            handle = _BytesZipFile(
            handle = _IOWrapper(handle)
            handle = get_bz2_file()(  # type: ignore[call-overload]
            handle = get_lzma_file()(
            handle = open(
            handle = open(handle, ioargs.mode)
            handle = zstd.open(
            handle,
            handle,  # type: ignore[arg-type]
            handle.close()
            handle.close()  # type: ignore[attr-defined]
            if "r" in handle.buffer.mode:
            if "r" in ioargs.mode:
            if content_encoding == "gzip":
            if filename.suffix == ".zip":
            if filepath_or_buffer.lower().endswith(extension):
            if handle.buffer.mode == "r":
            if is_potential_multiindex:
            if isinstance(handle, str):
            if storage_options is None:
            if suffix in (".gz", ".xz", ".bz2"):
            import_optional_dependency("botocore")
            ioargs.mode += "b"
            ioargs.mode = ioargs.mode.replace("t", "")
            isinstance(ioargs.filepath_or_buffer, str) or ioargs.should_close
            mmap.mmap(
            mode=fsspec_mode,
            mode=mode,
            mode=self.extend_mode(mode),
            msg = f"Unrecognized compression type: {compression}"
            name=name,
            newline="",
            not hasattr(handle, "readable")
            or not hasattr(handle, "seekable")
            or not hasattr(handle, "writable")
            pass
            raise ValueError(
            raise ValueError("cannot specify multi-index header with negative integers")
            raise ValueError("header must be integer or list of integers")
            raise ValueError("If mapping, compression must have key 'method'") from err
            raise ValueError(msg)
            reader = BytesIO(req.read())
            return
            return combined_bytestring
            return filename.name
            return filename.with_suffix("").name
            return filename.with_suffix("").with_suffix("").name
            return mode
            return None
            return self.buffer.readable()
            return self.buffer.seekable()
            return self.buffer.writable()
            return to_return
            RuntimeWarning,
            self.buffer.close()
            self.created_handles.remove(self.handle)
            self.handle.detach()
            self.handle.flush()
            self.overflow = b""
            self.overflow = combined_bytestring[n:]
            self.seek(0)
            should_close=False,
            should_close=True,
            stacklevel=find_stack_level(),
            suffix = Path(self.name).suffix
            to_return = combined_bytestring[:n]
            UnicodeWarning,
            with self.buffer:
            zstd = import_optional_dependency("zstandard")
           and other keys as compression options if compression
           May be a dict with key 'method' as compression mode
           mode is 'zip'.
           Passing compression options as keys in dict is
           supported for compression modes 'gzip', 'bz2', 'zstd' and 'zip'.
        """
        "w" in mode
        # "_IOWrapper"; expected "IO[bytes]"
        # "List[BaseBuffer]"; expected "List[Union[IO[bytes], IO[str]]]"
        # "Union[TextIOWrapper, GzipFile, BaseBuffer, typing.IO[bytes],
        # assuming storage_options is to be interpreted as headers
        # base class "_BufferedWriter" defined the type as "BytesIO")
        # Because a character can be represented by more than 1 byte,
        # Binary mode does not support 'encoding' and 'newline'.
        # but are equivalent to just "s3" from fsspec's point of view
        # BZ Compression
        # cc #11071
        # Check whether the filename is to be opened in binary mode.
        # classes that expect string but have 'b' in mode
        # Convert all path types (e.g. pathlib.Path) to strings
        # error: Argument "created_handles" to "IOHandles" has incompatible type
        # error: Argument "handle" to "IOHandles" has incompatible type
        # error: Argument 1 to "_IOWrapper" has incompatible type "mmap";
        # error: Argument 1 to "TextIOWrapper" has incompatible type
        # error: Incompatible types in assignment (expression has type "TarFile",
        # error: Incompatible types in assignment (expression has type "ZipFile",
        # expected "BaseBuffer"
        # file. This prevents opening the file a second time. infer_compression calls
        # GH 34626 Reads from Public Buckets without Credentials needs anon=True
        # GH 38125: some fsspec objects implement os.PathLike but have already opened a
        # gh-5874: if the filepath is too long will raise here
        # GZ Compression
        # If botocore is installed we fallback to reading with anon=True
        # Infer compression from the filename/URL extension
        # it is possible that reading will produce more bytes than n
        # not added to handles as it does not open/buffer resources
        # only marked as wrapped when the caller provided a handle
        # open mmap and adds *-able
        # overflow to the front of the bytestring the next time reading is performed
        # server responded with gzipped data
        # TAR Encoding
        # TarFile needs a non-empty string
        # this function with convert_file_like=True to infer the compression.
        # to allow reads from public buckets
        # TODO: fsspec can also handle HTTP via requests, but leaving this
        # two special-case s3-like protocols; these have special meaning in Hadoop,
        # typing.IO[Any]]"; expected "pandas._typing.IO[Any]"
        # unchanged. using fsspec appears to break the ability to infer if the
        # Unrecognized Compression
        # urlopen function defined elsewhere in this module
        # waiting until now for importing to match intended lazy logic of
        # We store the extra bytes in this overflow variable, and append the
        # When n=-1/n greater than remaining bytes: Read entire file/rest of file
        # XZ Compression
        # ZIP Compression
        # ZipFile needs a non-empty string
        # Zstd Compression
        )
        )  # just to appease mypy for this branch
        ):
        **kwargs,
        .. versionchanged:: 1.4.0 Zstandard support.
        and all(isinstance(c, tuple) for c in columns if c not in list(index_col))
        and bool(_RFC_3986_PATTERN.match(url))
        and compression_method in ["bz2", "xz"]
        and encoding in ["utf-16", "utf-32"]
        and not isinstance(columns, ABCMultiIndex)
        and not url.startswith(("http://", "https://"))
        archive_name = self.archive_name or self.infer_filename() or "tar"
        archive_name = self.archive_name or self.infer_filename() or "zip"
        archive_name: str | None = None,
        assert isinstance(
        assert not isinstance(handle, str)
        assert not isinstance(ioargs.filepath_or_buffer, str)
        assert self.buffer is not None
        avoid closing the potentially user-created buffer.
        bytes. This is not the same as `"b" not in mode`. If a string content is
        bytestring = self.buffer.read(n).encode(self.encoding)
        check_parent_directory(str(handle))
        Close all created buffers.
        codecs.lookup_error(errors)
        codecs.StreamReader,
        codecs.StreamReaderWriter,
        codecs.StreamWriter,
        Column or columns to use as the (possibly hierarchical) index
        combined_bytestring = self.overflow + bytestring
        compression or memory_map or _is_binary_mode(handle, ioargs.mode)
        compression_args = {}
        compression_args = dict(compression)
        compression_method = compression
        compression_method = None
        compression=compression,
        compression=ioargs.compression,
        CompressionDict,
        CompressionOptions,
        counts[col] = cur_count + 1
        created_handles=handles,  # type: ignore[arg-type]
        cur_count = counts[col]
        elif compression == "bz2":
        elif compression == "tar":
        elif compression == "xz":
        elif compression == "zip":
        elif compression == "zstd" and "b" not in ioargs.mode:
        elif compression == "zstd":
        elif filename.suffix in (".tar.gz", ".tar.bz2", ".tar.xz"):
        else:
        Encoding to use.
        encoding=encoding,
        err_types_to_retry_with_anon: list[Any] = []
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        except ImportError:
        except KeyError as err:
        except tuple(err_types_to_retry_with_anon):
        exists = os.path.exists(filepath_or_buffer)
        f"Unrecognized compression type: {compression}\n"
        f"Valid compression types are {valid}"
        file not to be named something.tar, because that causes confusion (GH39465).
        file not to be named something.zip, because that causes confusion (GH39465).
        File path or object.
        file: FilePath | ReadBuffer[bytes] | WriteBuffer[bytes],
        filename = Path(self.name)
        fileobj: ReadBuffer[bytes] | WriteBuffer[bytes] | None = None,
        FilePath,
        filepath_or_buffer = filepath_or_buffer.__fspath__()
        filepath_or_buffer = stringify_path(filepath_or_buffer, convert_file_like=True)
        filepath_or_buffer=filepath_or_buffer,
        for extension, compression in extension_to_compression.items():
        for handle in reversed(handles):
        for handle in self.created_handles:
        fsspec = import_optional_dependency("fsspec")
        fsspec_mode += "b"
        handle = _BytesIOWrapper(
        handle = open(handle, "rb")
        handle = TextIOWrapper(
        handle, "mode", mode
        handle=handle,  # type: ignore[arg-type]
        handles.append(handle)
        handles.append(ioargs.filepath_or_buffer)
        hasattr(filepath_or_buffer, "read") or hasattr(filepath_or_buffer, "write")
        header = cast(int, header)
        header = cast(Sequence, header)
        if (
        If `url` has a valid protocol return True otherwise False.
        If an explicit archive_name is not given, we still want the file inside the zip
        if any(i < 0 for i in header):
        if compression != "zstd":
        if compression == "gzip":
        if filename.suffix == ".tar":
        if filepath_or_buffer.startswith("s3a://"):
        if filepath_or_buffer.startswith("s3n://"):
        if hasattr(self.buffer, "readable"):
        if hasattr(self.buffer, "seekable"):
        if hasattr(self.buffer, "writable"):
        if header < 0:
        if ioargs.encoding and "b" not in ioargs.mode:
        if isinstance(self.buffer.filename, (os.PathLike, str)):
        if mode != "w":
        if n is None or n < 0 or n >= len(combined_bytestring):
        if not all(map(is_integer, header)):
        if not isinstance(filepath_or_buffer, str):
        if self.closed:
        if self.getbuffer().nbytes:
        if self.is_wrapped:
        if self.name is None:
        if self.name is not None:
        If string, specifies the compression method. If mapping, value at key
        import urllib.request
        index_col = []
        is_wrapped = not (
        is_wrapped=is_wrapped,
        isinstance(url, str)
        kwargs.setdefault("compression", zipfile.ZIP_DEFLATED)
        len(columns)
        'method' specifies compression method.
        mode += "b"
        mode = mode.replace("b", "")
        Mode to open path_or_buf with.
        mode: Literal["r", "a", "w", "x"] = "r",
        mode: str,
        mode=mode,
        msg = f"Invalid file path or buffer object type: {type(filepath_or_buffer)}"
        name: str | None = None,
        names[i] = col
        Note: If a TextIOWrapper was inserted, it is flushed and detached to
        Object which may or may not be convertible into a MultiIndex
        of options.
        pass
        Passed to _get_filepath_or_buffer
        passed to a binary file/buffer, a wrapper is inserted.
        Path to check parent directory of
        path_or_buf,
        raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
        raise TypeError(
        raise ValueError(
        raise ValueError(msg)
        ReadBuffer,
        req_info = urllib.request.Request(filepath_or_buffer, headers=storage_options)
        return
        return "b" in mode
        return cast(BaseBufferT, filepath_or_buffer)
        return compression
        return exists
        return False
        return filename.name
        return getattr(self.buffer, attr)
        return getattr(self.buffer, name)
        return handle, memory_map, handles
        return IOArgs(
        return mode
        return None
        return os.path.expanduser(filepath_or_buffer)
        return self
        return True
        See parsers._parser_params for more information. Only used by read_csv.
        See the errors argument for :func:`open` for a full list
        self,
        self.archive_name = archive_name
        self.buffer = buffer
        self.buffer.addfile(tarinfo, self)
        self.buffer.writestr(archive_name, self.getvalue())
        self.buffer: tarfile.TarFile = tarfile.TarFile.open(  # type: ignore[assignment]
        self.buffer: zipfile.ZipFile = zipfile.ZipFile(  # type: ignore[assignment]
        self.close()
        self.created_handles = []
        self.encoding = encoding
        self.is_wrapped = False
        self.name = name
        self.overflow = b""
        should_close=False,
        Specifies how encoding and decoding errors are to be handled.
        storage_options = storage_options or {}
        storage_options=storage_options,
        StorageOptions,
        super().__init__()
        super().close()
        tarinfo = tarfile.TarInfo(name=archive_name)
        tarinfo.size = len(self.getvalue())
        traceback: TracebackType | None,
        try:
        warnings.warn(
        Whether the type of the content passed to the file/buffer is string or
        while cur_count > 0:
        with urlopen(req_info) as req:
        with zstd.ZstdDecompressor().stream_reader(b"") as reader:
        wrapped = _IOWrapper(
        WriteBuffer,
    """
    """IO classes that that expect bytes"""
    """Test whether file exists."""
    """Try to memory map file/buffer."""
    """Whether the handle is opened in binary mode"""
    ".bz2": "bz2",
    ".gz": "gzip",
    ".tar": "tar",
    ".tar.bz2": "tar",
    ".tar.gz": "tar",
    ".tar.xz": "tar",
    ".xz": "xz",
    ".zip": "zip",
    ".zst": "zstd",
    # and writable. If we have a read-only buffer, we shouldn't need writable and vice
    # bz2 and xz do not write the byte order mark for utf-16 and utf-32
    # Compression has been specified. Check that it's valid
    # Convert BytesIO or file objects passed with an encoding
    # Created for compat with pyarrow read_csv
    # except when text mode is explicitly requested. The original mode is returned if
    # exceptions
    # fsspec is not used.
    # GH 16338
    # GH21227 internal compression is not used for non-binary handles.
    # handle compression dict
    # handle might not implement the IO-interface
    # have to use the `zstd.ZstdDecompressionReader` class for isinstance checks.
    # If a buffer does not have the above "-able" methods, we simple assume they are
    # Infer compression
    # is_file_like requires (read | write) & __iter__ but __iter__ is only
    # lazify expensive import (~30ms)
    # memory mapping needs to be the first step
    # methods, e.g., tempfile.SpooledTemporaryFile.
    # mmap used by only read_csv
    # need to open the file first
    # needed for read_csv(engine=python)
    # Only for write methods
    # only used for read_csv
    # open URLs
    # print a warning when writing such files
    # python-zstandard doesn't use any of the builtin base classes; instead we
    # read_csv does not know whether the buffer is opened in binary/text mode
    # See also https://github.com/indygreg/python-zstandard/pull/165.
    # seek/read/writ-able.
    # so we have to get it from a `zstd.ZstdDecompressor` instance.
    # specified by user
    # TextIOWrapper is overly strict: it request that the buffer has seekable, readable,
    # Unfortunately `zstd.ZstdDecompressionReader` isn't exposed by python-zstandard
    # Use binary mode when converting path-like objects to file-like objects (fsspec)
    # validate encoding and errors
    # versa. Some buffers, are seek/read/writ-able but they do not have the "-able"
    # Windows does not default to utf-8. Set to utf-8 for a consistent behavior
    # Wrapper that wraps a StringIO buffer and reads bytes from it
    )
    ) -> None:
    ):
    *,
    @abstractmethod
    ['x', 'y', 'x.1', 'x.2']
    {compression_options}
    {storage_options}
    >>> dedup_names(["x", "y", "x", "x"], is_potential_multiindex=False)
    a mapping containing additional arguments.
    a valid FILE URL
    abstractmethod,
    according to its __fspath__ method.
    Any other object is passed through unchanged, which includes bytes,
    Any,
    AnyStr,
    Attempt to convert a path-like object to a string.
    BaseBuffer,
    binary_classes: tuple[type, ...] = (BufferedIOBase, RawIOBase)
    bool : Whether or not columns could become a MultiIndex
    buffer = BytesIO()
    BufferedIOBase,
    but a custom pattern may be supported in the future.
    BytesIO,
    Can be used as a context manager.
    case an error is raised.
    cast,
    Check if parent directory of a file exists, raise OSError if it does not
    Check to see if a URL has a valid protocol.
    Check whether or not the `columns` parameter
    codecs.lookup(encoding)
    columns : array-like
    columns: Sequence[Hashable] | MultiIndex,
    compression : str or mapping
    compression = compression_args.pop("method")
    compression = dict(compression, method=compression_method)
    compression method is returned unchanged, unless it's invalid, in which
    compression: CompressionDict
    compression: CompressionOptions | None = None,
    compression: CompressionOptions = ...,
    compression: CompressionOptions,
    compression_args = dict(ioargs.compression)
    compression_method = infer_compression(filepath_or_buffer, compression_method)
    compression_method, compression = get_compression_method(compression)
    compression_method: str | None
    compression_options=_shared_docs["compression_options"] % "filepath_or_buffer",
    convert_file_like: bool = False,
    converts an absolute native path to a FILE URL.
    could be converted into a MultiIndex.
    counts: DefaultDict[Hashable, int] = defaultdict(int)
    created_handles: All file handles that are created by get_handle
    created_handles: list[IO[bytes] | IO[str]] = dataclasses.field(default_factory=list)
    Currently the renaming is done by appending a period and an autonumeric,
    def __enter__(self) -> IOHandles[AnyStr]:
    def __exit__(
    def __getattr__(self, attr: str):
    def __getattr__(self, name: str):
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def __init__(self, buffer: BaseBuffer) -> None:
    def __init__(self, buffer: StringIO | TextIOBase, encoding: str = "utf-8") -> None:
    def close(self) -> None:
    def extend_mode(self, mode: str) -> str:
    def infer_filename(self) -> str | None:
    def read(self, n: int | None = -1) -> bytes:
    def readable(self) -> bool:
    def seekable(self) -> bool:
    def writable(self) -> bool:
    def write_to_buffer(self) -> None:
    def write_to_buffer(self) -> None: ...
    DefaultDict,
    elif is_text and (
    elif isinstance(handle, str):
    elif storage_options:
    else:
    encoding : str or None
    encoding : the encoding to use to decode bytes, default is 'utf-8'
    encoding = encoding or "utf-8"
    encoding: str
    encoding: str | None = ...,
    encoding: str | None = None,
    encoding: str = "utf-8",
    errors : str, default 'strict'
    errors = errors or "strict"
    errors: str | None = ...,
    errors: str | None = None,
    Examples
    except (TypeError, ValueError):
    exists = False
    expanded_filepath_or_buffer : an expanded filepath or the
    filepath_or_buffer : a url, filepath (str, py.path.local or pathlib.Path),
    filepath_or_buffer : object to be converted
    filepath_or_buffer : object to be converted if possible
    filepath_or_buffer : str or file handle
    filepath_or_buffer = stringify_path(filepath_or_buffer)
    filepath_or_buffer: BaseBufferT, convert_file_like: bool = ...
    filepath_or_buffer: FilePath | BaseBuffer,
    filepath_or_buffer: FilePath | BaseBuffer, compression: str | None
    filepath_or_buffer: FilePath | BaseBufferT,
    filepath_or_buffer: FilePath, convert_file_like: bool = ...
    filepath_or_buffer: str | BaseBuffer
    finally:
    for i, col in enumerate(names):
    from pandas import MultiIndex
    from pandas._typing import (
    from types import TracebackType
    from urllib.request import pathname2url
    fsspec_mode = mode
    Get file handle for given path/buffer and mode.
    Get the compression method for filepath_or_buffer. If compression='infer',
    get_bz2_file,
    get_lzma_file,
    handle = cast(ReadCsvBuffer, handle)
    handle = ioargs.filepath_or_buffer
    handle, memory_map, handles = _maybe_memory_map(handle, memory_map)
    handle: IO[AnyStr]
    handle: str | BaseBuffer, memory_map: bool
    handle: The file handle to be used.
    handles.reverse()  # close the most recently added buffer first
    handles: list[BaseBuffer]
    handles: list[BaseBuffer] = []
    Hashable,
    if "r" in ioargs.mode and not hasattr(handle, "read"):
    if "r" not in mode and is_path:
    if "t" in mode or "b" in mode:
    if "t" not in fsspec_mode and "b" not in fsspec_mode:
    if (
    if _is_binary_mode(path_or_buf, mode) and "b" not in mode:
    if compression == "infer":
    if compression in _supported_compressions:
    if compression is None:
    if compression:
    if compression_method and hasattr(filepath_or_buffer, "write") and "b" not in mode:
    if header is None:
    if index_col is None or isinstance(index_col, bool):
    if ioargs.should_close:
    if is_bool(header):
    if is_fsspec_url(filepath_or_buffer):
    if is_integer(header):
    if is_list_like(header, allow_sets=False):
    if isinstance(compression, Mapping):
    if isinstance(errors, str):
    if isinstance(filepath_or_buffer, (str, bytes, mmap.mmap)):
    if isinstance(filepath_or_buffer, os.PathLike):
    if isinstance(filepath_or_buffer, str) and is_url(filepath_or_buffer):
    if isinstance(filepath_or_buffer, str):
    if isinstance(handle, str):
    if issubclass(type(handle), text_classes):
    if not (
    if not convert_file_like and is_file_like(filepath_or_buffer):
    if not is_text and ioargs.mode == "rb" and isinstance(handle, TextIOBase):
    if not isinstance(filepath_or_buffer, str):
    if not isinstance(url, str):
    if not memory_map:
    if not parent.is_dir():
    If the filepath_or_buffer is a url, translate and return the buffer.
    if zstd is not None:
    import urllib.request
    index_col : None, bool or list, optional
    index_col: bool | Sequence[int] | None = None,
    IO,
    ioargs = _get_filepath_or_buffer(
    is_bool,
    is_file_like,
    is_integer,
    is_list_like,
    is_path = isinstance(handle, str)
    is_text : bool, default True
    is_text: bool = ...,
    is_text: bool = True,
    is_text: Literal[False],
    is_text: Literal[True] = ...,
    is_wrapped = False
    is_wrapped: bool = False
    is_wrapped: Whether a TextIOWrapper needs to be detached.
    isurl : bool
    Lazy-import wrapper for stdlib urlopen, as that imports a big chunk of
    Literal,
    Mapping,
    memory_map &= hasattr(handle, "fileno") or isinstance(handle, str)
    memory_map : bool, default False
    memory_map: bool = ...,
    memory_map: bool = False,
    mode : str
    mode : str, optional
    mode: str
    mode: str = "r",
    mode: str,
    msg = (
    names = list(names)  # so we can index
    names: Sequence[Hashable], is_potential_multiindex: bool
    Notes
    Objects supporting the fspath protocol are coerced
    Otherwise passthrough.
    overload,
    Parameters
    parent = Path(path).parent
    path : a path in native format
    path: Path or str
    path_or_buf : str or file handle
    path_or_buf: FilePath | BaseBuffer,
    raise ValueError("header must be integer or list of integers")
    raise ValueError(msg)
    Raises
    RawIOBase,
    ReadCsvBuffer,
    Rename column names if duplicates exist.
    replaced by that user's home directory.
    return (
    return _expand_user(filepath_or_buffer)
    return binary_classes
    return bool(
    return compression_method, compression_args
    return exists
    return filepath_or_buffer
    return IOArgs(
    return IOHandles(
    return isinstance(handle, _get_binary_io_classes()) or "b" in getattr(
    return names
    return parse_url(url).scheme in _VALID_URLS
    Return the argument with an initial component of ~ or ~user
    return urljoin("file:", pathname2url(path))
    return urllib.request.urlopen(*args, **kwargs)
    Return value of io/common.py:_get_filepath_or_buffer.
    Return value of io/common.py:get_handle
    return wrapped, memory_map, [wrapped]
    Returns
    Returns the dataclass IOArgs.
    Returns the dataclass IOHandles
    Returns true if the given URL looks like
    Sequence,
    should_close: bool = False
    Simplifies a compression argument to a compression method string and
    Some objects do not support multiple .write() calls (TarFile and ZipFile).
    something fsspec can handle
    storage_options: StorageOptions | None = None,
    storage_options: StorageOptions = ...,
    storage_options: StorageOptions = None
    storage_options=_shared_docs["storage_options"],
    str_filepath_or_buffer : maybe a string version of the object
    string or None
    StringIO,
    strings, buffers, or anything else that's not even path-like.
    text_classes = (
    TextIOBase,
    TextIOWrapper is inserted.
    TextIOWrapper,
    the inferred compression method is returned. Otherwise, the input
    the stdlib.
    This is used to easily close created buffers and to handle corner cases when
    This wrapper writes to the underlying buffer on close.
    try:
    tuple of ({compression method}, Optional[str]
    TYPE_CHECKING,
    TypeVar,
    url : str or unicode
    urljoin,
    urlparse as parse_url,
    uses_netloc,
    uses_params,
    uses_relative,
    valid = ["infer", None] + sorted(_supported_compressions)
    ValueError on invalid compression specified.
    ValueError on mapping missing 'method' key
    zstd = import_optional_dependency("zstandard", errors="ignore")
  # type: ignore[misc]
"""Common IO api utilities"""
# error: Definition of "__enter__" in base class "IOBase" is incompatible
# with definition in base class "BinaryIO"
)
) -> BaseBufferT: ...
) -> bool:
) -> IOArgs:
) -> IOHandles[bytes]: ...
) -> IOHandles[str] | IOHandles[bytes]:
) -> IOHandles[str] | IOHandles[bytes]: ...
) -> IOHandles[str]: ...
) -> Sequence[Hashable]:
) -> str | BaseBufferT:
) -> str | None:
) -> str: ...
) -> tuple[str | BaseBuffer, bool, list[BaseBuffer]]:
) -> tuple[str | None, CompressionDict]:
@dataclasses.dataclass
@doc(
@doc(compression_options=_shared_docs["compression_options"] % "filepath_or_buffer")
@doc(compression_options=_shared_docs["compression_options"] % "path_or_buf")
@functools.lru_cache
@overload
_RFC_3986_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+\-+.]*://")
_supported_compressions = set(extension_to_compression.values())
_VALID_URLS = set(uses_relative + uses_netloc + uses_params)
_VALID_URLS.discard("")
}
BaseBufferT = TypeVar("BaseBufferT", bound=BaseBuffer)
class _BufferedWriter:
class _BytesIOWrapper:
class _BytesTarFile:
class _BytesZipFile:
class _IOWrapper:
class IOArgs:
class IOHandles:
def _expand_user(filepath_or_buffer: BaseBufferT) -> BaseBufferT: ...
def _expand_user(filepath_or_buffer: str | BaseBufferT) -> str | BaseBufferT:
def _expand_user(filepath_or_buffer: str) -> str: ...
def _get_binary_io_classes() -> tuple[type, ...]:
def _get_filepath_or_buffer(
def _is_binary_mode(handle: FilePath | BaseBuffer, mode: str) -> bool:
def _maybe_memory_map(
def check_parent_directory(path: Path | str) -> None:
def dedup_names(
def file_exists(filepath_or_buffer: FilePath | BaseBuffer) -> bool:
def file_path_to_url(path: str) -> str:
def get_compression_method(
def get_handle(
def infer_compression(
def is_fsspec_url(url: FilePath | BaseBuffer) -> bool:
def is_potential_multi_index(
def is_url(url: object) -> bool:
def stringify_path(
def urlopen(*args, **kwargs):
def validate_header_arg(header: object) -> None:
extension_to_compression = {
from __future__ import annotations
from abc import (
from collections import defaultdict
from collections.abc import (
from io import (
from pandas._typing import (
from pandas.compat import (
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.common import (
from pandas.core.dtypes.generic import ABCMultiIndex
from pandas.core.shared_docs import _shared_docs
from pandas.util._decorators import doc
from pandas.util._exceptions import find_stack_level
from pathlib import Path
from typing import (
from urllib.parse import (
if TYPE_CHECKING:
import codecs
import dataclasses
import functools
import gzip
import mmap
import os
import re
import tarfile
import warnings
import zipfile
