"""
This type stub file was generated by pyright.
"""

from matplotlib import _api

r"""
A module for parsing a subset of the TeX math syntax and rendering it to a
Matplotlib backend.

For a tutorial of its usage, see :doc:`/tutorials/text/mathtext`.  This
document is primarily concerned with implementation details.

The module uses pyparsing_ to parse the TeX expression.

.. _pyparsing: https://pypi.org/project/pyparsing/

The Bakoma distribution of the TeX Computer Modern fonts, and STIX
fonts are supported.  There is experimental support for using
arbitrary fonts, but results may vary without proper tweaking and
metrics for those fonts.
"""
_log = ...
@_api.caching_module_getattr
class __getattr__:
    ...


get_unicode_index = ...
class MathtextBackend:
    """
    The base class for the mathtext backend-specific code.  `MathtextBackend`
    subclasses interface between mathtext and specific Matplotlib graphics
    backends.

    Subclasses need to override the following:

    - :meth:`render_glyph`
    - :meth:`render_rect_filled`
    - :meth:`get_results`

    And optionally, if you need to use a FreeType hinting style:

    - :meth:`get_hinting_type`
    """
    def __init__(self) -> None:
        ...
    
    def set_canvas_size(self, w, h, d): # -> None:
        """Set the dimension of the drawing canvas."""
        ...
    
    def render_glyph(self, ox, oy, info):
        """
        Draw a glyph described by *info* to the reference point (*ox*,
        *oy*).
        """
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2):
        """
        Draw a filled black rectangle from (*x1*, *y1*) to (*x2*, *y2*).
        """
        ...
    
    def get_results(self, box):
        """
        Return a backend-specific tuple to return to the backend after
        all processing is done.
        """
        ...
    
    def get_hinting_type(self):
        """
        Get the FreeType hinting type to use with this particular
        backend.
        """
        ...
    


class MathtextBackendAgg(MathtextBackend):
    """
    Render glyphs and rectangles to an FTImage buffer, which is later
    transferred to the Agg image by the Agg backend.
    """
    def __init__(self) -> None:
        ...
    
    def set_canvas_size(self, w, h, d): # -> None:
        ...
    
    def render_glyph(self, ox, oy, info): # -> None:
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2): # -> None:
        ...
    
    def get_results(self, box, used_characters): # -> tuple[int, int, int | Unknown, int | Unknown, int | Unknown, Unknown | None, Unknown]:
        ...
    
    def get_hinting_type(self):
        ...
    


@_api.deprecated("3.4", alternative="`.mathtext.math_to_image`")
class MathtextBackendBitmap(MathtextBackendAgg):
    def get_results(self, box, used_characters): # -> tuple[Unknown | None, int | Unknown]:
        ...
    


@_api.deprecated("3.4", alternative="`.MathtextBackendPath`")
class MathtextBackendPs(MathtextBackend):
    """
    Store information to write a mathtext rendering to the PostScript backend.
    """
    _PSResult = ...
    def __init__(self) -> None:
        ...
    
    def render_glyph(self, ox, oy, info): # -> None:
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2): # -> None:
        ...
    
    def get_results(self, box, used_characters): # -> _PSResult:
        ...
    


@_api.deprecated("3.4", alternative="`.MathtextBackendPath`")
class MathtextBackendPdf(MathtextBackend):
    """Store information to write a mathtext rendering to the PDF backend."""
    _PDFResult = ...
    def __init__(self) -> None:
        ...
    
    def render_glyph(self, ox, oy, info): # -> None:
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2): # -> None:
        ...
    
    def get_results(self, box, used_characters): # -> _PDFResult:
        ...
    


@_api.deprecated("3.4", alternative="`.MathtextBackendPath`")
class MathtextBackendSvg(MathtextBackend):
    """
    Store information to write a mathtext rendering to the SVG
    backend.
    """
    def __init__(self) -> None:
        ...
    
    def render_glyph(self, ox, oy, info): # -> None:
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2): # -> None:
        ...
    
    def get_results(self, box, used_characters): # -> tuple[int | Unknown, int | Unknown, int | Unknown, SimpleNamespace, Unknown]:
        ...
    


class MathtextBackendPath(MathtextBackend):
    """
    Store information to write a mathtext rendering to the text path
    machinery.
    """
    _Result = ...
    def __init__(self) -> None:
        ...
    
    def render_glyph(self, ox, oy, info): # -> None:
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2): # -> None:
        ...
    
    def get_results(self, box, used_characters): # -> _Result:
        ...
    


@_api.deprecated("3.4", alternative="`.MathtextBackendPath`")
class MathtextBackendCairo(MathtextBackend):
    """
    Store information to write a mathtext rendering to the Cairo
    backend.
    """
    def __init__(self) -> None:
        ...
    
    def render_glyph(self, ox, oy, info): # -> None:
        ...
    
    def render_rect_filled(self, x1, y1, x2, y2): # -> None:
        ...
    
    def get_results(self, box, used_characters): # -> tuple[int | Unknown, int | Unknown, int | Unknown, list[Unknown], list[Unknown]]:
        ...
    


class MathTextWarning(Warning):
    ...


@_api.deprecated("3.4")
def ship(ox, oy, box): # -> None:
    ...

class MathTextParser:
    _parser = ...
    _backend_mapping = ...
    _font_type_mapping = ...
    def __init__(self, output) -> None:
        """Create a MathTextParser for the given backend *output*."""
        ...
    
    def parse(self, s, dpi=..., prop=..., *, _force_standard_ps_fonts=...):
        """
        Parse the given math expression *s* at the given *dpi*.  If *prop* is
        provided, it is a `.FontProperties` object specifying the "default"
        font to use in the math expression, used for all non-math text.

        The results are cached, so multiple calls to `parse`
        with the same expression should be fast.
        """
        ...
    
    @_api.deprecated("3.4", alternative="`.mathtext.math_to_image`")
    def to_mask(self, texstr, dpi=..., fontsize=...): # -> tuple[NDArray[Unknown], Unknown]:
        r"""
        Convert a mathtext string to a grayscale array and depth.

        Parameters
        ----------
        texstr : str
            A valid mathtext string, e.g., r'IQ: $\sigma_i=15$'.
        dpi : float
            The dots-per-inch setting used to render the text.
        fontsize : int
            The font size in points

        Returns
        -------
        array : 2D uint8 alpha
            Mask array of rasterized tex.
        depth : int
            Offset of the baseline from the bottom of the image, in pixels.
        """
        ...
    
    @_api.deprecated("3.4", alternative="`.mathtext.math_to_image`")
    def to_rgba(self, texstr, color=..., dpi=..., fontsize=...): # -> tuple[NDArray[uint8], Unknown]:
        r"""
        Convert a mathtext string to an RGBA array and depth.

        Parameters
        ----------
        texstr : str
            A valid mathtext string, e.g., r'IQ: $\sigma_i=15$'.
        color : color
            The text color.
        dpi : float
            The dots-per-inch setting used to render the text.
        fontsize : int
            The font size in points.

        Returns
        -------
        array : (M, N, 4) array
            RGBA color values of rasterized tex, colorized with *color*.
        depth : int
            Offset of the baseline from the bottom of the image, in pixels.
        """
        ...
    
    @_api.deprecated("3.4", alternative="`.mathtext.math_to_image`")
    def to_png(self, filename, texstr, color=..., dpi=..., fontsize=...):
        r"""
        Render a tex expression to a PNG file.

        Parameters
        ----------
        filename
            A writable filename or fileobject.
        texstr : str
            A valid mathtext string, e.g., r'IQ: $\sigma_i=15$'.
        color : color
            The text color.
        dpi : float
            The dots-per-inch setting used to render the text.
        fontsize : int
            The font size in points.

        Returns
        -------
        int
            Offset of the baseline from the bottom of the image, in pixels.
        """
        ...
    
    @_api.deprecated("3.4", alternative="`.mathtext.math_to_image`")
    def get_depth(self, texstr, dpi=..., fontsize=...):
        r"""
        Get the depth of a mathtext string.

        Parameters
        ----------
        texstr : str
            A valid mathtext string, e.g., r'IQ: $\sigma_i=15$'.
        dpi : float
            The dots-per-inch setting used to render the text.

        Returns
        -------
        int
            Offset of the baseline from the bottom of the image, in pixels.
        """
        ...
    


def math_to_image(s, filename_or_obj, prop=..., dpi=..., format=...):
    """
    Given a math expression, renders it in a closely-clipped bounding
    box to an image file.

    Parameters
    ----------
    s : str
        A math expression.  The math portion must be enclosed in dollar signs.
    filename_or_obj : str or path-like or file-like
        Where to write the image data.
    prop : `.FontProperties`, optional
        The size and style of the text.
    dpi : float, optional
        The output dpi.  If not set, the dpi is determined as for
        `.Figure.savefig`.
    format : str, optional
        The output format, e.g., 'svg', 'pdf', 'ps' or 'png'.  If not set, the
        format is determined as for `.Figure.savefig`.
    """
    ...
