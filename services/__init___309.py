
----------
--------------
------------------
-----------------------
--------------------------
----------------------------------------
   cholesky
   cond
   cross
   det
   diagonal (Array API compatible)
   eig
   eigh
   eigvals
   eigvalsh
   inv
   LinAlgError
   lstsq
   matmul
   matrix_norm
   matrix_power
   matrix_rank
   matrix_transpose (Array API compatible)
   multi_dot
   norm
   outer
   pinv
   qr
   slogdet
   solve
   svd
   svdvals
   tensordot
   tensorinv
   tensorsolve
   trace (Array API compatible)
   vector_norm
- OpenBLAS: https://www.openblas.net/
- threadpoolctl: https://github.com/joblib/threadpoolctl
"""
# To get sub-modules
__all__ = _linalg.__all__.copy()
``dot``, ``vdot``, ``inner``, ``outer``, ``matmul``, ``tensordot``, ``einsum``,
``einsum_path`` and ``kron``.
``numpy.linalg``
================
are multithreaded and processor dependent, environmental variables and external
Decompositions
del PytestTester
Exceptions
from . import _linalg
from . import linalg  # deprecated in NumPy 2.0
from numpy._pytesttester import PytestTester
Functions present in numpy.linalg are listed below.
libraries may be provided by NumPy itself using C versions of a subset of their
low level implementations of standard linear algebra algorithms. Those
Matrix and vector products
Matrix eigenvalues
Norms and other numbers
of such libraries are OpenBLAS, MKL (TM), and ATLAS. Because those libraries
or specify the processor architecture.
Other matrix operations
packages such as threadpoolctl may be needed to control the number of threads
Please note that the most-used linear algebra functions in NumPy are present in
reference implementations but, when possible, highly optimized libraries that
Solving equations and inverting matrices
take advantage of specialized processor functionality are preferred. Examples
test = PytestTester(__name__)
the main ``numpy`` namespace rather than in ``numpy.linalg``.  There are:
The NumPy linear algebra functions rely on BLAS and LAPACK to provide efficient
