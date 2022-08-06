"""
This type stub file was generated by pyright.
"""

from enum import Enum
from pandas._libs.tslibs.offsets import BaseOffset

_attrname_to_abbrevs: dict[str, str]
_period_code_map: dict[str, int]
class PeriodDtypeBase:
    _dtype_code: int
    def __new__(cls, code: int):
        ...
    
    def freq_group_code(self) -> int:
        ...
    
    def date_offset(self) -> BaseOffset:
        ...
    
    @classmethod
    def from_date_offset(cls, offset: BaseOffset) -> PeriodDtypeBase:
        ...
    
    @property
    def resolution(self) -> Resolution:
        ...
    


class FreqGroup(Enum):
    FR_ANN: int
    FR_QTR: int
    FR_MTH: int
    FR_WK: int
    FR_BUS: int
    FR_DAY: int
    FR_HR: int
    FR_MIN: int
    FR_SEC: int
    FR_MS: int
    FR_US: int
    FR_NS: int
    FR_UND: int
    @staticmethod
    def get_freq_group(code: int) -> FreqGroup:
        ...
    


class Resolution(Enum):
    RESO_NS: int
    RESO_US: int
    RESO_MS: int
    RESO_SEC: int
    RESO_MIN: int
    RESO_HR: int
    RESO_DAY: int
    RESO_MTH: int
    RESO_QTR: int
    RESO_YR: int
    def __lt__(self, other: Resolution) -> bool:
        ...
    
    def __ge__(self, other: Resolution) -> bool:
        ...
    
    @property
    def freq_group(self) -> FreqGroup:
        ...
    
    @property
    def attrname(self) -> str:
        ...
    
    @classmethod
    def from_attrname(cls, attrname: str) -> Resolution:
        ...
    
    @classmethod
    def get_reso_from_freq(cls, freq: str) -> Resolution:
        ...
    


