
            [pattern_unformatted % (f.name, f._pattern) for f in iter(self)]
        """
        )
        Called every time we care about the mapping of names to features.
        for using the lib2to3 patcomp.
        Format the above text with the name and minimum version required.
        Implement a simple mapping to get patterns from names.
        return " |\n".join(
        return message_unformatted % (self.name, self.version)
        return self.mapping[key]
        self._pattern = PATTERN
        self.mapping = {f.name: f for f in iter(self)}
        self.name = name
        self.update_mapping()
        self.version = version
        Uses the mapping of names to features to return a PATTERN suitable
    """
    @property
    A feature has a name, a pattern, and a minimum version of Python 2.x
    A set of features that generates a pattern for the features it contains.
    def __getitem__(self, key):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, name, PATTERN, version):
    def message_text(self):
    def PATTERN(self):
    def update_mapping(self):
    mapping = {}
    required to use the feature (or 3.x if there is no backwards-compatible
    This set will act like a mapping in that we map names to patterns.
    version of 2.x)
"""
%s is only supported in Python %s and above."""
Base classes for features that are backwards-incompatible.
class Feature:
class Features:
features = Features()
features.add(Feature("py3k_feature", "power< 'py3k' any* >", "2.7"))
message_unformatted = """
PATTERN = features.PATTERN
pattern_unformatted = "%s=%s"  # name=pattern, for dict lookups
Usage:
