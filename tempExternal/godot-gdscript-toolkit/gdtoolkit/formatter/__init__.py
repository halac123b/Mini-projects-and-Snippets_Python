import types

DEFAULT_CONFIG = types.MappingProxyType(
    {
        "excluded_directories": {".git"},
        "safety_checks": None,
        "use_spaces": None,
        "line_length": None,
    }
)