
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
                        version = plist_content["ProductVersion"]
                        ws = WorkingSet([])
                    "{} has no such extra feature {!r}".format(self, ext)
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
                    if "ProductVersion" in plist_content:
                    if dist is None:
                    if fallback:
                    if parent in ind:
                    if self._is_current(real_path, zip_path):
                    list(map(shadow_set.add, resolvees))
                    name.replace("/", os.sep),
                    or dversion == 8
                    parent = os.sep.join(parts[:-1])
                    plist_content = plistlib.readPlist(plist)
                    raise
                    raise DistributionNotFound(req, requirers)
                    req, ws, installer, replace_conflicting=replace_conflicting
                    requirers = required_by.get(req, None)
                    resolvees = shadow_set.resolve(req, env, installer)
                    return
                    return True
                    seen[key] = 1
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
                "and vulnerable to attack when "
                "Consider a more secure "
                "Extraction path is writable by group/others "
                "location (set with .set_extraction_path or the "
                "Module %s was already imported from %s, but %s is being added"
                '"os.rename" and "os.unlink" are not supported ' "on this platform"
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
                if hasattr(plistlib, "readPlist"):
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
                project_name, version, py_version, platform = match.group(
                raise
                raise packaging.version.InvalidVersion(f"{str(ex)} {info}") from None
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
                source = fid.read()
                stacklevel=2,
                try:
                while parts:
                ws = self
                ws.add_entry(entry)
                yield key
                yield line
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
            # We need to access _get_metadata_path() on the provider object
            # XXX add more info
            )
            ).format(**locals())
            ):
            )?
            *************************************************************************
            **kw,
            _bypass_ensure_directory(target_path)
            _handle_ns(packageName, path_item)
            _normalize_cached(filename), os.path.basename(filename), metadata, **kw
            {str(ex)}\n{notes}
            | {attr for attr in self._provider.__dir__() if not attr.startswith("_")}
            \n\n!!
            as a replacement to avoid breaking existing environments,
            break
            but no future compatibility is guaranteed.
            cache[script_filename] = (
            callback(dist)
            canonical_key = self.normalized_to_canonical_keys.get(req.key)
            Can't extract file(s) to egg cache
            cls = _distributionImpl[ext.lower()]
            code = compile(source, script_filename, "exec")
            content.append(line)
            data = data.items()
            data = split_sections(data)
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
            dm[s_extra] = [r for r in reqs_for_extra(extra) if r not in common]
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
            ep_map = self._ep_map
            ep_map = self._ep_map = EntryPoint.parse_map(
            exc.reason += " in {} file at path: {}".format(name, path)
            except AttributeError as e:
            except KeyError as e:
            except OSError:
            except packaging.version.InvalidVersion as ex:
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
            if line:
            if match:
            if modname in ("pkg_resources", "setuptools", "site"):
            if name is None or name == entry.name
            if not only and _is_egg_path(entry)
            if not replace_conflicting:
            if not req_extras.markers_pass(req, extras):
            if os.path.exists(plist):
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
            line = line.strip()
            loader = importer.find_module(packageName)
            loader_cls = getattr(importlib_machinery, name, type(None))
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
            new_extra = extra
            new_extra = safe_extra(new_extra) or None
            new_extra, _, marker = extra.partition(":")
            new_requirements = dist.requires(req.extras)[::-1]
            notes = "\n".join(getattr(ex, "__notes__", []))  # PEP 678
            or dist.py_version == self.python
            or dist.py_version is None
            or ntpath.isabs(path)
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
            plist = "/System/Library/CoreServices/SystemVersion.plist"
            print('Could not load', errors)
            processed[req] = True
            project_name=project_name,
            provDarwin = darwinVersionString.match(provided)
            -py(?P<pyver>[^-]+) (
            py_version=py_version,
            raise
            raise AttributeError(attr)
            raise ImportError("Entry point {!r} not found".format((group, name)))
            raise ImportError(str(exc)) from exc
            raise KeyError("No metadata except PKG-INFO is available")
            raise NotImplementedError(
            raise OSError(
            raise ResolutionError(
            raise TypeError("Can't add {!r} to environment".format(other))
            raise UnknownExtra("Can't require() without a distribution", self)
            raise ValueError("Can't change extraction path, files already extracted")
            raise ValueError("Invalid group name", group)
            raise ValueError("Invalid module name", module_name)
            raise ValueError()
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
            return ep_map.get(group, {})
            return False
            return float("inf")
            return fspath[len(self.egg_root) + 1:].split(os.sep)
            return fspath[len(self.zip_pre):]
            return functools.reduce(getattr, self.attrs, module)
            return ind
            return installer(requirement)
            return key
            return os.path.dirname(last)
            return os.path.join(base, *resource_name.split("/"))
            return registry[t]
            return self
            return self.__dep_map
            return self._dirindex
            return self._key
            return self._listdir(self._fn(self.egg_info, name))
            return self._parsed_version
            return self._pkg_info
            return self._version
            return self.egg_info
            return self.loader.get_data(path)
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
            self._dirindex = ind
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
            self.require(*args, **kwargs)
            self.specifier,
            self.url,
            self.version
            self[path] = self.manifest_mod(manifest, mtime)
            set(super().__dir__())
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
            with open(script_filename) as fid:
            ws.add(dist)
            ws.require(__requires__)
            yield Distribution.from_location(path_item, subitem, submeta)
            yield from dists
            yield from self.get_metadata_lines(name)
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
        """Return a string containing the contents of `resource_name`
        """Return a true filesystem path for `resource_name`
        """Return a true filesystem path for specified resource"""
        """Return absolute location in cache for `archive_name` and `names`
        """Return specified resource as a string"""
        """Return the `name` entry point of `group` or raise ImportError"""
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
        # 1980 offset already done
        # add any missing entries from sys.path
        # Aggressively disallow Windows absolute paths
        # Allow prereleases always in order to match the previous behavior of
        # and then put it back
        # are they the same major version and machine type?
        # Assume that metadata may be nested inside a "basket"
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
        # fallback for MacPorts
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
        # Track what packages are namespaces, so when new path items are added,
        # try it without defaults already on sys.path
        # try to download/install
        # Unpacked egg directories:
        # usable with the zipimport directory cache for our target archive
        # useful for reporting info about conflicts.
        # wheels are not supported with this finder
        # XXX
        # ymdhms+wday, yday, dst
        -(?P<ver>[^-]+) (
        (name, getattr(manager, name))
        (Note: you may not change the extraction path for a given resource
        (req,) = parse_requirements(s)
        (This is because ``sys.path`` can contain the same value more than
        )
        )._reload_version()
        ).lstrip()
        )?
        ...
        __import__(moduleOrReq)
        _bypass_ensure_directory(dirname)
        _cache.append(version.split("."))
        _cache[filename] = result = normalize_path(filename)
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
        `extras` is a list of the extras to be used with these requirements.
        `installer` is a standard installer callback as used by the
        `manager` must be an ``IResourceManager``"""
        `platform` is an optional string specifying the name of the platform
        `req`.  But, if there is an active distribution for the project and it
        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        `requirements` must be a string or a (possibly-nested) sequence
        `search_path` should be a sequence of ``sys.path`` items.  If not
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
        and zipfile.is_zipfile(path)
        Any distributions found are added to the environment.
        Any distributions found on `search_path` are added to the environment.
        any requirements are found on the path that have the correct name but
        appname="Python-Eggs"
        args = self.args + (required_by,)
        attempt to resolve older versions of a plugin if the newest version
        AttributeError: ...
        attrs = res["attr"].split(".") if res["attr"] else ()
        automatically called; you must call it explicitly or register it as an
        base ``Environment`` class, this routine just returns
        base_dir = os.path.dirname(egg_info)
        basename, ext = os.path.splitext(basename)
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
        common = types.MappingProxyType(dict.fromkeys(reqs_for_extra(None)))
        contains all currently-available distributions.  If `full_env` is not
        ContextualVersionConflict.
        converted to filenames (e.g., 1.11.0.dev0+2329eae to
        corresponding to the path entry, and they are added.  `entry` is
        date_time = zip_stat.date_time + (0, 0, -1)
        def namespace_handler(importer, path_entry, moduleName, module):
        def reqs_for_extra(extra):
        Delete all extracted resource files and directories, returning a list
        delete the extracted files when done.  There is no guarantee that
        demanded it.
        deps = []
        deps.extend(dm.get(None, ()))
        details.)
        directories. The `full_env`, if supplied, should be an ``Environment``
        directory exclusive to a single process.  This method is not
        directory used for extractions.
        dist = best.get(req.key)
        dist = Distribution(basedir, project_name=dist_name, metadata=metadata)
        dist = Distribution.from_filename(egg_path, metadata=metadata)
        dist = get_provider(dist)
        dist = Requirement.parse(dist)
        dist = self.by_key.get(req.key)
        dist_name = os.path.splitext(os.path.basename(egg_info))[0]
        distribution is found, and `installer` is supplied, then the result of
        distribution_key = project_name.lower()
        distributions = {}
        distributions = list(distributions)
        distributions in the working set, otherwise only ones matching
        distributions.sort()
        distributions_from_metadata
        dists = ws.resolve(reqs, Environment())
        dm = {}
        dm = self.__dep_map = {None: []}
        dm = self._dep_map
        dm[None].extend(common)
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
        env=None,
        environment markers and filter out any dependencies
        environment that meets the ``Requirement`` in `req`.  If no suitable
        ep = self.get_entry_info(group, name)
        equal ``sys.path``.)
        err = ExtractionError(tmpl.format(**locals()))
        err.cache_path = cache_path
        err.manager = self
        err.original_error = old_exc
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        error_info = {}
        Evaluate markers for req against each extra that
        evaluate_marker(text)
        evaluation. Otherwise, return True.
        Example usage::
        except AttributeError as e:
        except AttributeError as exc:
        except AttributeError:
        except Exception:
        except FileExistsError:
        except ImportError:
        except OSError:
        except packaging.version.InvalidVersion as ex:
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
        extras=None,
        f"Deprecated call to `pkg_resources.declare_namespace({packageName!r})`.\n"
        factory = dist_factory(path_item, entry, only)
        False
        filename = "{}-{}-py{}".format(
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
        for group, lines in data:
        for item in search_path:
        for item in self.entries:
        for key in self._distmap.keys():
        for line in f:
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
        fullpath = os.path.join(path_item, entry)
        g["_sset_" + _state_vars[k]](k, g[k], v)
        generally only be called when the extraction path is a temporary
        Given a mapping of extras to dependencies, strip off
        have anything special they should do.
        https://setuptools.pypa.io/en/latest/pkg_resources.html#basic-resource-access
        if
        if "/".join(self._parts(zip_path)) in eagers:
        if _is_egg_path(subitem):
        if _normalize_cached(item) == normalized:
        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        If `existing=True` (default),
        If `name` is None, yields all entry points in `group` from all
        if a known insecure location is used.
        if attr.startswith("_"):
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
        if hasattr(self.loader, "get_data"):
        if importer.prefix:
        if insert:
        if installer is not None:
        if int(provMac.group(2)) > int(reqMac.group(2)):
        if is_meta
        if isinstance(data, dict):
        if isinstance(item, Distribution):
        if isinstance(other, Distribution):
        if isinstance(self.parsed_version, packaging.version.Version):
        If it's added, any callbacks registered with the ``subscribe()`` method
        if len(os.listdir(path)) == 0:
        if line.startswith("["):
        if md_version:
        if mode & stat.S_IWOTH or mode & stat.S_IWGRP:
        if name != "PKG-INFO":
        if not existing:
        if not extras_spec:
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
        if not self.egg_info:
        if not self.egg_name:
        if not self.has_metadata(script):
        if not self.requirers:
        if not WRITE_SUPPORT:
        if ntpath.isabs(path) and not posixpath.isabs(path):
        if os.name == "nt" and not path.startswith(os.environ["windir"]):
        if os.name == "posix":
        if os.path.exists(script_filename):
        if packageName in _namespace_packages:
        if parent:
        if path is None:
        if path is sys.path:
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
        if self.extras and not self.dist:
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
        if version == "":
        if version is not None:
        If you do not call this routine before any extractions take place, the
        if zip_path in self._index():
        importlib.import_module(packageName)
        included, even if they were already activated in this working set.
        including its ".egg" extension.  `names`, if provided, should be a
        information given by the ``IResourceProvider``.  You may set this to a
        installer=None,
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
        lines = self._get_metadata(self.PKG_INFO)
        list(map(shadow_set.add, self))
        list(map(working_set.add, items))
        Load a manifest at path or return a suitable manifest already loaded.
        loader = spec.loader if spec else None
        loader_names = (
        loc = loc or self.location
        loc = normalize_path(self.location)
        location, such as /tmp, it opens up an opportunity for an attacker to
        location=None,
        lowercase as their key.
        m = cls.pattern.match(src)
        manager once resources have been extracted, unless you first call
        maps = {}
        marker = packaging.markers.Marker(text)
        md_version = self._get_version()
        metadata = FileMetadata("/path/to/PKG-INFO")
        metadata = FileMetadata(path)
        metadata = PathMetadata(base_dir, egg_info)
        metadata = PathMetadata(egg_path, os.path.join(egg_path,'EGG-INFO'))
        metadata = PathMetadata(root, path)
        metadata,
        metadata=None,
        method is called on, which will typically mean that every directory on
        mode = os.stat(path).st_mode
        module = __import__(self.module_name, fromlist=["__name__"], level=0)
        module = sys.modules[moduleOrReq]
        module = sys.modules[packageName] = types.ModuleType(packageName)
        module.__path__ = []
        module.__path__ = new_path
        module.__path__[:] = new_path
        module_parts = package_name.count(".") + 1
        msg = "Use of .. or absolute path in a resource path is not allowed."
        mtime = os.stat(path).st_mtime
        name = ns["__name__"]
        names = "project_name version py_version platform location precedence"
        namespace["__file__"] = script_filename
        needed = self.resolve(parse_requirements(requirements))
        new = self.__class__([], platform=None, python=None)
        nloc = _normalize_cached(loc)
        None is returned instead.  This method is a hook that allows subclasses
        Non-string values are not.
        normalized_name = packaging.utils.canonicalize_name(dist.key)
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
        path = sys.path
        path defaults to the return value of ``get_default_cache()``.  (Which
        path, _ = os.path.split(path)
        path.append(subpath)
        path.lower().endswith(".egg")
        path_parts = path.split(os.sep)
        platform=None,
        platform-specific fallbacks.  See that routine's documentation for more
        plugin_projects = list(plugin_env)
        plugin_projects.sort()
        precedence=DEVELOP_DIST,
        precedence=EGG_DIST,
        Prepare the master working set.
        processed = {}
        project_name = safe_name(self.name)
        project_name, version, py_version, platform = [None] * 4
        project_name=None,
        project's distributions use their project's name converted to all
        provMac = macosVersionString.match(provided)
        py_compat = (
        py_version=PY_MAJOR,
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
        raise TypeError("Expected string, Requirement, or Distribution", dist)
        raise TypeError("Not a package:", packageName)
        replace an extracted file with an unauthorized payload. Warn the user
        replace_conflicting=False,
        replacement_char = "�"
        req = Requirement.parse("x" + extras_spec)
        req_extras = _ReqExtras()
        reqs = []
        reqs = parse_requirements(req_spec)
        reqs = self.dist.requires(self.extras)
        Require packages for this EntryPoint, then resolve it.
        required_by = collections.defaultdict(set)
        requirements = list(requirements)[::-1]
        requirements are truly required.
        requirements specified when this environment was created, or False
        requirements,
        res = m.groupdict()
        Resolve the entry point from its module and attrs.
        Resource providers should call this method ONLY after successfully
        Resources are extracted to subdirectories of this path based upon
        rest = version
        rest = version[len(safe):]
        return
        return ""
        return ", ".join(self.requirers)
        return "{} {}".format(self.project_name, version)
        return "EntryPoint.parse(%r)" % str(self)
        return "Requirement.parse(%r)" % str(self)
        return (
        return []
        return [dep for dep in self._dep_map if dep]
        return _cache[filename]
        return base
        return classes + (object,)
        return cls(
        return cls(res["name"], res["module"], attrs, extras, dist)
        return cls.from_location(
        return ContextualVersionConflict(*args)
        return deps
        return dist
        return distributions, error_info
        return dm
        return e
        return ep.load()
        return ep_map
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
        return result
        return s
        return safe_sys_path_index(_normalize_cached(os.sep.join(parts)))
        return self
        return self.__class__(**kw)
        return self.__class__.__name__ + repr(self.args)
        return self.__dep_map
        return self.__hash
        return self._distmap.get(distribution_key, [])
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
        return self.egg_info and self._isdir(self._fn(self.egg_info, name))
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
        return str(packaging.version.Version(version))
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
        return version
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
        See Distribute #375 for more details.
        seen = {}
        self,
        self, req, best, replace_conflicting, env, installer, required_by, to_activate
        self, search_path=None, platform=get_supported_platform(), python=PY_MAJOR
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
        self.cached_files[target_path] = 1
        self.callbacks = []
        self.callbacks = callbacks[:]
        self.callbacks.append(callback)
        self.dist = dist
        self.egg_info = egg_info
        self.egg_info = os.path.join(path, "EGG-INFO")
        self.egg_name = os.path.basename(path)
        self.egg_root = path
        self.entries = []
        self.entries = entries[:]
        self.entries.append(entry)
        self.entry_keys = {}
        self.entry_keys = keys.copy()
        self.entry_keys.setdefault(entry, [])
        self.extraction_path = path
        self.extras = tuple(extras)
        self.extras = tuple(map(safe_extra, self.extras))
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
        this = {}
        This calls the ``find(req)`` method of the `working_set` to see if a
        This function does not have any concurrency protection, so it should
        This is important because extra requirements may look like `my_req;
        This is where Mac header rewrites should be done; other platforms don't
        This method returns a 2-tuple: (`distributions`, `error_info`), where
        This method should only be called by resource providers that need to
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
        version = _version_from_file(lines)
        version = platform.mac_ver()[0]
        version = version or "[unknown version]"
        version = version.replace(" ", ".")
        version=None,
        which uses an old safe_version, and so
        while requirements:
        while sys._getframe(level).f_globals is g:
        while True:
        will be called.
        will be invoked with each requirement that cannot be met by an
        Windows path separators are straight-up disallowed.
        wish to map *all* distributions, not just those compatible with the
        with ``#`` as the first non-blank character are omitted."""
        with open(file_path, "rb") as f:
        with open(path, "rb") as stream:
        with open(self.path, encoding="utf-8", errors="replace") as f:
        with warnings.catch_warnings():
        with zipfile.ZipFile(path) as zfile:
        Workaround for #520 and #513.
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
    """Locate distribution `dist_spec` and run its `script_name` script"""
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
    """Split a string or iterable thereof into (section, content) pairs
    """Try to implement resources and metadata for arbitrary PEP 302 loaders"""
    """Wrap an actual or potential sys.path entry w/metadata"""
    """Yield distributions accessible on a sys.path directory"""
    """Yield distributions accessible via `path_item`"""
    ".dist-info": DistInfoDistribution,
    ".egg": Distribution,
    ".egg-info": EggInfoDistribution,
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
    "pkg_resources is deprecated as an API. "
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
    "See https://setuptools.pypa.io/en/latest/pkg_resources.html",
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
    # access attribute to force import under delayed import mechanisms.
    # Activate all distributions already on sys.path with replace=False and
    # backward compatibility
    # Basic resource access and distribution/entry point discovery
    # Deprecated/backward compatibility only
    # Distribution "precedence" constants
    # ensure that all distributions added to the working set in the future
    # Environmental control
    # Exceptions
    # filesystem utilities
    # FIXME: 'Distribution.insert_on' is too complex (13)
    # FIXME: 'ZipProvider._extract_resource' is too complex (12)
    # macOS special cases
    # match order
    # may not know their name or version without loading PKG-INFO)
    # metadata until/unless it's actually needed.  (i.e., some distributions
    # no write support, probably under GAE
    # Parsing functions and string utilities
    # Primary implementation classes
    # Python 3.2 compatibility
    # scan for .egg and .egg-info in directory
    # These properties have to be lazy so that we don't have to load any
    # use find_spec (PEP 451) and fall-back to find_module (PEP 302)
    # Warnings
    # with higher priority (replace=True).
    # wrap up last segment
    # XXX Linux and other platforms' special cases should go here
    (?P<name>[^-]+) (
    )
    ):
    )?
    @classmethod
    @property
    @staticmethod
    []
    _, _, value = line.partition(":")
    _declare_state("object", working_set=working_set)
    _distribution_finders[importer_type] = distribution_finder
    _imp.acquire_lock()
    _isdir = _has = lambda self, path: False
    _namespace_handlers[importer_type] = namespace_handler
    _provider_factories[loader_type] = provider_factory
    _state_vars.update(dict.fromkeys(kw, vartype))
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
    API available.
    at their own risk.
    Attempt to list contents of path, but suppress some exceptions.
    Base class for warning about deprecations in ``pkg_resources``
    cache_path
    comment-only lines.  If there are any such lines before the first section
    content = []
    Contrary to POSIX 2008, on Cygwin, getcwd (3) contains
    Convert an arbitrary string to a standard version string
    corresponding to their sys.path order
    current version of the OS.
    def __add__(self, other):
    def __bool__(self):
    def __call__(self, fullpath):
    def __contains__(self, dist):
    def __contains__(self, item):
    def __dir__(self):
    def __eq__(self, other):
    def __ge__(self, other):
    def __getattr__(self, attr):
    def __getitem__(self, project_name):
    def __getstate__(self):
    def __gt__(self, other):
    def __hash__(self):
    def __iadd__(self, other):
    def __init__(
    def __init__(self):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, entries=None):
    def __init__(self, importer):
    def __init__(self, module):
    def __init__(self, name, module_name, attrs=(), extras=(), dist=None):
    def __init__(self, path):
    def __init__(self, path, egg_info):
    def __init__(self, requirement_string):
    def __iter__(self):
    def __le__(self, other):
    def __lt__(self, other):
    def __ne__(self, other):
    def __repr__(self):
    def __setstate__(self, e_k_b_n_c):
    def __str__(self):
    def _added_new(self, dist):
    def _build_dep_map(self):
    def _build_from_requirements(cls, req_spec):
    def _build_master(cls):
    def _compute_dependencies(self):
    def _dep_map(self):
    def _eager_to_zip(self, resource_name):
    def _extract_resource(self, manager, zip_path):  # noqa: C901
    def _filter_extras(dm):
    def _fn(self, base, resource_name):
    def _forgiving_parsed_version(self):
    def _get(self, path):
    def _get_date_and_size(zip_stat):
    def _get_eager_resources(self):
    def _get_metadata(self, name):
    def _get_metadata_path(self, name):
    def _get_metadata_path_for_display(self, name):
    def _get_version(self):
    def _has(self, fspath):
    def _has(self, path):
    def _index(self):
    def _is_current(self, file_path, zip_path):
    def _isdir(self, fspath):
    def _isdir(self, path):
    def _listdir(self, fspath):
    def _listdir(self, path):
    def _parse_extras(cls, extras_spec):
    def _parsed_pkg_info(self):
    def _parts(self, zip_path):
    def _register(cls):
    def _reload_version(self):
    def _resolve_dist(
    def _resource_to_zip(self, resource_name):
    def _set_egg(self, path):
    def _setup_prefix(self):
    def _validate_resource_path(path):
    def _warn_on_replacement(self, metadata):
    def _warn_unsafe_extraction_path(path):
    def _zipinfo_name(self, fspath):
    def activate(self, path=None, replace=False):
    def add(self, dist):
    def add(self, dist, entry=None, insert=True, replace=False):
    def add_entry(self, entry):
    def as_requirement(self):
    def best_match(self, req, working_set, installer=None, replace_conflicting=False):
    def build(cls, path):
    def can_add(self, dist):
    def check_version_conflict(self):
    def cleanup_resources(self, force=False):
    def clone(self, **kw):
    def dist(self):
    def egg_name(self):
    def extraction_error(self):
    def extras(self):
    def find(self, req):
    def find_plugins(self, plugin_env, full_env=None, installer=None, fallback=True):
    def from_filename(cls, filename, metadata=None, **kw):
    def from_location(cls, location, basename, metadata=None, **kw):
    def get_cache_path(self, archive_name, names=()):
    def get_entry_info(self, group, name):
    def get_entry_map(self, group=None):
    def get_metadata(name):
    def get_metadata(self, name):
    def get_metadata_lines(name):
    def get_metadata_lines(self, name):
    def get_resource_filename(manager, resource_name):
    def get_resource_filename(self, manager, resource_name):
    def get_resource_stream(manager, resource_name):
    def get_resource_stream(self, manager, resource_name):
    def get_resource_string(manager, resource_name):
    def get_resource_string(self, manager, resource_name):
    def has_metadata(name):
    def has_metadata(self, name):
    def has_resource(resource_name):
    def has_resource(self, resource_name):
    def has_version(self):
    def hashcmp(self):
    def insert_on(self, path, loc=None, replace=False):  # noqa: C901
    def is_version_line(line):
    def iter_entry_points(self, group, name=None):
    def key(self):
    def load(self, path):
    def load(self, require=True, *args, **kwargs):
    def load_entry_point(self, group, name):
    def markers_pass(self, req, extras=None):
    def metadata_isdir(name):
    def metadata_isdir(self, name):
    def metadata_listdir(name):
    def metadata_listdir(self, name):
    def obtain(self, requirement, installer=None):
    def parse(cls, src, dist=None):
    def parse(s):
    def parse_group(cls, group, lines, dist=None):
    def parse_map(cls, data, dist=None):
    def parsed_version(self):
    def position_in_sys_path(path):
    def postprocess(self, tempname, filename):
    def remove(self, dist):
    def report(self):
    def req(self):
    def require(self, *requirements):
    def require(self, env=None, installer=None):
    def required_by(self):
    def requirers(self):
    def requirers_str(self):
    def requires(self, extras=()):
    def resolve(
    def resolve(self):
    def resource_exists(self, package_or_requirement, resource_name):
    def resource_filename(self, package_or_requirement, resource_name):
    def resource_isdir(resource_name):
    def resource_isdir(self, package_or_requirement, resource_name):
    def resource_isdir(self, resource_name):
    def resource_listdir(resource_name):
    def resource_listdir(self, package_or_requirement, resource_name):
    def resource_listdir(self, resource_name):
    def resource_stream(self, package_or_requirement, resource_name):
    def resource_string(self, package_or_requirement, resource_name):
    def run_script(script_name, namespace):
    def run_script(self, requires, script_name):
    def run_script(self, script_name, namespace):
    def safe_sys_path_index(entry):
    def scan(self, search_path=None):
    def set_extraction_path(self, path):
    def subscribe(self, callback, existing=True):
    def version(self):
    def with_context(self, required_by):
    def zipinfo(self):
    DeprecationWarning,
    Determine if given path appears to be an egg.
    Determine if given path appears to be an unpacked egg.
    dirname = os.path.dirname(path)
    dirname, filename = split(path)
    dist_groups = map(find_distributions, resolved_paths)
    distutils.  But what we want when checking compatibility is to know the
    distutils.util.get_platform() normally reports the minimum version
    drop_comment,
    Each ``section`` is a stripped version of the section header ("[section]")
    eagers = None
    egg_info = None
    egg_name = None
    elif not hasattr(module, "__path__"):
    else:
    Ensure object appears in the mro even
    entries = (os.path.join(path_item, child) for child in safe_listdir(path_item))
    entry = os.path.basename(path)
    EQEQ = re.compile(r"([\(,])\s*(\d.*?)\s*([,\)])")
    equivalent subpath.  For an example namespace handler, see
    Evaluate a PEP 508 environment marker.
    except (PermissionError, NotADirectoryError):
    except AttributeError:
    except KeyError:
    except OSError as e:
    except packaging.markers.InvalidMarker as e:
    except packaging.version.InvalidVersion:
    except SyntaxError as e:
    except ValueError:
    explicitly require a newer version of macOS, we must also know the
    extraction_path = None
    f(*args, **kwargs)
    False
    FileExistsError
    FileExistsError = OSError
    finally:
    Find eggs in zip files; possibly multiple nested eggs.
    finder = _find_adapter(_distribution_finders, importer)
    for entry in sorted(entries):
    for item in module.__path__:
    for k, v in _state_vars.items():
    for k, v in state.items():
    for line in yield_lines(s):
    for old-style classes.
    for subitem in metadata.resource_listdir(""):
    for t in types:
    from os import mkdir, rename, unlink
    from sysconfig import get_platform
    g = globals()
    g.update(
    g["_manager"] = manager
    Given a path to an .egg-link, resolve distributions
    Given an iterable of lines from a Metadata file, return
    globals().update(kw)
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
    if not _cache:
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
    import _imp
    import imp as _imp
    import importlib.machinery as importlib_machinery
    importer = get_importer(path_item)
    importlib_machinery = None
    importlib_machinery.__name__
    Invocation by other packages is unsupported and done
    is_dist_info = lower.endswith(".dist-info") and os.path.isdir(
    is_egg_info = lower.endswith(".egg-info")
    is_meta = is_egg_info or is_dist_info
    item and the importer instance, yields ``Distribution`` instances found on
    iter_entry_points = working_set.iter_entry_points
    join_continuation,
    last = None
    level = 1
    line = next(iter(version_lines), "")
    list(map(working_set.add_entry, sys.path))
    load = build
    loader = getattr(module, "__loader__", None)
    loader = None
    local = f"sanitized.{_safe_segment(rest)}".strip(".")
    lower = entry.lower()
    m = macosVersionString.match(plat)
    manager
    manager = ResourceManager()
    manifest_mod = collections.namedtuple("manifest_mod", "manifest mtime")
    Map each requirement to the extras that demanded it.
    match = _PEP440_FALLBACK.search(version)
    Memoized zipfile manifests.
    metadata = EggMetadata(importer)
    module = sys.modules.get(packageName)
    module_path = None
    msg = (
    name = ns["__name__"]
    name = parts.pop()
    named "Python-Eggs".
    Namespace handlers are only called if the importer object has already
    needs some hacks for Linux and macOS.
    new_path = [_normalize_cached(p) for p in new_path]
    new_path = sorted(orig_path, key=position_in_sys_path)
    normalized = _normalize_cached(subpath)
    ns = sys._getframe(1).f_globals
    ns.clear()
    ns["__name__"] = name
    ob.__setstate__(state)
    ob.clear()
    ob.update(state)
    of macOS that would be required to *use* extensions produced by
    of pkg_resources. It is intended to be invoked once at
    old_open = os.open
    or a platform-relevant user cache dir for an app
    original_error
    os.makedirs(dirname, exist_ok=True)
    os.path.abspath() works around this limitation. A fix in os.getcwd()
    parts = packageName.split(".")
    path_item = _normalize_cached(path_item)
    pattern = re.compile(
    PEP 440.
    PKG_INFO = "METADATA"
    PKG_INFO = "PKG-INFO"
    plat = get_build_platform()
    plat = get_platform()
    platform strings, this function should be extended accordingly.
    Prepare the master working set and make the ``require()``
    present in the referenced path.
    r"""
    raise RuntimeError("Python 3.5 or later is required")
    Raise SyntaxError if marker is invalid.
    re.VERBOSE | re.IGNORECASE,
    Rebuild module.__path__ ensuring that all entries are ordered
    referenced_paths = non_empty_lines(path)
    register_finder(pkgutil.ImpImporter, find_on_path)
    register_namespace_handler(pkgutil.ImpImporter, file_ns_handler)
    reqMac = macosVersionString.match(required)
    require = working_set.require
    require(dist_spec)[0].run_script(script_name, ns)
    Requirement.
    requirements that required the installed Distribution.
    resolved_paths = (
    return (
    return ()
    return _cache[0]
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
    return map(Requirement, join_continuation(map(drop_comment, yield_lines(strs))))
    return name.replace("-", "_")
    return next(dist_groups, ())
    return None
    return os.environ.get("PYTHON_EGG_CACHE") or platformdirs.user_cache_dir(
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
    returns an ``IResourceProvider`` for that module.
    Returns true if either platform is ``None``, or the platforms are equal.
    root = os.path.dirname(path)
    run_main = run_script
    run_script = working_set.run_script
    section = None
    segment = re.sub("[^A-Za-z0-9.]+", "-", segment)
    segment = re.sub("-[^A-Za-z0-9]+", "-", segment)
    Should be initialized with the installed Distribution and the requested
    stacklevel=2,
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
    types = _always_object(inspect.getmro(getattr(ob, "__class__", type(ob))))
    Usage::
    Used when there is an issue with a version or specifier not complying with
    Validate text as a PEP 508 environment marker; return an exception
    version = version.replace(" ", ".")
    version of macOS that we are *running*.  To allow usage of packages that
    version_lines = filter(is_version_line, lines)
    visible by default.
    w/metadata, .dist-info style.
    warnings.warn(msg, DeprecationWarning, stacklevel=2)
    warnings.warn(stacklevel=level + 1, *args, **kw)
    which is treated as existing, and will be the contents of the file at
    while path != last:
    with open(path) as f:
    working_set = WorkingSet._build_master()
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
# backward compatibility
# because we want earlier uses of filterwarnings to take precedence over this
# capture these to bypass sandboxing
# declare some globals that will be defined later to
# from jaraco.functools 1.3
# one.
# randomly just because they use pkg_resources. We want to append the rule
# satisfy the linters.
# Silence the PEP440Warning by default, so that end users don't get hit by it
# XXX backward compat
# XXX backward compatibility
)
).match
.egg files, and unpacked .egg files.  It can also work in a limited way with
.zip files and with custom PEP 302 loaders that support the ``get_data()``
:mod:`importlib.metadata` and :pypi:`packaging` instead.
@_call_aside
]
__all__ = [
__import__("pip._vendor.packaging.markers")
__import__("pip._vendor.packaging.requirements")
__import__("pip._vendor.packaging.specifiers")
__import__("pip._vendor.packaging.utils")
__import__("pip._vendor.packaging.version")
_declare_state("dict", _distribution_finders={})
_declare_state("dict", _namespace_handlers={})
_declare_state("dict", _namespace_packages={})
_distribution_finders = None
_distributionImpl = {
_namespace_handlers = None
_namespace_packages = None
_PEP440_FALLBACK = re.compile(r"^v?(?P<safe>(?:[0-9]+!)?[0-9]+(?:\.[0-9]+)*)", re.I)
_provider_factories = {}
_sget_none = _sset_none = lambda *args: None
_state_vars = {}
}
A resource is a logical file contained within a package, or a logical
add_activation_listener = None
AvailableDistributions = Environment
BINARY_DIST = 2
CHECKOUT_DIST = 0
class _ReqExtras:
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
cleanup_resources = None
darwinVersionString = re.compile(r"darwin-(\d+)\.(\d+)\.(\d+)-(.*)")
def __getstate__():
def __setstate__(state):
def _always_object(classes):
def _bypass_ensure_directory(path):
def _call_aside(f, *args, **kwargs):
def _cygwin_patch(filename):  # pragma: nocover
def _declare_state(vartype, **kw):
def _find_adapter(registry, ob):
def _forgiving_version(version):
def _handle_ns(packageName, path_item):
def _initialize(g=globals()):
def _initialize_master_working_set():
def _is_egg_path(path):
def _is_unpacked_egg(path):
def _is_zip_egg(path):
def _macos_arch(machine):
def _macos_vers(_cache=[]):
def _mkstemp(*args, **kw):
def _normalize_cached(filename, _cache={}):
def _parents(path):
def _rebuild_mod_path(orig_path, package_name, module):
def _safe_segment(segment):
def _set_parent_ns(packageName):
def _sget_dict(val):
def _sget_object(val):
def _sset_dict(key, ob, state):
def _sset_object(key, ob, state):
def _version_from_file(lines):
def compatible_platforms(provided, required):
def declare_namespace(packageName):
def dist_factory(path_item, entry, only):
def distributions_from_metadata(path):
def ensure_directory(path):
def evaluate_marker(text, extra=None):
def file_ns_handler(importer, path_item, packageName, module):
def find_distributions(path_item, only=False):
def find_eggs_in_zip(importer, path_item, only=False):
def find_nothing(importer, path_item, only=False):
def find_on_path(importer, path_item, only=False):
def fixup_namespace_packages(path_item, parent=None):
def get_build_platform():
def get_default_cache():
def get_distribution(dist):
def get_entry_info(dist, group, name):
def get_entry_map(dist, group=None):
def get_provider(moduleOrReq):
def get_supported_platform():
def invalid_marker(text):
def issue_warning(*args, **kw):
def load_entry_point(dist, group, name):
def non_empty_lines(path):
def normalize_path(filename):
def null_ns_handler(importer, path_item, packageName, module):
def parse_requirements(strs):
def register_finder(importer_type, distribution_finder):
def register_loader_type(loader_type, provider_factory):
def register_namespace_handler(importer_type, namespace_handler):
def resolve_egg_link(path):
def run_script(dist_spec, script_name):
def safe_extra(extra):
def safe_listdir(path):
def safe_name(name):
def safe_version(version):
def split_sections(s):
def to_filename(name):
DefaultProvider._register()
DEVELOP_DIST = -1
EGG_DIST = 3
EGG_NAME = re.compile(
empty_provider = EmptyProvider()
except ImportError:
except NameError:
from os import open as os_open
from os import utime
from os.path import isdir, split
from pip._internal.utils._jaraco_text import (
from pip._vendor import packaging
from pip._vendor import platformdirs
from pkgutil import get_importer
get_platform = get_build_platform
if hasattr(pkgutil, "ImpImporter"):
if sys.version_info < (3, 5):
import collections
import email.parser
import errno
import functools
import importlib
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
iter_entry_points = None
macosVersionString = re.compile(r"macosx-(\d+)\.(\d+)-(.*)")
method.
MODULE = re.compile(r"\w+(\.\w+)*$").match
names being passed into the API.
Package resource API
parse_version = packaging.version.Version
path separator is.  Do not use os.path operations to manipulate resource
PY_MAJOR = "{}.{}".format(*sys.version_info)
register_finder(importlib_machinery.FileFinder, find_on_path)
register_finder(object, find_nothing)
register_finder(zipimport.zipimporter, find_eggs_in_zip)
register_loader_type(object, NullProvider)
register_loader_type(zipimport.zipimporter, ZipProvider)
register_namespace_handler(importlib_machinery.FileFinder, file_ns_handler)
register_namespace_handler(object, null_ns_handler)
register_namespace_handler(zipimport.zipimporter, file_ns_handler)
require = None
resource_dir = None
resource_exists = None
resource_filename = None
resource_isdir = None
resource_listdir = None
resource_stream = None
resource_string = None
resources_stream = None
run_main = run_script
set_extraction_path = None
SOURCE_DIST = 1
subdirectory thereof.  The package resource API expects resource names
The package resource API is designed to work with normal filesystem packages,
This module is deprecated. Users are directed to :mod:`importlib.resources`,
to have their path parts separated with ``/``, *not* whatever the local
try:
warnings.filterwarnings("ignore", category=PEP440Warning, append=True)
warnings.warn(
working_set = None
