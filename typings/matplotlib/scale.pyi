"""
This type stub file was generated by pyright.
"""

from matplotlib.transforms import Transform

"""
Scales define the distribution of data values on an axis, e.g. a log scaling.
They are defined as subclasses of `ScaleBase`.

See also `.axes.Axes.set_xscale` and the scales examples in the documentation.

See :doc:`/gallery/scales/custom_scale` for a full example of defining a custom
scale.

Matplotlib also supports non-separable transformations that operate on both
`~.axis.Axis` at the same time.  They are known as projections, and defined in
`matplotlib.projections`.
"""
class ScaleBase:
    """
    The base class for all scales.

    Scales are separable transformations, working on a single dimension.

    Subclasses should override

    :attr:`name`
        The scale's name.
    :meth:`get_transform`
        A method returning a `.Transform`, which converts data coordinates to
        scaled coordinates.  This transform should be invertible, so that e.g.
        mouse positions can be converted back to data coordinates.
    :meth:`set_default_locators_and_formatters`
        A method that sets default locators and formatters for an `~.axis.Axis`
        that uses this scale.
    :meth:`limit_range_for_scale`
        An optional method that "fixes" the axis range to acceptable values,
        e.g. restricting log-scaled axes to positive values.
    """
    def __init__(self, axis) -> None:
        r"""
        Construct a new scale.

        Notes
        -----
        The following note is for scale implementors.

        For back-compatibility reasons, scales take an `~matplotlib.axis.Axis`
        object as first argument.  However, this argument should not
        be used: a single scale object should be usable by multiple
        `~matplotlib.axis.Axis`\es at the same time.
        """
        ...
    
    def get_transform(self):
        """
        Return the `.Transform` object associated with this scale.
        """
        ...
    
    def set_default_locators_and_formatters(self, axis):
        """
        Set the locators and formatters of *axis* to instances suitable for
        this scale.
        """
        ...
    
    def limit_range_for_scale(self, vmin, vmax, minpos): # -> tuple[Unknown, Unknown]:
        """
        Return the range *vmin*, *vmax*, restricted to the
        domain supported by this scale (if any).

        *minpos* should be the minimum positive value in the data.
        This is used by log scales to determine a minimum value.
        """
        ...
    


class LinearScale(ScaleBase):
    """
    The default linear scale.
    """
    name = ...
    def __init__(self, axis) -> None:
        """
        """
        ...
    
    def set_default_locators_and_formatters(self, axis): # -> None:
        ...
    
    def get_transform(self): # -> IdentityTransform:
        """
        Return the transform for linear scaling, which is just the
        `~matplotlib.transforms.IdentityTransform`.
        """
        ...
    


class FuncTransform(Transform):
    """
    A simple transform that takes and arbitrary function for the
    forward and inverse transform.
    """
    input_dims = ...
    def __init__(self, forward, inverse) -> None:
        """
        Parameters
        ----------
        forward : callable
            The forward function for the transform.  This function must have
            an inverse and, for best behavior, be monotonic.
            It must have the signature::

               def forward(values: array-like) -> array-like

        inverse : callable
            The inverse of the forward function.  Signature as ``forward``.
        """
        ...
    
    def transform_non_affine(self, values):
        ...
    
    def inverted(self): # -> FuncTransform:
        ...
    


class FuncScale(ScaleBase):
    """
    Provide an arbitrary scale with user-supplied function for the axis.
    """
    name = ...
    def __init__(self, axis, functions) -> None:
        """
        Parameters
        ----------
        axis : `~matplotlib.axis.Axis`
            The axis for the scale.
        functions : (callable, callable)
            two-tuple of the forward and inverse functions for the scale.
            The forward function must be monotonic.

            Both functions must have the signature::

               def forward(values: array-like) -> array-like
        """
        ...
    
    def get_transform(self): # -> FuncTransform:
        """Return the `.FuncTransform` associated with this scale."""
        ...
    
    def set_default_locators_and_formatters(self, axis): # -> None:
        ...
    


class LogTransform(Transform):
    input_dims = ...
    def __init__(self, base, nonpositive=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def transform_non_affine(self, a): # -> Any:
        ...
    
    def inverted(self): # -> InvertedLogTransform:
        ...
    


class InvertedLogTransform(Transform):
    input_dims = ...
    def __init__(self, base) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def transform_non_affine(self, a):
        ...
    
    def inverted(self): # -> LogTransform:
        ...
    


class LogScale(ScaleBase):
    """
    A standard logarithmic scale.  Care is taken to only plot positive values.
    """
    name = ...
    def __init__(self, axis, *, base=..., subs=..., nonpositive=...) -> None:
        """
        Parameters
        ----------
        axis : `~matplotlib.axis.Axis`
            The axis for the scale.
        base : float, default: 10
            The base of the logarithm.
        nonpositive : {'clip', 'mask'}, default: 'clip'
            Determines the behavior for non-positive values. They can either
            be masked as invalid, or clipped to a very small positive number.
        subs : sequence of int, default: None
            Where to place the subticks between each major tick.  For example,
            in a log10 scale, ``[2, 3, 4, 5, 6, 7, 8, 9]`` will place 8
            logarithmically spaced minor ticks between each major tick.
        """
        ...
    
    base = ...
    def set_default_locators_and_formatters(self, axis): # -> None:
        ...
    
    def get_transform(self): # -> LogTransform:
        """Return the `.LogTransform` associated with this scale."""
        ...
    
    def limit_range_for_scale(self, vmin, vmax, minpos): # -> tuple[float | Unknown, float | Unknown]:
        """Limit the domain to positive values."""
        ...
    


class FuncScaleLog(LogScale):
    """
    Provide an arbitrary scale with user-supplied function for the axis and
    then put on a logarithmic axes.
    """
    name = ...
    def __init__(self, axis, functions, base=...) -> None:
        """
        Parameters
        ----------
        axis : `matplotlib.axis.Axis`
            The axis for the scale.
        functions : (callable, callable)
            two-tuple of the forward and inverse functions for the scale.
            The forward function must be monotonic.

            Both functions must have the signature::

                def forward(values: array-like) -> array-like

        base : float, default: 10
            Logarithmic base of the scale.
        """
        ...
    
    @property
    def base(self):
        ...
    
    def get_transform(self): # -> Transform | FuncTransform | CompositeAffine2D | CompositeGenericTransform | _NotImplementedType:
        """Return the `.Transform` associated with this scale."""
        ...
    


class SymmetricalLogTransform(Transform):
    input_dims = ...
    def __init__(self, base, linthresh, linscale) -> None:
        ...
    
    def transform_non_affine(self, a):
        ...
    
    def inverted(self): # -> InvertedSymmetricalLogTransform:
        ...
    


class InvertedSymmetricalLogTransform(Transform):
    input_dims = ...
    def __init__(self, base, linthresh, linscale) -> None:
        ...
    
    def transform_non_affine(self, a): # -> Any:
        ...
    
    def inverted(self): # -> SymmetricalLogTransform:
        ...
    


class SymmetricalLogScale(ScaleBase):
    """
    The symmetrical logarithmic scale is logarithmic in both the
    positive and negative directions from the origin.

    Since the values close to zero tend toward infinity, there is a
    need to have a range around zero that is linear.  The parameter
    *linthresh* allows the user to specify the size of this range
    (-*linthresh*, *linthresh*).

    Parameters
    ----------
    base : float, default: 10
        The base of the logarithm.

    linthresh : float, default: 2
        Defines the range ``(-x, x)``, within which the plot is linear.
        This avoids having the plot go to infinity around zero.

    subs : sequence of int
        Where to place the subticks between each major tick.
        For example, in a log10 scale: ``[2, 3, 4, 5, 6, 7, 8, 9]`` will place
        8 logarithmically spaced minor ticks between each major tick.

    linscale : float, optional
        This allows the linear range ``(-linthresh, linthresh)`` to be
        stretched relative to the logarithmic range. Its value is the number of
        decades to use for each half of the linear range. For example, when
        *linscale* == 1.0 (the default), the space used for the positive and
        negative halves of the linear range will be equal to one decade in
        the logarithmic range.
    """
    name = ...
    def __init__(self, axis, *, base=..., linthresh=..., subs=..., linscale=...) -> None:
        ...
    
    base = ...
    linthresh = ...
    linscale = ...
    def set_default_locators_and_formatters(self, axis): # -> None:
        ...
    
    def get_transform(self): # -> SymmetricalLogTransform:
        """Return the `.SymmetricalLogTransform` associated with this scale."""
        ...
    


class LogitTransform(Transform):
    input_dims = ...
    def __init__(self, nonpositive=...) -> None:
        ...
    
    def transform_non_affine(self, a): # -> Any:
        """logit transform (base 10), masked or clipped"""
        ...
    
    def inverted(self): # -> LogisticTransform:
        ...
    
    def __str__(self) -> str:
        ...
    


class LogisticTransform(Transform):
    input_dims = ...
    def __init__(self, nonpositive=...) -> None:
        ...
    
    def transform_non_affine(self, a):
        """logistic transform (base 10)"""
        ...
    
    def inverted(self): # -> LogitTransform:
        ...
    
    def __str__(self) -> str:
        ...
    


class LogitScale(ScaleBase):
    """
    Logit scale for data between zero and one, both excluded.

    This scale is similar to a log scale close to zero and to one, and almost
    linear around 0.5. It maps the interval ]0, 1[ onto ]-infty, +infty[.
    """
    name = ...
    def __init__(self, axis, nonpositive=..., *, one_half=..., use_overline=...) -> None:
        r"""
        Parameters
        ----------
        axis : `matplotlib.axis.Axis`
            Currently unused.
        nonpositive : {'mask', 'clip'}
            Determines the behavior for values beyond the open interval ]0, 1[.
            They can either be masked as invalid, or clipped to a number very
            close to 0 or 1.
        use_overline : bool, default: False
            Indicate the usage of survival notation (\overline{x}) in place of
            standard notation (1-x) for probability close to one.
        one_half : str, default: r"\frac{1}{2}"
            The string used for ticks formatter to represent 1/2.
        """
        ...
    
    def get_transform(self): # -> LogitTransform:
        """Return the `.LogitTransform` associated with this scale."""
        ...
    
    def set_default_locators_and_formatters(self, axis): # -> None:
        ...
    
    def limit_range_for_scale(self, vmin, vmax, minpos): # -> tuple[float | Unknown, float | Unknown]:
        """
        Limit the domain to values between 0 and 1 (excluded).
        """
        ...
    


_scale_mapping = ...
def get_scale_names(): # -> list[str]:
    """Return the names of the available scales."""
    ...

def scale_factory(scale, axis, **kwargs):
    """
    Return a scale class by name.

    Parameters
    ----------
    scale : {%(names)s}
    axis : `matplotlib.axis.Axis`
    """
    ...

if scale_factory.__doc__:
    ...
def register_scale(scale_class): # -> None:
    """
    Register a new kind of scale.

    Parameters
    ----------
    scale_class : subclass of `ScaleBase`
        The scale to register.
    """
    ...

