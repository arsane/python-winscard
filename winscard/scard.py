from ctypes import *
from ctypes.wintypes import *
from winscard import *


class SCard:
    context = SCARDCONTEXT()
    card = SCARDHANDLE()
    dwAutoAllocate = DWORD(-1)

    def __init__(self, dwScope=SCARD_SCOPE_USER, pvReserved1=None, pvReserved2=None):
        result = ULONG(scard_dll.SCardEstablishContext(dwScope, pvReserved1, pvReserved2, pointer(self.context)))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)

    def list_readers(self, mszGroups=None):
        _pstrReaders = POINTER(c_char)()
        result = ULONG(scard_dll.SCardListReadersA(self.context, mszGroups, pointer(_pstrReaders), pointer(self.dwAutoAllocate)))
        if not result.value == SCARD_S_SUCCESS:
            raise WinSCardError(result.value)
        self.reader_names = []
        # parse returned string array.
        start = 0
        cur   = 0
        while 1:
            if _pstrReaders[cur] == '\0':
                self.reader_names.append(_pstrReaders[start:cur])
                if _pstrReaders[cur+1] == '\0':
                    break
                start = cur + 1
            cur += 1
        # create reader instances.
        readers = [Reader(LPSTR(x), self.card, self.context) for x in self.reader_names]
        return readers
