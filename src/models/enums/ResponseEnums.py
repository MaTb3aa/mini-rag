from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds limit"
    FILE_VALID = "File is valid"
    FILE_VALIDATION_FAILED = "File validation failed"
    FILE_UPLOADED = "File uploaded successfully"
    FILE_NOT_UPLOADED = "File not uploaded"
    FILE_NOT_FOUND = "File not found"
    FILE_DELETED = "File deleted successfully"
    FILE_NOT_DELETED = "File not deleted"
    FILE_NOT_SAVED = "File not saved"
    FILE_SAVED = "File saved successfully"
    PROCESSING_FAILED = "processing_failed"
    PROCESSING_SUCCESS = "processing_success"

    
