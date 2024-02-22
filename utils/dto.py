# Defining Data transfer objects
from typing import Optional
from ninja import Schema





class QueryParams(Schema):
    text: Optional[str] = None
    voice_id: Optional[str] = None
    chuck_size: Optional[int] = None
    # Add other parameters