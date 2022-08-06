"""
This type stub file was generated by pyright.
"""

from collections.abc import Sequence

"""
Default legend handlers.

.. important::

    This is a low-level legend API, which most end users do not need.

    We recommend that you are familiar with the :doc:`legend guide
    </tutorials/intermediate/legend_guide>` before reading this documentation.

Legend handlers are expected to be a callable object with a following
signature. ::

    legend_handler(legend, orig_handle, fontsize, handlebox)

Where *legend* is the legend itself, *orig_handle* is the original
plot, *fontsize* is the fontsize in pixels, and *handlebox* is a
OffsetBox instance. Within the call, you should create relevant
artists (using relevant properties from the *legend* and/or
*orig_handle*) and add them into the handlebox. The artists needs to
be scaled according to the fontsize (note that the size is in pixel,
i.e., this is dpi-scaled value).

This module includes definition of several legend handler classes
derived from the base class (HandlerBase) with the following method::

    def legend_artist(self, legend, orig_handle, fontsize, handlebox)
"""
def update_from_first_child(tgt, src): # -> None:
    ...

class HandlerBase:
    """
    A Base class for default legend handlers.

    The derived classes are meant to override *create_artists* method, which
    has a following signature.::

      def create_artists(self, legend, orig_handle,
                         xdescent, ydescent, width, height, fontsize,
                         trans):

    The overridden method needs to create artists of the given
    transform that fits in the given dimension (xdescent, ydescent,
    width, height) that are scaled by fontsize if necessary.

    """
    def __init__(self, xpad=..., ypad=..., update_func=...) -> None:
        ...
    
    def update_prop(self, legend_handle, orig_handle, legend): # -> None:
        ...
    
    def adjust_drawing_area(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize): # -> tuple[Unknown, Unknown, Unknown, Unknown]:
        ...
    
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        """
        Return the artist that this HandlerBase generates for the given
        original artist/handle.

        Parameters
        ----------
        legend : `~matplotlib.legend.Legend`
            The legend for which these legend artists are being created.
        orig_handle : :class:`matplotlib.artist.Artist` or similar
            The object for which these legend artists are being created.
        fontsize : int
            The fontsize in pixels. The artists being created should
            be scaled according to the given fontsize.
        handlebox : `matplotlib.offsetbox.OffsetBox`
            The box which has been created to hold this legend entry's
            artists. Artists created in the `legend_artist` method must
            be added to this handlebox inside this method.

        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerNpoints(HandlerBase):
    """
    A legend handler that shows *numpoints* points in the legend entry.
    """
    def __init__(self, marker_pad=..., numpoints=..., **kwargs) -> None:
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.
        numpoints : int
            Number of points to show in legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
        ...
    
    def get_numpoints(self, legend):
        ...
    
    def get_xdata(self, legend, xdescent, ydescent, width, height, fontsize): # -> tuple[NDArray[floating[Any]] | list[Unknown], NDArray[floating[Any]] | list[Unknown]]:
        ...
    


class HandlerNpointsYoffsets(HandlerNpoints):
    """
    A legend handler that shows *numpoints* in the legend, and allows them to
    be individually offset in the y-direction.
    """
    def __init__(self, numpoints=..., yoffsets=..., **kwargs) -> None:
        """
        Parameters
        ----------
        numpoints : int
            Number of points to show in legend entry.
        yoffsets : array of floats
            Length *numpoints* list of y offsets for each point in
            legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpoints`.
        """
        ...
    
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize):
        ...
    


class HandlerLine2DCompound(HandlerNpoints):
    """
    Original handler for `.Line2D` instances, that relies on combining
    a line-only with a marker-only artist.  May be deprecated in the future.
    """
    def __init__(self, marker_pad=..., numpoints=..., **kwargs) -> None:
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.
        numpoints : int
            Number of points to show in legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpoints`.
        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Line2D]:
        ...
    


class _Line2DHandleList(Sequence):
    def __init__(self, legline) -> None:
        ...
    
    def __len__(self): # -> Literal[2]:
        ...
    
    def __getitem__(self, index):
        ...
    


class HandlerLine2D(HandlerNpoints):
    """
    Handler for `.Line2D` instances.

    See Also
    --------
    HandlerLine2DCompound : An earlier handler implementation, which used one
                            artist for the line and another for the marker(s).
    """
    def __init__(self, marker_pad=..., numpoints=..., **kw) -> None:
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.
        numpoints : int
            Number of points to show in legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpoints`.
        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> _Line2DHandleList:
        ...
    


class HandlerPatch(HandlerBase):
    """
    Handler for `.Patch` instances.
    """
    def __init__(self, patch_func=..., **kwargs) -> None:
        """
        Parameters
        ----------
        patch_func : callable, optional
            The function that creates the legend key artist.
            *patch_func* should have the signature::

                def patch_func(legend=legend, orig_handle=orig_handle,
                               xdescent=xdescent, ydescent=ydescent,
                               width=width, height=height, fontsize=fontsize)

            Subsequently the created artist will have its ``update_prop``
            method called and the appropriate transform will be applied.

        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Rectangle | Unknown]:
        ...
    


class HandlerStepPatch(HandlerBase):
    """
    Handler for `~.matplotlib.patches.StepPatch` instances.
    """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Rectangle | Line2D]:
        ...
    


class HandlerLineCollection(HandlerLine2D):
    """
    Handler for `.LineCollection` instances.
    """
    def get_numpoints(self, legend):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Line2D]:
        ...
    


class HandlerRegularPolyCollection(HandlerNpointsYoffsets):
    r"""Handler for `.RegularPolyCollection`\s."""
    def __init__(self, yoffsets=..., sizes=..., **kwargs) -> None:
        ...
    
    def get_numpoints(self, legend):
        ...
    
    def get_sizes(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize): # -> list[Unknown]:
        ...
    
    def update_prop(self, legend_handle, orig_handle, legend): # -> None:
        ...
    
    def create_collection(self, orig_handle, sizes, offsets, transOffset): # -> Any:
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Any]:
        ...
    


class HandlerPathCollection(HandlerRegularPolyCollection):
    r"""Handler for `.PathCollection`\s, which are used by `~.Axes.scatter`."""
    def create_collection(self, orig_handle, sizes, offsets, transOffset): # -> Any:
        ...
    


class HandlerCircleCollection(HandlerRegularPolyCollection):
    r"""Handler for `.CircleCollection`\s."""
    def create_collection(self, orig_handle, sizes, offsets, transOffset): # -> Any:
        ...
    


class HandlerErrorbar(HandlerLine2D):
    """Handler for Errorbars."""
    def __init__(self, xerr_size=..., yerr_size=..., marker_pad=..., numpoints=..., **kwargs) -> None:
        ...
    
    def get_err_size(self, legend, xdescent, ydescent, width, height, fontsize): # -> tuple[Unknown, Unknown]:
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerStem(HandlerNpointsYoffsets):
    """
    Handler for plots produced by `~.Axes.stem`.
    """
    def __init__(self, marker_pad=..., numpoints=..., bottom=..., yoffsets=..., **kwargs) -> None:
        """
        Parameters
        ----------
        marker_pad : float, default: 0.3
            Padding between points in legend entry.
        numpoints : int, optional
            Number of points to show in legend entry.
        bottom : float, optional

        yoffsets : array of floats, optional
            Length *numpoints* list of y offsets for each point in
            legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpointsYoffsets`.
        """
        ...
    
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Line2D]:
        ...
    


class HandlerTuple(HandlerBase):
    """
    Handler for Tuple.
    """
    def __init__(self, ndivide=..., pad=..., **kwargs) -> None:
        """
        Parameters
        ----------
        ndivide : int, default: 1
            The number of sections to divide the legend area into.  If None,
            use the length of the input tuple.
        pad : float, default: :rc:`legend.borderpad`
            Padding in units of fraction of font size.
        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Unknown]:
        ...
    


class HandlerPolyCollection(HandlerBase):
    """
    Handler for `.PolyCollection` used in `~.Axes.fill_between` and
    `~.Axes.stackplot`.
    """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): # -> list[Rectangle]:
        ...
    


