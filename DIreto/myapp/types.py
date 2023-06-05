from typing import Optional, Any, Union


Error = Optional[str]
Data = Optional[Union[Any,list[Any],dict[str,Any]]]


Response = tuple[Data,Error]