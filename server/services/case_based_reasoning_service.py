from repository.CaseRepository import CaseRepository
from services.annoy_matching_vector_service import AnnoyMatchingVectorService
import numpy as np


class CaseBasedReasoningService:

    def __init__(self) -> None:
        self.case_repository: CaseRepository = CaseRepository()
        self.cases = self.case_repository.get_vectorized_cases()
        self.cases_ids = self.cases[:, 0]
        self.cases_facts = self.cases[:, 1:-1]
        self.cases_punishments = self.cases[:, -1]

    def get_most_similar_cases(self, vector):
        annoy_matching_vector_service: AnnoyMatchingVectorService = AnnoyMatchingVectorService(self.cases_facts.shape[1], self.cases_facts)
        similar_cases: list = annoy_matching_vector_service.get_most_similar_vectors(vector)
        return {'similar_cases': [{'case_id': self.cases_ids[el[0]],
                                         'case_punishments': self.cases_punishments[el[0]],
                                         'case_similarity': el[1]} for el in similar_cases]}