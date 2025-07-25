
            "`_supports_reduction` instead.",
            "BaseBooleanReduceTests is deprecated and will be removed in a "
            "BaseNoReduceTests is deprecated and will be removed in a "
            "BaseNumericReduceTests is deprecated and will be removed in a "
            "future version. Use BaseReduceTests and override "
            FutureWarning,
        )
        f"module 'pandas.tests.extension.base' has no attribute '{name}'"
        from pandas.tests.extension.base.reduce import BaseBooleanReduceTests
        from pandas.tests.extension.base.reduce import BaseNoReduceTests
        from pandas.tests.extension.base.reduce import BaseNumericReduceTests
        return BaseBooleanReduceTests
        return BaseNoReduceTests
        return BaseNumericReduceTests
        warnings.warn(
       pass
       return MyDtype()
    )
    BaseAccumulateTests,
    BaseArithmeticOpsTests,
    BaseCastingTests,
    BaseComparisonOpsTests,
    BaseConstructorsTests,
    BaseDtypeTests,
    BaseGetitemTests,
    BaseGroupbyTests,
    BaseIndexTests,
    BaseInterfaceTests,
    BaseMethodsTests,
    BaseMissingTests,
    BaseOpsUtil,
    BaseParsingTests,
    BasePrintingTests,
    BaseReduceTests,
    BaseReshapingTests,
    BaseSetitemTests,
    BaseUnaryOpsTests,
    def __init__(self, *args, **kwargs): pass
    Dim2CompatTests,
    elif name == "BaseBooleanReduceTests":
    elif name == "BaseNumericReduceTests":
    if name == "BaseNoReduceTests":
    import warnings
    NDArrayBacked2DTests,
    pass
    raise AttributeError(
   @pytest.fixture
   class TestMyDtype:
   def dtype():
   from pandas.tests.extension.base import BaseDtypeTests
   import pytest
"""
#  BaseNoReduceTests, or BaseNumericReduceTests
# Note 1) this excludes Dim2CompatTests and NDArrayBacked2DTests.
# Note 2) this uses BaseReduceTests and and _not_ BaseBooleanReduceTests,
# One test class that you can inherit as an alternative to inheriting all the
# test classes above.
)
):
* A ``conftest.py`` in the same directory as your test class.
* The same module as your test class.
.. code-block:: python
``BaseDtypeTests``. pytest's fixture discover will supply your ``dtype``
Base test suite for extension arrays.
class ExtensionTests(
def __getattr__(name: str):
file.
for the tests. The fixtures may be located in either
from pandas.tests.extension.base.accumulate import BaseAccumulateTests
from pandas.tests.extension.base.casting import BaseCastingTests
from pandas.tests.extension.base.constructors import BaseConstructorsTests
from pandas.tests.extension.base.dim2 import (  # noqa: F401
from pandas.tests.extension.base.dtype import BaseDtypeTests
from pandas.tests.extension.base.getitem import BaseGetitemTests
from pandas.tests.extension.base.groupby import BaseGroupbyTests
from pandas.tests.extension.base.index import BaseIndexTests
from pandas.tests.extension.base.interface import BaseInterfaceTests
from pandas.tests.extension.base.io import BaseParsingTests
from pandas.tests.extension.base.methods import BaseMethodsTests
from pandas.tests.extension.base.missing import BaseMissingTests
from pandas.tests.extension.base.ops import (  # noqa: F401
from pandas.tests.extension.base.printing import BasePrintingTests
from pandas.tests.extension.base.reduce import BaseReduceTests
from pandas.tests.extension.base.reshaping import BaseReshapingTests
from pandas.tests.extension.base.setitem import BaseSetitemTests
Libraries are expected to implement a few pytest fixtures to provide data
renaming the tests should not be done lightly.
that their extension arrays and dtypes satisfy the interface. Moving or
The full list of fixtures may be found in the ``conftest.py`` next to this
These tests are intended for third-party libraries to subclass to validate
wherever the test requires it. You're free to implement additional tests.
Your class ``TestDtype`` will inherit all the tests defined on
