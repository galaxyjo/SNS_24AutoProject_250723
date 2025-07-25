
    "andrews_curves",
    "autocorrelation_plot",
    "bootstrap_plot",
    "boxplot",
    "boxplot_frame",
    "boxplot_frame_groupby",
    "deregister_matplotlib_converters",
    "hist_frame",
    "hist_series",
    "lag_plot",
    "parallel_coordinates",
    "plot_params",
    "PlotAccessor",
    "radviz",
    "register_matplotlib_converters",
    "scatter_matrix",
    "table",
    andrews_curves,
    autocorrelation_plot,
    bootstrap_plot,
    boxplot,
    boxplot_frame,
    boxplot_frame_groupby,
    deregister as deregister_matplotlib_converters,
    hist_frame,
    hist_series,
    lag_plot,
    parallel_coordinates,
    plot_params,
    PlotAccessor,
    radviz,
    register as register_matplotlib_converters,
    scatter_matrix,
    table,
  - andrews_curves
  - autocorrelation_plot
  - bootstrap_plot
  - lag_plot
  - parallel_coordinates
  - radviz
  - scatter_matrix
  - table
- area
- bar
- barh
- box
- boxplot (`pandas.plotting.boxplot(df)` equivalent to `DataFrame.boxplot`)
- boxplot_frame and boxplot_frame_groupby
- hexbin
- hist
- hist_series and hist_frame (for `Series.hist` and `DataFrame.hist`)
- kde
- line
- pie
- plot (describe above, used for `Series.plot` and `DataFrame.plot`)
- Plots not called as `Series` and `DataFrame` methods:
- register and deregister (register converters for the tick formats)
- scatter
"""
)
]
__all__ = [
Any other keyword argument is currently assumed to be backend specific,
Authors of third-party plotting backends should implement a module with a
but some parameters may be unified and added to the signature in the
Currently, all the Matplotlib functions in pandas are accessed through
for ``df.plot()`` the parameter `data` will contain the DataFrame `df`.
For the discussion about the API see
from pandas.plotting._core import (
from pandas.plotting._misc import (
future (e.g. `title` which should be useful for any backend).
https://github.com/pandas-dev/pandas/issues/26747.
https://github.com/pyviz/hvplot as a reference on how to write a backend.
In some cases, the data structure is transformed before being sent to
is expected to change, and the exact API is under discussion. But with
Plotting public API.
public ``plot(data, kind, **kwargs)``. The parameter `data` will contain
See the pandas API reference for documentation on each kind of plot.
the backend (see PlotAccessor.__call__ in pandas/plotting/_core.py for
the current version, backends are expected to implement the next functions:
the data structure and can be a `Series` or a `DataFrame`. For example,
the exact transformations).
The parameter `kind` will be one of:
the selected backend. For example, `pandas.plotting.boxplot` (equivalent
to `DataFrame.boxplot`) is also accessed in the selected backend. This
Use the code in pandas/plotting/_matplotib.py and
