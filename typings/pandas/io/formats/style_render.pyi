"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, TypedDict, Union
from pandas._typing import Level
from pandas import DataFrame, Index, Series

jinja2 = ...
BaseFormatter = Union[str, Callable]
ExtFormatter = Union[BaseFormatter, Dict[Any, Optional[BaseFormatter]]]
CSSPair = Tuple[str, Union[str, int, float]]
CSSList = List[CSSPair]
CSSProperties = Union[str, CSSList]
class CSSDict(TypedDict):
    selector: str
    props: CSSProperties
    ...


CSSStyles = List[CSSDict]
Subset = Union[slice, Sequence, Index]
class StylerRenderer:
    """
    Base class to process rendering a Styler with a specified jinja2 template.
    """
    loader = ...
    env = ...
    template_html = ...
    template_html_table = ...
    template_html_style = ...
    template_latex = ...
    def __init__(self, data: DataFrame | Series, uuid: str | None = ..., uuid_len: int = ..., table_styles: CSSStyles | None = ..., table_attributes: str | None = ..., caption: str | tuple | None = ..., cell_ids: bool = ..., precision: int | None = ...) -> None:
        ...
    
    def format(self, formatter: ExtFormatter | None = ..., subset: Subset | None = ..., na_rep: str | None = ..., precision: int | None = ..., decimal: str = ..., thousands: str | None = ..., escape: str | None = ..., hyperlinks: str | None = ...) -> StylerRenderer:
        r"""
        Format the text display value of cells.

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        subset : label, array-like, IndexSlice, optional
            A valid 2d input to `DataFrame.loc[<subset>]`, or, in the case of a 1d input
            or single key, to `DataFrame.loc[:, <subset>]` where the columns are
            prioritised, to limit ``data`` to *before* applying the function.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.

            .. versionadded:: 1.0.0

        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.

            .. versionadded:: 1.3.0

        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.

            .. versionadded:: 1.3.0

        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.

            .. versionadded:: 1.3.0

        escape : str, optional
            Use 'html' to replace the characters ``&``, ``<``, ``>``, ``'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use 'latex' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\`` in the cell display string with
            LaTeX-safe sequences.
            Escaping is done before ``formatter``.

            .. versionadded:: 1.3.0

        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \href
            commands if "latex".

            .. versionadded:: 1.4.0

        Returns
        -------
        self : Styler

        See Also
        --------
        Styler.format_index: Format the text display value of index labels.

        Notes
        -----
        This method assigns a formatting function, ``formatter``, to each cell in the
        DataFrame. If ``formatter`` is ``None``, then the default formatter is used.
        If a callable then that function should take a data value as input and return
        a displayable representation, such as a string. If ``formatter`` is
        given as a string this is assumed to be a valid Python format specification
        and is wrapped to a callable as ``string.format(x)``. If a ``dict`` is given,
        keys should correspond to column names, and values should be string or
        callable, as above.

        The default formatter currently expresses floats and complex numbers with the
        pandas display precision unless using the ``precision`` argument here. The
        default formatter does not adjust the representation of missing values unless
        the ``na_rep`` argument is used.

        The ``subset`` argument defines which region to apply the formatting function
        to. If the ``formatter`` argument is given in dict form but does not include
        all columns within the subset then these columns will have the default formatter
        applied. Any columns in the formatter dict excluded from the subset will
        be ignored.

        When using a ``formatter`` string the dtypes must be compatible, otherwise a
        `ValueError` will be raised.

        When instantiating a Styler, default formatting can be applied be setting the
        ``pandas.options``:

          - ``styler.format.formatter``: default None.
          - ``styler.format.na_rep``: default None.
          - ``styler.format.precision``: default 6.
          - ``styler.format.decimal``: default ".".
          - ``styler.format.thousands``: default None.
          - ``styler.format.escape``: default None.

        .. warning::
           `Styler.format` is ignored when using the output format `Styler.to_excel`,
           since Excel and Python have inherrently different formatting structures.
           However, it is possible to use the `number-format` pseudo CSS attribute
           to force Excel permissible formatting. See examples.

        Examples
        --------
        Using ``na_rep`` and ``precision`` with the default ``formatter``

        >>> df = pd.DataFrame([[np.nan, 1.0, 'A'], [2.0, np.nan, 3.0]])
        >>> df.style.format(na_rep='MISS', precision=3)  # doctest: +SKIP
                0       1       2
        0    MISS   1.000       A
        1   2.000    MISS   3.000

        Using a ``formatter`` specification on consistent column dtypes

        >>> df.style.format('{:.2f}', na_rep='MISS', subset=[0,1])  # doctest: +SKIP
                0      1          2
        0    MISS   1.00          A
        1    2.00   MISS   3.000000

        Using the default ``formatter`` for unspecified columns

        >>> df.style.format({0: '{:.2f}', 1: '£ {:.1f}'}, na_rep='MISS', precision=1)
        ...  # doctest: +SKIP
                 0      1     2
        0    MISS   £ 1.0     A
        1    2.00    MISS   3.0

        Multiple ``na_rep`` or ``precision`` specifications under the default
        ``formatter``.

        >>> df.style.format(na_rep='MISS', precision=1, subset=[0])
        ...     .format(na_rep='PASS', precision=2, subset=[1, 2])  # doctest: +SKIP
                0      1      2
        0    MISS   1.00      A
        1     2.0   PASS   3.00

        Using a callable ``formatter`` function.

        >>> func = lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
        >>> df.style.format({0: '{:.1f}', 2: func}, precision=4, na_rep='MISS')
        ...  # doctest: +SKIP
                0        1        2
        0    MISS   1.0000   STRING
        1     2.0     MISS    FLOAT

        Using a ``formatter`` with HTML ``escape`` and ``na_rep``.

        >>> df = pd.DataFrame([['<div></div>', '"A&B"', None]])
        >>> s = df.style.format(
        ...     '<a href="a.com/{0}">{0}</a>', escape="html", na_rep="NA"
        ...     )
        >>> s.to_html()  # doctest: +SKIP
        ...
        <td .. ><a href="a.com/&lt;div&gt;&lt;/div&gt;">&lt;div&gt;&lt;/div&gt;</a></td>
        <td .. ><a href="a.com/&#34;A&amp;B&#34;">&#34;A&amp;B&#34;</a></td>
        <td .. >NA</td>
        ...

        Using a ``formatter`` with LaTeX ``escape``.

        >>> df = pd.DataFrame([["123"], ["~ ^"], ["$%#"]])
        >>> df.style.format("\\textbf{{{}}}", escape="latex").to_latex()
        ...  # doctest: +SKIP
        \begin{tabular}{ll}
        {} & {0} \\
        0 & \textbf{123} \\
        1 & \textbf{\textasciitilde \space \textasciicircum } \\
        2 & \textbf{\$\%\#} \\
        \end{tabular}

        Pandas defines a `number-format` pseudo CSS attribute instead of the `.format`
        method to create `to_excel` permissible formatting. Note that semi-colons are
        CSS protected characters but used as separators in Excel's format string.
        Replace semi-colons with the section separator character (ASCII-245) when
        defining the formatting here.

        >>> df = pd.DataFrame({"A": [1, 0, -1]})
        >>> pseudo_css = "number-format: 0§[Red](0)§-§@;"
        >>> df.style.applymap(lambda v: css).to_excel("formatted_file.xlsx")
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/format_excel_css.png
        """
        ...
    
    def format_index(self, formatter: ExtFormatter | None = ..., axis: int | str = ..., level: Level | list[Level] | None = ..., na_rep: str | None = ..., precision: int | None = ..., decimal: str = ..., thousands: str | None = ..., escape: str | None = ..., hyperlinks: str | None = ...) -> StylerRenderer:
        r"""
        Format the text display value of index labels or column headers.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        axis : {0, "index", 1, "columns"}
            Whether to apply the formatter to the index or column headers.
        level : int, str, list
            The level(s) over which to apply the generic formatter.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.
        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.
        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.
        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.
        escape : str, optional
            Use 'html' to replace the characters ``&``, ``<``, ``>``, ``'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use 'latex' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\`` in the cell display string with
            LaTeX-safe sequences.
            Escaping is done before ``formatter``.
        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \href
            commands if "latex".

        Returns
        -------
        self : Styler

        See Also
        --------
        Styler.format: Format the text display value of data cells.

        Notes
        -----
        This method assigns a formatting function, ``formatter``, to each level label
        in the DataFrame's index or column headers. If ``formatter`` is ``None``,
        then the default formatter is used.
        If a callable then that function should take a label value as input and return
        a displayable representation, such as a string. If ``formatter`` is
        given as a string this is assumed to be a valid Python format specification
        and is wrapped to a callable as ``string.format(x)``. If a ``dict`` is given,
        keys should correspond to MultiIndex level numbers or names, and values should
        be string or callable, as above.

        The default formatter currently expresses floats and complex numbers with the
        pandas display precision unless using the ``precision`` argument here. The
        default formatter does not adjust the representation of missing values unless
        the ``na_rep`` argument is used.

        The ``level`` argument defines which levels of a MultiIndex to apply the
        method to. If the ``formatter`` argument is given in dict form but does
        not include all levels within the level argument then these unspecified levels
        will have the default formatter applied. Any levels in the formatter dict
        specifically excluded from the level argument will be ignored.

        When using a ``formatter`` string the dtypes must be compatible, otherwise a
        `ValueError` will be raised.

        .. warning::
           `Styler.format_index` is ignored when using the output format
           `Styler.to_excel`, since Excel and Python have inherrently different
           formatting structures.
           However, it is possible to use the `number-format` pseudo CSS attribute
           to force Excel permissible formatting. See documentation for `Styler.format`.

        Examples
        --------
        Using ``na_rep`` and ``precision`` with the default ``formatter``

        >>> df = pd.DataFrame([[1, 2, 3]], columns=[2.0, np.nan, 4.0])
        >>> df.style.format_index(axis=1, na_rep='MISS', precision=3)  # doctest: +SKIP
            2.000    MISS   4.000
        0       1       2       3

        Using a ``formatter`` specification on consistent dtypes in a level

        >>> df.style.format_index('{:.2f}', axis=1, na_rep='MISS')  # doctest: +SKIP
             2.00   MISS    4.00
        0       1      2       3

        Using the default ``formatter`` for unspecified levels

        >>> df = pd.DataFrame([[1, 2, 3]],
        ...     columns=pd.MultiIndex.from_arrays([["a", "a", "b"],[2, np.nan, 4]]))
        >>> df.style.format_index({0: lambda v: upper(v)}, axis=1, precision=1)
        ...  # doctest: +SKIP
                       A       B
              2.0    nan     4.0
        0       1      2       3

        Using a callable ``formatter`` function.

        >>> func = lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
        >>> df.style.format_index(func, axis=1, na_rep='MISS')
        ...  # doctest: +SKIP
                  STRING  STRING
            FLOAT   MISS   FLOAT
        0       1      2       3

        Using a ``formatter`` with HTML ``escape`` and ``na_rep``.

        >>> df = pd.DataFrame([[1, 2, 3]], columns=['"A"', 'A&B', None])
        >>> s = df.style.format_index('$ {0}', axis=1, escape="html", na_rep="NA")
        ...  # doctest: +SKIP
        <th .. >$ &#34;A&#34;</th>
        <th .. >$ A&amp;B</th>
        <th .. >NA</td>
        ...

        Using a ``formatter`` with LaTeX ``escape``.

        >>> df = pd.DataFrame([[1, 2, 3]], columns=["123", "~", "$%#"])
        >>> df.style.format_index("\\textbf{{{}}}", escape="latex", axis=1).to_latex()
        ...  # doctest: +SKIP
        \begin{tabular}{lrrr}
        {} & {\textbf{123}} & {\textbf{\textasciitilde }} & {\textbf{\$\%\#}} \\
        0 & 1 & 2 & 3 \\
        \end{tabular}
        """
        ...
    


def format_table_styles(styles: CSSStyles) -> CSSStyles:
    """
    looks for multiple CSS selectors and separates them:
    [{'selector': 'td, th', 'props': 'a:v;'}]
        ---> [{'selector': 'td', 'props': 'a:v;'},
              {'selector': 'th', 'props': 'a:v;'}]
    """
    ...

def non_reducing_slice(slice_: Subset): # -> tuple[Unknown | list[Unknown], ...]:
    """
    Ensure that a slice doesn't reduce to a Series or Scalar.

    Any user-passed `subset` should have this called on it
    to make sure we're always working with DataFrames.
    """
    ...

def maybe_convert_css_to_tuples(style: CSSProperties) -> CSSList:
    """
    Convert css-string to sequence of tuples format if needed.
    'color:red; border:1px solid black;' -> [('color', 'red'),
                                             ('border','1px solid red')]
    """
    ...

def refactor_levels(level: Level | list[Level] | None, obj: Index) -> list[int]:
    """
    Returns a consistent levels arg for use in ``hide_index`` or ``hide_columns``.

    Parameters
    ----------
    level : int, str, list
        Original ``level`` arg supplied to above methods.
    obj:
        Either ``self.index`` or ``self.columns``

    Returns
    -------
    list : refactored arg with a list of levels to hide
    """
    ...

class Tooltips:
    """
    An extension to ``Styler`` that allows for and manipulates tooltips on hover
    of ``<td>`` cells in the HTML result.

    Parameters
    ----------
    css_name: str, default "pd-t"
        Name of the CSS class that controls visualisation of tooltips.
    css_props: list-like, default; see Notes
        List of (attr, value) tuples defining properties of the CSS class.
    tooltips: DataFrame, default empty
        DataFrame of strings aligned with underlying Styler data for tooltip
        display.

    Notes
    -----
    The default properties for the tooltip CSS class are:

        - visibility: hidden
        - position: absolute
        - z-index: 1
        - background-color: black
        - color: white
        - transform: translate(-20px, -20px)

    Hidden visibility is a key prerequisite to the hover functionality, and should
    always be included in any manual properties specification.
    """
    def __init__(self, css_props: CSSProperties = ..., css_name: str = ..., tooltips: DataFrame = ...) -> None:
        ...
    


