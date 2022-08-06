"""
This type stub file was generated by pyright.
"""

from matplotlib import _api

"""
Streamline plotting for 2D vector fields.

"""
__all__ = ['streamplot']
def streamplot(axes, x, y, u, v, density=..., linewidth=..., color=..., cmap=..., norm=..., arrowsize=..., arrowstyle=..., minlength=..., transform=..., zorder=..., start_points=..., maxlength=..., integration_direction=...):
    """
    Draw streamlines of a vector flow.

    Parameters
    ----------
    x, y : 1D/2D arrays
        Evenly spaced strictly increasing arrays to make a grid.  If 2D, all
        rows of *x* must be equal and all columns of *y* must be equal; i.e.,
        they must be as if generated by ``np.meshgrid(x_1d, y_1d)``.
    u, v : 2D arrays
        *x* and *y*-velocities. The number of rows and columns must match
        the length of *y* and *x*, respectively.
    density : float or (float, float)
        Controls the closeness of streamlines. When ``density = 1``, the domain
        is divided into a 30x30 grid. *density* linearly scales this grid.
        Each cell in the grid can have, at most, one traversing streamline.
        For different densities in each direction, use a tuple
        (density_x, density_y).
    linewidth : float or 2D array
        The width of the stream lines. With a 2D array the line width can be
        varied across the grid. The array must have the same shape as *u*
        and *v*.
    color : color or 2D array
        The streamline color. If given an array, its values are converted to
        colors using *cmap* and *norm*.  The array must have the same shape
        as *u* and *v*.
    cmap : `~matplotlib.colors.Colormap`
        Colormap used to plot streamlines and arrows. This is only used if
        *color* is an array.
    norm : `~matplotlib.colors.Normalize`
        Normalize object used to scale luminance data to 0, 1. If ``None``,
        stretch (min, max) to (0, 1). This is only used if *color* is an array.
    arrowsize : float
        Scaling factor for the arrow size.
    arrowstyle : str
        Arrow style specification.
        See `~matplotlib.patches.FancyArrowPatch`.
    minlength : float
        Minimum length of streamline in axes coordinates.
    start_points : Nx2 array
        Coordinates of starting points for the streamlines in data coordinates
        (the same coordinates as the *x* and *y* arrays).
    zorder : int
        The zorder of the stream lines and arrows.
        Artists with lower zorder values are drawn first.
    maxlength : float
        Maximum length of streamline in axes coordinates.
    integration_direction : {'forward', 'backward', 'both'}, default: 'both'
        Integrate the streamline in forward, backward or both directions.
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    Returns
    -------
    StreamplotSet
        Container object with attributes

        - ``lines``: `.LineCollection` of streamlines

        - ``arrows``: `.PatchCollection` containing `.FancyArrowPatch`
          objects representing the arrows half-way along stream lines.

        This container will probably change in the future to allow changes
        to the colormap, alpha, etc. for both lines and arrows, but these
        changes should be backward compatible.
    """
    ...

class StreamplotSet:
    def __init__(self, lines, arrows) -> None:
        ...
    


class DomainMap:
    """
    Map representing different coordinate systems.

    Coordinate definitions:

    * axes-coordinates goes from 0 to 1 in the domain.
    * data-coordinates are specified by the input x-y coordinates.
    * grid-coordinates goes from 0 to N and 0 to M for an N x M grid,
      where N and M match the shape of the input data.
    * mask-coordinates goes from 0 to N and 0 to M for an N x M mask,
      where N and M are user-specified to control the density of streamlines.

    This class also has methods for adding trajectories to the StreamMask.
    Before adding a trajectory, run `start_trajectory` to keep track of regions
    crossed by a given trajectory. Later, if you decide the trajectory is bad
    (e.g., if the trajectory is very short) just call `undo_trajectory`.
    """
    def __init__(self, grid, mask) -> None:
        ...
    
    def grid2mask(self, xi, yi): # -> tuple[int, int]:
        """Return nearest space in mask-coords from given grid-coords."""
        ...
    
    def mask2grid(self, xm, ym): # -> tuple[Unknown, Unknown]:
        ...
    
    def data2grid(self, xd, yd): # -> tuple[Unknown, Unknown]:
        ...
    
    def grid2data(self, xg, yg): # -> tuple[Unknown, Unknown]:
        ...
    
    def start_trajectory(self, xg, yg): # -> None:
        ...
    
    def reset_start_point(self, xg, yg): # -> None:
        ...
    
    def update_trajectory(self, xg, yg): # -> None:
        ...
    
    def undo_trajectory(self): # -> None:
        ...
    


class Grid:
    """Grid of data."""
    def __init__(self, x, y) -> None:
        ...
    
    @property
    def shape(self): # -> tuple[int, int]:
        ...
    
    def within_grid(self, xi, yi):
        """Return whether (*xi*, *yi*) is a valid index of the grid."""
        ...
    


class StreamMask:
    """
    Mask to keep track of discrete regions crossed by streamlines.

    The resolution of this grid determines the approximate spacing between
    trajectories. Streamlines are only allowed to pass through zeroed cells:
    When a streamline enters a cell, that cell is set to 1, and no new
    streamlines are allowed to enter.
    """
    def __init__(self, density) -> None:
        ...
    
    def __getitem__(self, args): # -> Any:
        ...
    


class InvalidIndexError(Exception):
    ...


class TerminateTrajectory(Exception):
    ...


@_api.deprecated("3.5")
def get_integrator(u, v, dmap, minlength, maxlength, integration_direction): # -> tuple[list[Unknown], list[Unknown]] | list[tuple[Unknown]] | None:
    ...

class OutOfBounds(IndexError):
    ...


def interpgrid(a, xi, yi):
    """Fast 2D, linear interpolation on an integer grid"""
    ...
