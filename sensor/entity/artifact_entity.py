from dataclasses import dataclass

class DataIngestionArtifact:
    feature_store_file_path:str
    trai_file_path:str
    test_file_path:str


class DataValidationArtifiact:...
class DataTransformationArtifiact:...
class ModelTrainerArtifiact:...
class ModelEvaluationArtifiact:...
class ModelPusherArtifiact:...