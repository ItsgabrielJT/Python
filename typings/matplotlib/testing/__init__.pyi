"""
This type stub file was generated by pyright.
"""

import locale
import logging
import os
import subprocess
import sys
import matplotlib as mpl
from pathlib import Path
from tempfile import TemporaryDirectory
from matplotlib import _api

"""
Helper functions for testing.
"""
_log = ...
def set_font_settings_for_testing(): # -> None:
    ...

def set_reproducibility_for_testing(): # -> None:
    ...

def setup(): # -> None:
    ...

def subprocess_run_helper(func, *args, timeout, **extra_env): # -> CompletedProcess[str]:
    """
    Run a function in a sub-process

    Parameters
    ----------
    func : function
        The function to be run.  It must be in a module that is importable.

    *args : str
        Any additional command line arguments to be passed in
        the first argument to subprocess.run

    **extra_env : Dict[str, str]
        Any additional envromental variables to be set for
        the subprocess.

    """
    ...
