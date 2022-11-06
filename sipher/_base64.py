from __future__ import annotations

import os
import base64
from typing import AnyStr, Optional

from sipher._sipher import Sipher
from . import sipherutil as su


class Base64(Sipher):
    def __init__(self):
        self.__em = ''
        self.__dm = ''

    def encrypt(self, data: AnyStr | os.PathLike[AnyStr], key=None, copy_to_clipboard: bool = False,
                store: bool = False, store_path: Optional[str] = None):
        if isinstance(data, os.PathLike):
            data = self._get_data_from_file(data)
        base64_bytes = base64.b64encode(data.encode('ascii'))
        self.__em = base64_bytes.decode('ascii')
        if copy_to_clipboard is True:
            is_copied = su.copy_to_clipboard(self.__em)
            if is_copied:
                print("Encrypted message copied to clipboard.")
        if store is True:
            path = su.store(data=self.__em, path=store_path, alg=self.__class__.__name__.lower())
            if path.exists():
                print("Encrypted message stored in '" + path.__str__() + "'")
        return self.__em

    def decrypt(self, data: AnyStr | os.PathLike[AnyStr], key=None, copy_to_clipboard: bool = False,
                store: bool = False, store_path: Optional[str] = None):
        if isinstance(data, os.PathLike):
            data = self._get_data_from_file(data)
        data_bytes = base64.b64decode(data.encode('ascii'))
        self.__dm = data_bytes.decode('ascii')
        if copy_to_clipboard is True:
            is_copied = su.copy_to_clipboard(self.__dm)
            if is_copied:
                print("Decrypted message copied to clipboard.")
        if store is True:
            path = su.store(data=self.__dm, path=store_path, alg=self.__class__.__name__.lower())
            if path.exists():
                print("Decrypted message stored in '" + path.__str__() + "'")
        return self.__dm