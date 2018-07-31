from io import BufferedReader, BytesIO, TextIOWrapper
from django.core.files.base import ContentFile
from django.core.serializers.json import DjangoJSONEncoder
from tempfile import _TemporaryFileWrapper
from typing import Dict, List, Optional, Tuple, Type, Union

class FileResponse:
    def __init__(self, *args, as_attachment=..., filename=..., **kwargs) -> None: ...
    def _set_streaming_content(
        self, value: Union[_TemporaryFileWrapper, BufferedReader, ContentFile]
    ) -> None: ...
    def set_headers(
        self, filelike: Union[_TemporaryFileWrapper, BufferedReader, BytesIO]
    ) -> None: ...

class HttpResponse:
    def __init__(
        self, content: Union[int, TextIOWrapper, bytes, str] = ..., *args, **kwargs
    ) -> None: ...
    def __repr__(self) -> str: ...
    def getvalue(self) -> bytes: ...
    def writable(self) -> bool: ...
    def write(self, content: Union[str, bytes]) -> None: ...
    def writelines(self, lines: List[str]) -> None: ...

class HttpResponseBase:
    def __delitem__(self, header: str) -> None: ...
    def __getitem__(self, header: str) -> str: ...
    def __init__(
        self,
        content_type: Optional[str] = ...,
        status: Optional[Union[str, int]] = ...,
        reason: Optional[str] = ...,
        charset: Optional[str] = ...,
    ) -> None: ...
    def __setitem__(
        self, header: Union[str, bytes], value: Union[str, bytes, int]
    ) -> None: ...
    @property
    def _content_type_for_repr(self) -> str: ...
    def _convert_to_charset(
        self, value: Union[str, int], charset: str, mime_encode: bool = ...
    ) -> str: ...
    def close(self) -> None: ...
    def delete_cookie(
        self, key: str, path: str = ..., domain: Optional[str] = ...
    ) -> None: ...
    def get(
        self, header: str, alternate: Optional[Union[str, Tuple]] = ...
    ) -> Optional[Union[str, Tuple]]: ...
    def has_header(self, header: str) -> bool: ...
    def make_bytes(self, value: Union[bytes, int, str]) -> bytes: ...
    def seekable(self) -> bool: ...
    def serialize_headers(self) -> bytes: ...
    def set_cookie(
        self,
        key: str,
        value: str = ...,
        max_age: Optional[int] = ...,
        expires: Optional[str] = ...,
        path: str = ...,
        domain: Optional[str] = ...,
        secure: Optional[bool] = ...,
        httponly: bool = ...,
        samesite: Optional[str] = ...,
    ) -> None: ...
    def set_signed_cookie(
        self, key: str, value: str, salt: str = ..., **kwargs
    ) -> None: ...
    def setdefault(self, key: str, value: str) -> None: ...
    def tell(self): ...
    def write(self, content: str): ...
    def writelines(self, lines: List[str]): ...

class HttpResponseNotAllowed:
    def __init__(self, permitted_methods: List[str], *args, **kwargs) -> None: ...
    def __repr__(self) -> str: ...

class HttpResponseNotModified:
    def __init__(self, *args, **kwargs) -> None: ...

class HttpResponseRedirectBase:
    def __init__(self, redirect_to: str, *args, **kwargs) -> None: ...
    def __repr__(self) -> str: ...

class JsonResponse:
    def __init__(
        self,
        data: Dict[str, Union[Dict[str, bool], str, Dict[str, str], List[Dict[str, str]]]],
        encoder: Type[DjangoJSONEncoder] = ...,
        safe: bool = ...,
        json_dumps_params: None = ...,
        **kwargs,
    ) -> None: ...

class StreamingHttpResponse:
    def __init__(
        self,
        streaming_content: Union[
            _TemporaryFileWrapper, BufferedReader, str, List[str]
        ] = ...,
        *args,
        **kwargs,
    ) -> None: ...
    def __iter__(self) -> map: ...
    def _set_streaming_content(
        self, value: Union[TextIOWrapper, str, List[str], List[bytes]]
    ) -> None: ...
    @property
    def content(self): ...