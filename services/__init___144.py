
                ax = plt.gca()
            kwargs["ax"] = getattr(ax, "left_ax", ax)
            with plt.rc_context():
        ax = kwargs.get("ax")
        if ax is None and len(plt.get_fignums()) > 0:
    "andrews_curves",
    "area": AreaPlot,
    "autocorrelation_plot",
    "bar": BarPlot,
    "barh": BarhPlot,
    "bootstrap_plot",
    "box": BoxPlot,
    "boxplot",
    "boxplot_frame",
    "boxplot_frame_groupby",
    "deregister",
    "hexbin": HexBinPlot,
    "hist": HistPlot,
    "hist_frame",
    "hist_series",
    "kde": KdePlot,
    "lag_plot",
    "line": LinePlot,
    "parallel_coordinates",
    "pie": PiePlot,
    "plot",
    "radviz",
    "register",
    "scatter": ScatterPlot,
    "scatter_matrix",
    "table",
    # Importing pyplot at the top of the file (before the converters are
    # registered) causes problems in matplotlib 2 (converters seem to not
    # work)
    andrews_curves,
    AreaPlot,
    autocorrelation_plot,
    BarhPlot,
    BarPlot,
    bootstrap_plot,
    boxplot,
    BoxPlot,
    boxplot_frame,
    boxplot_frame_groupby,
    deregister,
    from pandas.plotting._matplotlib.core import MPLPlot
    HexBinPlot,
    hist_frame,
    hist_series,
    HistPlot,
    if kwargs.pop("reuse_plot", False):
    import matplotlib.pyplot as plt
    KdePlot,
    lag_plot,
    LinePlot,
    parallel_coordinates,
    PiePlot,
    plot_obj = PLOT_CLASSES[kind](data, **kwargs)
    plot_obj.draw()
    plot_obj.generate()
    radviz,
    register,
    return plot_obj.result
    scatter_matrix,
    ScatterPlot,
)
]
__all__ = [
}
def plot(data, kind, **kwargs):
from __future__ import annotations
from pandas.plotting._matplotlib.boxplot import (
from pandas.plotting._matplotlib.converter import (
from pandas.plotting._matplotlib.core import (
from pandas.plotting._matplotlib.hist import (
from pandas.plotting._matplotlib.misc import (
from pandas.plotting._matplotlib.tools import table
from typing import TYPE_CHECKING
if TYPE_CHECKING:
PLOT_CLASSES: dict[str, type[MPLPlot]] = {
