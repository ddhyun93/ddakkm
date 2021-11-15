from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class NestedComment(CommentBase):
    id: int
    user_id: int
    nickname: str
    like_count: int = 0
    created_at: datetime
    is_delete: bool
    user_is_like: bool
    user_is_active: bool


class Comment(CommentBase):
    id: int
    user_id: int
    nickname: str
    like_count: int = 0
    created_at: datetime
    is_delete: bool
    user_is_like: bool
    user_is_active: bool
    nested_comment: Optional[List[NestedComment]]

    class Config:
        orm_mode = True
