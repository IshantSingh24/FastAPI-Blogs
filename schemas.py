from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    aurthor: str = Field(min_length= 1, max_length=590)

class PostCreate(PostBase):
    pass

class postresponse(PostBase):
    id: int
    date_posted: str
    model_config = ConfigDict(from_attributes=True)