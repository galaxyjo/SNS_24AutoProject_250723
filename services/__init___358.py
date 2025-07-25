
                return style
            "Could not find style module %r" % mod
            + "."
            + (builtin and ", though it should be builtin")
            if name == found_name:
        # perhaps it got dropped into our styles package
        )
        builtin = ""
        builtin = "yes"
        cls = name.title() + "Style"
        for found_name, style in find_plugin_styles():
        mod = __import__("pygments.styles." + mod, None, None, [cls])
        mod = name
        mod, cls = STYLE_MAP[name].split("::")
        raise ClassNotFound(
        raise ClassNotFound("Could not find style class %r in style module." % cls)
        return getattr(mod, cls)
        yield name
    """
    """Return a generator for all styles by name, both builtin and plugin."""
    "abap": "abap::AbapStyle",
    "algol": "algol::AlgolStyle",
    "algol_nu": "algol_nu::Algol_NuStyle",
    "arduino": "arduino::ArduinoStyle",
    "autumn": "autumn::AutumnStyle",
    "borland": "borland::BorlandStyle",
    "bw": "bw::BlackWhiteStyle",
    "colorful": "colorful::ColorfulStyle",
    "default": "default::DefaultStyle",
    "dracula": "dracula::DraculaStyle",
    "emacs": "emacs::EmacsStyle",
    "friendly": "friendly::FriendlyStyle",
    "friendly_grayscale": "friendly_grayscale::FriendlyGrayscaleStyle",
    "fruity": "fruity::FruityStyle",
    "github-dark": "gh_dark::GhDarkStyle",
    "gruvbox-dark": "gruvbox::GruvboxDarkStyle",
    "gruvbox-light": "gruvbox::GruvboxLightStyle",
    "igor": "igor::IgorStyle",
    "inkpot": "inkpot::InkPotStyle",
    "lilypond": "lilypond::LilyPondStyle",
    "lovelace": "lovelace::LovelaceStyle",
    "manni": "manni::ManniStyle",
    "material": "material::MaterialStyle",
    "monokai": "monokai::MonokaiStyle",
    "murphy": "murphy::MurphyStyle",
    "native": "native::NativeStyle",
    "nord": "nord::NordStyle",
    "nord-darker": "nord::NordDarkerStyle",
    "one-dark": "onedark::OneDarkStyle",
    "paraiso-dark": "paraiso_dark::ParaisoDarkStyle",
    "paraiso-light": "paraiso_light::ParaisoLightStyle",
    "pastie": "pastie::PastieStyle",
    "perldoc": "perldoc::PerldocStyle",
    "rainbow_dash": "rainbow_dash::RainbowDashStyle",
    "rrt": "rrt::RrtStyle",
    "sas": "sas::SasStyle",
    "solarized-dark": "solarized::SolarizedDarkStyle",
    "solarized-light": "solarized::SolarizedLightStyle",
    "staroffice": "staroffice::StarofficeStyle",
    "stata": "stata_light::StataLightStyle",
    "stata-dark": "stata_dark::StataDarkStyle",
    "stata-light": "stata_light::StataLightStyle",
    "tango": "tango::TangoStyle",
    "trac": "trac::TracStyle",
    "vim": "vim::VimStyle",
    "vs": "vs::VisualStudioStyle",
    "xcode": "xcode::XcodeStyle",
    "zenburn": "zenburn::ZenburnStyle",
    are listed in :data:`pygments.styles.STYLE_MAP`.
    else:
    except AttributeError:
    except ImportError:
    for name, _ in find_plugin_styles():
    found.
    if name in STYLE_MAP:
    Return a style class by its short name. The names of the builtin styles
    try:
    Will raise :exc:`pygments.util.ClassNotFound` if no style of that name is
    yield from STYLE_MAP
"""
#: ``'submodule::classname'`` strings.
#: A dictionary of built-in styles, mapping style names to
:copyright: Copyright 2006-2023 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
}
~~~~~~~~~~~~~~~
Contains built-in styles.
def get_all_styles():
def get_style_by_name(name):
from pip._vendor.pygments.plugin import find_plugin_styles
from pip._vendor.pygments.util import ClassNotFound
pygments.styles
STYLE_MAP = {
