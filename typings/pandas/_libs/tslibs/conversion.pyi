"""
This type stub file was generated by pyright.
"""

import numpy as np
from datetime import datetime, tzinfo
from pandas._typing import npt

DT64NS_DTYPE: np.dtype
TD64NS_DTYPE: np.dtype
class OutOfBoundsTimedelta(ValueError):
    ...


def precision_from_unit(unit: str) -> tuple[int, int,]:
    ...

def ensure_datetime64ns(arr: np.ndarray, copy: bool = ...) -> np.ndarray:
    ...

def ensure_timedelta64ns(arr: np.ndarray, copy: bool = ...) -> np.ndarray:
    ...

def datetime_to_datetime64(values: npt.NDArray[np.object_]) -> tuple[np.ndarray, tzinfo | None,]:
    ...

def localize_pydatetime(dt: datetime, tz: tzinfo | None) -> datetime:
    ...
