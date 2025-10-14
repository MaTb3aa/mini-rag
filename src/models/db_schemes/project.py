from pydantic import BaseModel,Field,validator
from typing import Optional
from bson.objectid import objectId

class Project(BaseModel):
    _id: Optional[objectId]
    project_id: Field(...,min_length=1)
    
    @validator('project_id')
    def validate_project_id(cls,value):
        if not value.islnum():
            raise ValueError('project_id must be alphanumeric')
        return value

    class Config:
        """ ignore any wired data"""
        arbitrary_types_allowed = True
    


        

