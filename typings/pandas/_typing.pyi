"""
This type stub file was generated by pyright.
"""

import numpy as np
import numpy.typing as npt
from datetime import datetime, timedelta, tzinfo
from typing import Any, Callable, Collection, Dict, Hashable, Iterator, List, Literal, Mapping, Optional, Protocol, Sequence, TYPE_CHECKING, Tuple, Type as type_t, TypeVar, Union

if TYPE_CHECKING:
    NumpyValueArrayLike = Union[npt._ScalarLike_co, npt.ArrayLike]
    NumpySorter = Optional[npt._ArrayLikeInt_co]
else:
    ...
ArrayLike = Union["ExtensionArray", np.ndarray]
AnyArrayLike = Union[ArrayLike, "Index", "Series"]
PythonScalar = Union[str, int, float, bool]
DatetimeLikeScalar = Union["Period", "Timestamp", "Timedelta"]
PandasScalar = Union["Period", "Timestamp", "Timedelta", "Interval"]
Scalar = Union[PythonScalar, PandasScalar]
IntStrT = TypeVar("IntStrT", int, str)
TimestampConvertibleTypes = Union["Timestamp", datetime, np.datetime64, int, np.int64, float, str]
TimedeltaConvertibleTypes = Union["Timedelta", timedelta, np.timedelta64, int, np.int64, float, str]
Timezone = Union[str, tzinfo]
NDFrameT = TypeVar("NDFrameT", bound="NDFrame")
Axis = Union[str, int]
IndexLabel = Union[Hashable, Sequence[Hashable]]
Level = Union[Hashable, int]
Shape = Tuple[int, ...]
Suffixes = Tuple[Optional[str], Optional[str]]
Ordered = Optional[bool]
JSONSerializable = Optional[Union[PythonScalar, List, Dict]]
Frequency = Union[str, "DateOffset"]
Axes = Collection[Any]
RandomState = Union[int, ArrayLike, np.random.Generator, np.random.BitGenerator, np.random.RandomState,]
NpDtype = Union[str, np.dtype, type_t[Union[str, float, int, complex, bool, object]]]
Dtype = Union["ExtensionDtype", NpDtype]
AstypeArg = Union["ExtensionDtype", "npt.DTypeLike"]
DtypeArg = Union[Dtype, Dict[Hashable, Dtype]]
DtypeObj = Union[np.dtype, "ExtensionDtype"]
Renamer = Union[Mapping[Hashable, Any], Callable[[Hashable], Hashable]]
T = TypeVar("T")
FuncType = Callable[..., Any]
F = TypeVar("F", bound=FuncType)
ValueKeyFunc = Optional[Callable[["Series"], Union["Series", AnyArrayLike]]]
IndexKeyFunc = Optional[Callable[["Index"], Union["Index", AnyArrayLike]]]
AggFuncTypeBase = Union[Callable, str]
AggFuncTypeDict = Dict[Hashable, Union[AggFuncTypeBase, List[AggFuncTypeBase]]]
AggFuncType = Union[AggFuncTypeBase, List[AggFuncTypeBase], AggFuncTypeDict,]
AggObjType = Union["Series", "DataFrame", "GroupBy", "SeriesGroupBy", "DataFrameGroupBy", "BaseWindow", "Resampler",]
PythonFuncType = Callable[[Any], Any]
AnyStr_cov = TypeVar("AnyStr_cov", str, bytes, covariant=True)
AnyStr_con = TypeVar("AnyStr_con", str, bytes, contravariant=True)
class BaseBuffer(Protocol):
    @property
    def mode(self) -> str:
        ...
    
    def fileno(self) -> int:
        ...
    
    def seek(self, __offset: int, __whence: int = ...) -> int:
        ...
    
    def seekable(self) -> bool:
        ...
    
    def tell(self) -> int:
        ...
    


class ReadBuffer(BaseBuffer, Protocol[AnyStr_cov]):
    def read(self, __n: int | None = ...) -> AnyStr_cov:
        ...
    


class WriteBuffer(BaseBuffer, Protocol[AnyStr_con]):
    def write(self, __b: AnyStr_con) -> Any:
        ...
    
    def flush(self) -> Any:
        ...
    


class ReadPickleBuffer(ReadBuffer[bytes], Protocol):
    def readline(self) -> AnyStr_cov:
        ...
    


class WriteExcelBuffer(WriteBuffer[bytes], Protocol):
    def truncate(self, size: int | None = ...) -> int:
        ...
    


class ReadCsvBuffer(ReadBuffer[AnyStr_cov], Protocol):
    def __iter__(self) -> Iterator[AnyStr_cov]:
        ...
    
    def readline(self) -> AnyStr_cov:
        ...
    
    @property
    def closed(self) -> bool:
        ...
    


FilePath = Union[str, "PathLike[str]"]
StorageOptions = Optional[Dict[str, Any]]
CompressionDict = Dict[str, Any]
CompressionOptions = Optional[Union[Literal["infer", "gzip", "bz2", "zip", "xz", "zstd"], CompressionDict]]
XMLParsers = Literal["lxml", "etree"]
FormattersType = Union[List[Callable], Tuple[Callable, ...], Mapping[Union[str, int], Callable]]
ColspaceType = Mapping[Hashable, Union[str, int]]
FloatFormatType = Union[str, Callable, "EngFormatter"]
ColspaceArgType = Union[str, int, Sequence[Union[str, int]], Mapping[Hashable, Union[str, int]]]
FillnaOptions = Literal["backfill", "bfill", "ffill", "pad"]
Manager = Union["ArrayManager", "SingleArrayManager", "BlockManager", "SingleBlockManager"]
SingleManager = Union["SingleArrayManager", "SingleBlockManager"]
Manager2D = Union["ArrayManager", "BlockManager"]
ScalarIndexer = Union[int, np.integer]
SequenceIndexer = Union[slice, List[int], np.ndarray]
PositionalIndexer = Union[ScalarIndexer, SequenceIndexer]
PositionalIndexerTuple = Tuple[PositionalIndexer, PositionalIndexer]
PositionalIndexer2D = Union[PositionalIndexer, PositionalIndexerTuple]
if TYPE_CHECKING:
    TakeIndexer = Union[Sequence[int], Sequence[np.integer], npt.NDArray[np.integer]]
else:
    ...
WindowingRankType = Literal["average", "min", "max"]
CSVEngine = Literal["c", "python", "pyarrow", "python-fwf"]
