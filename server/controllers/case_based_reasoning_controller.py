from schemas.CaseBaseFactsSchema import CaseBaseFacts
from services.case_based_reasoning_service import CaseBasedReasoningService
import numpy as np

class CaseBasedReasoningController:

    def __init__(self, facts: CaseBaseFacts) -> None:
        self.facts: CaseBaseFacts = facts
        self.case_based_reasoning_service = CaseBasedReasoningService()
    

    def get_most_similar_cases(self):
        vectorized_facts: np.array = self.facts.get_vectorized_case()
        return self.case_based_reasoning_service.get_most_similar_cases(vectorized_facts)