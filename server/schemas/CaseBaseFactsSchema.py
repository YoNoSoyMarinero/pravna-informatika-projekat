from marshmallow import Schema, fields, post_load
import numpy as np

class CaseBaseFacts:
    def __init__(self, convicted: bool,
                       self_usage: bool,
                       allowed_usage: bool,
                       marginalized_group: bool,
                       providing_logistics: bool,
                       married: bool,
                       smuggling: bool,
                       organized_group: bool,
                       trafficking: bool,
                       snitched: bool,
                       has_children: bool,
                       admited: bool,
                       great_amount_without_trafficking: bool,
                       small_amount_without_trafficking: bool,
                       amount_of_heroine: int,
                       amount_of_cocaine: int,
                       amount_of_marijuana: int):
        
        self.convicted: int = 1 if convicted else 0
        self.self_usage: int = 1 if self_usage else 0 
        self.marginalized_group: int = 1 if marginalized_group else 0
        self.providing_logistics: int = 1 if providing_logistics else 0
        self.married: int = 1 if married else 0
        self.smuggling: int = 1 if smuggling else 0
        self.allowed_usage: int = 1 if smuggling else 0
        self.organized_group: int = 1 if organized_group else 0
        self.trafficking: int = 1 if trafficking else 0
        self.snitched: int = 1 if snitched else 0
        self.admited: int = 1 if admited else 0
        self.great_amount_without_trafficking = 1 if great_amount_without_trafficking else 0
        self.small_amount_without_trafficking = 1 if small_amount_without_trafficking else 0
        self.has_children: int = 1 if has_children else 0
        self.amount_of_cocaine: int = amount_of_cocaine
        self.amount_of_heroine: int = amount_of_heroine
        self.amount_of_marijuana: int = amount_of_marijuana

    def get_vectorized_case(self):
        return np.array([
            self.convicted,
            self.amount_of_cocaine,
            self.amount_of_heroine,
            self.amount_of_marijuana,
            self.self_usage,
            self.smuggling,
            self.trafficking,
            self.allowed_usage,
            self.marginalized_group,
            self.providing_logistics,
            self.great_amount_without_trafficking,
            self.small_amount_without_trafficking,
            self.admited,
            self.married,
            self.has_children,
            self.snitched
        ])

class CaseBaseFactsSchema(Schema):
    convicted: bool = fields.Bool(required=True)
    self_usage: bool = fields.Bool(required=True)
    marginalized_group: bool = fields.Bool(required=True)
    providing_logistics: bool = fields.Bool(required=True)
    married: bool = fields.Bool(required=True)
    smuggling: bool = fields.Bool(required=True)
    organized_group: bool = fields.Bool(required=True)
    trafficking: bool = fields.Bool(required=True)
    snitched: bool = fields.Bool(required=True)
    admited: bool = fields.Bool(required=True)
    great_amount_without_trafficking: bool = fields.Bool(required=True)
    small_amount_without_trafficking: bool = fields.Bool(required=True)
    allowed_usage: bool = fields.Bool(required=True)
    has_children: bool = fields.Bool(required=True)
    amount_of_cocaine: int = fields.Int(required=True)
    amount_of_heroine: int = fields.Int(required=True)
    amount_of_marijuana: int = fields.Int(required=True)

    @post_load()
    def create_rule_base_facts(self, data, **kwargs):
        return CaseBaseFacts(**data)