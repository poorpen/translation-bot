from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GetHistory:
    user_id: Optional[int]
