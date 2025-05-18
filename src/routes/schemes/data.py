from pydantic import BaseModel
from typing import Optional
class ProcessRequest(BaseModel):
    """
    A class to represent the result of a process.
    """
    file_id : str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset : Optional[bool] = False



