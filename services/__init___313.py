
------
--------------- ---------------------------------------------------------
-------------------- ---------------------------------------------------------
-------------------- ----------------------------------------------------------
--------------------------------------------- ---
                     (deprecated, use ``integers(..., closed=True)`` instead)
    """
    """Return a RandomState instance.
    "beta",
    "binomial",
    "BitGenerator",
    "bytes",
    "chisquare",
    "choice",
    "default_rng",
    "dirichlet",
    "exponential",
    "f",
    "gamma",
    "Generator",
    "geometric",
    "get_state",
    "gumbel",
    "hypergeometric",
    "laplace",
    "logistic",
    "lognormal",
    "logseries",
    "MT19937",
    "multinomial",
    "multivariate_normal",
    "negative_binomial",
    "noncentral_chisquare",
    "noncentral_f",
    "normal",
    "pareto",
    "PCG64",
    "PCG64DXSM",
    "permutation",
    "Philox",
    "poisson",
    "power",
    "rand",
    "randint",
    "randn",
    "random",
    "random_integers",
    "random_sample",
    "RandomState",
    "ranf",
    "rayleigh",
    "sample",
    "seed",
    "SeedSequence",
    "set_state",
    "SFC64",
    "shuffle",
    "standard_cauchy",
    "standard_exponential",
    "standard_gamma",
    "standard_normal",
    "standard_t",
    "triangular",
    "uniform",
    "vonmises",
    "wald",
    "weibull",
    "zipf",
    function's entire purpose is to return a newly allocated RandomState whose
    is a freshly allocated copy with a seed=0.
    Note that the state of the RandomState returned here is irrelevant, as this
    return RandomState(seed=0)
    See https://github.com/numpy/numpy/issues/4763 for a detailed discussion
    state pickle can set.  Consequently the RandomState returned by this function
    This function exists solely to assist (un)pickling.
"""
# add these for module-freeze analysis (like PyInstaller)
]
__all__ += [
__all__ = [
=============== =========================================================
==================== =========================================================
==================== ==========================================================
========================
============================================= ===
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
BitGenerator Streams that work with Generator
bytes                Uniformly distributed random bytes.
chisquare            :math:`\\chi^2` distribution.
choice               Random sample from 1-D array.
Compatibility
def __RandomState_ctor():
default_rng     Default constructor for ``Generator``
del PytestTester
dirichlet            Multivariate generalization of Beta distribution.
distributions
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
For backwards compatibility with previous versions of numpy before 1.17, the
from ._generator import Generator, default_rng
from ._mt19937 import MT19937
from ._pcg64 import PCG64, PCG64DXSM
from ._philox import Philox
from ._sfc64 import SFC64
from .bit_generator import SeedSequence, BitGenerator
from .mtrand import *
from numpy._pytesttester import PytestTester
functions - removed
gamma                Gamma distribution.
Generator
Generator       Class implementing all of the random number distributions
geometric            Geometric distribution.
get_state            Get tuple representing internal state of generator.
Getting entropy to initialize a BitGenerator
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
in the new API
Internal functions
laplace              Laplace distribution.
Legacy
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
MT19937
multinomial          Multivariate generalization of the binomial distribution.
Multivariate
multivariate_normal  Multivariate generalization of the normal distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
PCG64
PCG64DXSM
permutation          Randomly permute a sequence / generate a random sequence.
Philox
poisson              Poisson distribution.
power                Power distribution.
rand                 Uniformly distributed values.
randint              Uniformly distributed integers in a given range
randn                Normally distributed values.
random               Uniformly distributed floats over ``[0, 1)``
Random Number Generation
random_integers      Uniformly distributed integers in a given range.
random_sample        Alias for `random_sample`
ranf                 Uniformly distributed floating point numbers.
rayleigh             Rayleigh distribution.
seed                 Seed the legacy random number generator.
SeedSequence
set_state            Set state of generator.
SFC64
shuffle              Randomly permute a sequence in place.
Standard
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
test = PytestTester(__name__)
triangular           Triangular distribution.
uniform              Uniform distribution.
Univariate
Use ``default_rng()`` to create a `Generator` and call its methods.
use the new `Generator` API.
Utility functions
various aliases to the global `RandomState` methods are left alone and do not
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
