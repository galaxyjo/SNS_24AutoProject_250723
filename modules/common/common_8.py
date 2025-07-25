
    -------
    ----------
                    assert axes.get_title() == key
                    assert value.ax.get_title() == key
                    assert value.get_title() == key
                    tm.assert_almost_equal(label.get_fontsize(), xlabelsize)
                    tm.assert_almost_equal(label.get_fontsize(), ylabelsize)
                    tm.assert_almost_equal(label.get_rotation(), xrot)
                    tm.assert_almost_equal(label.get_rotation(), yrot)
                # If minor ticks has NullFormatter, rot / fontsize are not
                # Line2D may contains string color expression
                # retained
                # returned as list of np.array
                assert isinstance(r, Axes)
                assert isinstance(value.ax, Axes)
                assert isinstance(value.lines, dict)
                axes = line.axes
                if check_ax_title:
                if xlabelsize is not None:
                if xrot is not None:
                if ylabelsize is not None:
                if yrot is not None:
                labels = ax.get_xticklabels()
                labels = ax.get_xticklabels() + ax.get_xticklabels(minor=True)
                labels = ax.get_yticklabels()
                labels = ax.get_yticklabels() + ax.get_yticklabels(minor=True)
                line = value["medians"][0]
                raise AssertionError
                result = conv.to_rgba(result)
                result = patch.get_color()
                result = patch.get_edgecolor()
                result = patch.get_facecolor()
                result = patch.get_facecolor()[0]
                result = tuple(patch.get_edgecolor()[0])
                result = tuple(result)
                xerr_count += 1
                yerr_count += 1
            - All required axes instances will be created automatically
            - Create new subplot(212) and plot there as well
            - If `ax` not in `kwargs`, then create subplot(211) and plot there
            - It is recommended to use it when the plotting function
            - Mind special corner case for bootstrap_plot (see `_gen_two_subplots`)
            - Simply run plotting function with kwargs provided
            # check axes coordinates to estimate layout
            # check returned dict has correct mapping
            # check something drawn on visible axes
            _check_text_labels(ax.get_legend().get_texts(), labels)
            assert ax.get_legend() is None
            assert ax.get_legend() is not None
            assert is_grid_on()
            assert isinstance(returned.ax, Axes)
            assert isinstance(returned.lines, dict)
            assert isinstance(value, types[return_type])
            assert label == e
            assert len(ax.get_children()) > 0
            assert patch.fill == filled
            assert result == expected
            creates multiple axes itself. It helps avoid warnings like
            elif isinstance(patch, (PolyCollection, LineCollection)):
            elif return_type == "both":
            elif return_type == "dict":
            else:
            expected = conv.to_rgba(color)
            facecolors = _get_colors_mapped(mapping, facecolors)
            facecolors = facecolors[: len(collections)]
            for label in labels:
            for r in _flatten_visible(returned):
            has_xerr = getattr(c, "has_xerr", False)
            has_yerr = getattr(c, "has_yerr", False)
            if has_xerr:
            if has_yerr:
            if isinstance(ax.xaxis.get_minor_formatter(), NullFormatter):
            if isinstance(ax.yaxis.get_minor_formatter(), NullFormatter):
            if isinstance(patch, Collection):
            if isinstance(patch, Line2D):
            if isinstance(result, np.ndarray):
            if return_type == "axes":
            linecolors = _get_colors_mapped(mapping, linecolors)
            linecolors = linecolors[: len(collections)]
            mpl.pyplot.clf()
            mpl.pyplot.subplot(1, 4 * len(kinds), spndx)
            mpl.rc("axes", grid=False)
            mpl.rc("axes", grid=True)
            obj.plot(kind=kind, **kws)
            obj.plot(kind=kind, grid=True, **kws)
            points = ax.get_position().get_points()
            return
            return_type = "dict"
            spndx += 1
            the figure containing the passed axes is being cleared'
            tm.assert_is_valid_plot_return_object(ret)
            'UserWarning: To output multiple subplots,
            x_set.add(points[0][0])
            y_set.add(points[0][1])
        # should be fixed when the returning default is changed
        assert "ax" not in kwargs
        assert ax.get_legend() is None
        assert ax.xaxis.get_scale() == xaxis
        assert ax.yaxis.get_scale() == yaxis
        assert isinstance(returned, Series)
        assert isinstance(returned, types[return_type])
        assert len(collections) == len(facecolors)
        assert len(collections) == len(linecolors)
        assert len(labels) == len(expected)
        assert len(visible_axes) == axes_num
        assert markers == expected_markers
        assert not is_grid_on()
        assert patch.get_visible() == visible
        assert result == layout
        assert sorted(returned.keys()) == sorted(expected_keys)
        assert texts.get_text() == expected
        assert xerr == xerr_count
        assert yerr == yerr_count
        Collection,
        collections = [collections]
        containers = ax.containers
        else:
        expected figsize. default is matplotlib default
        expected filling
        expected layout, (expected number of rows , columns)
        expected legend labels
        expected legend markers
        expected legend visibility. labels are checked only when visible is
        expected number of axes. Unnecessary axes should be set to
        expected number of x errorbar
        expected number of y errorbar
        expected text label, or its list
        expected visibility
        expected xaxis scale
        expected xticks font size
        expected xticks rotation
        expected yaxis scale
        expected yticks font size
        expected yticks rotation
        fig = kwargs.get("figure", plt.gcf())
        fig.add_subplot(211)
        figsize = (6.4, 4.8)
        for ax in flatten_axes(axes):
        for ax in visible_axes:
        for c in containers:
        for key, value in returned.items():
        for label, e in zip(labels, expected):
        for patch in ax.patches:
        for patch, color in zip(collections, facecolors):
        for patch, color in zip(collections, linecolors):
        for ret in gen_plots(f, fig, **kwargs):
        gen_plots = _gen_default_plot
        gen_plots = _gen_two_subplots
        group labels in subplot case. If not passed,
        handles, _ = ax.get_legend_handles_labels()
        If False (default):
        if kind not in ["pie", "hexbin", "scatter"]:
        if mapping is not None:
        if return_type == "both":
        if return_type is None:
        If True:
        if visible:
        if xlabelsize is not None or xrot is not None:
        if ylabelsize is not None or yrot is not None:
        Intended to be checked by calling from ``boxplot``.
        invisible.
        Keyword arguments passed to the plotting function.
        kwargs["ax"] = fig.add_subplot(212)
        labels = [t.get_text() for t in texts]
        LineCollection,
        list of expected face colors
        list of expected line colors
        list or collection of target artist
        markers = [handle.get_marker() for handle in handles]
        mpl.pyplot.clf()
        mpl.pyplot.subplot(1, 4 * len(kinds), spndx)
        mpl.rc("axes", grid=False)
        mpl.rc("axes", grid=True)
        Normal ``plot`` doesn't attach ``ax.title``, it must be disabled.
        np.array(figsize, dtype=np.float64),
        obj.plot(kind=kind, **kws)
        obj.plot(kind=kind, grid=False, **kws)
        Plotting function.
        plt.clf()
        plt.close(fig)
        PolyCollection,
        raise ValueError("labels must be specified when visible is True")
        raise ValueError("Markers must be specified when visible is True")
        result = (len(y_set), len(x_set))
        return not (xoff and yoff)
        return_type passed to boxplot
        rsdata = rsl.get_xydata()
        Series used for color grouping key
        spndx += 1
        target Artist or its list or collection
        target text, or its list
        the function checks assuming boxplot uses single ax
        tm.assert_almost_equal(xpdata, rsdata)
        True
        used for andrew_curves, parallel_coordinates, radviz test
        visible_axes[0].figure.get_size_inches(),
        Whether to check the ax.title is the same as expected_key
        x_set = set()
        xerr_count = 0
        xoff = all(not g.gridline.get_visible() for g in xticks)
        xpdata = xpl.get_xydata()
        xticks = mpl.pyplot.gca().xaxis.get_major_ticks()
        y_set = set()
        yerr_count = 0
        yoff = all(not g.gridline.get_visible() for g in yticks)
        yticks = mpl.pyplot.gca().yaxis.get_major_ticks()
    """
    # depending on slice value
    # Make sure plot defaults to rcParams['axes.grid'] setting, GH 9792
    # unique and colors length can be differed
    )
    **kwargs
    assert len(xp_lines) == len(rs_lines)
    Auxiliary function for correctly unpacking cycler after MPL >= 1.5
    ax : matplotlib Axes object
    axes : matplotlib Axes object, or its list-like
    axes = [ax for ax in axes_ndarray if ax.get_visible()]
    axes = _flatten_visible(axes)
    axes_ndarray = flatten_axes(axes)
    axes_num : number
    Check ax has expected legend markers
    Check axes has expected number of errorbars
    Check box returned type is correct
    Check each artist has expected line colors and face colors
    Check each artist is visible or not
    Check each axes has expected legend labels
    Check each axes has expected scales
    Check each axes has expected tick properties
    Check each axes has identical lines
    Check each text has expected labels
    Check expected number of axes is drawn in expected layout
    Check for each artist whether it is filled or not
    check_ax_title : bool
    collections : list-like
    collections : matplotlib Artist or its list-like
    conv = colors.ColorConverter
    Create plot and ensure that plot return object is valid.
    Create plot in a default way.
    Create plot on two subplots forcefully created.
    def is_grid_on():
    default_axes : bool, optional
    else:
    expected : str or list-like which has the same length as texts
    expected_keys : list-like, optional
    expected_markers : list-like
    f : func
    facecolors : list-like which has the same length as collections
    figsize : tuple
    filled : bool
    finally:
    Flatten axes, and filter only visible
    for ax in axes:
    for kind in kinds:
    for patch in collections:
    for xpl, rsl in zip(xp_lines, rs_lines):
    from collections.abc import Sequence
    from matplotlib import colors
    from matplotlib.axes import Axes
    from matplotlib.collections import (
    from matplotlib.collections import Collection
    from matplotlib.lines import Line2D
    from matplotlib.ticker import NullFormatter
    from pandas.plotting._matplotlib.tools import flatten_axes
    if "ax" not in kwargs:
    if axes_num is not None:
    if default_axes:
    if expected_keys is None:
    if f is pd.plotting.bootstrap_plot:
    if facecolors is not None:
    if figsize is None:
    if layout is not None:
    if linecolors is not None:
    if not is_list_like(texts):
    if not isinstance(collections, Collection) and not is_list_like(collections):
    if visible and (expected_markers is None):
    if visible and (labels is None):
    if visible:
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    labels : list-like
    layout : tuple
    linecolors : list-like which has the same length as collections
    mapped = dict(zip(unique, colors))
    mapping : Series
    Parameters
    Plot object returned by the last plotting.
    plt.close("all")
    ret = None
    return [mapped[v] for v in series.values]
    return [v[field] for v in rcParams["axes.prop_cycle"]]
    return ax._shared_axes["x"]
    return ax._shared_axes["y"]
    return axes
    return ret
    return_type : str
    returned : object to be tested, returned from boxplot
    returned, return_type, expected_keys=None, check_ax_title=True
    Returns
    rs : matplotlib Axes object
    rs_lines = rs.get_lines()
    spndx = 1
    texts : matplotlib Text object, or its list-like
    tm.assert_numpy_array_equal(
    try:
    types = {"dict": dict, "axes": Axes, "both": tuple}
    unique = series.unique()
    visible : bool
    visible_axes = _flatten_visible(axes)
    xaxis : {'linear', 'log'}
    xerr : number
    xlabelsize : number
    xp : matplotlib Axes object
    xp_lines = xp.get_lines()
    xrot : number
    yaxis : {'linear', 'log'}
    yerr : number
    yield f(**kwargs)
    ylabelsize : number
    yrot : number
"""
):
def _check_ax_scales(axes, xaxis="linear", yaxis="linear"):
def _check_axes_shape(axes, axes_num=None, layout=None, figsize=None):
def _check_box_return_type(
def _check_colors(collections, linecolors=None, facecolors=None, mapping=None):
def _check_data(xp, rs):
def _check_grid_settings(obj, kinds, kws={}):
def _check_has_errorbars(axes, xerr=0, yerr=0):
def _check_legend_labels(axes, labels=None, visible=True):
def _check_legend_marker(ax, expected_markers=None, visible=True):
def _check_patches_all_filled(axes: Axes | Sequence[Axes], filled: bool = True) -> None:
def _check_plot_works(f, default_axes=False, **kwargs):
def _check_text_labels(texts, expected):
def _check_ticks_props(axes, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None):
def _check_visible(collections, visible=True):
def _flatten_visible(axes: Axes | Sequence[Axes]) -> Sequence[Axes]:
def _gen_default_plot(f, fig, **kwargs):
def _gen_two_subplots(f, fig, **kwargs):
def _get_colors_mapped(series, colors):
def _unpack_cycler(rcParams, field="color"):
def get_x_axis(ax):
def get_y_axis(ax):
from __future__ import annotations
from pandas import Series
from pandas.core.dtypes.api import is_list_like
from typing import TYPE_CHECKING
if TYPE_CHECKING:
import numpy as np
import pandas as pd
import pandas._testing as tm
Module consolidating common testing functions for checking plotting.
