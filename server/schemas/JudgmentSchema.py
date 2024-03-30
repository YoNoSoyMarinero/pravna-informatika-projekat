from marshmallow import Schema, fields, post_load
import numpy as np

class Judgment:
    def __init__(self, court_name: str,
                       date: str,
                       title: str,
                       judgment_body: str,
                       conclusion: str):
        
        self.court_name: str = court_name
        self.date: str = date
        self.title: str = title
        self.judgment_body: str = judgment_body
        self.conclusion: int = conclusion


class JudgmentSchema(Schema):
    court_name: str = fields.String(required=True)
    date: str = fields.String(required=True)
    title: str = fields.String(required=True)
    judgment_body: str = fields.String(required=True)
    conclusion: str = fields.Str(required=True)

    @post_load()
    def create_judgment(self, data, **kwargs):
        return Judgment(**data)