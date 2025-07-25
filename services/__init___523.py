
                    message = f"Invalid licenseref: {final_token!r}"
                    message = f"Unknown license: {final_token!r}"
                    raise InvalidLicenseExpression(message)
                final_token = token
                final_token = token[:-1]
                if final_token not in LICENSES:
                if not license_ref_allowed.match(final_token):
                message = f"Unknown license exception: {token!r}"
                normalized_tokens.append(license_refs[final_token] + suffix)
                normalized_tokens.append(LICENSES[final_token]["id"] + suffix)
                raise InvalidLicenseExpression(message)
                suffix = ""
                suffix = "+"
            continue
            else:
            if final_token.startswith("licenseref-"):
            if token not in EXCEPTIONS:
            if token.endswith("+"):
            message = f"Invalid license expression: {raw_license_expression!r}"
            normalized_tokens.append(EXCEPTIONS[token]["id"])
            normalized_tokens.append(token.upper())
            python_tokens.append("False")
            python_tokens.append("or")
            python_tokens.append(token)
            raise InvalidLicenseExpression(message)
        ...
        elif token == "(" and python_tokens and python_tokens[-1] not in {"or", "and"}:
        elif token == "with":
        else:
        for ref in license_expression.split()
        if normalized_tokens and normalized_tokens[-1] == "WITH":
        if ref.lower().startswith(licenseref_prefix.lower())
        if token in {"or", "and", "with", "(", ")"}:
        if token not in {"or", "and", "with", "(", ")"}:
        invalid = eval(python_expression, globals(), locals())
        invalid = True
        message = f"Invalid license expression: {raw_license_expression!r}"
        normalized_expression.replace("( ", "(").replace(" )", ")"),
        NormalizedLicenseExpression,
        raise InvalidLicenseExpression(message)
        raise InvalidLicenseExpression(message) from None
        ref.lower(): "LicenseRef-" + ref[len(licenseref_prefix):]
    """
    """Raised when a license-expression string is invalid
    "canonicalize_license_expression",
    "InvalidLicenseExpression",
    "NormalizedLicenseExpression",
    # `False` and the expression should evaluate as such.
    # and so boolean operators are Python-compatible.
    # Normalize to lower case so we can look up licenses/exceptions
    # Pad any parentheses so tokenization can be achieved by merely splitting on
    # parse. Everything that is not involved with the grammar itself is treated as
    # Rather than implementing boolean logic, we create an expression that Python can
    # Take a final pass to check for unknown licenses/exceptions.
    # whitespace.
    )
    }
    >>> canonicalize_license_expression("invalid")
    def __init__(self, *args, **kwargs): pass
    except Exception:
    for token in tokens:
    if invalid is not False:
    if not raw_license_expression:
    license_expression = license_expression.lower()
    license_expression = raw_license_expression.replace("(", " ( ").replace(")", " ) ")
    license_refs = {
    licenseref_prefix = "LicenseRef-"
    normalized_expression = " ".join(normalized_tokens)
    normalized_tokens = []
    packaging.licenses.InvalidLicenseExpression: Invalid license expression: 'invalid'
    python_expression = " ".join(python_tokens)
    python_tokens = []
    raw_license_expression: str,
    return cast(
    tokens = license_expression.split()
    Traceback (most recent call last):
    try:
#
#  https://github.com/pypa/hatch/blob/5352e44/backend/src/hatchling/licenses/parse.py
# `LicenseRef-Public-Domain` and `LicenseRef-Proprietary`.
# Adapted from:
# conditions:
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# Copyright (c) 2017-present Ofek Lev <oss@ofek.dev>
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# MIT License
# or substantial portions of the Software.
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# permit persons to whom the Software is furnished to do so, subject to the following
# software and associated documentation files (the "Software"), to deal in the Software
# The above copyright notice and this permission notice shall be included in all copies
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# With additional allowance of arbitrary `LicenseRef-` identifiers, not just
# without restriction, including without limitation the rights to use, copy, modify,
#######################################################################################
) -> NormalizedLicenseExpression:
]
__all__ = [
class InvalidLicenseExpression:
def canonicalize_license_expression(
from __future__ import annotations
from pip._vendor.packaging.licenses._spdx import EXCEPTIONS, LICENSES
from typing import NewType, cast
import re
license_ref_allowed = re.compile("^[A-Za-z0-9.-]*$")
NormalizedLicenseExpression = NewType("NormalizedLicenseExpression", str)
