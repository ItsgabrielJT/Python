"""
This type stub file was generated by pyright.
"""

from typing import Any, TYPE_CHECKING
from pandas._typing import FilePath, ReadPickleBuffer
from pandas import DataFrame, Series

if TYPE_CHECKING:
    ...
_network_error_messages = ...
_network_errno_vals = ...
def optional_args(decorator): # -> (*args: Unknown, **kwargs: Unknown) -> (Unknown | ((f: Unknown) -> Unknown)):
    """
    allows a decorator to take optional positional and keyword arguments.
    Assumes that taking a single, callable, positional argument means that
    it is decorating a function, i.e. something like this::

        @my_decorator
        def function(): pass

    Calls decorator with decorator(f, *args, **kwargs)
    """
    ...

@optional_args
def network(t, url=..., raise_on_error=..., check_before_test=..., error_classes=..., skip_errnos=..., _skip_on_messages=...): # -> (*args: Unknown, **kwargs: Unknown) -> Unknown:
    """
    Label a test as requiring network connection and, if an error is
    encountered, only raise if it does not find a network connection.

    In comparison to ``network``, this assumes an added contract to your test:
    you must assert that, under normal conditions, your test will ONLY fail if
    it does not have network connectivity.

    You can call this in 3 ways: as a standard decorator, with keyword
    arguments, or with a positional argument that is the url to check.

    Parameters
    ----------
    t : callable
        The test requiring network connectivity.
    url : path
        The url to test via ``pandas.io.common.urlopen`` to check
        for connectivity. Defaults to 'https://www.google.com'.
    raise_on_error : bool
        If True, never catches errors.
    check_before_test : bool
        If True, checks connectivity before running the test case.
    error_classes : tuple or Exception
        error classes to ignore. If not in ``error_classes``, raises the error.
        defaults to OSError. Be careful about changing the error classes here.
    skip_errnos : iterable of int
        Any exception that has .errno or .reason.erno set to one
        of these values will be skipped with an appropriate
        message.
    _skip_on_messages: iterable of string
        any exception e for which one of the strings is
        a substring of str(e) will be skipped with an appropriate
        message. Intended to suppress errors where an errno isn't available.

    Notes
    -----
    * ``raise_on_error`` supersedes ``check_before_test``

    Returns
    -------
    t : callable
        The decorated test ``t``, with checks for connectivity errors.

    Example
    -------

    Tests decorated with @network will fail if it's possible to make a network
    connection to another URL (defaults to google.com)::

      >>> from pandas import _testing as tm
      >>> @tm.network
      ... def test_network():
      ...     with pd.io.common.urlopen("rabbit://bonanza.com"):
      ...         pass
      >>> test_network()  # doctest: +SKIP
      Traceback
         ...
      URLError: <urlopen error unknown url type: rabbit>

      You can specify alternative URLs::

        >>> @tm.network("https://www.yahoo.com")
        ... def test_something_with_yahoo():
        ...    raise OSError("Failure Message")
        >>> test_something_with_yahoo()  # doctest: +SKIP
        Traceback (most recent call last):
            ...
        OSError: Failure Message

    If you set check_before_test, it will check the url first and not run the
    test on failure::

        >>> @tm.network("failing://url.blaher", check_before_test=True)
        ... def test_something():
        ...     print("I ran!")
        ...     raise ValueError("Failure")
        >>> test_something()  # doctest: +SKIP
        Traceback (most recent call last):
            ...

    Errors not related to networking will always be raised.
    """
    ...

with_connectivity_check = ...
def can_connect(url, error_classes=...): # -> bool:
    """
    Try to connect to the given url. True if succeeds, False if OSError
    raised

    Parameters
    ----------
    url : basestring
        The URL to try to connect to

    Returns
    -------
    connectable : bool
        Return True if no OSError (unable to connect) or URLError (bad url) was
        raised
    """
    ...

def round_trip_pickle(obj: Any, path: FilePath | ReadPickleBuffer | None = ...) -> DataFrame | Series:
    """
    Pickle an object and then read it again.

    Parameters
    ----------
    obj : any object
        The object to pickle and then re-read.
    path : str, path object or file-like object, default None
        The path where the pickled object is written and then read.

    Returns
    -------
    pandas object
        The original object that was pickled and then re-read.
    """
    ...

def round_trip_pathlib(writer, reader, path: str | None = ...):
    """
    Write an object to file specified by a pathlib.Path and read it back

    Parameters
    ----------
    writer : callable bound to pandas object
        IO writing function (e.g. DataFrame.to_csv )
    reader : callable
        IO reading function (e.g. pd.read_csv )
    path : str, default None
        The path where the object is written and then read.

    Returns
    -------
    pandas object
        The original object that was serialized and then re-read.
    """
    ...

def round_trip_localpath(writer, reader, path: str | None = ...):
    """
    Write an object to file specified by a py.path LocalPath and read it back.

    Parameters
    ----------
    writer : callable bound to pandas object
        IO writing function (e.g. DataFrame.to_csv )
    reader : callable
        IO reading function (e.g. pd.read_csv )
    path : str, default None
        The path where the object is written and then read.

    Returns
    -------
    pandas object
        The original object that was serialized and then re-read.
    """
    ...

def write_to_compressed(compression, path, data, dest=...): # -> None:
    """
    Write data to a compressed file.

    Parameters
    ----------
    compression : {'gzip', 'bz2', 'zip', 'xz', 'zstd'}
        The compression type to use.
    path : str
        The file path to write the data.
    data : str
        The data to write.
    dest : str, default "test"
        The destination file (for ZIP only)

    Raises
    ------
    ValueError : An invalid compression value was passed in.
    """
    ...

def close(fignum=...): # -> None:
    ...
