from __future__ import annotations

import os
import abc
from srutil import util
from typing import AnyStr, Optional

from . import sipherutil as su


class Sipher:

    @staticmethod
    def _get_data_from_file(file: os.PathLike[AnyStr], mode='r'):
        path = file.__str__().replace("\\", "/")
        file_name = os.path.basename(path)
        data_path = path.replace(util.stringbuilder('/', file_name), "")
        data = su.retrieve(path=data_path, file_name=file_name, mode=mode)
        return data

    @abc.abstractmethod
    def encrypt(self, data: AnyStr | os.PathLike[AnyStr], key=None, copy_to_clipboard: bool = False,
                store: bool = False, store_path: Optional[str] = None):
        pass

    @abc.abstractmethod
    def decrypt(self, data: AnyStr | os.PathLike[AnyStr], key=None, copy_to_clipboard: bool = False,
                store: bool = False, store_path: Optional[str] = None):
        pass
