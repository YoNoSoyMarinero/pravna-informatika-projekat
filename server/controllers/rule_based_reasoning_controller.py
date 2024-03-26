from schemas.RuleBaseFactsSchema import RuleBaseFacts
from services.rule_based_reasoning_service import RuleBaseReasoningService

class RuleBasedReasoningController:

    def __init__(self, rule_base_facts: RuleBaseFacts) -> None:
        self.rule_base_facts: RuleBaseFacts = rule_base_facts

    def get_judgment(self) -> dict:
        rule_base_service: RuleBaseReasoningService = RuleBaseReasoningService(self.rule_base_facts)
        return rule_base_service.reason()