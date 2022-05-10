from pydantic import BaseModel, validator
# from datetime import datetime
# from dateutil import parser

class BaseEntity(BaseModel):
    pass
    # @validator('*')
    # def validate_datetime_type_var(cls, v):
    #     # if isinstance(v, datetime):
    #     #     print(type(v))
    #     #     print(parser.parse(v))
    #     #     return parser.parse(v)
    #     return v
