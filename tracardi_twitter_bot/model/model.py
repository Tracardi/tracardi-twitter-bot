from pydantic import BaseModel
from tracardi.domain.entity import Entity


class TwitterCredentials(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str


class Config(BaseModel):
    source: Entity
    action: str
