
    -------
    ----------
    --------------------------------------------------------------------------
        -------
        ----------
                                        : target[key],
                                        : typeof target[key] === "function"
                                        ? false
                                        ? target[key].bind(target)
                                        ANDROID: 'android',
                                        APP_UPDATE: 'app_update',
                                        ARM: 'arm',
                                        ARM64: 'arm64',
                                        CANNOT_RUN: 'cannot_run',
                                        CHROME_UPDATE: 'chrome_update',
                                        CROS: 'cros',
                                        DISABLED: 'disabled',
                                        INSTALL: 'install',
                                        INSTALLED: 'installed',
                                        LINUX: 'linux',
                                        MAC: 'mac',
                                        MIPS: 'mips',
                                        MIPS64: 'mips64',
                                        NO_UPDATE: 'no_update',
                                        NOT_INSTALLED: 'not_installed'
                                        OPENBSD: 'openbsd',
                                        OS_UPDATE: 'os_update',
                                        PERIODIC: 'periodic'
                                        READY_TO_RUN: 'ready_to_run',
                                        RUNNING: 'running'
                                        SHARED_MODULE_UPDATE: 'shared_module_update',
                                        THROTTLED: 'throttled',
                                        UPDATE: 'update'
                                        UPDATE_AVAILABLE: 'update_available'
                                        WIN: 'win'
                                        X86_32: 'x86-32',
                                        X86_64: 'x86-64'
                                      key === "webdriver"
                                    : originalQuery(parameters)
                                    ? Promise.resolve({ state: window.Notification.permission })
                                    }
                                    },
                                    get: (target, key) =>
                                    has: (target, key) => (key === "webdriver" ? false : key in target),
                                    InstallState: {
                                    isInstalled: false,
                                    OnInstalledReason: {
                                    OnRestartRequiredReason: {
                                    permission: 'denied'
                                    PlatformArch: {
                                    PlatformNaclArch: {
                                    PlatformOs: {
                                    RequestUpdateCheckStatus: {
                                    return 'function query() { [native code] }'
                                    return nativeToStringFunctionString
                                    RunningState: {
                                  }),
                                  value: new Proxy(navigator, {
                                }
                                });
                                },
                                app: {
                                if (this === functionToString) {
                                if (this === window.navigator.permissions.query) {
                                Object.defineProperty(window, "navigator", {
                                parameters.name === 'notifications'
                                return oldCall.apply(this, arguments)
                                return oldCall.call(oldToString, this)
                                runtime: {
                                window.Notification = {
                            """
                            "return navigator.userAgent"
                            // eslint-disable-next-line
                            // https://github.com/microlinkhq/browserless/blob/master/packages/goto/src/evasions/chrome-runtime.js
                            // https://github.com/microlinkhq/browserless/blob/master/packages/goto/src/evasions/navigator-permissions.js
                            }
                            arg, m[1]
                            const nativeToStringFunctionString = Error.toString().replace(/Error/g, 'toString')
                            const oldCall = Function.prototype.call
                            const oldToString = Function.prototype.toString
                            const originalQuery = window.navigator.permissions.query
                            function call() {
                            function functionToString() {
                            Function.prototype.call = call
                            Function.prototype.toString = functionToString
                            if (!window.Notification) {
                            Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 1});
                            Object.defineProperty(navigator.connection, 'rtt', {get: () => 100});
                            window.chrome = {
                            window.navigator.permissions.__proto__.query = parameters =>
                           Object.defineProperty(window, "navigator", {
                        "calling %s with args %s and kwargs %s\n"
                        "no user data dir could be extracted from supplied argument %s "
                        "source": """
                        "userAgent": self.execute_script(
                        "user-data-dir found in user argument {} => {}".format(
                        "When removing the temp profile, a %s occured: %s\nretrying..."
                        % (e.__class__.__name__, e)
                        % (original.__qualname__, args, kwargs)
                        % arg
                        )
                        ).replace("Headless", "")
                    """
                    "/Applications/Chromium.app/Contents/MacOS/Chromium",
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "created a temporary folder in which the user-data (profile) will be stored during this\n"
                    "Google/Chrome Beta/Application",
                    "Google/Chrome Canary/Application",
                    "Google/Chrome/Application",
                    "Network.setUserAgentOverride",
                    "Page.addScriptToEvaluateOnNewDocument",
                    "selenium.webdriver.remote.remote_connection"
                    "session, and added it to chrome startup arguments: %s" % arg
                    "use uc.Chrome(user_data_dir='/xyz/some/data') in case you need existing profile folder"
                    "user_data_dir property found in options object: %s" % user_data_dir
                    "using ChromeOptions.user_data_dir might stop working in future versions."
                    # fixing the restore-tabs-nag
                    )
                    {
                    },
                    break
                    candidates.add(os.sep.join((item, subitem, "chrome.exe")))
                    config["profile"]["exit_type"] = None
                    keep_user_data_dir = True
                    language = "en-US,en;q=0.9"
                    language = m[1]
                    logger.debug(
                    logger.debug("successfully removed %s" % self.user_data_dir)
                    logger.debug("will set the language to en-US,en;q=0.9")
                    pass
                    return original(*args, **kwargs)
                    setattr(service, attr_name, service_creationflags)
                    shutil.rmtree(self.user_data_dir, ignore_errors=False)
                    user_data_dir = m[1]
                "chrome",
                "chromium",
                "chromium-browser",
                "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
                "google-chrome",
                "google-chrome-stable",
                #  as it just appends arguments, not replace them
                #  prevent reuse of options,
                #  you'll get conflicts starting chrome
                # yourcallback is an callable which accepts exactly 1 dict as parameter
                )
                ).setLevel(20)
                ):
                [
                [options.binary_location, *options.arguments],
                ]
                arg = "--user-data-dir=%s" % user_data_dir
                browser_executable_path or find_chrome_executable()
                candidates.add(os.sep.join((item, subitem)))
                close_fds=IS_POSIX,
                config = json.load(fs)
                def newfunc(*args, **kwargs):
                driver.add_cdp_listener("Network.dataReceived", yourcallback)
                else selenium.webdriver.common.service.utils.free_port()
                else:
                encoding="latin1",
                except (RuntimeError, OSError, PermissionError) as e:
                except FileNotFoundError:
                except IndexError:
                for subitem in (
                fs.seek(0, 0)
                fs.truncate()  # the file might be shorter
                if config["profile"]["exit_type"] is not None:
                if hasattr(service, attr_name):
                if port != 0
                import locale
                import warnings
                json.dump(config, fs)
                keep_user_data_dir = False
                keep_user_data_dir = True
                language = "en-US"
                language = locale.getdefaultlocale()[0].replace("_", "-")
                logger.debug(
                logger.debug("fixed exit_type flag")
                logger.info("patch navigator.webdriver")
                logger.info("patch user-agent string")
                logging.getLogger(
                m = re.search("(?:--)?lang(?:[ =])?(.*)", arg)
                m = re.search("(?:--)?user-data-dir(?:[ =])?(.*)", arg)
                mode="r+",
                options, "user_data_dir", None
                options.add_argument("--headless=chrome")
                options.add_argument("--headless=new")
                options.add_argument("--user-data-dir=%s" % options.user_data_dir)
                options.add_argument(arg)
                options.arguments.remove(arg)
                options.binary_location, *options.arguments
                options.headless = True
                os.path.join(user_data_dir, "Default/Preferences"),
                pass
                port
                program exits or using .quit()
                raise RuntimeError("you cannot reuse the ChromeOptions object")
                return newfunc
                self.execute_cdp_cmd(
                self.patcher.executable_path, port, service_args, service_log_path
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                This fixes a LOT of issues, like multithreaded run, but mst importantly. shutting corectly after
                time.sleep(0.1)
                try:
                user_data_dir = os.path.normpath(tempfile.mkdtemp())
                warnings.warn(
                you should be knowing what you're doing, and know how python works.
              ! setting it to True comes with NO support when being detected. !
              and will be greeted with an error, since the program exists before chrome has a change to launch.
              d = uc.Chrome()
              d.get('https://somesite/')
              ---end script --
              import undetected_chromedriver as uc
              in that case you can set this to `True`. The browser will start via subprocess, and will keep running most of times.
              --start script--
              unfortunately, there  is always an edge case in which one would like to write an single script with the only contents being:
             path to log information from the driver.
             this option has a default of True since many people seem to run this as root (....) , and chrome does not start
             uses the --no-sandbox option, and additionally does suppress the "unsecure option" status bar
             when running as root without using --no-sandbox flag.
             Whether to configure ChromeRemoteConnection to use HTTP keep-alive.
            "--log-level=%d" % log_level
            # backward compatiblity
            # check if an old uc.ChromeOptions is used, and extract the user data dir
            ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA", "PROGRAMW6432"),
            )
            ) as fs:
            ):
            :: currently for chrome only
            <selenium.webdriver.remote.webelement.WebElement (session="85ff0f671512fa535630e71ee951b1f2", element="6357cb55-92c3-4c0f-9416-b174f9c1b8c4")>
            <WebElement(<a class="mobile-show-inline-block mc-update-infos init-ok" href="#" id="main-cat-switcher-mobile">)>
            a "welcome" alert might show up on *nix-like systems asking whether you want to set
            advanced webelement repr
            an older version of Chrome. You can specify it's full rounded version number
            and hasattr(self, "user_data_dir")
            and hasattr(self.service, "process")
            and hasattr(self.service.process, "kill")
            and isinstance(self.reactor, Reactor)
            and not self.keep_user_data_dir
            and self.reactor is not None
            and turn off automatic removal mechanism at exit.
            any customizations MAY lead to trigger bot migitation systems.
            anything other dan the default, for example extensions or startup options
            are not supported in case of failure, and can probably lowers your undetectability.
            arguments to pass to the driver service
            browser = subprocess.Popen(
            can also be specified in the options instance.
            candidates.update(
            capabilities = self.options.to_capabilities()
            capabilities, browser_profile
            cdp = CDP(self.options)
            cdp.tab_new(url)
            chrome as your default browser, and if you want to send even more data to google.
            Chrome has everything included to work out of the box.
            debug_host = "127.0.0.1"
            debug_host, debug_port = options.debugger_address.split(":")
            debug_port = (
            debug_port = int(debug_port)
            default webelement repr:
            desired_capabilities = options.to_capabilities()
            desired_capabilities=desired_capabilities,
            Dictionary object with non-browser specific capabilities only, such as "item" or "loggingPref".
            elif self.patcher.version_main >= 108:
            else:
            except Exception:
            executable_path=driver_executable_path,
            executable_path=self.patcher.executable_path,
            False (the default) makes sure Chrome will get it's own process (so no subprocess of chromedriver.exe or python
            for _ in range(5):
            for attr_name in ("creationflags", "creation_flags"):
            for subitem in (
            force=patcher_force_close,
            from .cdp import CDP
            hasattr(self, "keep_user_data_dir")
            hasattr(self, "service")
            here. Example: 87 for all versions of 87
            if "lang" in arg:
            if "user-data-dir" in arg:
            if any([_ in arg for _ in ("--headless", "headless")]):
            if hasattr(options, "_session") and options._session is not None:
            if hasattr(options, "user_data_dir") and getattr(
            if inspect.ismethod(original) and not inspect.isclass(original):
            if item is not None:
            if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            if not language:
            If not specified, make sure the executable's folder is in $PATH
            if self.execute_script("return navigator.webdriver"):
            if self.patcher.version_main < 108:
            if the file is locked, it will force shutdown all instances.
            if user_data_dir is a path to a valid chrome profile directory, use it,
            if you, for god knows whatever reason, use
            import inspect
            in an interactive environment
            instructs the patcher to do whatever it can to access the chromedriver binary
            it does not `need` customizations.
            keep_alive=keep_alive,
            leave it at 0 unless you know what you are doing.
            logger.debug("did not find a bad exit_type flag ")
            logger.debug("gracefully closed browser")
            logger.debug("shutting down reactor")
            logger.debug("webdriver process ended")
            logger.debug(e)
            logger.debug(e, exc_info=True)
            makes it easier to recognize elements like you know them from html/browser inspection, especially when working
            Note: if you don't handle the nag screen in time, the browser loses it's connection and throws an Exception.
            note: when retrieving large amounts of elements ( example: find_elements_by_tag("*") ) and print them, it does take a little more time.
            now, in case you are nag-fetishist, or a diagnostics data feeder to google, you can set this to False.
            options = ChromeOptions()
            options.add_argument("--user-data-dir=%s" % user_data_dir)
            options.arguments.extend(["--no-default-browser-check", "--no-first-run"])
            options.arguments.extend(["--no-sandbox", "--test-type"])
            options.binary_location = (
            options.debugger_address = "%s:%d" % (debug_host, debug_port)
            options.handle_prefs(user_data_dir)
            options.set_capability(
            options=options,
            or divmod(logging.getLogger().getEffectiveLevel(), 10)[0]
            original = super().__getattribute__(item)
            os.environ.get,
            os.kill(self.browser_pid, 15)
            pass
            Path to the browser executable.
            port to be used by the chromedriver executable, this is NOT the debugger port.
            port=port,
            reactor = Reactor(self)
            reactor.start()
            return orig_get(*args, **kwargs)
            return original
            return os.path.normpath(candidate)
            return self.reactor.handlers
            return super().__getattribute__(item)
            selenium.webdriver.remote.command.Command.NEW_WINDOW, {"type": "window"}
            self._configure_headless()
            self._web_element_cls = UCWebElement
            self._web_element_cls = WebElement
            self.browser_pid = browser.pid
            self.browser_pid = start_detached(
            self.reactor
            self.reactor = reactor
            self.reactor.add_event_handler(event_name, callback)
            self.reactor.event.set()
            self.reactor.handlers.clear()
            self.service.process.kill()
            self.service.start()
            self.service.stop()
            self.start_session()
            service = None
            service = selenium.webdriver.common.service.Service(
            service_args=service_args,
            service_log_path=service_log_path,
            service=service,  # needed or the service will be re-created
            setting it is not recommended, unless you know the implications and think
            Specify whether you want to use the browser in headless mode.
            the default value of 0 automatically picks an available port.
            this enables the handling of wire messages
            this takes an instance of ChromeOptions, mainly to customize browser behavior.
            try:
            version_main=version_main,
            warning: this lowers undetectability and not fully supported.
            when enabled, you can subscribe to CDP events by using:
            with open(
            you might need it.
         888                                                  888
         888                                                  888         d8b
         888                                                  888         Y8P
        """
        #     self._hook_remove_cdc_props()
        # dereference patcher, so patcher can start cleaning up as well.
        # fix exit_type flag to prevent tab-restore nag
        # fixes "could not connect to chrome" error when running
        # if self._get_cdc_props():
        # needs to be a classmethod so finalize can find the reference
        # on linux using privileged user like root (which i don't recommend)
        # see if a custom user profile is specified in options
        # self.patcher = patcher
        # super(Chrome, self).start_session(capabilities, browser_profile)
        # this must come last, otherwise it will throw 'in use' errors
        )
        ):
        **kw,
        advanced_elements:  bool, optional, default: False
        advanced_elements=False,
        apparently, that passes all tests directly!
        browser_executable_path: str, optional, default: None - use find_chrome_executable
        browser_executable_path=None,
        Creates a new instance of the chrome driver.
        debug=False,
        def get_wrapped(*args, **kwargs):
        desired_capabilities: dict, optional, default: None - auto from config
        desired_capabilities=None,
        differentiates from the regular method in that it does not
        driver_executable_path: str, optional, default: None(=downloads and patches new binary)
        driver_executable_path=None,
        else:
        enable_cdp_events: bool, default: False
        enable_cdp_events=False,
        except (AttributeError, RuntimeError, OSError):
        except AttributeError:
        except Exception as e:
        except Exception as e:  # noqa
        except:  # noqa
        finalize(self, self._ensure_close, self)
        for arg in options.arguments:
        for item in map(
        for item in os.environ.get("PATH").split(os.pathsep):
        headless: bool, optional, default: False
        headless=False,
        if "darwin" in sys.platform:
        if (
        if advanced_elements:
        if enable_cdp_events:
        if hasattr(options, "handle_prefs"):
        if headless or options.headless:
        if no_sandbox:
        if not capabilities:
        if not desired_capabilities:
        if not hasattr(self, "cdp"):
        if not language:
        if not options.binary_location:
        if not options.debugger_address:
        if not options:
        if not super().__getattribute__("debug"):
        if not use_subprocess:
        if not user_data_dir:
        if options.headless:
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
        if self.reactor and isinstance(self.reactor, Reactor):
        if service_creationflags:
        if suppress_welcome:
        if user_data_dir:
        keep_alive: bool, optional, default: True
        keep_alive=True,
        language, keep_user_data_dir = None, bool(user_data_dir)
        log_level: int, optional, default: adapts to python global log level
        log_level=0,
        logger.info("ensuring close")
        logger.info("setting properties for headless")
        no_sandbox: bool, optional, default=True
        no_sandbox=True,
        NOTE:
        options._session = self
        options.add_argument(
        options.add_argument("--lang=%s" % language)
        options.add_argument("--no-sandbox")
        options.add_argument("--remote-debugging-host=%s" % debug_host)
        options.add_argument("--remote-debugging-port=%s" % debug_port)
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options: ChromeOptions, optional, default: None - automatic useful defaults
        options=None,
        orig_get = self.get
        Parameters
        patcher_force_close: bool, optional, default: False
        patcher_force_close=False,
        port: int, optional, default: 0
        port=0,
        -recreate session
        recreated from the options at creation time.
        require a capabilities argument. The capabilities are automatically
        return False
        return hash(self.options.debugger_address)
        return object.__dir__(self)
        return self
        return super().get(url)
        Returns
        self,
        self._delay = 3
        self.debug = debug
        self.execute(
        self.get = get_wrapped
        self.keep_user_data_dir = keep_user_data_dir
        self.options = options
        self.patcher = None
        self.patcher = Patcher(
        self.patcher.auto()
        self.quit()
        self.reactor = None
        self.service.start()
        self.service.stop()
        self.start_session()
        self.user_data_dir = user_data_dir
        service_args: list of str, optional, default: None
        service_args=None,
        service_creationflags=None,
        service_log_path: str, optional, default: None
        service_log_path=None,
        -starts the chromedriver service which runs in the background
        Starts the service and then creates new instance of chrome driver.
        -stops the chromedriver service which runs in the background
        super().__init__(
        super(selenium.webdriver.chrome.webdriver.WebDriver, self).start_session(
        suppress_welcome: bool, optional , default: True
        suppress_welcome=True,
        the full file path to found executable
        this can be useful in case of heavy detection methods
        this opens a url in a new tab.
        time.sleep(self._delay)
        time.sleep(timeout)
        try:
        url
        use_subprocess: bool, optional , default: True,
        use_subprocess=True,
        user_data_dir: str , optional, default: None (creates temp profile)
        user_data_dir=None,
        version_main: int, optional, default: None (=auto)
        version_main=None,
    """
    "CDP",
    "Chrome",
    "ChromeOptions",
    "find_chrome_executable",
    "Patcher",
    "Reactor",
    #
    #                                     &&delete window[p]&&console.log('removed',p))
    #                     result = [];
    #                   objectToInspect = Object.getPrototypeOf(objectToInspect); }
    #                 """
    #                 { result = result.concat(Object.getOwnPropertyNames(objectToInspect));
    #                 let objectToInspect = window,
    #                 result.forEach(p => p.match(/^([a-zA-Z]){27}(Array|Promise|Symbol)$/ig)
    #                 while(objectToInspect !== null)
    #             "source": """
    #             result = [];
    #           objectToInspect = Object.getPrototypeOf(objectToInspect); }
    #         """
    #         "Page.addScriptToEvaluateOnNewDocument",
    #         {
    #         { result = result.concat(Object.getOwnPropertyNames(objectToInspect));
    #         },
    #         let objectToInspect = window,
    #         return result.filter(i => i.match(/^([a-zA-Z]){27}(Array|Promise|Symbol)$/ig))
    #         while(objectToInspect !== null)
    #     )
    #     return self.execute_script(
    #     self.execute_cdp_cmd(
    # def _get_cdc_props(self):
    # def _hook_remove_cdc_props(self):
    ):
    @classmethod
    _instances = set()
    Attributes
    candidates = set()
    Controls the ChromeDriver and allows you to drive the browser.
    debug = False
    def __del__(self):
    def __dir__(self):
    def __enter__(self):
    def __exit__(self, exc_type, exc_val, exc_tb):
    def __getattribute__(self, item):
    def __hash__(self):
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def _configure_headless(self):
    def _ensure_close(cls, self):
    def add_cdp_listener(self, event_name, callback):
    def clear_cdp_listeners(self):
    def get(self, url):
    def quit(self):
    def reconnect(self, timeout=0.1):
    def start_session(self, capabilities=None, browser_profile=None):
    def tab_new(self, url: str):
    def window_new(self):
    else:
    executable_path :  str
    Finds the chrome, chrome beta, chrome canary, chromium executable
    for candidate in candidates:
    if IS_POSIX:
    Methods
    reconnect()
    Returns
    session_id = None
    start_session(capabilities=None, browser_profile=None)
    The webdriver file will be downloaded by this module automatically,
    you do not need to specify this. however, you may if you wish.
 "Y8888P 888  888 888     "Y88P"  888  888  888  "Y8888   "Y88888 888     888   Y88P    "Y8888  888   88888888
 .d8888b 88888b.  888d888 .d88b.  88888b.d88b.   .d88b.   .d88888 888d888 888 888  888  .d88b.  888d888
"""
#!/usr/bin/env python3
)
__all__ = (
__version__ = "3.4.6"
888      888  888 888    888  888 888  888  888 88888888 888  888 888     888 Y88  88P 88888888 888
by UltrafunkAmsterdam (https://github.com/ultrafunkamsterdam)
class Chrome:
d88P"    888 "88b 888P"  d88""88b 888 "888 "88b d8P  Y8b d88" 888 888P"   888 888  888 d8P  Y8b 888P"
def find_chrome_executable():
from .cdp import CDP
from .dprocess import start_detached
from .options import ChromeOptions
from .patcher import IS_POSIX
from .patcher import Patcher
from .reactor import Reactor
from .webelement import UCWebElement
from .webelement import WebElement
from __future__ import annotations
from weakref import finalize
import json
import logging
import os
import re
import selenium.webdriver.chrome.service
import selenium.webdriver.chrome.webdriver
import selenium.webdriver.common.service
import selenium.webdriver.remote.command
import selenium.webdriver.remote.webdriver
import shutil
import subprocess
import sys
import tempfile
import time
logger = logging.getLogger("uc")
logger.setLevel(logging.getLogger().getEffectiveLevel())
Y88b.    888  888 888    Y88..88P 888  888  888 Y8b.     Y88b 888 888     888  Y8bd8P  Y8b.     888
