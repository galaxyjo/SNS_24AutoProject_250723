
                                "consider removing or adjusting your testpaths configuration. "
                                "No files were found in testpaths; "
                                "Searching recursively from the current directory instead."
                                PytestConfigWarning(warning_text), stacklevel=3
                            "This is not supposed to happen. Please report this issue to pytest."
                            )
                            f"found that the module {mod} is already loaded with path {mod.__file__}. "
                            f"While trying to load conftest path {conftestpath!s}, "
                            self.issue_config_time_warning(
                            warning_text = (
                        )
                        conftestpath,
                        consider_namespace_packages=consider_namespace_packages,
                        if warn:
                        importmode,
                        name.replace("_", "-")
                        parg = args[i]
                        raise AssertionError(
                        result.extend(sorted(glob.iglob(path, recursive=True)))
                        return
                        rootpath,
                        x,
                    " and FAILING TESTS WILL PASS.  Are you"
                    " because assert statements are not executed "
                    " plugins will be ignored"
                    " using python -O?"
                    "(are you using python -O?)\n"
                    "{} plugin has been merged into the core, "
                    "\nNOTE: displaying only minimal help due to UsageError.\n\n"
                    "ASSERTIONS ARE NOT EXECUTED"
                    "assertions not in test modules or"
                    "by the underlying Python interpreter "
                    "please remove it from your requirements.".format(
                    "spec",
                    ("firstresult", "historic"),
                    )
                    + args
                    anchor,
                    buffering=1,
                    clist.append(mod)
                    consider_namespace_packages=consider_namespace_packages,
                    continue
                    encoding=encoding,
                    except IndexError:
                    f"{self.inipath}: 'minversion' must be a single value"
                    f"{self.inipath}: 'minversion' requires pytest-{minver}, actual pytest-{pytest.__version__}'"
                    f"-o/--override-ini expects option=value style (got: {ini_config!r})."
                    for path in testpaths:
                    i += 1
                    if mod in mods:
                    if testpaths and not result:
                    importmode,
                    location=location,
                    manager=self,
                    method,
                    mod = self._importconftest(
                    mode=err.mode,
                    mods.append(mod)
                    nodeid="",
                    os.dup(err.fileno()),
                    parg = opt[2:]
                    plugin_name=plugin_name,
                    plugin=plugin,
                    pluginmanager.consider_pluginarg(plugin)
                    pluginmanager.register(plugin)
                    PytestConfigWarning(f"could not load initial conftests: {e.path}"),
                    result = []
                    result = testpaths
                    return ExitCode(ret)
                    return ret
                    rootpath,
                    self._loadconftestmodules(
                    self._validate_args(shlex.split(env_addopts), "via PYTEST_ADDOPTS")
                    stacklevel=2,
                    try:
                    value = user_ini_value
                    warning_message=records[0],
                    when="config",
                "  {}\n"
                "  https://docs.pytest.org/en/stable/deprecations.html#pytest-plugins-in-non-top-level-conftest-files"
                "consider_namespace_packages"
                "Defining 'pytest_plugins' in a non-top-level conftest is no longer supported:\n"
                "For more information, visit:\n"
                "It affects the entire test suite instead of just below the conftest as expected.\n"
                "Missing required plugins: {}".format(", ".join(missing_plugins)),
                "Please move it to a top level conftest file at the rootdir:\n"
                # so just let is pass and print a warning at the end
                # we don't want to prevent --help/--version to work
                )
                ) from e
                args, namespace=copy.copy(self.option)
                args, self.option, namespace=self.option
                args[:] = (
                args=(), plugins=None, dir=pathlib.Path.cwd()
                args=args,
                confcutdir = str(self.inipath.parent)
                confcutdir = str(self.rootpath)
                config._ensure_unconfigure()
                conftestpath = parent / "conftest.py"
                conftestpath,
                consider_namespace_packages=consider_namespace_packages,
                continue
                del sys.modules[conftestpath.stem]
                early_config=self, args=args, parser=self._parser
                elif opt.startswith("-p"):
                else exc_info.exconly()
                else self.invocation_params.dir
                else:
                err = open(
                error_template.format(error=f"invalid lineno {lineno_!r}: {e}")
                exc_info.getrepr(style="short", chain=False)
                except ValueError:
                f'Error importing plugin "{modname}": {e.args[0]}'
                filter_traceback_for_conftest_import_failure
                foundanchor = True
                from _pytest.helpconfig import showversion
                getattr(self.option, "help", False) or "--help" in args or "-h" in args
                hook = _pytest.assertion.install_importhook(self)
                if conftestpath.is_file():
                if dirpath in path.parents or path == dirpath:
                if exc_info.traceback
                if exclude_only and not parg.startswith("no:"):
                if isinstance(plugin, str):
                if key == name:
                if opt == "-p":
                if pyargs:
                if self.inipath is not None
                if x.is_dir():
                import pytest
                importmode,
                invocation_dir,
                invocation_dir=self.invocation_params.dir,
                key, user_ini_value = ini_config.split("=", 1)
                kwargs=dict(
                missing_plugins.append(required_plugin)
                mode = "plain"
                mode=importmode,
                new_package_files.append(new_fn)
                opts = _get_legacy_hook_marks(  # type: ignore[assignment]
                parg = parg.strip()
                pass
                path = path[:i]
                pyargs=self.known_args_namespace.pyargs,
                pytest.skip(f"no {name!r} option found")
                PytestConfigWarning(
                PytestConfigWarning(f"skipped plugin {module_name!r}: {msg}"),
                PytestConfigWarning(warning_text),
                raise
                raise AttributeError(name)
                raise pytest.UsageError(
                raise UsageError(
                raise UsageError(f"plugin {name} cannot be disabled")
                raise ValueError("number is negative")
                relroot = absolutepath(modpath / relroot)
                relroot = pathlib.Path(relroot)
                relroot = relroot.replace("/", os.sep)
                req = Requirement(required_plugin)
                result = []
                result = [str(invocation_dir)]
                ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
                return
                return [t for t in map(lambda x: x.strip(), value.split("\n")) if t]
                return default
                return mod, getattr(mod, name)
                return value
                root=rootpath,
                rootpath,
                rootpath=self.rootpath,
                seen_some = True
                self._mark_plugins_for_rewrite(hook)
                self._parser._getparser().print_help()
                self._try_load_conftest(
                self._validate_args(self.getini("addopts"), "via addopts config") + args
                self.consider_module(plugin)
                self.consider_pluginarg(parg)
                self.inipath.parent
                self.issue_config_time_warning(
                self.set_blocked("pytest_" + name)
                self.set_blocked("pytest_stepwise")
                self.set_blocked("stepwise")
                self.unblock("pytest_" + name)
                setattr(self.option, opt.dest, opt.default)
                showversion(self)
                source = Config.ArgsSource.INVOCATION_DIR
                source = Config.ArgsSource.TESTPATHS
                stacklevel=2,
                stacklevel=3,
                sys.stderr.flush()
                sys.stderr.write(f"INTERNALERROR> {line}\n")
                sys.stdout.write(
                testpaths=self.getini("testpaths"),
                try:
                tw.line(line.rstrip(), red=True)
                value = self.inicfg[name]
                Version(plugin_dist_info[req.name]), prereleases=True
                warn=True,
                warning_text = (
                yield module_name
              action:message:category:module:line
            """
            "`args` parameter expected to be a list of strings, got: {!r} (type: {})"
            "DEPRECATED, use @pytest.hookimpl(tryfirst=True) instead.",
            "DEPRECATED, use @pytest.hookimpl(trylast=True) instead.",
            "https://docs.python.org/3/library/warnings.html#describing-warning-filters"
            "markers",
            "plugin machinery will try to call it first/as early as possible. "
            "plugin machinery will try to call it last/as late as possible. "
            "Plugins that must be present for pytest to run",
            "required_plugins",
            "terminalreporter"
            "tryfirst: mark a hook implementation function such that the "
            "trylast: mark a hook implementation function such that the "
            # as well as editable installation finder modules made by setuptools
            # content of pytest.ini
            # Don't autoload from distribution package entry point. Only
            # Ensure we do not break if what appears to be an anchor
            # explicitly specified plugins are going to be loaded.
            # Handle --version and --help here in a minimal fashion.
            # Imported lazily to improve start-up time.
            # is in fact a very long option (#10169, #11394).
            # no need to continue.
            # Only process path part
            # PR #4304: remove stepwise if cacheprovider is blocked.
            # pytest_cmdline_main is not called in case of errors.
            # remove node-id syntax
            # This gets done via helpconfig normally, but its
            # Unblock the plugin.
            # We don't autoload from distribution package entry points,
            # we ignore "setup.py" at the root of the distribution
            )
            ) from None
            ),
            ).with_traceback(e.__traceback__) from e
            ):
            *,
            [pytest]
            __import__(importspec)
            _ispytest=True,
            absolutepath(invocation_dir / confcutdir) if confcutdir else None
            action_)  # type: ignore[attr-defined]
            anchor = absolutepath(invocation_dir / path)
            anchor,
            and not self._using_pyargs
            and self._configured
            apply_warning_filters(config_filters, cmdline_filters)
            args = self._parser.parse_setoption(
            args, namespace=copy.copy(self.known_args_namespace)
            args, namespace=copy.copy(self.option)
            args: Iterable[str],
            args[:] = (
            args=args or (),
            args=args,
            args=early_config.known_args_namespace.file_or_dir,
            args=ns.file_or_dir + unknown_args,
            assert e.__traceback__ is not None
            base_path_part, *nodeid_part = nodeid.split("::")
            confcutdir=early_config.known_args_namespace.confcutdir,
            config = _prepareconfig(args, plugins)
            Config._verbosity_ini_name(verbosity_type),
            config.pluginmanager.consider_pluginarg(x)
            configured for the given type, that value will be returned. If the
            consider_namespace_packages=consider_namespace_packages,
            consider_namespace_packages=early_config.getini(
            default=[],
            default=Config._VERBOSITY_INI_DEFAULT,
            del self._parser._config_source_hint  # type: ignore
            description, type, default = self._parser._inidict[name]
            dir: pathlib.Path,
            dir=pathlib.Path.cwd(),
            dp = (
            elif (
            elif not req.specifier.contains(
            else:
            encoding: str = getattr(err, "encoding", "utf8")
            env_addopts = os.environ.get("PYTEST_ADDOPTS", "")
            err: IO[str] = sys.stderr
            exc_info = ExceptionInfo.from_exception(e.cause)
            exc_info.traceback = exc_info.traceback.filter(
            exc_repr = (
            except AttributeError:
            except Exception:
            except InvalidRequirement:
            except KeyError:
            except SystemError:
            except ValueError as e:
            f"""\
            fail(msg.format(conftestpath, self._confcutdir), pytrace=False)
            fin = self._cleanup.pop()
            fin()
            finally:
            for dist in importlib.metadata.distributions()
            for file in dist.files or []
            for line in formatted_tb.splitlines():
            for line in str(excrepr).split("\n"):
            For more information please consult: {doc_url}
            for path, mods in self._dirpath2confmods.items():
            for plugin in plugins:
            for x in anchor.glob("test*"):
            formatted_tb = str(exc_repr)
            frame = sys._getframe(stacklevel - 1)
            from packaging.version import Version
            fullname=method.__qualname__,
            fullpath = self.rootpath / base_path_part
            funcargs=True, showlocals=getattr(option, "showlocals", False), style=style
            given type is not a known verbosity type, the global verbosity
            global verbosity level will be returned.
            hasattr(mod, "pytest_plugins")
            help=help,
            hook.mark_rewrite(name)
            hook_opts=hook_opts,
            i += 1
            i = path.find("::")
            if any(ep.group == "pytest11" for ep in dist.entry_points)
            if default is not notset:
            if getattr(self.option, "version", False) or "--version" in args:
            if i != -1:
            if invocation_dir == rootpath:
            if isinstance(opt, str):
            if isinstance(plugin, types.ModuleType):
            if isinstance(relroot, os.PathLike):
            if isinstance(value, str):
            if len(env_addopts):
            if lineno < 0:
            if loaded:
            if mode == "plain":
            if module_name != "setup" and not module_name.startswith("__editable__"):
            if name == "cacheprovider":
            if name in essential_plugins:
            if name.startswith("pytest_"):
            if new_fn:
            if not hasattr(self.option, opt.dest):
            if not isinstance(minver, str):
            if not name.startswith("pytest_"):
            if not result:
            if req.name not in plugin_dist_info:
            if safe_exists(anchor):
            if self._is_in_confcutdir(parent):
            if self.inipath is not None:
            if self.known_args_namespace.help or self.known_args_namespace.version:
            if skip:
            if val is None and skip:
            if Version(minver) > Version(pytest.__version__):
            import _pytest.assertion
            importmode,
            importmode=early_config.known_args_namespace.importmode,
            ini option are handled by pytest, not being included in the ``args`` attribute.
            inifile=ns.inifilename,
            input_values = shlex.split(value) if isinstance(value, str) else value
            invocation_dir=early_config.invocation_params.dir,
            invocation_dir=self.invocation_params.dir,
            invocation_params = self.InvocationParams(
            kwargs=dict(parser=self._parser, pluginmanager=self.pluginmanager)
            kwargs=dict(pluginmanager=self.pluginmanager)
            level will be returned. If the given type is None (default), the
            lineno = int(lineno_)
            loaded = self.load_setuptools_entrypoints("pytest11", name=modname)
            location = frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name
            method = getattr(module_or_class, name)
            method, "impl", ("tryfirst", "trylast", "optionalhook", "hookwrapper")
            mod = import_path(
            mod = sys.modules[importspec]
            mod, relroots = self.pluginmanager._rget_with_confmod(name, path)
            modname, str
            module_name, _ = os.path.splitext(fn)
            msg = (
            must_warn.append(f"{opt_name}={opt_attr}")
            must_warn.append(f"{opt_name}=True")
            name = arg
            name = arg[3:]
            new_fn = "/".join(parts[1:])
            noconftest=early_config.known_args_namespace.noconftest,
            nodeid = "::".join([relative_path, *nodeid_part])
            Note that even if ``True``, if a default was specified it will be returned instead of a skip.
            Note that the environment variable ``PYTEST_ADDOPTS`` and the ``addopts``
            Note this parameter will be ignored when the option is **declared** even if the option's value is ``None``.
            object.__setattr__(self, "args", tuple(args))
            object.__setattr__(self, "dir", dir)
            object.__setattr__(self, "plugins", plugins)
            opt = args[i]
            opts[opt_name] = False
            opts[opt_name] = True
            os.environ.pop("PYTEST_VERSION", None)
            os.environ["PYTEST_VERSION"] = old_pytest_version
            package_name = os.path.dirname(fn)
            parts = fn.split("/")
            pass
            path = str(initial_path)
            pluginmanager=pluginmanager, args=args
            Plugins accessing ``InvocationParams`` must be aware of that.
            plugins: Sequence[str | _PluggyPlugin] | None,
            plugins=plugins,
            print(config.get_verbosity())  # 1
            print(config.get_verbosity(Config.VERBOSITY_ASSERTIONS))  # 2
            processopt=self._processopt,
            pyargs=early_config.known_args_namespace.pyargs,
            pytest -v
            raise
            raise ConftestImportFailure(conftestpath, cause=e) from e
            raise ImportError(
            raise UsageError(
            raise UsageError(message)
            raise ValueError(f"no option named {name!r}") from e
            raise ValueError(f"unknown configuration value: {name!r}") from e
            relative_path = bestrelpath(self.invocation_params.dir, fullpath)
            result = args
            return
            return (yield)
            return [dp / x for x in input_values]
            return _strtobool(str(value).strip())
            return cast(types.ModuleType, existing)
            return ExitCode.USAGE_ERROR
            return global_level
            return None
            return opts
            return self._getini_unknown_type(name, type, value)
            return self._inicache[name]
            return shlex.split(value) if isinstance(value, str) else value
            return True
            return val
            return value
            rootdir_cmd_arg=ns.rootdir or None,
            rootpath,
            rootpath=early_config.rootpath,
            seen_some = True
            self,
            self._configured = False
            self._inicache[name] = val = self._getini(name)
            self._opt2dest[name] = opt.dest
            self._parser.parse_known_and_unknown_args(
            self._try_load_conftest(
            self._validate_config_options()
            self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")
            self.args == []
            self.args, self.args_source = self._decide_args(
            self.enable_tracing()
            self.hook.pytest_configure._call_history = []
            self.hook.pytest_configure.call_historic(kwargs=dict(config=self))
            self.hook.pytest_load_initial_conftests(
            self.hook.pytest_plugin_registered.call_historic(
            self.hook.pytest_unconfigure(config=self)
            self.hook.pytest_warning_recorded.call_historic(
            self.import_plugin(arg, consider_entry_points=True)
            self.import_plugin(import_spec)
            self.issue_config_time_warning(
            self.known_args_namespace.confcutdir = confcutdir
            self.parse(args)
            self.pluginmanager.hook)  # type: ignore[assignment]
            self.pluginmanager.load_setuptools_entrypoints("pytest11")
            self.register(mod, modname)
            self.set_blocked(name)
            self.skipped_plugins.append((modname, e.msg or ""))
            self.trace.root.setwriter(err.write)
            self.unblock(name)
            source = Config.ArgsSource.ARGS
            str(file)
            style = "native"
            style: TracebackStyle = "long"
            testpaths=early_config.getini("testpaths"),
            the literal ``--OPT`` option instead of the "dest" option name.
            Too many fields ({len(parts)}), expected at most 5 separated by colons:
            try:
            tw = TerminalWriter(sys.stderr)
            tw.line(f"ERROR: {msg}\n", red=True)
            tw.line(f"ImportError while loading conftest '{e.path}'.", red=True)
            type="args",
            type="string",
            type=hook_type,
            usage=f"%(prog)s [options] [{_a}] [{_a}] [...]",
            val = getattr(self.option, name)
            value = override_value
            values.append(relroot)
            verbosity_assertions = 2
            warn=False,
            warnings.simplefilter("always", type(warning))
            warnings.simplefilter("default")
            warnings.warn(
            warnings.warn(warning, stacklevel=stacklevel)
            yield from _iter_rewritable_modules(new_package_files)
            yield package_name
          {arg}
        """
        """:meta private:"""
        """A place where plugins can store information on the config for their
        """Access to command line option as attributes.
        """Add a function to be called when the config object gets out of
        """Add a line to an ini-file option. The option must have been
        """Add a output verbosity configuration option for the given output type.
        """Constructor usable for subprocesses."""
        """Decide the args (initial paths/nodeids) to use given the relevant inputs.
        """Deprecated, use getoption() instead."""
        """Deprecated, use getoption(skip=True) instead."""
        """Extra plugins, might be `None`."""
        """Given an importhook, mark for rewrite any top-level
        """Holds parameters passed during :func:`pytest.main`.
        """Import a plugin with ``modname``.
        """Install the PEP 302 import hook if using assertion rewriting.
        """Issue and handle a warning during the "configure" stage.
        """Load initial conftest files given a preparsed "namespace".
        """Return command line option value.
        """Return configuration value from an :ref:`ini file <configfiles>`.
        """Return whether a plugin with the given name is registered."""
        """The command-line arguments as passed to :func:`pytest.main`."""
        """The directory from which :func:`pytest.main` was invoked. :type: pathlib.Path"""
        """The parameters with which pytest was invoked.
        """The path to the :ref:`configfile <configfiles>`.
        """The path to the :ref:`rootdir <rootdir>`.
        """The plugin manager handles plugin registration and hook invocation.
        """Validate known args."""
        """Whether to consider the given path to load conftests from."""
        #
        #     a_line_list = "tests acceptance"
        #     a_line_list = ["tests", "acceptance"]
        #   Do not load a conftest if it is found upwards from confcut dir.
        #   in this case, we already have a list ready to use.
        #   in this case, we need to split the string to obtain a list of strings.
        #   ini:
        #   Load only conftests from confcutdir or below.
        #   toml:
        # -- State related to local conftest plugins.
        # "src" based source trees for example).
        # "terminal" or "capture".  Those plugins are registered under their
        # (see #9767 for a regression where the logic was inverted).
        # (see issue #1073).
        # _getconftestmodules()'s call to _get_directory() causes a stat
        # _pytest prefix.
        # abuse typeguard from importlib to avoid massive method type union that's lacking an alias
        # All conftest modules applicable for a directory.
        # All loaded conftest modules.
        # Always use the last item if multiple values are set for same ini-name,
        # are rarer.
        # as those of its parent directories.
        # Assumes always called with same importmode and rootpath.
        # At first glance they might seem the same thing, however we do support use cases where
        # At this point we did not find any packages or modules suitable for assertion
        # basename for historic purposes but must be imported with the
        # before loading the new one, otherwise the existing one will be
        # But this is *not* the same as:
        # Coerce the values based on types.
        # Collect unmarked hooks as long as they have the `pytest_' prefix.
        # Config._consider_importhook will set a real object if required.
        # conftest.py files there are not in a Python package all have module
        # Consider only actual functions for hooks (#3775).
        # Cutoff directory above which conftests are no longer discovered.
        # Deprecated alias. Was never public. Can be removed in a few releases.
        # discovering the initial conftests. So "pre-run" the logic here.
        # e.g. -o foo=bar1 -o foo=bar2 will set foo to bar2.
        # early_config.args it not set yet. But we need it for
        # For example:
        # get either str or list of str values (see _parse_ini_config_from_pyproject_toml).
        # Handle any "-p no:plugin" args.
        # If set, conftest loading is skipped.
        # Ignore names which cannot be hooks.
        # Imported lazily to improve start-up time.
        # in completely different directory hierarchies like packages installed
        # in out-of-source trees.
        # It will be done for real in `parse()`.
        # just stored here to be used later.
        # let's also consider test* subdirs
        # list of (module name, skip reason)
        # Most often modname refers to builtin modules, e.g. "pytester",
        # name "conftest", and thus conflict with each other. Clear the existing
        # nodeid's are relative to the rootpath, compute relative to cwd.
        # Note: some coercions are only required if we are reading from .ini files, because
        # Optimization: avoid repeated searches in the same directory.
        # options added by late-loading conftest files.
        # override_ini is a list of "ini=value" options.
        # Parse given cmdline arguments into this config object.
        # plugins that were explicitly skipped with pytest.skip
        # previously we would issue a warning when a plugin was skipped, but
        # pytest hooks are always prefixed with "pytest_",
        # Python flushes standard streams on exit; redirect remaining output
        # returned from the module cache.
        # rewriting, so we try again by stripping the first path component (to account for
        # session (#9478), often with the same path, so cache it.
        # since we refactored warnings as first citizens of Config, they are
        # so we avoid accessing possibly non-readable attributes
        # storm when it's called potentially thousands of times in a test
        # Support deprecated naming because plugins (xdist e.g.) use it.
        # the file format doesn't contain type information, but when reading from toml we will
        # The semantics here are literally:
        # This approach lets us have the common case continue to be fast, as egg-distributions
        # This includes the directory's own conftest modules as well
        # to devnull to avoid another BrokenPipeError at shutdown
        # Used to know when we are importing conftests after the pytest_configure stage.
        # Validate invalid ini keys after collection is done so we take in account
        # We haven't fully parsed the command line arguments yet, so
        # we should remove tryfirst/trylast as markers.
        # we want to load conftests that are not found in confcutdir or below, but are found
        # XXX now that the pluginmanager exposes hookimpl(tryfirst...)
        )
        ) -> None:
        ),
        ), "can only parse cmdline args at most once per Config object"
        ), f"module name as text required, got {modname!r}"
        ):
        *,
        .. code-block:: console
        .. code-block:: ini
        .. code-block:: python
        .. note::
        .. versionadded:: 5.1
        .. versionadded:: 6.1
        .. versionadded:: 7.2
        :func:`parser.addini <pytest.Parser.addini>` call (usually from a
        :func:`parser.addini <pytest.Parser.addini>` will be returned.
        :func:`parser.addini <pytest.Parser.addini>`, then a default value
        :func:`parser.addini <pytest.Parser.addini>`, then the configuration
        :param default: Fallback value if no option of that name is **declared** via :hook:`pytest_addoption`.
        :param help: Description of the output this type controls.
        :param name: Name of the option. You may also specify
        :param parser: Parser for command line arguments and ini-file values.
        :param skip: If ``True``, raise :func:`pytest.skip` if option is undeclared or has a ``None`` value.
        :param stacklevel: stacklevel forwarded to warnings.warn.
        :param verbosity_type: Fine-grained verbosity category.
        :param verbosity_type: Verbosity type to get level for. If a level is
        :param warn: Whether can issue warnings.
        :param warning: The warning instance.
        :py:func:`config.get_verbosity(type) <pytest.Config.get_verbosity>`.
        :ref:`ini file <configfiles>`, then the ``default`` value provided while
        :returns: The args and the args source. Guaranteed to be non-empty.
        :type: argparse.Namespace
        :type: InvocationParams
        :type: pathlib.Path
        :type: PytestPluginManager
        :type: Stash
        _a = FILE_OR_DIR
        ``bool`` : ``False``
        ``paths``, ``pathlist``, ``args`` and ``linelist`` : empty list ``[]``
        ``pytest_configure`` (or similar stages).
        ``string`` : empty string ``""``
        {{error}}
        A pytest PluginManager.
        action: warnings._ActionKind = warnings._getaction(
        All builtin and 3rd party plugins will have been loaded, however, so
        all pytest plugins."""
        anchor: pathlib.Path,
        and a numeric value for the verbosity level. A special value of "auto"
        and find all the installed plugins to mark them for rewriting
        args = [os.fspath(args)]
        args = sys.argv[1:]
        args, args_source = early_config._decide_args(
        args: list[str],
        args: Sequence[str | pathlib.Path],
        args: tuple[str, ...]
        arguments ('--my-opt somepath') we might get some false positives.
        arguments directly from the process command line (:data:`sys.argv`).
        As conftest files may add their own command line options which have
        assert (
        assert False
        assert inspect.isroutine(method)
        assert isinstance(
        assert isinstance(global_level, int)
        assert isinstance(x, list)
        assert mod.__file__ is not None
        assert not self._configured
        assert terminalreporter is not None
        based on the ``type`` parameter passed to
        by the importhook.
        can be used to explicitly use the global verbosity level.
        category: type[Warning] = _resolve_warning_category(category_)
        cause: Exception,
        clist = []
        cmdline_filters = self.known_args_namespace.pythonwarnings or []
        code = main()
        common options will not confuse our logic here.
        confcutdir: pathlib.Path | None,
        config = get_config(args)
        config = pluginmanager.hook.pytest_cmdline_parse(
        config._ensure_unconfigure()
        config.addinivalue_line(
        config.option.__dict__.update(option_dict)
        config.parse(args, addopts=False)
        config_filters = self.getini("filterwarnings")
        configuration file should have a setting for the configuration name
        conftestpath: pathlib.Path,
        conftestpath_plugin_name = str(conftestpath)
        consider_namespace_packages: bool,
        considered to find a plugin.
        declared but might not yet be set in which case the line becomes
        def __init__(
        default value.
        devnull = os.open(os.devnull, os.O_WRONLY)
        dir: pathlib.Path
        directory = self._get_directory(path)
        dirpath = conftestpath.parent
        doc_url = (
        During ``pytest_configure`` we can't capture warnings using the ``catch_warnings_for_item``
        elif is_package:
        elif opt_name in known_marks:
        elif type == "args":
        elif type == "bool":
        elif type == "linelist":
        elif type == "string":
        elif type is None:
        else:
        error = dedent(
        Example:
        exc_info = ExceptionInfo.from_current()
        except AttributeError as e:
        except ConftestImportFailure as e:
        except Exception as e:
        except ImportError as e:
        except KeyError as e:
        except KeyError:
        except PrintHelp:
        except Skipped as e:
        except UsageError:
        except ValueError as e:
        exception_text = exc_info.getrepr(style="native")
        excinfo: ExceptionInfo[BaseException],
        excrepr = excinfo.getrepr(
        existing = self.get_plugin(conftestpath_plugin_name)
        f"""\
        f"Plugins may be specified as a sequence or a ','-separated string of plugin names. Got: {specs!r}"
        finally:
        for fn in package_files:
        for import_spec in plugins:
        for ini_config in self._override_ini:
        for initial_path in args:
        for key in sorted(self._get_unknown_ini_keys()):
        for mod in reversed(modules):
        for module_name, msg in self.pluginmanager.skipped_plugins:
        for msg in e.args:
        for name in _iter_rewritable_modules(package_files):
        for name in opt._short_opts + opt._long_opts:
        for parent in reversed((directory, *directory.parents)):
        for relroot in relroots:
        for required_plugin in required_plugins:
        for x in config.option.plugins:
        foundanchor = False
        from .argparsing import FILE_OR_DIR
        from .argparsing import Parser
        from packaging.requirements import InvalidRequirement
        from packaging.requirements import Requirement
        from packaging.version import Version
        function because it is not possible to have hook wrappers around ``pytest_configure``.
        global_level = self.getoption("verbose", default=0)
        hook_opts = ", ".join(must_warn)
        https://github.com/pytest-dev/pytest-mock/issues/167
        i = 0
        if (
        If ``consider_entry_points`` is True, entry point names are also
        If ``default`` is not provided while registering using
        If a configuration value is not defined in an
        if addopts:
        if anchor.is_dir():
        if arg.startswith("no:"):
        if args:
        if consider_entry_points:
        if directory in self._dirpath2confmods:
        if dirpath in self._dirpath2confmods:
        if existing is not None:
        if hasattr(opt, "default"):
        if ini_name not in self._parser._inidict:
        if invocation_params is None:
        if is_simple_module:
        if level == Config._VERBOSITY_INI_DEFAULT:
        if minver:
        if missing_plugins:
        if mode == "rewrite":
        if name == "pytest_plugins":
        if name in _pytest.deprecated.DEPRECATED_EXTERNAL_PLUGINS:
        If neither the ``default`` nor the ``type`` parameter is passed
        if new_package_files:
        if not _assertion_supported():
        if not any(res):
        if not foundanchor:
        if not inspect.isroutine(method):
        if not name.startswith("pytest_"):
        if not os.environ.get("PYTEST_DISABLE_PLUGIN_AUTOLOAD"):
        if not required_plugins:
        if old_pytest_version is None:
        if opt_attr is not AttributeError:
        if option and getattr(option, "fulltrace", False):
        if opts is None:
        if opts is not None:
        if os.environ.get("PYTEST_DEBUG"):
        if os.environ.get("PYTEST_DISABLE_PLUGIN_AUTOLOAD"):
        if override_value is None:
        if pkgpath is None:
        if plugin_name is not None:
        if plugins:
        if records:
        if self._confcutdir is None:
        if self._configured:
        if self._noconftest:
        if self.invocation_params.dir != self.rootpath:
        if self.is_blocked(modname) or self.get_plugin(modname) is not None:
        if self.known_args_namespace.confcutdir is None:
        if self.known_args_namespace.strict_config:
        if self.pluginmanager.is_blocked("warnings"):
        If the specified name hasn't been registered through a prior
        if type == "paths":
        if verbosity_type is None:
        import _pytest.assertion
        import builtins as m
        import pytest
        importmode: ImportMode | str,
        importmode: str | ImportMode,
        importspec = "_pytest." + modname if modname in builtin_plugins else modname
        ini_name = Config._verbosity_ini_name(verbosity_type)
        invocation.
        invocation_dir: pathlib.Path,
        invocation_params: InvocationParams | None = None,
        invocation_params=Config.InvocationParams(
        is treated as a string and a default empty string '' is returned.
        is_package = fn.count("/") == 1 and fn.endswith("__init__.py")
        is_simple_module = "/" not in fn and fn.endswith(".py")
        klass = category
        level = self.getini(ini_name)
        LICENSE
        lineno = 0
        List of command line arguments. If `None` or not given, defaults to reading
        m = __import__(module, None, None, [klass])
        message = _pytest.deprecated.HOOK_LEGACY_MARKING.format(
        message = re.escape(message)
        method = getattr(plugin, name)
        minver = self.inicfg.get("minversion", None)
        missing_plugins = []
        mod: types.ModuleType,
        mode = getattr(ns, "assertmode", "plain")
        modpath = pathlib.Path(mod.__file__).parent
        module = re.escape(module) + r"\Z"
        module, _, klass = category.rpartition(".")
        modules = self._getconftestmodules(path)
        modules or packages in the distribution package for
        msg = (  # type:ignore[unreachable]
        msg = f"unknown configuration type: {type}"
        n = len(args)
        name = self._opt2dest.get(name, name)
        name: str,
        Needs to parse the --assert=<mode> option from the commandline
        new_package_files = []
        noconftest: bool,
        ns, unknown_args = self._parser.parse_known_and_unknown_args(
        ns, unknown_args = self._parser.parse_known_and_unknown_args(args)
        Object containing parameters regarding the :func:`pytest.main`
        opt_attr = getattr(method, opt_name, AttributeError)
        option: argparse.Namespace | None = None,
        opts = super().parse_hookimpl_opts(plugin, name)
        opts = super().parse_hookspec_opts(module_or_class, name)
        os.dup2(devnull, sys.stdout.fileno())
        os.environ["PYTEST_VERSION"] = __version__
        override_value = self._get_override_ini_value(name)
        own use.
        package_files = (
        parser.addini(
        parser_inicfg = self._parser._inidict
        parts.append("")
        path: pathlib.Path,
        pkgpath = resolve_package_path(conftestpath)
        Please note that you can even provide ``None`` as a valid
        plugin), a ValueError is raised.
        plugin: _PluggyPlugin | None = self.get_plugin(name)
        plugin_dist_info = {dist.project_name: dist.version for _, dist in plugin_info}
        plugin_info = self.pluginmanager.list_plugin_distinfo()
        plugin_name = super().register(plugin, name)
        pluginmanager,
        pluginmanager.consider_preparse(args, exclude_only=True)
        pluginmanager.import_plugin(spec)
        pluginmanager: PytestPluginManager,
        plugins = _get_plugin_specs_as_list(spec)
        plugins: Sequence[str | _PluggyPlugin] | None
        pyargs: bool,
        pytest_mock.egg-info/PKG-INFO
        pytest_mock/__init__.py
        pytest_mock/_version.py
        pytest_mock/plugin.py
        r"""Retrieve the verbosity level for a fine-grained verbosity type.
        raise
        raise KeyError(name)
        raise TypeError(msg.format(args, type(args)))
        raise UsageError(error_template.format(error=error))
        raise UsageError(error_template.format(error=exception_text)) from None
        raise UsageError(error_template.format(error=str(e))) from None
        raise UsageError(f"{cat} is not a Warning subclass")
        raise UsageError(f"{optname} must be a directory, given: {path}")
        raise UsageError(f"{optname} must be a filename, given: {path}")
        raise ValueError(f"invalid truth value {val!r}")
        raise ValueError(msg, value)  # pragma: no cover
        registering the configuration through
        required_plugins = sorted(self.getini("required_plugins"))
        res = self.hook.pytest_internalerror(excrepr=excrepr, excinfo=excinfo)
        return "<NOTSET>"
        return []
        return [name for name in self.inicfg if name not in parser_inicfg]
        return _get_legacy_hook_marks(  # type: ignore[return-value]
        return 1  # Python exits with error code 1 on EPIPE
        return args
        return bool(self.get_plugin(name))
        return code
        return config
        return ExitCode.USAGE_ERROR
        return f"{type(self.cause).__name__}: {self.cause} (from {self.path})"
        return f"verbosity_{verbosity_type}"
        return False
        return False  # type: ignore[unreachable]
        return int(level)
        return list(specs)
        return mod
        return nodeid
        return opts
        return path
        return path not in self._confcutdir.parents
        return path.parent
        return plugin
        return plugin_name
        return result, source
        return self
        return self._dirpath2confmods.get(directory, ())
        return self._inipath
        return self._rootpath
        return self.getoption(name)
        return self.getoption(name, skip=True)
        return specs.split(",") if specs else []
        return terminalreporter._tw
        return True
        return value
        return values
        return Warning
        rootpath, inipath, inicfg = determine_setup(
        rootpath: pathlib.Path,
        self,
        self, args: Sequence[str], *, exclude_only: bool = False
        self, conftestmodule: types.ModuleType, registration_name: str
        self, name: str, path: pathlib.Path
        self, plugin: _PluggyPlugin, name: str
        self, pluginmanager: PytestPluginManager, args: list[str]
        self, spec: None | types.ModuleType | str | Sequence[str]
        self._check_non_top_pytest_plugins(mod, conftestpath)
        self._checkversion()
        self._cleanup.append(func)
        self._cleanup: list[Callable[[], None]] = []
        self._confcutdir = (
        self._confcutdir: pathlib.Path | None = None
        self._configured = False
        self._configured = True
        self._conftest_plugins.add(mod)
        self._conftest_plugins: set[types.ModuleType] = set()
        self._consider_importhook(args)
        self._dirpath2confmods: dict[pathlib.Path, list[types.ModuleType]] = {}
        self._dirpath2confmods[directory] = clist
        self._get_directory = lru_cache(256)(_get_directory)
        self._import_plugin_specs(getattr(mod, "pytest_plugins", []))
        self._import_plugin_specs(os.environ.get("PYTEST_PLUGINS"))
        self._inicache: dict[str, Any] = {}
        self._inipath = inipath
        self._initini(args)
        self._loadconftestmodules(
        self._noconftest = False
        self._noconftest = noconftest
        self._opt2dest: dict[str, str] = {}
        self._override_ini = ns.override_ini or ()
        self._override_ini: Sequence[str] = ()
        self._parser = Parser(
        self._parser._config_source_hint = via  # type: ignore
        self._parser.addini(
        self._parser.addini("addopts", "Extra command line options", "args")
        self._parser.addini("minversion", "Minimally required pytest version")
        self._parser.after_preparse = True  # type: ignore
        self._parser.extra_info["inifile"] = str(self.inipath)
        self._parser.extra_info["rootdir"] = str(self.rootpath)
        self._preparse(args, addopts=addopts)
        self._rootpath = rootpath
        self._store = self.stash
        self._using_pyargs = pyargs
        self._validate_plugins()
        self._warn_about_missing_assertion(mode)
        self._warn_about_skipped_plugins()
        self.add_hookspecs(_pytest.hookspec)
        self.args: list[str] = []
        self.args_source = Config.ArgsSource.ARGS
        self.cause = cause
        self.consider_conftest(mod, registration_name=conftestpath_plugin_name)
        self.hook.pytest_addhooks.call_historic(
        self.hook.pytest_addoption.call_historic(
        self.hook: pluggy.HookRelay = PathAwareHookProxy(
        self.inicfg = inicfg
        self.invocation_params = invocation_params
        self.issue_config_time_warning(PytestConfigWarning(message), stacklevel=3)
        self.known_args_namespace = self._parser.parse_known_args(
        self.option = argparse.Namespace()
        self.path = path
        self.pluginmanager = pluginmanager
        self.pluginmanager._set_initial_conftests(
        self.pluginmanager.consider_env()
        self.pluginmanager.consider_preparse(args, exclude_only=False)
        self.pluginmanager.register(self, "pytestconfig")
        self.pluginmanager.rewrite_hook = hook
        self.register(conftestmodule, name=registration_name)
        self.register(self)
        self.rewrite_hook = _pytest.assertion.DummyRewriteHook()
        self.rewrite_hook.mark_rewrite(importspec)
        self.skipped_plugins: list[tuple[str, str]] = []
        self.stash = Stash()
        self.trace = self.pluginmanager.trace.root.get("config")
        self.trace(f"loading conftestmodule {mod!r}")
        setup.py
        src/pytest_mock.egg-info/PKG-INFO
        src/pytest_mock/__init__.py
        src/pytest_mock/_version.py
        src/pytest_mock/plugin.py
        super().__init__("pytest")
        sys.stdout.flush()
        terminalreporter: TerminalReporter | None = self.pluginmanager.get_plugin(
        testpaths: list[str],
        The default values based on ``type`` are:
        the first line in its value."""
        The object attributes are read-only.
        The value should be retrieved via a call to
        This error occurred:
        This function is mainly intended for plugins that need to issue warnings during
        To configure a level for a fine-grained verbosity type, the
        try:
        tw = TerminalWriter(sys.stderr)
        tw.code_highlight = False
        tw.code_highlight = True
        tw.hasmarkup = False
        tw.hasmarkup = True
        use (usually coinciding with pytest_unconfigure)."""
        value = None
        values: list[pathlib.Path] = []
        warn: bool,
        warn_explicit_for(cast(FunctionType, method), message)
        warnings.filterwarnings(*parse_warning_filter(arg, escape=False))
        warnings.filterwarnings(*parse_warning_filter(arg, escape=True))
        while i < n:
        while parsing the following warning configuration:
        while registering the configuration through
        while self._cleanup:
        with warnings.catch_warnings():
        with warnings.catch_warnings(record=True) as records:
        x = self.getini(name)
        x.append(line)  # modifies the cached list inline
      ``pytest_plugins`` global variables found in plugins being loaded.
    """
    """A :py:class:`pluggy.PluginManager <pluggy.PluginManager>` with
    """Access to configuration values, pluginmanager and plugin hooks.
    """Applies pytest-configured filters to the warnings module"""
    """Argparse type validator for directory arguments.
    """Argparse type validator for filename arguments.
    """Convert a string representation of truth to True or False.
    """Create a TerminalWriter instance configured according to the options
    """Encodes the valid exit codes by pytest.
    """Filter tracebacks entries which point to pytest internals or importlib.
    """Get the directory of a path - itself if already a directory."""
    """Given an iterable of file names in a source distribution, return the "names" that should
    """Indicates the source of the test arguments.
    """Obtain a new instance of the
    """Parse a plugins specification into a list of plugin names."""
    """Parse a warnings filter string.
    """Perform an in-process test run.
    """The CLI entry point of pytest.
    "assertion",
    "cacheprovider",
    "capture",
    "debugging",
    "doctest",
    "faulthandler",
    "fixtures",
    "freeze_support",
    "helpconfig",  # Provides -p.
    "junitxml",
    "legacypath",
    "logging",
    "main",
    "mark",
    "monkeypatch",
    "pastebin",
    "python",
    "python_path",
    "recwarn",
    "reports",
    "runner",
    "setuponly",
    "setupplan",
    "skipping",
    "stepwise",
    "terminal",
    "threadexception",
    "tmpdir",
    "unittest",
    "unraisableexception",
    "warnings",
    #
    # API for bootstrapping plugin loading
    # Can be inlined back (with no cover removed) once legacypath is gone.
    # Comma-separated list.
    # Direct specification.
    # Filters should be applied in the inverse order of precedence.
    # Filters should have this precedence: cmdline options, config.
    # https://docs.python.org/3/library/signal.html#note-on-sigpipe
    # Internal API for local conftest plugin handling.
    # Meant for easy monkeypatching by legacypath plugin.
    # None means empty.
    # Set by cacheprovider plugin.
    # subsequent calls to main will create a fresh instance
    # Workaround for #3899 - a submodule which happens to be called "pytest_plugins".
    #: An internal error got in the way.
    #: Command line arguments.
    #: Invocation directory.
    #: pytest couldn't find tests.
    #: pytest was interrupted.
    #: pytest was misused.
    #: 'testpaths' configuration value.
    #: Tests failed.
    #: Tests passed.
    #: Verbosity type for failed assertions (see :confval:`verbosity_assertions`).
    #: Verbosity type for test case execution (see :confval:`verbosity_test_cases`).
    (which are still very much in use for "editable" installs).
    )
    ) -> Config:
    ) -> HookimplOpts | None:
    ) -> list[pathlib.Path] | None:
    ) -> None:
    ) -> tuple[list[str], ArgsSource]:
    ) -> tuple[types.ModuleType, Any]:
    ) -> types.ModuleType:
    * ``conftest.py`` loading during start-up.
    * Does not apply the filter.
    * Escaping is optional.
    * Loading plugins from the command line, ``PYTEST_PLUGINS`` env variable and
    * Raises UsageError so we get nice error messages on failure.
    *essential_plugins,
    .. note:: Copied from distutils.util.
    .. versionadded:: 5.0
    :optname: Name of the option.
    :param args:
    :param InvocationParams invocation_params:
    :param plugins: List of plugin objects to be auto-registered during initialization.
    :param PytestPluginManager pluginmanager:
    :path: Path of directory.
    :path: Path of filename.
    :py:class:`pytest.PytestPluginManager`, with default plugins
    :returns: An exit code.
    @classmethod
    @dataclasses.dataclass(frozen=True)
    @final
    @hookimpl(trylast=True)
    @hookimpl(wrapper=True)
    @property
    @staticmethod
    __tracebackhide__ = True
    _VERBOSITY_INI_DEFAULT: Final = "auto"
    action_, message, category_, module, lineno_ = (s.strip() for s in parts)
    additional pytest-specific functionality:
    already loaded.
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    arg: str, *, escape: bool
    ARGS = enum.auto()
    args: list[str] | None = None,
    args: list[str] | os.PathLike[str] | None = None,
    be marked for assertion rewrite.
    cache: Cache
    cat = getattr(m, klass)
    class ArgsSource:
    class InvocationParams:
    config = Config(
    config = get_config(args, plugins)
    config object should use this function.
    config: Config, file: TextIO | None = None
    config_filters: Iterable[str], cmdline_filters: Iterable[str]
    Copied from warnings._getcategory, but changed so it lets exceptions (specially ImportErrors)
    Currently users and plugins may supply other exit codes as well.
    def __init__(
    def __init__(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def __str__(self) -> str:
    def _add_verbosity_ini(parser: Parser, verbosity_type: str, help: str) -> None:
    def _check_non_top_pytest_plugins(
    def _checkversion(self) -> None:
    def _consider_importhook(self, args: Sequence[str]) -> None:
    def _decide_args(
    def _do_configure(self) -> None:
    def _ensure_unconfigure(self) -> None:
    def _get_override_ini_value(self, name: str) -> str | None:
    def _get_unknown_ini_keys(self) -> list[str]:
    def _getconftest_pathlist(
    def _getconftestmodules(self, path: pathlib.Path) -> Sequence[types.ModuleType]:
    def _getini(self, name: str):
    def _getini_unknown_type(self, name: str, type: str, value: str | list[str]):
    def _import_plugin_specs(
    def _importconftest(
    def _initini(self, args: Sequence[str]) -> None:
    def _is_in_confcutdir(self, path: pathlib.Path) -> bool:
    def _loadconftestmodules(
    def _mark_plugins_for_rewrite(self, hook) -> None:
    def _preparse(self, args: list[str], addopts: bool = True) -> None:
    def _processopt(self, opt: Argument) -> None:
    def _rget_with_confmod(
    def _set_initial_conftests(
    def _try_load_conftest(
    def _validate_args(self, args: list[str], via: str) -> list[str]:
    def _validate_config_options(self) -> None:
    def _validate_plugins(self) -> None:
    def _verbosity_ini_name(verbosity_type: str) -> str:
    def _warn_about_missing_assertion(self, mode: str) -> None:
    def _warn_about_skipped_plugins(self) -> None:
    def _warn_or_fail_if_strict(self, message: str) -> None:
    def add_cleanup(self, func: Callable[[], None]) -> None:
    def addinivalue_line(self, name: str, line: str) -> None:
    def consider_conftest(
    def consider_env(self) -> None:
    def consider_module(self, mod: types.ModuleType) -> None:
    def consider_pluginarg(self, arg: str) -> None:
    def consider_preparse(
    def cwd_relative_nodeid(self, nodeid: str) -> str:
    def fromdictargs(cls, option_dict, args) -> Config:
    def get_terminal_writer(self) -> TerminalWriter:
    def get_verbosity(self, verbosity_type: str | None = None) -> int:
    def getini(self, name: str):
    def getoption(self, name: str, default=notset, skip: bool = False):
    def getplugin(self, name: str):
    def getvalue(self, name: str, path=None):
    def getvalueorskip(self, name: str, path=None):
    def hasplugin(self, name: str) -> bool:
    def import_plugin(self, modname: str, consider_entry_points: bool = False) -> None:
    def inipath(self) -> pathlib.Path | None:
    def issue_config_time_warning(self, warning: Warning, stacklevel: int) -> None:
    def notify_exception(
    def parse(self, args: list[str], addopts: bool = True) -> None:
    def parse_hookimpl_opts(
    def parse_hookspec_opts(self, module_or_class, name: str) -> HookspecOpts | None:
    def pytest_cmdline_parse(
    def pytest_collection(self) -> Generator[None, object, object]:
    def pytest_configure(self, config: Config) -> None:
    def pytest_load_initial_conftests(self, early_config: Config) -> None:
    def register(self, plugin: _PluggyPlugin, name: str | None = None) -> str | None:
    def rootpath(self) -> pathlib.Path:
    elif config.option.code_highlight == "no":
    elif config.option.color == "no":
    elif isinstance(args, os.PathLike):
    elif not isinstance(args, list):
    elif val in ("n", "no", "f", "false", "off", "0"):
    else:
    entry: _pytest._code.TracebackEntry,
    error_template = dedent(
    Every code which requires a TerminalWriter object and has access to a
    except AssertionError:
    except BaseException:
    except BrokenPipeError:
    except Exception:
    except UsageError as e:
    except warnings._OptionError as e:
    finally:
    for arg in cmdline_filters:
    for arg in config_filters:
    For example the package "pytest_mock/__init__.py" should be added as "pytest_mock" in
    for fn in package_files:
    for opt_name in opt_names:
    for spec in default_plugins:
    from _pytest.cacheprovider import Cache
    from _pytest.terminal import TerminalReporter
    Here are the file names as seen in a dist-info based distribution:
    Here are the file names as seen in an egg based distribution:
    hook_type: str,
    if "." not in category:
    if args is None:
    if args is not None:
    if config.option.code_highlight == "yes":
    if config.option.color == "yes":
    if isinstance(specs, collections.abc.Sequence):
    if isinstance(specs, str):
    if isinstance(specs, types.ModuleType):
    if len(parts) > 5:
    if lineno_:
    if message and escape:
    if module and escape:
    if must_warn:
    if not category:
    if not issubclass(cat, Warning):
    if not os.path.isdir(path):
    if not seen_some:
    if os.path.isdir(path):
    if path.is_file():
    if specs is None:
    if TYPE_CHECKING:
    if val in ("y", "yes", "t", "true", "on", "1"):
    in _pytest.pathlib.import_path.
    in the config object.
    INCOVATION_DIR = INVOCATION_DIR  # backwards compatibility alias
    INTERNAL_ERROR = 3
    INTERRUPTED = 2
    into pytest to run tests into an IDE.
    INVOCATION_DIR = enum.auto()
    known_marks: set[str] = {m.name for m in getattr(method, "pytestmark", [])}
    main = staticmethod(main)
    Make a special case for importlib because we use it to import test modules and conftest files
    method: Any,
    More information:
    must_warn: list[str] = []
    names should be considered for assertion rewriting.
    NO_TESTS_COLLECTED = 5
    OK = 0
    old_pytest_version = os.environ.get("PYTEST_VERSION")
    opt_names: tuple[str, ...],
    opts: dict[str, bool] = {}
    package_files = list(package_files)
    parts = arg.split(":")
    pluginmanager = config.pluginmanager
    pluginmanager = PytestPluginManager()
    plugins: Sequence[str | _PluggyPlugin] | None = None,
    propagate so we can get access to their tracebacks (#9218).
    raise UsageError(
    return action, message, category, module, lineno
    return cast(Type[Warning], cat)
    return config
    return filter_traceback(entry) and "importlib" not in str(entry.path).split(os.sep)
    return get_config().pluginmanager
    return opts
    return path
    return tw
    seen_some = False
    specs: None | types.ModuleType | str | Sequence[str],
    TESTPATHS = enum.auto()
    TESTS_FAILED = 1
    the assertion rewrite mechanism.
    This function can be used by integration with other tools, like hooking
    This function has to deal with dist-info based distributions and egg based distributions
    This function is not meant for programmable use; use `main()` instead.
    This is copied from warnings._setoption with the following changes:
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    try:
    tw = TerminalWriter(file=file)
    USAGE_ERROR = 4
    val = val.lower()
    'val' is anything else.
    VERBOSITY_ASSERTIONS: Final = "assertions"
    VERBOSITY_TEST_CASES: Final = "test_cases"
    We have to take in account those two distribution flavors in order to determine which
    while len(parts) < 5:
"""
"""A type to represent plugin objects.
"""Command line options, ini-file and conftest.py processing."""
# mypy: allow-untyped-defs
# Plugins that cannot be disabled via "-p no:X" currently.
)
) -> bool:
) -> Config:
) -> dict[str, bool]:
) -> int | ExitCode:
) -> list[str]:
) -> None:
) -> TerminalWriter:
) -> tuple[warnings._ActionKind, str, type[Warning], str, int]:
@final
@lru_cache(maxsize=50)
_PluggyPlugin = object
alias to make the intent clear.
builtin_plugins = set(default_plugins)
builtin_plugins.add("pytester")
builtin_plugins.add("pytester_assertions")
class cmdline:  # compatibility namespace
class Config:
class ConftestImportFailure:
class ExitCode:
class Notset:
class PytestPluginManager:
def _assertion_supported() -> bool:
def _get_directory(path: pathlib.Path) -> pathlib.Path:
def _get_legacy_hook_marks(
def _get_plugin_specs_as_list(
def _iter_rewritable_modules(package_files: Iterable[str]) -> Iterator[str]:
def _prepareconfig(
def _resolve_warning_category(category: str) -> type[Warning]:
def _strtobool(val: str) -> bool:
def apply_warning_filters(
def console_main() -> int:
def create_terminal_writer(
def directory_arg(path: str, optname: str) -> str:
def filename_arg(path: str, optname: str) -> str:
def filter_traceback_for_conftest_import_failure(
def get_config(
def get_plugin_manager() -> PytestPluginManager:
def main(
def parse_warning_filter(
default_plugins = (
essential_plugins = (
from .compat import PathAwareHookProxy
from .exceptions import PrintHelp as PrintHelp
from .exceptions import UsageError as UsageError
from .findpaths import determine_setup
from __future__ import annotations
from _pytest import __version__
from _pytest._code import ExceptionInfo
from _pytest._code import filter_traceback
from _pytest._code.code import TracebackStyle
from _pytest._io import TerminalWriter
from _pytest.config.argparsing import Argument
from _pytest.config.argparsing import Parser
from _pytest.outcomes import fail
from _pytest.outcomes import Skipped
from _pytest.pathlib import absolutepath
from _pytest.pathlib import bestrelpath
from _pytest.pathlib import import_path
from _pytest.pathlib import ImportMode
from _pytest.pathlib import resolve_package_path
from _pytest.pathlib import safe_exists
from _pytest.stash import Stash
from _pytest.warning_types import PytestConfigWarning
from _pytest.warning_types import warn_explicit_for
from functools import lru_cache
from pluggy import HookimplMarker
from pluggy import HookimplOpts
from pluggy import HookspecMarker
from pluggy import HookspecOpts
from pluggy import PluginManager
from textwrap import dedent
from types import FunctionType
from typing import Any
from typing import Callable
from typing import cast
from typing import Final
from typing import final
from typing import Generator
from typing import IO
from typing import Iterable
from typing import Iterator
from typing import Sequence
from typing import TextIO
from typing import Type
from typing import TYPE_CHECKING
hookimpl = HookimplMarker("pytest")
hookspec = HookspecMarker("pytest")
Ideally this type would be provided by pluggy itself.
if TYPE_CHECKING:
import _pytest._code
import _pytest.deprecated
import _pytest.hookspec
import argparse
import collections.abc
import copy
import dataclasses
import enum
import glob
import importlib.metadata
import inspect
import os
import pathlib
import pluggy
import re
import shlex
import sys
import types
import warnings
notset = Notset()
Plugins can be any namespace, so we can't narrow it down much, but we use an
