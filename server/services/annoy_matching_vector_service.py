from annoy import AnnoyIndex
import numpy as np

class AnnoyMatchingVectorService:

    def __init__(self, vector_dimension: int, vectors: np.array) -> None:
        self.vector_dimension = vector_dimension
        self.annoy_index = AnnoyIndex(vector_dimension, 'angular')
        self.vectors = vectors
        self.__create_database()

    def __create_database(self):
        for i, vector in enumerate(self.vectors):
            self.annoy_index.add_item(i, vector)
        self.annoy_index.build(n_trees=10)

    def __distance_to_similarity(self, distance):
        return 1 / (1 + distance)  

    def get_most_similar_vectors(self, vector: np.array):
        similar_indices_with_distances = self.annoy_index.get_nns_by_vector(vector, 3, include_distances=True)
        return [(index, self.__distance_to_similarity(distance)) for index, distance in zip(*similar_indices_with_distances)] 