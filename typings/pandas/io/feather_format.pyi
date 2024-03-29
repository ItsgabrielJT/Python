"""
This type stub file was generated by pyright.
"""

from typing import Hashable, Sequence
from pandas._typing import FilePath, ReadBuffer, StorageOptions, WriteBuffer
from pandas.util._decorators import doc
from pandas.core.api import DataFrame
from pandas.core.shared_docs import _shared_docs

""" feather-format compat """
@doc(storage_options=_shared_docs["storage_options"])
def to_feather(df: DataFrame, path: FilePath | WriteBuffer[bytes], storage_options: StorageOptions = ..., **kwargs): # -> None:
    """
    Write a DataFrame to the binary Feather format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, or file-like object
    {storage_options}

        .. versionadded:: 1.2.0

    **kwargs :
        Additional keywords passed to `pyarrow.feather.write_feather`.

        .. versionadded:: 1.1.0
    """
    ...

@doc(storage_options=_shared_docs["storage_options"])
def read_feather(path: FilePath | ReadBuffer[bytes], columns: Sequence[Hashable] | None = ..., use_threads: bool = ..., storage_options: StorageOptions = ...):
    """
    Load a feather-format object from the file path.

    Parameters
    ----------
    path : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``read()`` function. The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be: ``file://localhost/path/to/table.feather``.
    columns : sequence, default None
        If not provided, all columns are read.
    use_threads : bool, default True
        Whether to parallelize reading using multiple threads.
    {storage_options}

        .. versionadded:: 1.2.0

    Returns
    -------
    type of object stored in file
    """
    ...

