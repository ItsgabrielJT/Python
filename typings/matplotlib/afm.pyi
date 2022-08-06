"""
This type stub file was generated by pyright.
"""

"""
A python interface to Adobe Font Metrics Files.

Although a number of other Python implementations exist, and may be more
complete than this, it was decided not to go with them because they were
either:

1) copyrighted or used a non-BSD compatible license
2) had too many dependencies and a free standing lib was needed
3) did more than needed and it was easier to write afresh rather than
   figure out how to get just what was needed.

It is pretty easy to use, and has no external dependencies:

>>> import matplotlib as mpl
>>> from pathlib import Path
>>> afm_path = Path(mpl.get_data_path(), 'fonts', 'afm', 'ptmr8a.afm')
>>>
>>> from matplotlib.afm import AFM
>>> with afm_path.open('rb') as fh:
...     afm = AFM(fh)
>>> afm.string_width_height('What the heck?')
(6220.0, 694)
>>> afm.get_fontname()
'Times-Roman'
>>> afm.get_kern_dist('A', 'f')
0
>>> afm.get_kern_dist('A', 'y')
-92.0
>>> afm.get_bbox_char('!')
[130, -9, 238, 676]

As in the Adobe Font Metrics File Format Specification, all dimensions
are given in units of 1/1000 of the scale factor (point size) of the font
being used.
"""
_log = ...
CharMetrics = ...
CompositePart = ...
class AFM:
    def __init__(self, fh) -> None:
        """Parse the AFM file in file object *fh*."""
        ...
    
    def get_bbox_char(self, c, isord=...):
        ...
    
    def string_width_height(self, s): # -> tuple[Literal[0], Literal[0]] | tuple[Unknown | Literal[0], float]:
        """
        Return the string width (including kerning) and string height
        as a (*w*, *h*) tuple.
        """
        ...
    
    def get_str_bbox_and_descent(self, s): # -> tuple[Literal[0], Literal[0], Literal[0], Literal[0], Literal[0]] | tuple[int, float, Unknown | Literal[0], float, float]:
        """Return the string bounding box and the maximal descent."""
        ...
    
    def get_str_bbox(self, s): # -> tuple[Literal[0], Literal[0], Literal[0], Literal[0]] | tuple[int, float, Unknown | Literal[0], float]:
        """Return the string bounding box."""
        ...
    
    def get_name_char(self, c, isord=...):
        """Get the name of the character, i.e., ';' is 'semicolon'."""
        ...
    
    def get_width_char(self, c, isord=...):
        """
        Get the width of the character from the character metric WX field.
        """
        ...
    
    def get_width_from_char_name(self, name):
        """Get the width of the character from a type1 character name."""
        ...
    
    def get_height_char(self, c, isord=...):
        """Get the bounding box (ink) height of character *c* (space is 0)."""
        ...
    
    def get_kern_dist(self, c1, c2): # -> int:
        """
        Return the kerning pair distance (possibly 0) for chars *c1* and *c2*.
        """
        ...
    
    def get_kern_dist_from_name(self, name1, name2): # -> int:
        """
        Return the kerning pair distance (possibly 0) for chars
        *name1* and *name2*.
        """
        ...
    
    def get_fontname(self):
        """Return the font name, e.g., 'Times-Roman'."""
        ...
    
    @property
    def postscript_name(self):
        ...
    
    def get_fullname(self):
        """Return the font full name, e.g., 'Times-Roman'."""
        ...
    
    def get_familyname(self): # -> str:
        """Return the font family name, e.g., 'Times'."""
        ...
    
    @property
    def family_name(self): # -> str:
        """The font family name, e.g., 'Times'."""
        ...
    
    def get_weight(self):
        """Return the font weight, e.g., 'Bold' or 'Roman'."""
        ...
    
    def get_angle(self):
        """Return the fontangle as float."""
        ...
    
    def get_capheight(self):
        """Return the cap height as float."""
        ...
    
    def get_xheight(self):
        """Return the xheight as float."""
        ...
    
    def get_underline_thickness(self):
        """Return the underline thickness as float."""
        ...
    
    def get_horizontal_stem_width(self): # -> None:
        """
        Return the standard horizontal stem width as float, or *None* if
        not specified in AFM file.
        """
        ...
    
    def get_vertical_stem_width(self): # -> None:
        """
        Return the standard vertical stem width as float, or *None* if
        not specified in AFM file.
        """
        ...
    


