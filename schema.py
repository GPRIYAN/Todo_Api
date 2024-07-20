from pydantic import BaseModel

class SubPageBase(BaseModel):
    heading : str
    description : str
    footer : str
    pg_no : int 
    pg_dim : float

class SubPagecreate(SubPageBase):
    pass

class Subpage(SubPageBase):
    id : int
    class Config:
        orm_mode = True 