
--------------------
                        #  so proceed.
                        # any further conflicts with the conflicting
                        # distribution
                        # give up on this project, keep going
                        # the file became current since it was checked above,
                        # try the next older version of project
                        # Use an empty environment and workingset to avoid
                        break
                        continue
                        env = Environment([])
                        env = Environment(self.entries)
                        ind[parent] = [parts.pop()]
                        ind[parent].append(parts[-1])
                        rename(tmpnam, real_path)
                        return real_path
                        unlink(real_path)
                        ws = WorkingSet([])
                    "{} has no such extra feature {!r}".format(self, ext)
                    '"egg_name" is empty. This likely means no egg could be found from the "module_path".'
                    "name", "ver", "pyver", "plat"
                    # don't modify path (even removing duplicates) if
                    # found and not replace
                    # save error info
                    # success, no need to try any more versions of this project
                    # Windows, del old file and retry
                    **locals()
                    and macosversion >= "10.3"
                    and macosversion >= "10.4"
                    break
                    continue
                    declare_namespace(pkg)
                    distributions.update(dict.fromkeys(resolvees))
                    dversion == 7
                    eagers.extend(self.get_metadata_lines(name))
                    elif os.name == "nt":
                    else:
                    error_info[dist] = v
                    ex.add_note(info)  # PEP 678
                    if dist is None:
                    if fallback:
                    if parent in ind:
                    if self._is_current(real_path, zip_path):
                    list(map(shadow_set.add, resolvees))
                    name.replace("/", os.sep),
                    or dversion == 8
                    parent = os.sep.join(parts[:-1])
                    raise
                    raise DistributionNotFound(req, requirers)
                    req, ws, installer, replace_conflicting=replace_conflicting
                    requirers = required_by.get(req, None)
                    resolvees = shadow_set.resolve(req, env, installer)
                    return
                    return True
                    seen.add(key)
                    self.add(dist)
                    self.check_version_conflict()
                    self.PKG_INFO, path
                    yield req
                    yield section, content
                    yield self.by_key[key]
                    zfile.getinfo(name),
                " to sys.path" % (modname, fn, self.location),
                ".$extract",
                ".require separately.",
                "`base` parameter in `_fn` is `None`. Either override this method or check the parameter first."
                "and vulnerable to attack when "
                "Consider a more secure "
                "Extraction path is writable by group/others "
                "location (set with .set_extraction_path or the "
                "Module %s was already imported from %s, but %s is being added"
                '"os.rename" and "os.unlink" are not supported on this platform'
                "Parameters to load are deprecated.  Call .resolve and "
                "PYTHON_EGG_CACHE environment variable)."
                "resource_filename() only supported for .egg, not .zip"
                "Script {script!r} not found in metadata at {self.egg_info!r}".format(
                "used with get_resource_filename ({path}). "
                # ha!
                # if it's an .egg, give it precedence over its directory
                # Ignore cyclic or redundant dependencies
                # UNLESS it's already been added to sys.path and replace=False
                # workaround a cache issue
                (
                -(?P<plat>.+)
                )
                ) from e
                ),
                ):
                __import__(parent)
                _macos_arch(machine),
                0,
                break
                content = []
                continue
                del npath[np], path[np]
                deps.extend(dm[safe_extra(ext)])
                dir=os.path.dirname(real_path),
                dist = best[req.key] = env.best_match(
                dist = self.by_key.get(canonical_key)
                dists.append(dist)
                dists.sort(key=operator.attrgetter("hashcmp"), reverse=True)
                dm.setdefault(extra, []).extend(parse_requirements(reqs))
                dversion = int(provDarwin.group(1))
                else NoDists()
                else:
                Environment(plugin_dirlist)
                except ResolutionError as v:
                fixup_namespace_packages(subpath, package)
                for dist in other[project]:
                for name in zfile.namelist()
                if (
                if (not replace) and nloc in npath[p:]:
                if dist is None:
                if env is None:
                if hasattr(ex, "add_note"):
                if key not in seen:
                if not lines:
                if not only and lower.endswith(".egg-link")
                if not req.marker or req.marker.evaluate({"extra": extra}):
                if os.path.isfile(real_path):
                if path is sys.path:
                if pkg in sys.modules:
                if replace:
                if section or content:
                if self.has_metadata(name):
                info = f"(package: {self.project_name})"
                insert just ahead of the parent,
                insert just ahead of the parent.
                int(version[0]),
                int(version[1]),
                invalid_marker(marker) or not evaluate_marker(marker)
                last = self._extract_resource(manager, os.path.join(zip_path, name))
                len(script_text),
                macosversion = "{}.{}".format(reqMac.group(1), reqMac.group(2))
                modname not in sys.modules
                msg = ("Missing 'Version:' header and/or {} file at path: {}").format(
                normalize_path(fn).startswith(loc) or fn.startswith(self.location)
                np = npath.index(nloc, p + 1)
                npath.insert(p, nloc)
                or modname in _namespace_packages
                or modname in nsp
                p = np
                parts = path.split(os.sep)
                path = self._get_metadata_path_for_display(self.PKG_INFO)
                path = sys.modules[parent].__path__
                path.append(loc)
                path.insert(0, loc)
                path.insert(p, loc)
                PkgResourcesDeprecationWarning,
                plist_content = plistlib.load(fh)
                project_name, version, py_version, platform = match.group(
                r for r in reqs_for_extra(extra) if r not in common
                raise
                raise _packaging_version.InvalidVersion(f"{str(ex)} {info}") from None
                raise OSError(
                raise TypeError("Not a package:", parent) from e
                raise UnknownExtra(
                raise ValueError("Duplicate entry point", group, ep.name)
                raise ValueError("Duplicate group name", group)
                raise ValueError("Entry points must be listed in groups")
                raise ValueError("Invalid section heading", line)
                raise ValueError(msg, self) from e
                removing any lower-priority entries.
                rename(tmpnam, real_path)
                req = [dist.as_requirement()]
                req, best, replace_conflicting, env, installer, required_by, to_activate
                req.key = canonical_key
                req_extras[new_requirement] = req.extras
                reqs = []
                required_by[new_requirement].add(req.project_name)
                resolve_egg_link
                return dist
                return False
                return real_path
                script_filename,
                script_text.split("\n"),
                section = line[1:-1].strip()
                self._extract_resource(manager, self._eager_to_zip(name))
                self._get_metadata("entry_points.txt"), self
                self._parsed_version = parse_version(self.version)
                self.add(dist)
                self.check_version_conflict()
                stacklevel=2,
                try:
                version = plist_content["ProductVersion"]
                while parts:
                ws = self
                ws.add_entry(entry)
                yield key
              - Else: add it to the front of path.
              - Else: add to the end of path.
              - If it's an egg and its parent directory is on path,
              {cache_path}
              {old_exc}
              do nothing.
              or higher priority than its parent (eggs)
            - Else:
            - If location is already in path anywhere, do nothing.
            - If location is already on path anywhere (not eggs)
            """
            "Can't perform this operation for loaders without 'get_data()'"
            "Can't perform this operation for unregistered loader type"
            "SourceFileLoader",
            "SourcelessFileLoader",
            #  and temp directories are not writable by other users, so
            #  bypass the warning.
            # add plugins+libs to sys.path
            # Already checked get_data exists
            # but keeping `*args` and `**kwargs` for backwards compatibility
            # directly rather than through this class's __getattr__()
            # display errors
            # egg isn't macOS or legacy darwin
            # empty metadata dir; skip
            # Ensure all the parent's path items are reflected in the child,
            # Find the best distribution and add it to the map
            # if someone is running a non-Mac darwin system, this will fall
            # if they apply
            # ignore hidden distros
            # ignore the inevitable setuptools self-conflicts  :(
            # Include the path in the error message to simplify
            # It's not a Distribution, so they are not equal
            # Make the resource executable
            # not macOS
            # On Windows, permissions are generally restrictive by default
            # Oops, the "best" so far conflicts with a dependency
            # process dependencies breadth-first
            # push the new requirements onto the stack
            # Register the new requirements needed by req
            # report a user-friendly error
            # return a path_entry to use for child packages
            # return the extracted directory name
            # setuptools 0.6. All packages built after this point will
            # since _get_metadata_path() is marked private.
            # The main program does not list any requirements
            # this is backwards compatibility for packages built before
            # through to the default implementation
            # TODO: remove this except clause when python/cpython#103632 is fixed.
            # troubleshooting, and without changing the exception type.
            # use the new macOS designation.
            # We could pass `env` and `installer` directly,
            # We need to access _get_metadata_path() on the provider object
            # XXX add more info
            )
            ).format(**locals())
            ):
            )?
            *************************************************************************
            **kw,
            ]
            _bypass_ensure_directory(target_path)
            _data = data.items()
            _data = split_sections(data)
            _handle_ns(packageName, path_item)
            _normalize_cached(filename), os.path.basename(filename), metadata, **kw
            {str(ex)}\n{notes}
            | _InstallerType
            | _InstallerTypeT[_DistributionT]
            | {attr for attr in self._provider.__dir__() if not attr.startswith("_")}
            | None
            \n\n!!
            as a replacement to avoid breaking existing environments,
            break
            but no future compatibility is guaranteed.
            cache[script_filename] = (
            Callable[[Requirement], None]
            callback(dist)
            canonical_key = self.normalized_to_canonical_keys.get(req.key)
            Can't extract file(s) to egg cache
            cls = _distributionImpl[ext.lower()]
            code = compile(source, script_filename, "exec")
            content.append(line)
            declare_namespace(parent)
            dependent_req = required_by[req]
            DeprecationWarning,
            dist = None
            dist = self._resolve_dist(
            dist = self.by_key.get(req.key)
            dist = working_set.find(req)
            dist.insert_on(self.entries, entry, replace=replace)
            distributions, errors = working_set.find_plugins(
            dists = find_eggs_in_zip(zipimport.zipimporter(subpath), subpath)
            dists = self._distmap.setdefault(dist.key, [])
            dm.setdefault(new_extra, []).extend(reqs)
            eagers = []
            elif item == bdir and self.precedence == EGG_DIST:
            else (
            else:
            entries = sys.path
            entry
            entry = dist.location
            env += plugin_env
            env = Environment(self.entries)
            env = full_env + plugin_env
            environment variable to point to an accessible directory.
            ep = cls.parse(line, dist)
            error_cls = UnknownExtra if self.extras else AttributeError
            exc.reason += " in {} file at path: {}".format(name, path)
            except _packaging_version.InvalidVersion as ex:
            except AttributeError as e:
            except KeyError as e:
            except OSError:
            except ValueError:
            exec(code, namespace, namespace)
            exec(script_code, namespace, namespace)
            fails_marker = marker and (
            file_contents = f.read()
            filename += "-" + self.platform
            find_distributions
            fixup_namespace_packages(self.location)
            fn = getattr(sys.modules[modname], "__file__", None)
            for dist in find_distributions(item):
            for dist in plugin_env[project_name]:
            for dist in self
            for entry in dist.get_entry_map(group).values()
            for extra in self.get(req, ()) + (extras or (None,))
            for extra, reqs in split_sections(self._get_metadata(name)):
            for key in self.entry_keys[item]:
            for name in ("native_libs.txt", "eager_resources.txt"):
            for name in eagers:
            for name in self._index()[zip_path]:
            for new_requirement in new_requirements:
            for path in self.zipinfo:
            for pkg in self._get_metadata("namespace_packages.txt"):
            for project in other:
            for req in reqs:
            For the time being, `pkg_resources` will use `{self._parsed_version}`
            from __main__ import __requires__
            from linecache import cache
            frozenset(self.extras),
            group = group.strip()
            if "ProductVersion" in plist_content:
            if (
            if canonical_key is not None:
            if dist in req:
            if dist is None or (dist not in req and replace_conflicting):
            if dist not in dists:
            if entry not in ws.entries:
            if ep.name in this:
            if fails_marker:
            if fn and (
            if group in maps:
            if group is None:
            if item == nloc:
            if item not in self.entry_keys:
            if item.key != self.key:
            if line.endswith("]"):
            if match:
            if modname in ("pkg_resources", "setuptools", "site"):
            if name is None or name == entry.name
            if not only and _is_egg_path(entry)
            if not replace_conflicting:
            if not req_extras.markers_pass(req, extras):
            if not self.egg_name:
            if parent not in _namespace_packages:
            if path is sys.path:
            if provDarwin:
            if replace:
            if req in processed:
            if self._is_current(real_path, zip_path):
            if self[key]:
            if subpath:
            if version is None:
            If you maintain package {self.project_name} you should implement
            ind = {}
            issue_warning(
            issue_warning("Unbuilt egg for " + repr(self))
            item = item.version
            items = (
            keys.append(dist.key)
            keys2.append(dist.key)
            kw.setdefault(attr, getattr(self, attr, None))
            level += 1
            loader = importer.find_module(packageName)
            loader_cls = getattr(importlib.machinery, name, type(None))
            location,
            machine = os.uname()[4].replace(" ", "_")
            manager.extraction_error()
            manager.postprocess(tmpnam, real_path)
            manifest = self.build(path)
            map(working_set.add, distributions)
            maps[group] = cls.parse_group(group, lines, dist)
            match = EGG_NAME(basename)
            metadata = f.read()
            metadata = self.get_metadata(self.PKG_INFO)
            metadata,
            metadata=PathMetadata(path_item, os.path.join(path_item, "EGG-INFO")),
            mkdir(dirname, 0o755)
            mode = ((os.stat(tempname).st_mode) | 0o555) & 0o7777
            msg = "EntryPoint must be in 'name=module:attrs [extras]' format"
            msg = (
            msg = f"""!!\n\n
            msg = tmpl.format(**locals())
            msg[:-1] + " and will raise exceptions in a future release.",
            name = some.module:some.attr [extra1, extra2]
            new += env
            new_extra = safe_extra(new_extra) or None
            new_extra, _, marker = extra.partition(":")
            new_extra: str | None = extra
            new_requirements = dist.requires(req.extras)[::-1]
            notes = "\n".join(getattr(ex, "__notes__", []))  # PEP 678
            or dist.py_version == self.python
            or dist.py_version is None
            or ntpath.isabs(path)
            or path.startswith("\\")
            or posixpath.isabs(path)
            os.chmod(tempname, mode)
            os.close(outf)
            os.path.pardir in path.split(posixpath.sep)
            os.write(outf, self.loader.get_data(zip_path))
            outf, tmpnam = _mkstemp(
            pass
            path = self._provider._get_metadata_path(name)
            path = sys.path
            path_item,
            Perhaps your account does not have write access to this directory?
            plat = "macosx-{}-{}".format(".".join(_macos_vers()[:2]), m.group(3))
            platform=platform,
            print('Could not load', errors)
            processed.add(req)
            project_name=project_name,
            provDarwin = darwinVersionString.match(provided)
            -py(?P<pyver>[^-]+) (
            py_version=py_version,
            raise
            raise AttributeError(attr)
            raise error_cls("Can't require() without a distribution", self)
            raise ImportError("Entry point {!r} not found".format((group, name)))
            raise ImportError(str(exc)) from exc
            raise KeyError("No metadata except PKG-INFO is available")
            raise NotImplementedError(
            raise OSError(
            raise ResolutionError(
            raise TypeError(
            raise TypeError("Can't add {!r} to environment".format(other))
            raise ValueError
            raise ValueError("Can't change extraction path, files already extracted")
            raise ValueError("Invalid group name", group)
            raise ValueError("Invalid module name", module_name)
            raise ValueError(msg)
            raise ValueError(msg, src)
            raise VersionConflict(dist, req)
            raise VersionConflict(dist, req).with_context(dependent_req)
            real_path = manager.get_cache_path(self.egg_name, self._parts(zip_path))
            register_loader_type(loader_cls, cls)
            req = requirements.pop(0)
            req.marker.evaluate({"extra": extra})
            reqs = dm.pop(extra)
            reqs.extend(parse_requirements(req))
            requirements.extend(new_requirements)
            return
            return ""
            return "[could not detect]"
            return "{} ({})".format(self, self.location)
            return "macosx-%d.%d-%s" % (
            return "the application"
            return ()
            return cls._build_from_requirements(__requires__)
            return dict(items)
            return dist
            return f.read()
            return False
            return float("inf")
            return fspath[len(self.egg_root) + 1:].split(os.sep)
            return fspath[len(self.zip_pre):]
            return functools.reduce(getattr, self.attrs, module)
            return ind
            return key
            return os.path.dirname(last)
            return os.path.join(base, *resource_name.split("/"))
            return registry[t]
            return self
            return self.__dep_map
            return self._dirindex
            return self._ep_map.get(group, {})
            return self._key
            return self._listdir(self._fn(self.egg_info, name))
            return self._parsed_version
            return self._pkg_info
            return self._version
            return self.loader.get_data(path)  # type: ignore[attr-defined]
            return self.parsed_version
            return str(self)
            return stream.read()
            return sys_path.index(entry)
            return value.decode("utf-8")
            return version
            return ws
            s += " [%s]" % ",".join(self.extras)
            s += ":" + ".".join(self.attrs)
            s_extra = safe_extra(extra.strip())
            script_code = compile(script_text, script_filename, "exec")
            search_path = sys.path
            self, resource_name
            self.__dep_map = self._compute_dependencies()
            self.__dep_map = self._filter_extras(self._build_dep_map())
            self.__dep_map[s_extra] = [
            self._dirindex = ind
            self._ep_map = EntryPoint.parse_map(
            self._forgiving_parsed_version,
            self._key = key = self.project_name.lower()
            self._parsed_version = parse_version(_forgiving_version(self.version))
            self._pkg_info = email.parser.Parser().parsestr(metadata)
            self._version = md_version
            self._version = safe_version(version)
            self.add(dist)
            self.add(dist, entry, False)
            self.add(other)
            self.add_entry(entry)
            self.by_key.copy(),
            self.callbacks[:],
            self.eagers = eagers
            self.entries[:],
            self.entry_keys.copy(),
            self.extraction_error()
            self.key,
            self.location,
            self.module_path = importer.archive
            self.module_path = os.path.join(importer.archive, importer.prefix)
            self.normalized_to_canonical_keys.copy(),
            self.platform or "",
            self.precedence,
            self.py_version or "",
            self.py_version or PY_MAJOR,
            self.python is None
            self.require(*args, **kwargs)  # type: ignore
            self.specifier,
            self.url,
            self.version
            self[path] = self.manifest_mod(manifest, mtime)
            set(super().__dir__())
            source = _read_utf8_with_fallback(script_filename)
            spec = "{}=={}".format(self.project_name, self.parsed_version)
            spec = "{}==={}".format(self.project_name, self.parsed_version)
            str(self.marker) if self.marker else None,
            submeta = EggMetadata(zipimport.zipimporter(subpath))
            submeta.egg_info = subpath
            subpath = _handle_ns(package, path_item)
            subpath = os.path.join(path_item, subitem)
            The following error occurred while trying to extract file(s)
            The Python egg cache directory is currently set to:
            the relevant changes to adequate the project to PEP 440 immediately.
            This is a long overdue deprecation.
            this[ep.name] = ep
            tmpl = "{self.path} could not be properly decoded in UTF-8"
            to the Python egg cache:
            to_activate.append(dist)
            to_filename(self.project_name),
            to_filename(self.version),
            try:
            utime(tmpnam, (timestamp, timestamp))
            version = _macos_vers()
            version = getattr(self, "version", None)
            version = None
            version = self._get_version()
            version=version,
            warnings.simplefilter("ignore")
            warnings.warn(
            warnings.warn(msg)
            warnings.warn(msg, DeprecationWarning)
            warnings.warn(msg, UserWarning)
            with open(plist, "rb") as fh:
            ws.add(dist)
            ws.require(__requires__)
            yield Distribution.from_location(path_item, subitem, submeta)
            yield from dists
            yield from self.get_metadata_lines(name)
            yield line
            You can change the cache directory by setting the PYTHON_EGG_CACHE
        """
        """Add `dist` if we ``can_add()`` it and it has not already been added"""
        """Add `dist` to working set, associated with `entry`
        """Add a path item to ``.entries``, finding any distributions on it
        """Add an environment or distribution to an environment"""
        """Copy this distribution, substituting in any changed keyword args"""
        """Create a metadata provider from a zipimporter"""
        """Create working set from list of path entries (default=sys.path)"""
        """Delegate all unrecognized public attributes to .metadata provider"""
        """DO NOT CALL THIS UNDOCUMENTED METHOD; use Requirement.parse()!"""
        """Does the named resource exist?"""
        """Does the package contain the named resource?"""
        """Does the package's distribution contain the named metadata?"""
        """Ensure distribution is importable on `path` (default=sys.path)"""
        """Ensure self.location is on path
        """Ensure that distributions matching `requirements` are activated
        """Execute the named script in the supplied namespace dictionary"""
        """Find a distribution matching requirement `req`
        """Find all activatable distributions in `plugin_env`
        """Find distribution best matching `req` and usable on `working_set`
        """Give an error message for problems extracting file(s)"""
        """In-place addition of a distribution or environment"""
        """Invoke `callback` for all distributions
        """Is distribution `dist` acceptable for this environment?
        """Is the named metadata a directory?  (like ``os.path.isdir()``)"""
        """Is the named resource a directory?  (like ``os.path.isdir()``)"""
        """Is the named resource an existing directory?"""
        """List all distributions needed to (recursively) meet `requirements`
        """List of metadata names in the directory (like ``os.listdir()``)"""
        """List of Requirements needed for this distro if `extras` are used"""
        """List of resource names in the directory (like ``os.listdir()``)"""
        """List the contents of the named resource directory"""
        """Locate distribution for `requires` and run `script_name` script"""
        """Obtain a distribution matching `requirement` (e.g. via download)
        """Parse a map of entry point groups"""
        """Parse a single entry point from string `src`
        """Parse an entry point group"""
        """Parse and cache metadata"""
        """Perform any platform-specific postprocessing of `tempname`
        """Recompute this distribution's dependencies."""
        """Remove `dist` from the environment"""
        """Return a ``Requirement`` that matches this distribution exactly"""
        """Return a newest-to-oldest list of distributions for `project_name`
        """Return a readable file-like object for `resource_name`
        """Return a readable file-like object for specified resource"""
        """Return a true filesystem path for `resource_name`
        """Return a true filesystem path for specified resource"""
        """Return absolute location in cache for `archive_name` and `names`
        """Return specified resource as :obj:`bytes`"""
        """Return the `name` entry point of `group` or raise ImportError"""
        """Return the contents of `resource_name` as :obj:`bytes`
        """Return the entry point map for `group`, or the full entry map"""
        """Return the EntryPoint object for `group`+`name`, or ``None``"""
        """Return what this distribution's standard .egg filename should be"""
        """Scan `search_path` for distributions usable in this environment
        """Set the base path where resources will be extracted to, if needed.
        """Snapshot distributions available on a search path
        """The named metadata resource as a string"""
        """True if `dist` is the active distribution for its project"""
        """Yield distributions for non-duplicate projects in the working set
        """Yield entry point objects from `group` matching `name`
        """Yield named metadata resource as list of non-blank non-comment lines
        """Yield the unique project names of the available distributions"""
        "and is required by {self.requirers_str}"
        "Implementing implicit namespace packages (as specified in PEP 420) "
        "is preferred to `pkg_resources.declare_namespace`. "
        "keywords.html#keyword-namespace-packages"
        "See https://setuptools.pypa.io/en/latest/references/"
        "The '{self.req}' distribution was not found "
        #       See comment in setuptools.unicode_utils._Utf8EncodingNeeded
        # 1980 offset already done
        # add any missing entries from sys.path
        # Aggressively disallow Windows absolute paths
        # Allow prereleases always in order to match the previous behavior of
        # and then put it back
        # are they the same major version and machine type?
        # Assume that metadata may be nested inside a "basket"
        # Bad type narrowing, dist has to be a Requirement here, so get_provider has to return Distribution
        # by starting with an empty path
        # capture warnings due to #1111
        # check that the contents match
        # Convert a virtual filename (full path to file) into a zipfile subpath
        # Convert a zipfile subpath into an egg-relative path part list.
        # Development eggs:
        # dist-info distributions, the working set will assume that the
        # don't yield nested distros
        # easy case
        # ensure the requirements are met
        # find the first stack frame that is *not* code in
        # for compatibility, warn; in future
        # Get the requirements for this entry point with all its extras and
        # Handle exceptions e.g. in case the distribution's metadata
        # Ignore the directory if does not exist, not a directory or
        # Including any condition expressions
        # is the required OS major update >= the provided one?
        # is this a Mac package?
        # key -> dist
        # Mapping of requirement to set of distributions that required it;
        # more accurately.
        # no need to lock for extraction, since we use temp names
        # normalize the version
        # of multiple eggs and use module_path instead of .archive.
        # Only return the path if it's not already there
        # p is the spot where we found or inserted loc; now remove duplicates
        # packaging.requirements.Requirement uses a set for its extras. We use a variable-length tuple
        # permission denied
        # provider doesn't support _get_metadata_path().
        # pseudo-fs path
        # put all our entries in shadow_set
        # raise ValueError(msg)
        # requirements for that extra are purely optional and skip over them.
        # return list of distros to activate
        # scan project names in alphabetic order
        # set of processed requirements
        # set up the stack
        # temporarily bypass sandboxing
        # that the working set knows what extras we want. Otherwise, for
        # the pkg_resources module, to use for the warning
        # then copy back to sys.path
        # then resolve them. We have to pass `extras` along when resolving so
        # they can be updated
        # they don't have PKG-INFO metadata, and won't ever contain eggs
        # this method. In the future this should be smarter and follow PEP 440
        # TODO: Add a deadline?
        # Track what packages are namespaces, so when new path items are added,
        # try it without defaults already on sys.path
        # try to download/install
        # Unpacked egg directories:
        # Unsafely unpacking. But keeping **kw for backwards and subclassing compatibility
        # usable with the zipimport directory cache for our target archive
        # useful for reporting info about conflicts.
        # wheels are not supported with this finder
        # XXX
        # ymdhms+wday, yday, dst
        -(?P<ver>[^-]+) (
        (e.g. by updating `build-system.requires` in its `pyproject.toml`)
        (name, getattr(manager, name))
        (Note: you may not change the extraction path for a given resource
        (req,) = parse_requirements(s)
        (This is because ``sys.path`` can contain the same value more than
        )
        ) = None,
        )._reload_version()
        ).lstrip()
        )?
        ********************************************************************************
        **kw: int,  # We could set `precedence` explicitly, but keeping this as `**kw` for full backwards and subclassing compatibility
        **kwargs: Any,
        **kwargs: Environment | _InstallerType | None,
        *,
        *args: Any,
        *args: Environment | _InstallerType | None,
        ...
        __import__(moduleOrReq)
        _bypass_ensure_directory(dirname)
        _data: Iterable[tuple[str | None, str | Iterable[str]]]
        _imp.release_lock()
        _namespace_packages.setdefault(packageName, [])
        _namespace_packages.setdefault(parent or None, []).append(packageName)
        _rebuild_mod_path(path, packageName, module)
        _set_parent_ns(packageName)
        ``[extras]`` parts are optional
        ``atexit`` function if you wish to ensure cleanup of a temporary
        ``cleanup_resources()`` will be able to remove all extracted files.
        ``cleanup_resources()``.)
        ``find_distributions(entry, True)`` is used to find distributions
        ``installer(requirement)``, unless `installer` is None, in which case
        ``None``.
        ``resolve()`` method. The `fallback` flag indicates whether we should
        ``sys.path`` will be scanned for distributions.
        ``VersionConflict`` if an unsuitable version of the project is already
        ``VersionConflict`` instance.
        `dist` is only added to the working set if it's for a project that
        `distributions` is a list of the distributions found in `plugin_env`
        `encoding="utf-8"` fails with {file!r}, trying `encoding={fallback_encoding!r}`.
        `extras` is a list of the extras to be used with these requirements.
        `installer` is a standard installer callback as used by the
        `manager` must be a ``ResourceManager``"""
        `platform` is an optional string specifying the name of the platform
        `req`.  But, if there is an active distribution for the project and it
        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        `requirements` must be a string or a (possibly-nested) sequence
        `search_path` should be a sequence of ``sys.path`` items.  If not
        `setuptools/pkg_resources` may not implement it.
        `tempname` is the current (temporary) name of the file, and `filename`
        >>> bool(warned)
        >>> vrp = NullProvider._validate_resource_path
        >>> vrp('')
        >>> vrp('../foo/bar.txt')
        >>> vrp('/foo/bar.txt')
        >>> vrp('foo/../../bar.txt')
        >>> vrp('foo/bar.txt')
        >>> vrp('foo/f../bar.txt')
        >>> vrp(None)
        >>> vrp(r'\\foo/bar.txt')
        >>> vrp(r'C:\\foo/bar.txt')
        >>> warned = getfixture('recwarn')
        >>> warned.clear()
        >>> warnings.simplefilter('always')
        1.11.0.dev0_2329eae). These distributions will not be
        A map of extra to its list of (direct) requirements
        activated to fulfill the requirements; all relevant distributions are
        active in the specified `working_set`.)  If a suitable distribution
        added to the working set.
        already-installed distribution; it should return a ``Distribution`` or
        always appended to ``.entries``, even if it is already present.
        and os.path.isfile(path)
        and re-building/re-installing the package with a newer version of `setuptools`
        and zipfile.is_zipfile(path)
        Any distributions found are added to the environment.
        Any distributions found on `search_path` are added to the environment.
        any requirements are found on the path that have the correct name but
        args = self.args + (required_by,)
        attempt to resolve older versions of a plugin if the newest version
        AttributeError: ...
        attrs = res["attr"].split(".") if res["attr"] else ()
        attrs: Iterable[str] = (),
        automatically called; you must call it explicitly or register it as an
        base ``Environment`` class, this routine just returns
        base_dir = os.path.dirname(egg_info)
        basename, ext = os.path.splitext(basename)
        basename: StrPath,
        bdir = os.path.dirname(nloc)
        best = {}
        Blank values are allowed
        both `group` and `name` are yielded (in distribution order).
        Build a dictionary similar to the zipimport directory
        Build a working set from a requirement spec. Rewrites sys.path.
        cache_path = self.extraction_path or get_default_cache()
        caches, except instead of tuples, store ZipInfo objects.
        call on all existing ones, as well.
        calling the environment's ``obtain(req, installer)`` method will be
        cannot be resolved.
        cls,
        common = types.MappingProxyType(dict.fromkeys(reqs_for_extra(None)))
        contains all currently-available distributions.  If `full_env` is not
        ContextualVersionConflict.
        converted to filenames (e.g., 1.11.0.dev0+2329eae to
        corresponding to the path entry, and they are added.  `entry` is
        data: str | Iterable[str] | dict[str, str | Iterable[str]],
        date_time = zip_stat.date_time + (0, 0, -1)
        def namespace_handler(importer, path_entry, moduleName, module):
        def reqs_for_extra(extra):
        Delete all extracted resource files and directories, returning a list
        delete the extracted files when done.  There is no guarantee that
        demanded it.
        deps.extend(dm.get(None, ()))
        deps: list[Requirement] = []
        details.)
        dict[Distribution, Exception],
        directories. The `full_env`, if supplied, should be an ``Environment``
        directory exclusive to a single process.  This method is not
        directory used for extractions.
        dist = best.get(req.key)
        dist = Distribution(basedir, project_name=dist_name, metadata=metadata)
        dist = Distribution.from_filename(egg_path, metadata=metadata)
        dist = get_provider(dist)  # type: ignore[assignment]
        dist = Requirement.parse(dist)
        dist = self.by_key.get(req.key)
        dist: Distribution | None = None,
        dist: Distribution,
        dist_name = os.path.splitext(os.path.basename(egg_info))[0]
        distribution is found, and `installer` is supplied, then the result of
        distribution_key = project_name.lower()
        distributions in the working set, otherwise only ones matching
        distributions: dict[Distribution, Exception | None] = {}
        distributions_from_metadata
        dists = ws.resolve(reqs, Environment())
        dm = {}
        dm = self._dep_map
        does *not* meet the `req` requirement, ``VersionConflict`` is raised.
        doesn't already have a distribution in the set, unless `replace=True`.
        downstream by Distribution and safe_version, so
        e.filename = None
        e.lineno = None
        eagers = self._get_eager_resources()
        egg = next(eggs, None)
        egg and self._set_egg(egg)
        egg_info = "/path/to/PackageName.egg-info"
        egg_path = "/path/to/PackageName-ver-pyver-etc.egg"
        eggs = filter(_is_egg_path, _parents(self.module_path))
        elif isinstance(other, Environment):
        elif subitem.lower().endswith((".dist-info", ".egg-info")):
        else (
        else:
        enclosing egg (which may not be the name of the enclosing zipfile!),
        entries, keys, by_key, normalized_to_canonical_keys, callbacks = e_k_b_n_c
        entry or distribution in the working set.  `installer`, if supplied,
        Entry point syntax follows the form::
        entry,
        entry: str | None = None,
        env: Environment | None = None,
        env: Environment | None,
        environment markers and filter out any dependencies
        environment that meets the ``Requirement`` in `req`.  If no suitable
        ep = self.get_entry_info(group, name)
        equal ``sys.path``.)
        err = ExtractionError(tmpl.format(**locals()))
        err.cache_path = cache_path
        err.manager = self
        err.original_error = old_exc
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        error_info: dict[Distribution, Exception] = {}
        Evaluate markers for req against each extra that
        evaluate_marker(text)
        evaluation. Otherwise, return True.
        Example usage::
        except _packaging_version.InvalidVersion as ex:
        except AttributeError as e:
        except AttributeError as exc:
        except AttributeError:
        except Exception:
        except FileExistsError:
        except ImportError:
        except OSError:
        except SystemError:
        except UnicodeDecodeError as exc:
        except ValueError:
        except VersionConflict:
        existing=False,
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        extra_evals = (
        extract, as it tracks the generated names for possible cleanup later.
        extract_path = self.extraction_path or get_default_cache()
        extracting a compressed resource.  They must NOT call it on resources
        extras = cls._parse_extras(res["extras"])
        extras: Iterable[str] = (),
        extras: tuple[str, ...] | None = None,
        f"Deprecated call to `pkg_resources.declare_namespace({packageName!r})`.\n"
        factory = dist_factory(path_item, entry, only)
        fallback: bool = True,
        False
        filename = "{}-{}-py{}".format(
        filename: StrPath,
        for attr in names.split():
        for callback in self.callbacks:
        for compatibility with pypy on Windows.
        for dist in dists:
        for dist in find_distributions(entry, True):
        for dist in needed:
        for dist in self:
        for dist in self[req.key]:
        for entry in entries:
        for entry in sys.path:
        for env in self, other:
        for ext in extras:
        for extra in list(filter(None, dm)):
        for extra in self._parsed_pkg_info.get_all("Provides-Extra") or []:
        for group, lines in _data:
        for item in search_path:
        for item in self.entries:
        for key in self._distmap.keys():
        for line in yield_lines(lines):
        for modname in self._get_metadata("top_level.txt"):
        for name in "requires.txt", "depends.txt":
        for name in dir(manager)
        for name in loader_names:
        for p, item in enumerate(npath):
        for package in _namespace_packages.get(parent, ()):
        for path_item in path:
        for project_name in plugin_projects:
        for req in self._parsed_pkg_info.get_all("Requires-Dist") or []:
        for this distribution, including the null extra.
        fspath = fspath.rstrip(os.sep)
        fspath = self.zip_pre + zip_path
        full_env: Environment | None = None,
        full_env: Environment | None,
        fullpath = os.path.join(path_item, entry)
        g["_sset_" + _state_vars[k]](k, g[k], v)
        generally only be called when the extraction path is a temporary
        Given a mapping of extras to dependencies, strip off
        group: str,
        have anything special they should do.
        https://setuptools.pypa.io/en/latest/pkg_resources.html#basic-resource-access
        if
        if "/".join(self._parts(zip_path)) in eagers:
        if (path.startswith("\\") or ntpath.isabs(path)) and not posixpath.isabs(path):
        if _is_egg_path(subitem):
        if _normalize_cached(item) == normalized:
        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        If `existing=True` (default),
        If `name` is None, yields all entry points in `group` from all
        if a known insecure location is used.
        if attr.startswith("_"):
        if base is None:
        if callback in self.callbacks:
        if dist is None:
        if dist is not None and dist not in req:
        if dist is not None:
        if dist not in req:
        if dist.key not in keys:
        if dist.key not in keys2:
        if e.errno not in (errno.ENOTDIR, errno.EACCES, errno.ENOENT):
        if entries is None:
        if entry is None:
        if ep is None:
        if ext.lower() in _distributionImpl:
        if fspath == self.loader.archive:
        if fspath.startswith(self.egg_root + os.sep):
        if fspath.startswith(self.zip_pre):
        if full_env is None:
        if group is not None:
        if hasattr(self.loader, "get_data") and self.loader:
        if importer.prefix:
        if insert:
        if int(provMac.group(2)) > int(reqMac.group(2)):
        if is_meta
        if isinstance(data, dict):
        if isinstance(item, Distribution):
        if isinstance(other, Distribution):
        if isinstance(self.parsed_version, _packaging_version.Version):
        If it's added, any callbacks registered with the ``subscribe()`` method
        if len(os.listdir(path)) == 0:
        if line.startswith("["):
        if line:
        if md_version:
        if mode & stat.S_IWOTH or mode & stat.S_IWGRP:
        if name != "PKG-INFO":
        if not existing:
        if not extras_spec:
        if not hasattr(self, "_ep_map"):
        if not hasattr(self, "_parsed_version"):
        if not invalid:
        if not isinstance(other, self.__class__):
        if not loc:
        if not m:
        if not MODULE(group):
        if not MODULE(module_name):
        if not name.startswith("_")
        if not os.path.isfile(file_path):
        if not provMac:
        if not replace and dist.key in self.by_key:
        if not require or args or kwargs:
        if not required_by:
        if not self.dist:
        if not self.egg_info:
        if not self.egg_name:
        if not self.has_metadata(script):
        if not self.requirers:
        if not WRITE_SUPPORT:
        if os.name == "nt" and not path.startswith(os.environ["windir"]):
        if os.name == "posix":
        if os.path.exists(plist):
        if os.path.exists(script_filename):
        if packageName in _namespace_packages:
        if parent:
        if path is None:
        if path is sys.path and self.location is not None:
        if path not in self or self[path].mtime != mtime:
        if provMac.group(1) != reqMac.group(1) or provMac.group(3) != reqMac.group(3):
        If replace=False (default):
        If replace=True:
        if replacement_char in metadata:
        if req.specs:
        if require:
        If required_by is non-empty, return a version of self that is a
        if resource_name:
        if search_path is None:
        if self.attrs:
        if self.cached_files:
        if self.can_add(dist) and dist.has_version():
        if self.eagers is None:
        if self.egg_info:
        if self.extras:
        if self.has_metadata(name):
        if self.key == "setuptools":
        if self.location:
        if self.platform:
        if stat.st_size != size or stat.st_mtime != timestamp:
        if supplied, should be an ``Environment`` instance.  If
        if t in registry:
        If the default extraction path is overridden and set to an insecure
        If there is an active distribution for the requested project, this
        If there is no active distribution for the requested project, ``None``
        If this file was produced by `setuptools` itself, cleaning up the cached files
        if version is not None:
        If you do not call this routine before any extractions take place, the
        if zip_path in self._index():
        importlib.import_module(packageName)
        included, even if they were already activated in this working set.
        including its ".egg" extension.  `names`, if provided, should be a
        information given by the ``IResourceProvider``.  You may set this to a
        insert: bool = True,
        installer: (
        installer: _InstallerType | None | _InstallerTypeT[_DistributionT] = None,
        installer: _InstallerType | None = None,
        installer: _InstallerTypeT[_DistributionT],
        installer: Callable[[Requirement], None] | None = None,
        invalid = (
        invoked to obtain the correct version of the requirement and activate
        is based on the ``PYTHON_EGG_CACHE`` environment variable, with various
        is returned.
        is the name it will be renamed to by the caller after this routine
        isn't active, this method returns the newest distribution in the
        issue_warning(
        it defaults to the current version.
        it.
        items = working_set.resolve(reqs, env, installer, extras=self.extras)
        keys = self.entry_keys.setdefault(entry, [])
        keys2 = self.entry_keys.setdefault(dist.location, [])
        kw.setdefault("metadata", self._provider)
        lambda dist: dist.activate(replace=True),
        last = path
        Leading and trailing whitespace is stripped from each line, and lines
        line = line.strip()
        lines = self._get_metadata(self.PKG_INFO)
        lines: _NestedStr,
        list(map(shadow_set.add, self))
        list(map(working_set.add, items))
        list[Distribution] | list[_DistributionT],
        Load a manifest at path or return a suitable manifest already loaded.
        loader = spec.loader if spec else None
        loader_names = (
        loc = loc or self.location
        loc = normalize_path(self.location)
        loc=None,
        location, such as /tmp, it opens up an opportunity for an attacker to
        location: str | None = None,
        location: str,
        lowercase as their key.
        m = cls.pattern.match(src)
        manager once resources have been extracted, unless you first call
        maps: dict[str, dict[str, Self]] = {}
        marker = _packaging_markers.Marker(text)
        md_version = self._get_version()
        metadata = FileMetadata("/path/to/PKG-INFO")
        metadata = FileMetadata(path)
        metadata = PathMetadata(base_dir, egg_info)
        metadata = PathMetadata(egg_path, os.path.join(egg_path,'EGG-INFO'))
        metadata,
        metadata: _MetadataType = None,
        metadata: _MetadataType = PathMetadata(root, path)
        method is called on, which will typically mean that every directory on
        might solve the problem.
        mode = os.stat(path).st_mode
        module = __import__(self.module_name, fromlist=["__name__"], level=0)
        module = sys.modules[moduleOrReq]
        module = sys.modules[packageName] = types.ModuleType(packageName)
        module.__path__ = []
        module.__path__ = new_path
        module.__path__[:] = new_path
        module_name: str,
        module_parts = package_name.count(".") + 1
        msg = "Use of .. or absolute path in a resource path is not allowed."
        msg = f"""\
        mtime = os.stat(path).st_mtime
        name = ns["__name__"]
        name: str,
        names = "project_name version py_version platform location precedence"
        namespace["__file__"] = script_filename
        needed = self.resolve(parse_requirements(requirements))
        new = self.__class__([], platform=None, python=None)
        nloc = _normalize_cached(loc)
        None is returned instead.  This method is a hook that allows subclasses
        Non-string values are not.
        normalized_name = _packaging_utils.canonicalize_name(dist.key)
        not already exist.  `archive_name` should be the base filename of the
        not matching the markers.
        not supplied, it defaults to all distributions available within any
        npath = [(p and _normalize_cached(p) or p) for p in path]
        ns = sys._getframe(1).f_globals
        ns.clear()
        ns["__name__"] = name
        nsp = dict.fromkeys(self._get_metadata("namespace_packages.txt"))
        Obtain a distro that matches requirement (e.g. via download).  In the
        obtain an extraction location, and only for names they intend to
        of the file and directory names that could not be successfully removed.
        old_exc = sys.exc_info()[1]
        On exit from this routine, `entry` is added to the end of the working
        once, and the ``.entries`` of the ``sys.path`` WorkingSet should always
        only distributions that are in the project's "plugin directory" or
        optional requirement.  Instead, we want to be able to assert that these
        optional string naming the desired version of Python (e.g. ``'3.6'``);
        os.open = old_open
        os.open = os_open
        os.path.join(os.path.dirname(path), ref) for ref in referenced_paths
        os.path.join(path, "EGG-INFO", "PKG-INFO")
        os.path.join(path_item, entry)
        Packages installed by distutils (e.g. numpy or scipy),
        parent = ".".join(parts)
        parent, _, _ = packageName.rpartition(".")
        parsed properly
        parts = path_parts[:-module_parts]
        pass
        path = module.__path__
        path = os.path.normpath(path)
        path = self._get_metadata_path(name)
        path defaults to the return value of ``get_default_cache()``.  (Which
        path, _ = os.path.split(path)
        path.append(subpath)
        path.lower().endswith(".egg")
        path: list[str],
        path: MutableSequence[str] = sys.path
        path_parts = path.split(os.sep)
        platform: str | None = get_supported_platform(),
        platform: str | None = None,
        platform-specific fallbacks.  See that routine's documentation for more
        Please encode {file!r} with "utf-8" to ensure future builds will succeed.
        plist = "/System/Library/CoreServices/SystemVersion.plist"
        plugin_env: Environment,
        plugin_projects = list(plugin_env)
        plugin_projects.sort()
        precedence: int = EGG_DIST,
        precedence=DEVELOP_DIST,
        Prepare the master working set.
        processed = set()
        project_name = safe_name(self.name)
        project_name, version, py_version, platform = [None] * 4
        project_name: str | None = None,
        project's distributions use their project's name converted to all
        provMac = macosVersionString.match(provided)
        py_compat = (
        py_version: str | None = PY_MAJOR,
        python: str | None = PY_MAJOR,
        r"(:\s*(?P<attr>[\w.]+))?\s*"
        r"(?P<extras>\[.*\])?\s*$"
        r"(?P<module>[\w.]+)\s*"
        r"(?P<name>.+?)\s*"
        r"\s*"
        r"=\s*"
        raise AssertionError("{} is not a subpath of {}".format(fspath, self.egg_root))
        raise AssertionError("{} is not a subpath of {}".format(fspath, self.zip_pre))
        raise err
        raise NotImplementedError(
        raise OSError('"os.mkdir" not supported on this platform.')
        raise SyntaxError(e) from e
        raise TypeError("Expected str, Requirement, or Distribution", dist)
        raise TypeError("Not a package:", packageName)
        replace an extracted file with an unauthorized payload. Warn the user
        replace: bool = False,
        replace_conflicting: bool = False,
        replacement_char = "�"
        req = Requirement.parse("x" + extras_spec)
        req: Requirement,
        req_extras = _ReqExtras()
        reqs = parse_requirements(req_spec)
        reqs = self.dist.requires(self.extras)
        reqs: list[Requirement] = []
        Require packages for this EntryPoint, then resolve it.
        require: bool = True,
        require: Literal[False],
        require: Literal[True] = True,
        required_by = collections.defaultdict(set)
        requirement: Requirement,
        requirements = list(requirements)[::-1]
        requirements are truly required.
        requirements specified when this environment was created, or False
        requirements: Iterable[Requirement],
        res = m.groupdict()
        Resolve the entry point from its module and attrs.
        Resource providers should call this method ONLY after successfully
        Resources are extracted to subdirectories of this path based upon
        rest = version
        rest = version[len(safe):]
        return
        return ", ".join(self.requirers)
        return "{} {}".format(self.project_name, version)
        return "EntryPoint.parse(%r)" % str(self)
        return "Requirement.parse(%r)" % str(self)
        return (
        return []
        return [dep for dep in self._dep_map if dep]
        return _version_from_file(lines)
        return b""
        return base
        return bool(self.egg_info and self._isdir(self._fn(self.egg_info, name)))
        return classes + (object,)
        return cls(
        return cls(res["name"], res["module"], attrs, extras, dist)
        return cls.from_location(
        return ContextualVersionConflict(*args)
        return deps
        return dist
        return dm
        return e
        return ep.load()
        return False
        Return False if the req has a marker and fails
        return filename
        return get_provider(package_or_requirement).get_resource_filename(
        return get_provider(package_or_requirement).get_resource_stream(
        return get_provider(package_or_requirement).get_resource_string(
        return get_provider(package_or_requirement).has_resource(resource_name)
        return get_provider(package_or_requirement).resource_isdir(resource_name)
        return get_provider(package_or_requirement).resource_listdir(resource_name)
        return getattr(self._provider, attr)
        return hash(self.hashcmp)
        return installer(requirement) if installer else None
        return io.BytesIO(self.get_resource_string(manager, resource_name))
        return isinstance(other, Requirement) and self.hashCmp == other.hashCmp
        return iter(())
        return line.lower().startswith("version:")
        return list(
        return list(self._index().get(self._zipinfo_name(fspath), ()))
        return maps
        return marker.evaluate()
        return metadata
        return name == "PKG-INFO" and os.path.isfile(self.path)
        return needed
        return new
        return None
        return normalize_path(filename)
        return not req.marker or any(extra_evals)
        return not self == other
        return open(self._fn(self.module_path, resource_name), "rb")
        return os.listdir(path)
        return os.path.exists(path)
        return os.path.isdir(path)
        return path
        return py_compat and compatible_platforms(dist.platform, self.platform)
        return re.sub("[^A-Za-z0-9.]+", "-", version)
        return real_path
        return req
        return req.extras
        return Requirement.parse(spec)
        return s
        return safe_sys_path_index(_normalize_cached(os.sep.join(parts)))
        return self
        return self.__class__(**kw)  # type:ignore[arg-type]
        return self.__class__.__name__ + repr(self.args)
        return self.__dep_map
        return self.__hash
        return self._distmap.get(distribution_key, [])
        return self._ep_map
        return self._extract_resource(manager, zip_path)
        return self._fn(self.egg_info, name)
        return self._fn(self.module_path, resource_name)
        return self._get(self._fn(self.module_path, resource_name))
        return self._has(path)
        return self._has(self._fn(self.module_path, resource_name))
        return self._isdir(self._fn(self.module_path, resource_name))
        return self._listdir(self._fn(self.module_path, resource_name))
        return self._parsed_version
        return self._template.format(**locals())
        return self._zip_manifests.load(self.loader.archive)
        return self._zipinfo_name(fspath) in self._index()
        return self._zipinfo_name(self._fn(self.egg_root, resource_name))
        return self._zipinfo_name(self._fn(self.module_path, resource_name))
        return self.args[0]
        return self.args[1]
        return self.args[2]
        return self.by_key.get(dist.key) == dist
        return self.eagers
        return self.get_entry_map(group).get(name)
        return self.hashcmp < other.hashcmp
        return self.hashcmp <= other.hashcmp
        return self.hashcmp == other.hashcmp
        return self.hashcmp > other.hashcmp
        return self.hashcmp >= other.hashcmp
        return self.obtain(req, installer)
        return self.path
        return self.report()
        return self.resolve()
        return self.specifier.contains(item, prereleases=True)
        return self[path].manifest
        return sorted_distributions, error_info
        return str(_packaging_version.Version(version))
        return subpath
        return target_path
        return tempfile.mkstemp(*args, **kw)
        Return the ordinal of the path based on its position in sys.path
        Return the path to the given metadata file, if available.
        return this
        return timestamp, size
        return to_activate
        return True
        Return True if the file_path is current for this zip_path
        return value is a sequence of the distributions that needed to be
        return working_set.find(moduleOrReq) or require(str(moduleOrReq))[0]
        return ws
        return yield_lines(self.get_metadata(name))
        return zip_contents == file_contents
        return zip_path in self.zipinfo or zip_path in self._index()
        returned.
        returns it as long as it meets the version requirement specified by
        returns.
        root,
        running platform or Python version.
        s = "{} = {}".format(self.name, self.module_name)
        safe = "0"
        safe = match["safe"]
        script = "scripts/" + script_name
        script_filename = self._fn(self.egg_info, script)
        script_text = script_text.replace("\r", "\n")
        script_text = self.get_metadata(script).replace("\r\n", "\n")
        search_path: Iterable[str] | None = None,
        See Distribute #375 for more details.
        seen = set()
        self,
        self, callback: Callable[[Distribution], object], existing: bool = True
        self, manager: ResourceManager, resource_name: str
        self, manager: ResourceManager, zip_path
        self, package_or_requirement: _PkgReqType, resource_name: str
        self, req, best, replace_conflicting, env, installer, required_by, to_activate
        self.__dep_map: dict[str | None, list[Requirement]] = {None: []}
        self.__dep_map[None].extend(common)
        self.__hash = hash(self.hashCmp)
        self._added_new(dist)
        self._distmap = {}
        self._distmap[dist.key].remove(dist)
        self._provider = metadata or empty_provider
        self._setup_prefix()
        self._validate_resource_path(resource_name)
        self._warn_on_replacement(metadata)
        self._warn_unsafe_extraction_path(extract_path)
        self.attrs = tuple(attrs)
        self.by_key = {}
        self.by_key = by_key.copy()
        self.by_key[dist.key] = dist
        self.cached_files = {}
        self.cached_files[target_path] = True
        self.callbacks = []
        self.callbacks = callbacks[:]
        self.callbacks.append(callback)
        self.dist = dist
        self.egg_info = egg_info
        self.egg_info = os.path.join(path, "EGG-INFO")
        self.egg_name = os.path.basename(path)
        self.egg_root = path
        self.entries = entries[:]
        self.entries.append(entry)
        self.entries: list[str] = []
        self.entry_keys = {}
        self.entry_keys = keys.copy()
        self.entry_keys.setdefault(entry, [])
        self.extraction_path = path
        self.extras = tuple(extras)
        self.extras: tuple[str] = tuple(map(safe_extra, self.extras))
        self.hashCmp = (
        self.insert_on(path, replace=replace)
        self.loader = getattr(module, "__loader__", None)
        self.loader = importer
        self.location = location
        self.module_name = module_name
        self.module_path = os.path.dirname(getattr(module, "__file__", ""))
        self.module_path = path
        self.name = name
        self.normalized_to_canonical_keys = {}
        self.normalized_to_canonical_keys = normalized_to_canonical_keys.copy()
        self.normalized_to_canonical_keys[normalized_name] = dist.key
        self.path = path
        self.platform = platform
        self.precedence = precedence
        self.project_name = safe_name(project_name or "Unknown")
        self.project_name, self.key = project_name, project_name.lower()
        self.py_version = py_version
        self.python = python
        self.require(requires)[0].run_script(script_name, ns)
        self.scan(search_path)
        self.specs = [(spec.operator, spec.version) for spec in self.specifier]
        self.unsafe_name = self.name
        self.zip_pre = importer.archive + os.sep
        self.zip_pre = self.loader.archive + os.sep
        sequence of path name parts "under" the egg's extraction location.
        setattr(sys.modules[parent], name, sys.modules[packageName])
        set's ``.entries`` (if it wasn't already present).
        shadow_set = self.__class__([])
        size = zip_stat.file_size
        sorted_distributions = list(distributions)
        sorted_distributions.sort()
        spec = importer.find_spec(packageName)
        stat = os.stat(file_path)
        state[k] = g["_sget_" + v](g[k])
        suitable distribution is already active.  (This may raise
        super().__init__(module)
        super().__init__(requirement_string)
        supplied, ``sys.path`` is used.
        supplied, ``sys.path`` is used.  Only distributions conforming to
        supplied, one is created automatically from the ``WorkingSet`` this
        sys.path[:] = ws.entries
        take an extra step and try to get the version number from
        target_path = os.path.join(extract_path, archive_name + "-tmp", *names)
        temporary directory, but then you must call ``cleanup_resources()`` to
        that are already in the filesystem.
        that platform-specific distributions must be compatible with.  If
        that were loadable, along with any other distributions that are needed
        The `plugin_env` should be an ``Environment`` instance that contains
        The base directory for resource extraction
        The distribution must match the platform and python version
        The entry name and module name are required, but the ``:attrs`` and
        The exception instance that caused extraction to fail
        the metadata file itself instead of the filename.
        The parent directory of the resulting path will be created if it does
        the platform/python version defined at initialization are added.
        The resource manager that raised this exception
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        The yield order is the order in which the items' path entries were
        their version numbers can get mangled when
        thereof, specifying the distributions and versions required.  The
        This calls the ``find(req)`` method of the `working_set` to see if a
        This fallback behaviour is considered **deprecated** and future versions of
        This function does not have any concurrency protection, so it should
        This is important because extra requirements may look like `my_req;
        This is where Mac header rewrites should be done; other platforms don't
        This method returns a 2-tuple: (`distributions`, `error_info`), where
        This method should only be called by resource providers that need to
        this: dict[str, Self] = {}
        timestamp = time.mktime(date_time)
        timestamp, size = self._get_date_and_size(self.zipinfo[zip_path])
        tmpl = textwrap.dedent(
        to attempt other ways of obtaining a distribution before falling back
        to resolve their dependencies.  `error_info` is a dictionary mapping
        to the `installer` argument."""
        to_activate = []
        Traceback (most recent call last):
        True
        try:
        Unless `replace_conflicting=True`, raises a VersionConflict exception
        unloadable plugin distributions to an exception instance describing the
        unspecified, it defaults to the current platform.  `python` is an
        Use a platform-specific path separator (os.sep) for the path keys
        Uses case-insensitive `project_name` comparison, assuming all the
        Validate the resource paths according to the docs.
        value = self._get(path)
        ValueError: Use of .. or absolute path in a resource path \
        version = version or "[unknown version]"
        version = version.replace(" ", ".")
        version: str | None = None,
        warnings.warn(msg, PkgResourcesDeprecationWarning, stacklevel=2)
        which uses an old safe_version, and so
        while requirements:
        while sys._getframe(level).f_globals is g:
        while True:
        will be called.
        will be invoked with each requirement that cannot be met by an
        Windows path separators are straight-up disallowed.
        wish to map *all* distributions, not just those compatible with the
        with ``#`` as the first non-blank character are omitted."""
        with open(file, encoding="utf-8") as f:
        with open(file, encoding=fallback_encoding) as f:
        with open(file_path, "rb") as f:
        with open(path, "rb") as stream:
        with open(self.path, encoding="utf-8", errors="replace") as f:
        with warnings.catch_warnings():
        with zipfile.ZipFile(path) as zfile:
        Workaround for #520 and #513.
        working_set: WorkingSet,
        ws = cls()
        ws = cls([])
        yield Distribution.from_filename(
        yield Distribution.from_filename(path_item, metadata=metadata)
        yield from factory(fullpath)
        yield path
        You may explicitly set `platform` (and/or `python`) to ``None`` if you
        zip_contents = self.loader.get_data(zip_path)
        zip_path = self._resource_to_zip(resource_name)
        zip_path = self._zipinfo_name(fspath)
    """
    """,
    """A collection of active distributions on sys.path (or a similar list)"""
    """A requested distribution was not found"""
    """Abstract base for dependency resolution errors"""
    """An error occurred extracting a resource
    """An object that provides access to package resources"""
    """Can code for the `provided` platform run on the `required` platform?
    """Compute an ns-package subpath for a filesystem or zipfile importer"""
    """Convert a project or version name to its filename-escaped form
    """Convert an arbitrary string into a safe segment"""
    """Convert an arbitrary string to a standard distribution name
    """Convert an arbitrary string to a standard 'extra' name
    """Declare that package 'packageName' is a namespace package"""
    """Distribution doesn't have an "extra feature" of the given name"""
    """Ensure that named package includes a subpath of path_item (if needed)"""
    """Ensure that previously-declared namespace packages include path_item"""
    """Ensure that the parent directory of `path` exists"""
    """Fallback when ``safe_version`` is not safe enough
    """Manage resource extraction and packages"""
    """Metadata handler for standalone PKG-INFO files
    """Metadata provider for .egg files"""
    """Metadata provider for egg directories
    """Normalize a file/dir name for comparison purposes"""
    """Object representing an advertised importable object"""
    """Provider based on a virtual filesystem"""
    """Provider that returns nothing for all requests"""
    """Provides access to package resources in the filesystem"""
    """Register `distribution_finder` to find distributions in sys.path items
    """Register `namespace_handler` to declare namespace packages
    """Register `provider_factory` to make providers for `loader_type`
    """Resource support for zips and eggs"""
    """Return `name` entry point of `group` for `dist` or raise ImportError"""
    """Return a current distribution object for a Requirement or string"""
    """Return a dist_factory for the given entry."""
    """Return an adapter factory for `ob` from `registry`"""
    """Return an IResourceProvider for the named module or requirement"""
    """Return the entry point map for `group`, or the full entry map"""
    """Return the EntryPoint object for `group`+`name`, or ``None``"""
    """Return this platform's maximum compatible version.
    """Return this platform's string for platform-specific distributions
    """Sandbox-bypassing version of ensure_directory()"""
    """Searchable snapshot of distributions on a search path"""
    """See setuptools.unicode_utils._read_utf8_with_fallback"""
    """Split a string or iterable thereof into (section, content) pairs
    """Try to implement resources and metadata for arbitrary PEP 302 loaders"""
    """Wrap an actual or potential sys.path entry w/metadata"""
    """Yield distributions accessible on a sys.path directory"""
    """Yield distributions accessible via `path_item`"""
    ".dist-info": DistInfoDistribution,
    ".egg": Distribution,
    ".egg-info": EggInfoDistribution,
    "_AdapterT", _DistFinderType[Any], _ProviderFactoryType, _NSHandlerType[Any]
    "add_activation_listener",
    "AvailableDistributions",
    "BINARY_DIST",
    "CHECKOUT_DIST",
    "cleanup_resources",
    "Compatibility wrapper for InvalidRequirement"
    "compatible_platforms",
    "declare_namespace",
    "DefaultProvider",
    "DEVELOP_DIST",
    "dict", "_distribution_finders", {}
    "dict", "_namespace_handlers", {}
    "dict", "_namespace_packages", {}
    "Distribution",
    "DistributionNotFound",
    "EGG_DIST",
    "EggMetadata",
    "EggProvider",
    "empty_provider",
    "EmptyProvider",
    "ensure_directory",
    "EntryPoint",
    "Environment",
    "evaluate_marker",
    "ExtractionError",
    "FileMetadata",
    "find_distributions",
    "fixup_namespace_packages",
    "get_default_cache",
    "get_distribution",
    "get_entry_info",
    "get_entry_map",
    "get_importer",
    "get_platform",
    "get_provider",
    "IMetadataProvider",
    "invalid_marker",
    "IResourceProvider",
    "iter_entry_points",
    "load_entry_point",
    "normalize_path",
    "NullProvider",
    "parse_requirements",
    "parse_version",
    "PathMetadata",
    "PEP440Warning",
    "PkgResourcesDeprecationWarning",
    "register_finder",
    "register_loader_type",
    "register_namespace_handler",
    "require",
    "Requirement",
    "ResolutionError",
    "resource_exists",
    "resource_filename",
    "resource_isdir",
    "resource_listdir",
    "resource_stream",
    "resource_string",
    "ResourceManager",
    "run_main",
    "run_script",
    "safe_extra",
    "safe_name",
    "safe_version",
    "Set up global resource manager (deliberately not state-saved)"
    "set_extraction_path",
    "SOURCE_DIST",
    "split_sections",
    "to_filename",
    "UnknownExtra",
    "VersionConflict",
    "working_set",
    "WorkingSet",
    "yield_lines",
    "ZipProvider",
    # "Provider" interfaces, implementations, and registration/lookup APIs
    # (e.g. by calling ``require()``) will get activated as well,
    # _find_adapter would previously return None, and immediately be called.
    # `path` could be `StrPath | IO[bytes]` but that violates the LSP for `MemoizedZipManifests.load`
    # A special case, we don't want all Providers inheriting from NullProvider to have a potentially None module_path
    # Activate all distributions already on sys.path with replace=False and
    # All of these are set by the @_call_aside methods above
    # backward compatibility
    # Basic resource access and distribution/entry point discovery
    # Deprecated/backward compatibility only
    # Distribution "precedence" constants
    # ensure that all distributions added to the working set in the future
    # Environmental control
    # Exceptions
    # fallback for MacPorts
    # filesystem utilities
    # FIXME: 'Distribution.insert_on' is too complex (13)
    # FIXME: 'ZipProvider._extract_resource' is too complex (12)
    # https://github.com/python/mypy/issues/16261
    # https://github.com/python/typeshed/issues/6347
    # macOS special cases
    # match order
    # may not know their name or version without loading PKG-INFO)
    # metadata until/unless it's actually needed.  (i.e., some distributions
    # no write support, probably under GAE
    # Parsing functions and string utilities
    # Primary implementation classes
    # scan for .egg and .egg-info in directory
    # So we're raising a TypeError to keep backward compatibility if anyone depended on that behaviour.
    # These properties have to be lazy so that we don't have to load any
    # type: ignore[override] # ZipManifests.load is a classmethod
    # use find_spec (PEP 451) and fall-back to find_module (PEP 302)
    # Warnings
    # with higher priority (replace=True).
    # wrap up last segment
    # XXX Linux and other platforms' special cases should go here
    # ZipProvider's loader should always be a zipimporter or equivalent
    (?P<name>[^-]+) (
    )
    ) -> _DistributionT: ...
    ) -> _ResolvedEntryPoint:
    ) -> _ResolvedEntryPoint: ...
    ) -> _ResourceStream:
    ) -> bytes:
    ) -> Distribution | None:
    ) -> Distribution | None: ...
    ) -> Distribution:
    ) -> list[_DistributionT]: ...
    ) -> list[Distribution] | list[_DistributionT]:
    ) -> list[Distribution]: ...
    ) -> None: ...
    ) -> str:
    ) -> str:  # noqa: C901
    ) -> tuple[
    ) -> tuple[list[_DistributionT], dict[Distribution, Exception]]: ...
    ) -> tuple[list[Distribution], dict[Distribution, Exception]]: ...
    ):
    )?
    @classmethod
    @functools.lru_cache(maxsize=None)
    @overload
    @property
    @staticmethod
    []
    ]:
    _, _, value = line.partition(":")
    __loader__: zipimport.zipimporter
    __resource_manager = ResourceManager()  # Won't exist at runtime
    _distribution_finders[importer_type] = distribution_finder
    _imp.acquire_lock()
    _isdir = _has = lambda self, path: False
    _namespace_handlers[importer_type] = namespace_handler
    _provider_factories[loader_type] = provider_factory
    _state_vars[varname] = vartype
    _template = "{self.dist} is installed but {self.req} is required"
    _template = (
    _template = VersionConflict._template + " by {self.required_by}"
    _zip_manifests = MemoizedZipManifests()
    ``pkg_resources.file_ns_handler``.
    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    `loader_type` is the type or class of a PEP 302 ``module.__loader__``,
    `strs` must be a string, or a (possibly-nested) iterable thereof.
    <Version('0.23.dev0+sanitized')>
    <Version('0.23.dev0+sanitized.ubuntu1')>
    <Version('0.dev0+sanitized')>
    <Version('0.dev0+sanitized.hello.world')>
    <Version('42.dev0+sanitized.1')>
    >>> bool(NoDists())
    >>> list(NoDists()('anything'))
    >>> parse_version(_forgiving_version('0.-_'))
    >>> parse_version(_forgiving_version('0.23-'))
    >>> parse_version(_forgiving_version('0.23ubuntu1'))
    >>> parse_version(_forgiving_version('42.+?1'))
    >>> parse_version(_forgiving_version('hello world'))
    A VersionConflict that accepts a third parameter, the set of the
    add_activation_listener = working_set.subscribe
    add_activation_listener(
    agreed that it can handle the relevant path item, and they should only
    An already-installed version conflicts with the requested version.
    and `provider_factory` is a function that, passed a *module* object,
    and each ``content`` is a list of stripped lines excluding blank lines and
    and the result is always lowercased.
    Any '-' characters are currently replaced with '_'.
    Any runs of non-alphanumeric characters are replaced with a single '_',
    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    Any,
    API available.
    at their own risk.
    Attempt to list contents of path, but suppress some exceptions.
    Base class for warning about deprecations in ``pkg_resources``
    cache_path
    cache_path: str
    Callable,
    class manifest_mod:
    cleanup_resources = __resource_manager.cleanup_resources
    comment-only lines.  If there are any such lines before the first section
    content = []
    Contrary to POSIX 2008, on Cygwin, getcwd (3) contains
    Convert an arbitrary string to a standard version string
    corresponding to their sys.path order
    current version of the OS.
    def __add__(self, other: Distribution | Environment):
    def __bool__(self):
    def __call__(self, fullpath):
    def __contains__(self, dist: Distribution) -> bool:
    def __contains__(self, item: Distribution | str | tuple[str, ...]) -> bool:
    def __dir__(self):
    def __eq__(self, other: object):
    def __ge__(self, other: Distribution):
    def __getattr__(self, attr):
    def __getitem__(self, project_name: str) -> list[Distribution]:
    def __getstate__(self):
    def __gt__(self, other: Distribution):
    def __hash__(self):
    def __iadd__(self, other: Distribution | Environment):
    def __init__(
    def __init__(self):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, entries: Iterable[str] | None = None):
    def __init__(self, importer: zipimport.zipimporter):
    def __init__(self, module: _ModuleLike):
    def __init__(self, module: _ZipLoaderModule):
    def __init__(self, path: str, egg_info: str):
    def __init__(self, path: StrPath):
    def __init__(self, requirement_string: str):
    def __iter__(self) -> Iterator[Distribution]:
    def __iter__(self) -> Iterator[str]:
    def __le__(self, other: Distribution):
    def __lt__(self, other: Distribution):
    def __ne__(self, other):
    def __ne__(self, other: object):
    def __repr__(self):
    def __setstate__(self, e_k_b_n_c):
    def __str__(self):
    def _added_new(self, dist):
    def _build_dep_map(self):
    def _build_from_requirements(cls, req_spec):
    def _build_master(cls):
    def _compute_dependencies(self) -> dict[str | None, list[Requirement]]:
    def _dep_map(self):
    def _eager_to_zip(self, resource_name: str):
    def _extract_resource(
    def _filter_extras(dm: dict[str | None, list[Requirement]]):
    def _fn(self, base: str | None, resource_name: str):
    def _forgiving_parsed_version(self):
    def _get(self, path) -> bytes:
    def _get_date_and_size(zip_stat):
    def _get_eager_resources(self):
    def _get_metadata(self, name):
    def _get_metadata_path(self, name):
    def _get_metadata_path_for_display(self, name):
    def _get_version(self):
    def _has(self, fspath) -> bool:
    def _has(self, path) -> bool:
    def _index(self):
    def _is_current(self, file_path, zip_path):
    def _isdir(self, fspath) -> bool:
    def _isdir(self, path) -> bool:
    def _listdir(self, fspath):
    def _listdir(self, path) -> list[str]:
    def _listdir(self, path):
    def _normalize_cached(filename):
    def _normalize_cached(filename: BytesPath) -> bytes: ...
    def _normalize_cached(filename: StrOrBytesPath) -> str | bytes: ...
    def _normalize_cached(filename: StrPath) -> str: ...
    def _parse_extras(cls, extras_spec):
    def _parsed_pkg_info(self):
    def _parts(self, zip_path):
    def _register(cls):
    def _reload_version(self):
    def _resolve_dist(
    def _resource_to_zip(self, resource_name: str):
    def _set_egg(self, path: str):
    def _setup_prefix(self):
    def _validate_resource_path(path):
    def _warn_on_replacement(self, metadata):
    def _warn_unsafe_extraction_path(path):
    def _zipinfo_name(self, fspath):
    def activate(self, path: list[str] | None = None, replace: bool = False):
    def add(
    def add(self, dist: Distribution):
    def add_entry(self, entry: str):
    def as_requirement(self):
    def best_match(
    def build(cls, path: str):
    def can_add(self, dist: Distribution):
    def check_version_conflict(self):
    def cleanup_resources(self, force: bool = False) -> list[str]:
    def clone(self, **kw: str | int | IResourceProvider | None):
    def dist(self) -> Distribution:
    def egg_name(self):
    def extraction_error(self) -> NoReturn:
    def extras(self):
    def find(self, req: Requirement) -> Distribution | None:
    def find_plugins(
    def from_filename(
    def from_location(
    def get_cache_path(self, archive_name: str, names: Iterable[StrPath] = ()):
    def get_entry_info(self, group: str, name: str):
    def get_entry_map(self, group: None = None) -> dict[str, dict[str, EntryPoint]]: ...
    def get_entry_map(self, group: str | None = None):
    def get_entry_map(self, group: str) -> dict[str, EntryPoint]: ...
    def get_metadata(self, name: str) -> str:
    def get_metadata(self, name: str):
    def get_metadata_lines(self, name: str) -> Iterator[str]:
    def get_resource_filename(
    def get_resource_filename(self, manager: ResourceManager, resource_name: str):
    def get_resource_stream(
    def get_resource_stream(self, manager: object, resource_name: str):
    def get_resource_stream(self, manager: ResourceManager, resource_name: str):
    def get_resource_string(
    def has_metadata(self, name: str) -> bool:
    def has_resource(self, resource_name: str) -> bool:
    def has_resource(self, resource_name: str):
    def has_version(self):
    def hashcmp(self):
    def insert_on(  # noqa: C901
    def is_version_line(line):
    def iter_entry_points(self, group: str, name: str | None = None):
    def key(self):
    def load(
    def load(self, path: str) -> dict[str, zipfile.ZipInfo]:
    def load_entry_point(self, group: str, name: str) -> _ResolvedEntryPoint:
    def load_module(self, fullname: str, /) -> types.ModuleType: ...
    def markers_pass(self, req: Requirement, extras: tuple[str, ...] | None = None):
    def metadata_isdir(self, name: str) -> bool:
    def metadata_listdir(self, name: str) -> list[str]:
    def obtain(
    def parse(cls, src: str, dist: Distribution | None = None):
    def parse(s: str | Iterable[str]):
    def parse_group(
    def parse_map(
    def parsed_version(self):
    def position_in_sys_path(path):
    def postprocess(self, tempname: StrOrBytesPath, filename: StrOrBytesPath):
    def remove(self, dist: Distribution):
    def report(self):
    def req(self) -> Requirement:
    def require(
    def require(self, *requirements: _NestedStr):
    def required_by(self) -> set[str]:
    def requirers(self) -> set[str] | None:
    def requirers_str(self):
    def requires(self, extras: Iterable[str] = ()):
    def resolve(
    def resolve(self) -> _ResolvedEntryPoint:
    def resource_exists(self, package_or_requirement: _PkgReqType, resource_name: str):
    def resource_filename(
    def resource_isdir(self, package_or_requirement: _PkgReqType, resource_name: str):
    def resource_isdir(self, resource_name: str) -> bool:
    def resource_isdir(self, resource_name: str):
    def resource_listdir(self, package_or_requirement: _PkgReqType, resource_name: str):
    def resource_listdir(self, resource_name: str) -> list[str]:
    def resource_listdir(self, resource_name: str):
    def resource_stream(self, package_or_requirement: _PkgReqType, resource_name: str):
    def resource_string(
    def run_script(self, requires: str, script_name: str):
    def run_script(self, script_name: str, namespace: dict[str, Any]) -> None:
    def run_script(self, script_name: str, namespace: dict[str, Any]):
    def safe_sys_path_index(entry):
    def scan(self, search_path: Iterable[str] | None = None):
    def set_extraction_path(self, path: str):
    def subscribe(
    def version(self):
    def with_context(self, required_by: set[Distribution | str]):
    def zipinfo(self):
    Determine if given path appears to be an egg.
    Determine if given path appears to be an unpacked egg.
    Dict,
    dirname = os.path.dirname(path)
    dirname, filename = split(path)
    dist: _EPDistType, group: None = None
    dist_groups = map(find_distributions, resolved_paths)
    distutils.  But what we want when checking compatibility is to know the
    distutils.util.get_platform() normally reports the minimum version
    drop_comment,
    Each ``section`` is a stripped version of the section header ("[section]")
    eagers: list[str] | None = None
    egg_info: str | None = None
    egg_name: str | None = None
    elif not hasattr(module, "__path__"):
    else:
    Ensure object appears in the mro even
    entries = (os.path.join(path_item, child) for child in safe_listdir(path_item))
    entry = os.path.basename(path)
    EQEQ = re.compile(r"([\(,])\s*(\d.*?)\s*([,\)])")
    equivalent subpath.  For an example namespace handler, see
    Evaluate a PEP 508 environment marker.
    except (PermissionError, NotADirectoryError):
    except _packaging_markers.InvalidMarker as e:
    except _packaging_version.InvalidVersion:
    except AttributeError:
    except KeyError:
    except OSError as e:
    except SyntaxError as e:
    except UnicodeDecodeError:  # pragma: no cover
    except ValueError:
    explicitly require a newer version of macOS, we must also know the
    extraction_path: str | None = None
    f(*args, **kwargs)
    False
    finally:
    Find eggs in zip files; possibly multiple nested eggs.
    finder = _find_adapter(_distribution_finders, importer)
    for entry in sorted(entries):
    for item in module.__path__:
    for k, v in _state_vars.items():
    for k, v in state.items():
    for line in _read_utf8_with_fallback(path).splitlines():
    for line in yield_lines(s):
    for old-style classes.
    for subitem in metadata.resource_listdir(""):
    for t in types:
    from _typeshed import BytesPath, StrPath, StrOrBytesPath
    from os import mkdir, rename, unlink
    from pip._vendor.typing_extensions import Self
    from sysconfig import get_platform
    g = globals()
    g.update(
    g["_manager"] = manager
    Given a path to an .egg-link, resolve distributions
    Given an iterable of lines from a Metadata file, return
    globals().update(locals())
    handler = _find_adapter(_namespace_handlers, importer)
    handler), and `distribution_finder` is a callable that, passed a path
    handler), and `namespace_handler` is a callable like this::
    header, they're returned in a first ``section`` of ``None``.
    if _is_unpacked_egg(path_item):
    if dirname and filename and not isdir(dirname):
    if importer is None:
    if importer.archive.endswith(".whl"):
    if invalid or False otherwise.
    if isinstance(dist, Requirement):
    if isinstance(dist, str):
    if isinstance(module.__path__, list):
    if isinstance(moduleOrReq, Requirement):
    if loader is None:
    if m is not None and sys.platform == "darwin":
    if match:
    if metadata.has_metadata("PKG-INFO"):
    if module is None:
    if not isinstance(dist, Distribution):
    if not WRITE_SUPPORT:
    if object not in classes:
    if only:
    if os.path.isdir(path):
    if parts:
    if provided is None or required is None or provided == required:
    if reqMac:
    if subpath is not None:
    if sys.platform == "darwin" and not plat.startswith("macosx-"):
    If this condition occurs for any other platform with a version in its
    if version == "":
    importer = get_importer(path_item)
    importer: object | None, path_item: str | None, only: bool | None = False
    importer: object,
    importer: zipimport.zipimporter, path_item: str, only: bool = False
    importer_type: type[_T], namespace_handler: _NSHandlerType[_T]
    Invocation by other packages is unsupported and done
    is_dist_info = lower.endswith(".dist-info") and os.path.isdir(
    is_egg_info = lower.endswith(".egg-info")
    is_meta = is_egg_info or is_dist_info
    item and the importer instance, yields ``Distribution`` instances found on
    iter_entry_points = working_set.iter_entry_points
    Iterable,
    Iterator,
    join_continuation,
    last = None
    level = 1
    line = next(iter(version_lines), "")
    list(map(working_set.add_entry, sys.path))
    Literal,
    load = build
    loader = getattr(module, "__loader__", None)
    loader: _LoaderProtocol | None = None
    loader: zipimport.zipimporter
    loader_type: type[_ModuleLike], provider_factory: _ProviderFactoryType
    local = f"sanitized.{_safe_segment(rest)}".strip(".")
    lower = entry.lower()
    m = macosVersionString.match(plat)
    manager
    manager = ResourceManager()
    manager: ResourceManager
    manifest: dict[str, zipfile.ZipInfo]
    Map each requirement to the extras that demanded it.
    Mapping,
    match = _PEP440_FALLBACK.search(version)
    Memoized zipfile manifests.
    metadata = EggMetadata(importer)
    module = sys.modules.get(packageName)
    module: _ModuleLike | None,
    module: types.ModuleType,
    module_path: str | None = None  # type: ignore[assignment]
    msg = (
    mtime: float
    MutableSequence,
    name = parts.pop()
    named "Python-Eggs".
    NamedTuple,
    Namespace handlers are only called if the importer object has already
    needs some hacks for Linux and macOS.
    new_path = [_normalize_cached(p) for p in new_path]
    new_path = sorted(orig_path, key=position_in_sys_path)
    NoReturn,
    normalized = _normalize_cached(subpath)
    ob.__setstate__(state)
    ob.clear()
    ob.update(state)
    of macOS that would be required to *use* extensions produced by
    of pkg_resources. It is intended to be invoked once at
    old_open = os.open
    or a platform-relevant user cache dir for an app
    original_error
    original_error: BaseException | None
    os.makedirs(dirname, exist_ok=True)
    os.path.abspath() works around this limitation. A fix in os.getcwd()
    overload,
    packageName: str | None,
    packageName: str,
    parts = packageName.split(".")
    path_item = _normalize_cached(path_item)
    path_item: str | None,
    path_item: StrPath,
    pattern = re.compile(
    PEP 440.
    PKG_INFO = "METADATA"
    PKG_INFO = "PKG-INFO"
    plat = get_build_platform()
    plat = get_platform()
    platform strings, this function should be extended accordingly.
    Prepare the master working set and make the ``require()``
    present in the referenced path.
    Protocol,
    r"""
    raise RuntimeError("Python 3.8 or later is required")
    Raise SyntaxError if marker is invalid.
    raise TypeError(f"Could not find adapter for {registry} and {ob}")
    re.VERBOSE | re.IGNORECASE,
    Rebuild module.__path__ ensuring that all entries are ordered
    referenced_paths = non_empty_lines(path)
    register_finder(pkgutil.ImpImporter, find_on_path)
    register_namespace_handler(pkgutil.ImpImporter, file_ns_handler)
    reqMac = macosVersionString.match(required)
    require = working_set.require
    Requirement.
    requirements that required the installed Distribution.
    resolved_paths = (
    resource_exists = __resource_manager.resource_exists
    resource_filename = __resource_manager.resource_filename
    resource_isdir = __resource_manager.resource_isdir
    resource_listdir = __resource_manager.resource_listdir
    resource_stream = __resource_manager.resource_stream
    resource_string = __resource_manager.resource_string
    return (
    return ()
    return _find_adapter(_provider_factories, loader)(module)
    return _is_zip_egg(path) or _is_unpacked_egg(path)
    return {"PowerPC": "ppc", "Power_Macintosh": "ppc"}.get(machine, machine)
    Return a boolean indicating the marker result in this environment.
    return a subpath if the module __path__ does not already contain an
    return classes
    return dist
    return f
    return f"{safe}.dev0+{local}"
    return False
    return finder(importer, path_item, only)
    return get_distribution(dist).get_entry_info(group, name)
    return get_distribution(dist).get_entry_map(group)
    return get_distribution(dist).load_entry_point(group, name)
    return initial_value
    return map(Requirement, join_continuation(map(drop_comment, yield_lines(strs))))
    return name.replace("-", "_")
    return next(dist_groups, ())
    return None
    return os.environ.get("PYTHON_EGG_CACHE") or _user_cache_dir(appname="Python-Eggs")
    return os.path.abspath(filename) if sys.platform == "cygwin" else filename
    return os.path.normcase(os.path.realpath(os.path.normpath(_cygwin_patch(filename))))
    return path.lower().endswith(".egg") and os.path.isfile(
    return plat
    return re.sub("[^A-Za-z0-9.]+", "-", name)
    return re.sub("[^A-Za-z0-9.-]+", "_", extra).lower()
    return re.sub(r"\.[^A-Za-z0-9]+", ".", segment).strip(".-")
    return safe_version(value.strip()) or None
    return state
    return subpath
    Return the ``PYTHON_EGG_CACHE`` environment variable
    return val.__getstate__()
    return val.copy()
    return version.split(".")
    returns an ``IResourceProvider`` for that module.
    Returns true if either platform is ``None``, or the platforms are equal.
    root = os.path.dirname(path)
    run_main = run_script
    run_script = working_set.run_script
    section = None
    segment = re.sub("[^A-Za-z0-9.]+", "-", segment)
    segment = re.sub("-[^A-Za-z0-9]+", "-", segment)
    set_extraction_path = __resource_manager.set_extraction_path
    Should be initialized with the installed Distribution and the requested
    state = {}
    subpath = handler(importer, path_item, packageName, module)
    subpath = os.path.join(path_item, packageName.split(".")[-1])
    symlink components. Using
    sys_path = [_normalize_cached(p) for p in sys.path]
    that path item.  See ``pkg_resources.find_on_path`` for an example."""
    that this seems to be by design...
    The following attributes are available from instances of this exception:
    the initialization of this module.
    the provided location.
    the value of the Version field, if present, or None otherwise.
    This class is not derived from ``DeprecationWarning``, and as such is
    This function has explicit effects on the global state
    This implementation uses the 'pyparsing' module.
    This provider rejects all data and metadata requests except for PKG-INFO,
    try:
    tuple(dist.activate(replace=False) for dist in working_set)
    Tuple,
    TYPE_CHECKING,
    types = _always_object(inspect.getmro(getattr(ob, "__class__", type(ob))))
    TypeVar,
    Union,
    Usage::
    Used when there is an issue with a version or specifier not complying with
    Validate text as a PEP 508 environment marker; return an exception
    version = platform.mac_ver()[0]
    version = version.replace(" ", ".")
    version of macOS that we are *running*.  To allow usage of packages that
    version_lines = filter(is_version_line, lines)
    visible by default.
    w/metadata, .dist-info style.
    warnings.warn(msg, DeprecationWarning, stacklevel=2)
    warnings.warn(stacklevel=level + 1, *args, **kw)
    which is treated as existing, and will be the contents of the file at
    while path != last:
    working_set = _declare_state("object", "working_set", WorkingSet._build_master())
    working_set = WorkingSet()
    working_set.entries = []
    would probably better, in Cygwin even more so, except
    Wrap an actual or potential sys.path entry
    WRITE_SUPPORT = False
    WRITE_SUPPORT = True
    XXX Currently this is the same as ``distutils.util.get_platform()``, but it
    XXX Needs compatibility checks for Linux and other unixy OSes.
    Yield ``Requirement`` objects for each specification in `strs`.
    yield all parents of path including path
    yield Distribution.from_location(
    Yield non-empty lines from file at path
    yield section, content
    yield_lines,
    zip manifest builder
"""
# Any object works, but let's indicate we expect something like a module (optionally has __loader__ or __file__)
# Any: Should be _ModuleLike but we end up with issues where _ModuleLike doesn't have _ZipLoaderModule's __loader__
# because we want earlier uses of filterwarnings to take precedence over this
# capture these to bypass sandboxing
# causes immediate exceptions.
# For now we'd simply use implicit Any/Unknown which would add redundant annotations
# from jaraco.functools 1.3
# mypy: disable-error-code="var-annotated"
# one.
# Patch: Remove deprecation warning from vendored pkg_resources.
# Ported from ``setuptools`` to avoid introducing an import inter-dependency:
# randomly just because they use pkg_resources. We want to append the rule
# See https://github.com/pypa/pip/issues/12243
# Setting PYTHONWARNINGS=error to verify builds produce no warnings
# Silence the PEP440Warning by default, so that end users don't get hit by it
# TODO: Add Generic type annotations to initialized collections.
# Type aliases
# Use _typeshed.importlib.LoaderProtocol once available https://github.com/python/typeshed/pull/11890
# XXX backward compat
# XXX backward compatibility
)
) -> dict[str, dict[str, EntryPoint]]: ...
) -> Iterator[Distribution]:
).match
):
.egg files, and unpacked .egg files.  It can also work in a limited way with
.zip files and with custom PEP 302 loaders that support the ``get_data()``
:mod:`importlib.metadata` and :pypi:`packaging` instead.
@_call_aside
@functools.lru_cache(maxsize=None)
@overload
]
__all__ = [
_AdapterT = TypeVar(
_DistFinderType = Callable[[_T, str, bool], Iterable["Distribution"]]
_distribution_finders: dict[type, _DistFinderType[Any]] = _declare_state(
_distributionImpl = {
_DistributionT = TypeVar("_DistributionT", bound="Distribution")
_EPDistType = Union["Distribution", _PkgReqType]
_InstallerType = Callable[["Requirement"], Union["Distribution", None]]
_InstallerTypeT = Callable[["Requirement"], "_DistributionT"]
_LOCALE_ENCODING = "locale" if sys.version_info >= (3, 10) else None
_MetadataType = Union["IResourceProvider", None]
_ModuleLike = Union[object, types.ModuleType]
_namespace_handlers: dict[type, _NSHandlerType[Any]] = _declare_state(
_namespace_packages: dict[str | None, list[str]] = _declare_state(
_NestedStr = Union[str, Iterable[Union[str, Iterable["_NestedStr"]]]]
_NSHandlerType = Callable[[_T, str, str, types.ModuleType], Union[str, None]]
_PEP440_FALLBACK = re.compile(r"^v?(?P<safe>(?:[0-9]+!)?[0-9]+(?:\.[0-9]+)*)", re.I)
_PkgReqType = Union[str, "Requirement"]
_provider_factories: dict[type[_ModuleLike], _ProviderFactoryType] = {}
_ProviderFactoryType = Callable[[Any], "IResourceProvider"]
_ResolvedEntryPoint = Any  # Can be any attribute in the module
_ResourceStream = Any  # TODO / Incomplete: A readable file-like object
_sget_none = _sset_none = lambda *args: None
_state_vars: dict[str, str] = {}
_T = TypeVar("_T")
}
A resource is a logical file contained within a package, or a logical
AvailableDistributions = Environment
BINARY_DIST = 2
CHECKOUT_DIST = 0
class _LoaderProtocol:
class _ReqExtras:
class _ZipLoaderModule:
class ContextualVersionConflict:
class DefaultProvider:
class DistInfoDistribution:
class Distribution:
class DistributionNotFound:
class EggInfoDistribution:
class EggMetadata:
class EggProvider:
class EmptyProvider:
class EntryPoint:
class Environment:
class ExtractionError:
class FileMetadata:
class IMetadataProvider:
class IResourceProvider:
class MemoizedZipManifests:
class NoDists:
class NullProvider:
class PathMetadata:
class PEP440Warning:
class PkgResourcesDeprecationWarning:
class Requirement:
class RequirementParseError:
class ResolutionError:
class ResourceManager:
class UnknownExtra:
class VersionConflict:
class WorkingSet:
class ZipManifests:
class ZipProvider:
darwinVersionString = re.compile(r"darwin-(\d+)\.(\d+)\.(\d+)-(.*)")
def __getstate__() -> dict[str, Any]:
def __setstate__(state: dict[str, Any]) -> dict[str, Any]:
def _always_object(classes):
def _bypass_ensure_directory(path):
def _call_aside(f, *args, **kwargs):
def _cygwin_patch(filename: StrOrBytesPath):  # pragma: nocover
def _declare_state(vartype: str, varname: str, initial_value: _T) -> _T:
def _find_adapter(registry: Mapping[type, _AdapterT], ob: object) -> _AdapterT:
def _forgiving_version(version):
def _handle_ns(packageName, path_item):
def _initialize(g=globals()):
def _initialize_master_working_set():
def _is_egg_path(path):
def _is_unpacked_egg(path):
def _is_zip_egg(path):
def _macos_arch(machine):
def _macos_vers():
def _mkstemp(*args, **kw):
def _parents(path):
def _read_utf8_with_fallback(file: str, fallback_encoding=_LOCALE_ENCODING) -> str:
def _rebuild_mod_path(orig_path, package_name, module: types.ModuleType):
def _safe_segment(segment):
def _set_parent_ns(packageName):
def _sget_dict(val):
def _sget_object(val):
def _sset_dict(key, ob, state):
def _sset_object(key, ob, state):
def _version_from_file(lines):
def compatible_platforms(provided: str | None, required: str | None):
def declare_namespace(packageName: str):
def dist_factory(path_item, entry, only):
def distributions_from_metadata(path: str):
def ensure_directory(path: StrOrBytesPath):
def evaluate_marker(text: str, extra: str | None = None) -> bool:
def file_ns_handler(
def find_distributions(path_item: str, only: bool = False):
def find_eggs_in_zip(
def find_nothing(
def find_on_path(importer: object | None, path_item, only=False):
def fixup_namespace_packages(path_item: str, parent: str | None = None):
def get_build_platform():
def get_default_cache() -> str:
def get_distribution(dist: _DistributionT) -> _DistributionT: ...
def get_distribution(dist: _PkgReqType) -> Distribution: ...
def get_distribution(dist: Distribution | _PkgReqType) -> Distribution:
def get_entry_info(dist: _EPDistType, group: str, name: str):
def get_entry_map(
def get_entry_map(dist: _EPDistType, group: str | None = None):
def get_entry_map(dist: _EPDistType, group: str) -> dict[str, EntryPoint]: ...
def get_provider(moduleOrReq: Requirement) -> Distribution: ...
def get_provider(moduleOrReq: str | Requirement) -> IResourceProvider | Distribution:
def get_provider(moduleOrReq: str) -> IResourceProvider: ...
def get_supported_platform():
def invalid_marker(text: str):
def issue_warning(*args, **kw):
def load_entry_point(dist: _EPDistType, group: str, name: str) -> _ResolvedEntryPoint:
def non_empty_lines(path):
def normalize_path(filename: BytesPath) -> bytes: ...
def normalize_path(filename: StrOrBytesPath):
def normalize_path(filename: StrPath) -> str: ...
def null_ns_handler(
def parse_requirements(strs: _NestedStr):
def register_finder(importer_type: type[_T], distribution_finder: _DistFinderType[_T]):
def register_loader_type(
def register_namespace_handler(
def resolve_egg_link(path):
def safe_extra(extra: str):
def safe_listdir(path: StrOrBytesPath):
def safe_name(name: str):
def safe_version(version: str):
def split_sections(s: _NestedStr) -> Iterator[tuple[str | None, list[str]]]:
def to_filename(name: str):
DefaultProvider._register()
DEVELOP_DIST = -1
EGG_DIST = 3
EGG_NAME = re.compile(
else:
empty_provider = EmptyProvider()
except ImportError:
from __future__ import annotations
from os import open as os_open
from os import utime
from os.path import isdir, split
from pip._internal.utils._jaraco_text import (
from pip._vendor.packaging import markers as _packaging_markers
from pip._vendor.packaging import requirements as _packaging_requirements
from pip._vendor.packaging import utils as _packaging_utils
from pip._vendor.packaging import version as _packaging_version
from pip._vendor.platformdirs import user_cache_dir as _user_cache_dir
from pkgutil import get_importer
from typing import (
get_platform = get_build_platform
if hasattr(pkgutil, "ImpImporter"):
if sys.version_info < (3, 8):  # noqa: UP036 # Check for unsupported versions
if TYPE_CHECKING:
import _imp
import collections
import email.parser
import errno
import functools
import importlib
import importlib.abc
import importlib.machinery
import inspect
import io
import ntpath
import operator
import os
import pkgutil
import platform
import plistlib
import posixpath
import re
import stat
import sys
import tempfile
import textwrap
import time
import types
import warnings
import zipfile
import zipimport
is not allowed.
macosVersionString = re.compile(r"macosx-(\d+)\.(\d+)-(.*)")
method.
MODULE = re.compile(r"\w+(\.\w+)*$").match
names being passed into the API.
Package resource API
parse_version = _packaging_version.Version
path separator is.  Do not use os.path operations to manipulate resource
PY_MAJOR = "{}.{}".format(*sys.version_info)
register_finder(importlib.machinery.FileFinder, find_on_path)
register_finder(object, find_nothing)
register_finder(zipimport.zipimporter, find_eggs_in_zip)
register_loader_type(object, NullProvider)
register_loader_type(zipimport.zipimporter, ZipProvider)
register_namespace_handler(importlib.machinery.FileFinder, file_ns_handler)
register_namespace_handler(object, null_ns_handler)
register_namespace_handler(zipimport.zipimporter, file_ns_handler)
SOURCE_DIST = 1
subdirectory thereof.  The package resource API expects resource names
The package resource API is designed to work with normal filesystem packages,
This module is deprecated. Users are directed to :mod:`importlib.resources`,
to have their path parts separated with ``/``, *not* whatever the local
try:
warnings.filterwarnings("ignore", category=PEP440Warning, append=True)
