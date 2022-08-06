"""
This type stub file was generated by pyright.
"""

from typing import Any

"""
For compatibility with numpy libraries, pandas functions or methods have to
accept '*args' and '**kwargs' parameters to accommodate numpy arguments that
are not actually used or respected in the pandas implementation.

To ensure that users do not abuse these parameters, validation is performed in
'validators.py' to make sure that any extra parameters passed correspond ONLY
to those in the numpy signature. Part of that validation includes whether or
not the user attempted to pass in non-default values for these extraneous
parameters. As we want to discourage users from relying on these parameters
when calling the pandas implementation, we want them only to pass in the
default values for these parameters.

This module provides a set of commonly used default arguments for functions and
methods that are spread throughout the codebase. This module will make it
easier to adjust to future upstream changes in the analogous numpy signatures.
"""
class CompatValidator:
    def __init__(self, defaults, fname=..., method: str | None = ..., max_fname_arg_count=...) -> None:
        ...
    
    def __call__(self, args, kwargs, fname=..., max_fname_arg_count=..., method: str | None = ...) -> None:
        ...
    


ARGMINMAX_DEFAULTS = ...
validate_argmin = ...
validate_argmax = ...
def process_skipna(skipna, args): # -> tuple[Unknown | Literal[True], Unknown]:
    ...

def validate_argmin_with_skipna(skipna, args, kwargs): # -> Literal[True]:
    """
    If 'Series.argmin' is called via the 'numpy' library, the third parameter
    in its signature is 'out', which takes either an ndarray or 'None', so
    check if the 'skipna' parameter is either an instance of ndarray or is
    None, since 'skipna' itself should be a boolean
    """
    ...

def validate_argmax_with_skipna(skipna, args, kwargs): # -> Literal[True]:
    """
    If 'Series.argmax' is called via the 'numpy' library, the third parameter
    in its signature is 'out', which takes either an ndarray or 'None', so
    check if the 'skipna' parameter is either an instance of ndarray or is
    None, since 'skipna' itself should be a boolean
    """
    ...

ARGSORT_DEFAULTS: dict[str, int | str | None] = ...
validate_argsort = ...
ARGSORT_DEFAULTS_KIND: dict[str, int | None] = ...
validate_argsort_kind = ...
def validate_argsort_with_ascending(ascending, args, kwargs): # -> Literal[True]:
    """
    If 'Categorical.argsort' is called via the 'numpy' library, the first
    parameter in its signature is 'axis', which takes either an integer or
    'None', so check if the 'ascending' parameter has either integer type or is
    None, since 'ascending' itself should be a boolean
    """
    ...

CLIP_DEFAULTS: dict[str, Any] = ...
validate_clip = ...
def validate_clip_with_axis(axis, args, kwargs): # -> None:
    """
    If 'NDFrame.clip' is called via the numpy library, the third parameter in
    its signature is 'out', which can takes an ndarray, so check if the 'axis'
    parameter is an instance of ndarray, since 'axis' itself should either be
    an integer or None
    """
    ...

CUM_FUNC_DEFAULTS: dict[str, Any] = ...
validate_cum_func = ...
validate_cumsum = ...
def validate_cum_func_with_skipna(skipna, args, kwargs, name): # -> Literal[True]:
    """
    If this function is called via the 'numpy' library, the third parameter in
    its signature is 'dtype', which takes either a 'numpy' dtype or 'None', so
    check if the 'skipna' parameter is a boolean or not
    """
    ...

ALLANY_DEFAULTS: dict[str, bool | None] = ...
validate_all = ...
validate_any = ...
LOGICAL_FUNC_DEFAULTS = ...
validate_logical_func = ...
MINMAX_DEFAULTS = ...
validate_min = ...
validate_max = ...
RESHAPE_DEFAULTS: dict[str, str] = ...
validate_reshape = ...
REPEAT_DEFAULTS: dict[str, Any] = ...
validate_repeat = ...
ROUND_DEFAULTS: dict[str, Any] = ...
validate_round = ...
SORT_DEFAULTS: dict[str, int | str | None] = ...
validate_sort = ...
STAT_FUNC_DEFAULTS: dict[str, Any | None] = ...
SUM_DEFAULTS = ...
PROD_DEFAULTS = ...
MEDIAN_DEFAULTS = ...
validate_stat_func = ...
validate_sum = ...
validate_prod = ...
validate_mean = ...
validate_median = ...
STAT_DDOF_FUNC_DEFAULTS: dict[str, bool | None] = ...
validate_stat_ddof_func = ...
TAKE_DEFAULTS: dict[str, str | None] = ...
validate_take = ...
def validate_take_with_convert(convert, args, kwargs): # -> Literal[True]:
    """
    If this function is called via the 'numpy' library, the third parameter in
    its signature is 'axis', which takes either an ndarray or 'None', so check
    if the 'convert' parameter is either an instance of ndarray or is None
    """
    ...

TRANSPOSE_DEFAULTS = ...
validate_transpose = ...
def validate_window_func(name, args, kwargs) -> None:
    ...

def validate_rolling_func(name, args, kwargs) -> None:
    ...

def validate_expanding_func(name, args, kwargs) -> None:
    ...

def validate_groupby_func(name, args, kwargs, allowed=...) -> None:
    """
    'args' and 'kwargs' should be empty, except for allowed kwargs because all
    of their necessary parameters are explicitly listed in the function
    signature
    """
    ...

RESAMPLER_NUMPY_OPS = ...
def validate_resampler_func(method: str, args, kwargs) -> None:
    """
    'args' and 'kwargs' should be empty because all of their necessary
    parameters are explicitly listed in the function signature
    """
    ...

def validate_minmax_axis(axis: int | None, ndim: int = ...) -> None:
    """
    Ensure that the axis argument passed to min, max, argmin, or argmax is zero
    or None, as otherwise it will be incorrectly ignored.

    Parameters
    ----------
    axis : int or None
    ndim : int, default 1

    Raises
    ------
    ValueError
    """
    ...

