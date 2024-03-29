"""
This type stub file was generated by pyright.
"""

from typing import Callable, TypeVar
from pandas.util._decorators import doc
from pandas.core.arrays import IntervalArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
from pandas.core.indexes.base import Index

"""
Shared methods for Index subclasses backed by ExtensionArray.
"""
_T = TypeVar("_T", bound="NDArrayBackedExtensionIndex")
_ExtensionIndexT = TypeVar("_ExtensionIndexT", bound="ExtensionIndex")
def inherit_names(names: list[str], delegate: type, cache: bool = ..., wrap: bool = ...) -> Callable[[type[_ExtensionIndexT]], type[_ExtensionIndexT]]:
    """
    Class decorator to pin attributes from an ExtensionArray to a Index subclass.

    Parameters
    ----------
    names : List[str]
    delegate : class
    cache : bool, default False
    wrap : bool, default False
        Whether to wrap the inherited result in an Index.
    """
    ...

class ExtensionIndex(Index):
    """
    Index subclass for indexes backed by ExtensionArray.
    """
    _data: IntervalArray | NDArrayBackedExtensionArray
    @doc(Index.map)
    def map(self, mapper, na_action=...):
        ...
    


class NDArrayBackedExtensionIndex(ExtensionIndex):
    """
    Index subclass for indexes backed by NDArrayBackedExtensionArray.
    """
    _data: NDArrayBackedExtensionArray
    ...


