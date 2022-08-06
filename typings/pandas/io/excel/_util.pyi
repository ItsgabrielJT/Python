"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Hashable, Literal, MutableMapping, Sequence, TYPE_CHECKING, TypeVar, overload
from pandas.io.excel._base import ExcelWriter

if TYPE_CHECKING:
    ExcelWriter_t = type[ExcelWriter]
    usecols_func = TypeVar("usecols_func", bound=Callable[[Hashable], object])
_writers: MutableMapping[str, ExcelWriter_t] = ...
def register_writer(klass: ExcelWriter_t) -> None:
    """
    Add engine to the excel writer registry.io.excel.

    You must use this method to integrate with ``to_excel``.

    Parameters
    ----------
    klass : ExcelWriter
    """
    ...

def get_default_engine(ext: str, mode: Literal["reader", "writer"] = ...) -> str:
    """
    Return the default reader/writer for the given extension.

    Parameters
    ----------
    ext : str
        The excel file extension for which to get the default engine.
    mode : str {'reader', 'writer'}
        Whether to get the default engine for reading or writing.
        Either 'reader' or 'writer'

    Returns
    -------
    str
        The default engine for the extension.
    """
    ...

def get_writer(engine_name: str) -> ExcelWriter_t:
    ...

@overload
def maybe_convert_usecols(usecols: str | list[int]) -> list[int]:
    ...

@overload
def maybe_convert_usecols(usecols: list[str]) -> list[str]:
    ...

@overload
def maybe_convert_usecols(usecols: usecols_func) -> usecols_func:
    ...

@overload
def maybe_convert_usecols(usecols: None) -> None:
    ...

def maybe_convert_usecols(usecols: str | list[int] | list[str] | usecols_func | None) -> None | list[int] | list[str] | usecols_func:
    """
    Convert `usecols` into a compatible format for parsing in `parsers.py`.

    Parameters
    ----------
    usecols : object
        The use-columns object to potentially convert.

    Returns
    -------
    converted : object
        The compatible format of `usecols`.
    """
    ...

@overload
def validate_freeze_panes(freeze_panes: tuple[int, int]) -> Literal[True]:
    ...

@overload
def validate_freeze_panes(freeze_panes: None) -> Literal[False]:
    ...

def validate_freeze_panes(freeze_panes: tuple[int, int] | None) -> bool:
    ...

def fill_mi_header(row: list[Hashable], control_row: list[bool]) -> tuple[list[Hashable], list[bool]]:
    """
    Forward fill blank entries in row but only inside the same parent index.

    Used for creating headers in Multiindex.

    Parameters
    ----------
    row : list
        List of items in a single row.
    control_row : list of bool
        Helps to determine if particular column is in same parent index as the
        previous value. Used to stop propagation of empty cells between
        different indexes.

    Returns
    -------
    Returns changed row and control_row
    """
    ...

def pop_header_name(row: list[Hashable], index_col: int | Sequence[int]) -> tuple[Hashable | None, list[Hashable]]:
    """
    Pop the header name for MultiIndex parsing.

    Parameters
    ----------
    row : list
        The data row to parse for the header name.
    index_col : int, list
        The index columns for our data. Assumed to be non-null.

    Returns
    -------
    header_name : str
        The extracted header name.
    trimmed_row : list
        The original data row with the header name removed.
    """
    ...

def combine_kwargs(engine_kwargs: dict[str, Any] | None, kwargs: dict) -> dict:
    """
    Used to combine two sources of kwargs for the backend engine.

    Use of kwargs is deprecated, this function is solely for use in 1.3 and should
    be removed in 1.4/2.0. Also _base.ExcelWriter.__new__ ensures either engine_kwargs
    or kwargs must be None or empty respectively.

    Parameters
    ----------
    engine_kwargs: dict
        kwargs to be passed through to the engine.
    kwargs: dict
        kwargs to be psased through to the engine (deprecated)

    Returns
    -------
    engine_kwargs combined with kwargs
    """
    ...
