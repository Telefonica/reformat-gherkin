from typing import List, Optional

from attr import dataclass

from .comment import Comment
from .feature import Feature


@dataclass(slots=True)
class GherkinDocument:
    comments: List[Comment]
    feature: Optional[Feature] = None
