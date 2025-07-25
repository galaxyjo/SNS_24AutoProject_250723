
--------
---------
----------
-------------
--------------
---------------
-----------------
----------------------
-----------------------------
        12-13.  Cambridge Univ. Press, Cambridge, UK.
        19: 297-301.
        2007, *Numerical Recipes: The Art of Scientific Computing*, ch.
        machine calculation of complex Fourier series," *Math. Comput.*
   :toctree: generated/
   \\qquad k = 0, \\ldots, M-1;\\quad l = 0, \\ldots, N-1,
   \\qquad k = 0,\\ldots,n-1.
   \\qquad m = 0,\\ldots,n-1.
   A_{kl} =  \\sum_{m=0}^{M-1} \\sum_{n=0}^{N-1}
   a_{mn}\\exp\\left\\{-2\\pi i \\left({mk\\over M}+{nl\\over N}\\right)\\right\\}
   A_k =  \\sum_{m=0}^{n-1} a_m \\exp\\left\\{-2\\pi i{mk \\over n}\\right\\}
   a_m = \\frac{1}{n}\\sum_{k=0}^{n-1}A_k\\exp\\left\\{2\\pi i{mk\\over n}\\right\\}
   fft       Discrete Fourier transform.
   fft2      Discrete Fourier transform in two dimensions.
   fftfreq   Discrete Fourier Transform sample frequencies.
   fftn      Discrete Fourier transform in N-dimensions.
   fftshift  Shift zero-frequency component to center of spectrum.
   hfft      Hermitian discrete Fourier transform.
   ifft      Inverse discrete Fourier transform.
   ifft2     Inverse discrete Fourier transform in two dimensions.
   ifftn     Inverse discrete Fourier transform in N dimensions.
   ifftshift Inverse of fftshift.
   ihfft     Inverse Hermitian discrete Fourier transform.
   irfft     Inverse real discrete Fourier transform.
   irfft2    Inverse real discrete Fourier transform in two dimensions.
   irfftn    Inverse real discrete Fourier transform in N dimensions.
   rfft      Real discrete Fourier transform.
   rfft2     Real discrete Fourier transform in two dimensions.
   rfftfreq  DFT sample frequencies (for usage with rfft, irfft).
   rfftn     Real discrete Fourier transform in N dimensions.
"""
# be deleted once downstream libraries move to `numpy.fft`.
# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should
.. [CT] Cooley, James W., and John W. Tukey, 1965, "An algorithm for the
.. [NR] Press, W., Teukolsky, S., Vetterline, W.T., and Flannery, B.P.,
.. autosummary::
.. currentmodule:: numpy.fft
.. math::
:math:`1/\\sqrt{n}`. Finally, setting the keyword argument ``norm`` to
:math:`a_m = \\exp\\{2\\pi i\\,f m\\Delta t\\}`, where :math:`\\Delta t`
__all__ += _helper.__all__
__all__ = _pocketfft.__all__.copy()
``"forward"`` has the direct transforms scaled by :math:`1/n` and the inverse
``complex128`` arrays respectively. For an FFT implementation that does not
``np.fft.fftshift(A)`` shifts transforms and their frequencies to put the
`None` is an alias of the default option ``"backward"`` for backward
`numpy.fft` promotes ``float32`` and ``complex64`` arrays to ``float64`` and
=============================================
also be a faster way to compute large convolutions, using the property
an odd number of input points, ``A[(n-1)/2]`` contains the largest positive
applications.
argument and the default normalization by :math:`1/n`.
as
Background information
Because the discrete Fourier transform separates its input into
compatibility.
component at frequency :math:`f_k` is the complex conjugate of the
component at frequency :math:`-f_k`, which means that for real
components that contribute at discrete frequencies, it has a great number
components.  When both the function and its Fourier transform are
computing only the positive frequency components, up to and including the
contains the positive-frequency terms, and ``A[n/2+1:]`` contains the
Correspondingly, when the spectrum is purely real, the signal is
del PytestTester
designed to operate on real inputs, and exploits this symmetry by
Discrete Fourier Transform (:mod:`numpy.fft`)
domain*.
Examples
exponent, normalization, etc.  In this implementation, the DFT is defined
fft(a, n)``, then ``A[0]`` contains the zero-frequency term (the sum of
filtering.  The computational efficiency of the FFT means that it can
For an even number of input points, ``A[n/2]`` represents both positive and
For examples, see the various functions.
Fourier analysis is fundamentally a method for expressing a function as a
Fourier Transform (FFT), which was known to Gauss (1805) and was brought
frequency, while ``A[(n+1)/2]`` contains the largest negative frequency.
from . import _pocketfft, _helper
from numpy._pytesttester import PytestTester
Helper routines
Hermitian FFTs
Hermitian.  The `hfft` family of functions exploits this symmetry by
Higher dimensions
Implementation details
in higher dimensions also extend in the same way.
In higher dimensions, FFTs are used, e.g., for image analysis and
In two dimensions, the DFT is defined as
inputs there is no information in the negative frequency components that
is called a *spectrum* or *transform* and exists in the *frequency
is its amplitude spectrum and ``np.abs(A)**2`` is its power spectrum.
is not already available from the positive frequency components.
is the sampling interval.
It differs from the forward transform by the sign of the exponential
its input, and for an output of ``n`` points uses ``n/2+1`` input points.
multiplication in the frequency domain.
negative Nyquist frequency, and is also purely real for real input.  For
negative-frequency terms, in order of decreasingly negative frequency.
Normalization
Nyquist frequency.  Thus, ``n`` input points produce ``n/2+1`` complex
of ``numpy.fft``, which includes only a basic set of routines.
of applications in digital signal processing, e.g., for filtering, and in
of corresponding elements in the output.  The routine
output points.  The inverses of this family assumes the same symmetry of
part because of a very fast algorithm for computing it, called the Fast
points in the frequency domain.
possible to obtain unitary transforms by setting the keyword argument ``norm``
promote input arrays, see `scipy.fftpack`.
provide an accessible introduction to Fourier analysis and its
Real and Hermitian transforms
Real FFTs
References
referred to as a *signal*, which exists in the *time domain*.  The output
replaced with discretized counterparts, it is called the discrete Fourier
represented by a complex exponential
single-frequency component at linear frequency :math:`f` is
Standard FFTs
sum of periodic components, and for recovering the function from those
test = PytestTester(__name__)
that a convolution in the time domain is equivalent to a point-by-point
that shift.
The argument ``norm`` indicates which direction of the pair of direct/inverse
The default normalization (``"backward"``) has the direct (forward) transforms
The DFT is in general defined for complex inputs and outputs, and a
The family of `rfft` functions is
The inverse DFT is defined as
The phase spectrum is obtained by ``np.angle(A)``.
The routine ``np.fft.fftfreq(n)`` returns an array giving the frequencies
The SciPy module `scipy.fft` is a more comprehensive superset
the signal), which is always purely real for real inputs. Then ``A[1:n/2]``
The values in the result follow so-called "standard" order: If ``A =
There are many ways to define the DFT, varying in the sign of the
this context the discretized input to the transform is customarily
to ``"ortho"`` so that both direct and inverse transforms are scaled by
to light in its current form by Cooley and Tukey [CT]_.  Press et al. [NR]_
transform (DFT).  The DFT has become a mainstay of numerical computing in
transforms is scaled and with what normalization factor.
transforms unscaled (i.e. exactly opposite to the default ``"backward"``).
Type Promotion
unscaled and the inverse (backward) transforms scaled by :math:`1/n`. It is
using ``n/2+1`` complex points in the input (time) domain for ``n`` real
When the input `a` is a time-domain signal and ``A = fft(a)``, ``np.abs(A)``
When the input is purely real, its transform is Hermitian, i.e., the
which extends in the obvious way to higher dimensions, and the inverses
zero-frequency components in the middle, and ``np.fft.ifftshift(A)`` undoes
