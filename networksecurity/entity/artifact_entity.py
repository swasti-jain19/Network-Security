"""
This code defines several artifact classes using Python's @dataclass decorator. 
These artifacts are used to store and pass structured outputs between different stages of a ML pipeline.
Using @dataclass simplifies class creation by automatically generating the constructor and __repr__ methods.
"""

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str