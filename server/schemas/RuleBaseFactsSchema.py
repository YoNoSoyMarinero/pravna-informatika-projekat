from marshmallow import Schema, fields, post_load

class RuleBaseFacts:
    def __init__(self, drug_posession: bool,
                       allowing_usage: bool,
                       marginalized_group: bool,
                       providing_logistics: bool,
                       drug_trafficking: bool,
                       smuggling: bool,
                       organized_group: bool,
                       article_52_violation: bool,
                       estimated_drug_price: float):
        
        self.drug_posession: str = 'yes' if drug_posession else 'no'
        self.allowing_usage: str = 'yes' if allowing_usage else 'no' 
        self.marginalized_group: str = 'yes' if marginalized_group else 'no'
        self.providing_logistics: str = 'yes' if providing_logistics else 'no'
        self.drug_trafficking: str = 'yes' if drug_trafficking else 'no'
        self.smuggling: str = 'yes' if smuggling else 'no'
        self.organized_group: str = 'yes' if organized_group else 'no'
        self.article_52_violation: str = 'yes' if article_52_violation else 'no'
        self.estimated_drug_price: int = estimated_drug_price


class RuleBaseFactsSchema(Schema):
    drug_posession: bool = fields.Bool(required=True)
    allowing_usage: bool = fields.Bool(required=True)
    providing_logistics: bool = fields.Bool(required=True)
    drug_trafficking: bool = fields.Bool(required=True)
    smuggling: bool = fields.Bool(required=True)
    organized_group: bool = fields.Bool(required=True)
    article_52_violation: bool = fields.Bool(required=True)
    marginalized_group: bool = fields.Bool(required=True)
    estimated_drug_price: int = fields.Int(required=True)

    @post_load()
    def create_rule_base_facts(self, data, **kwargs):
        return RuleBaseFacts(**data)