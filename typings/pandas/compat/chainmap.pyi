"""
This type stub file was generated by pyright.
"""

from typing import ChainMap, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
class DeepChainMap(ChainMap[_KT, _VT]):
    """
    Variant of ChainMap that allows direct updates to inner scopes.

    Only works when all passed mapping are mutable.
    """
    def __setitem__(self, key: _KT, value: _VT) -> None:
        ...
    
    def __delitem__(self, key: _KT) -> None:
        """
        Raises
        ------
        KeyError
            If `key` doesn't exist.
        """
        ...
    


