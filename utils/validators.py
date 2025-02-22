from core.constants import Constants
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_file_size(value):
    """
    Validator function to check the file size limit.
    """
    filesize = value.size
    print("file_size", filesize)
    if filesize > Constants.MAX_FILE_SIZE:
        raise ValidationError("You cannot upload file more than 2Mb")
    else:
        return value

def validate_25MB_file_size(value):
    """
    Validator function to check the file size limit.
    """
    filesize = value.size
    print("file_size", filesize)
    if filesize > Constants.FILE_25MB_SIZE:
        raise ValidationError("You cannot upload file more than 25Mb")
    else:
        return value

def validate_image_type(file):
    """
    Validator function to check check for image types
    """
    file_extension = str(file).split(".")[-1]
    # if file_type not in settings.IMAGE_TYPES_ALLOWED and file_extension not in settings.IMAGE_TYPES_ALLOWED:
    if file_extension not in settings.IMAGE_TYPES_ALLOWED:
        raise ValidationError(
            "Image type not supported. Image type allowed: png, jpg, jpeg"
        )
    return file_extension


def validate_document_type(file):
    """
    Validator function to check check for document types
    """
    file_extension = str(file).split(".")[-1]
    # if file_type not in settings.FILE_TYPES_ALLOWED and file_extension not in settings.FILE_TYPES_ALLOWED:
    if file_extension not in settings.FILE_TYPES_ALLOWED:
        raise ValidationError(
            "Document type not supported. Document type allowed: pdf, doc, docx"
        )
    return file


def validate_dataset_type(file, extensions):
    """
    Validator function to check check for dataset types

    """
    file_extension = str(file).split(".")[-1]
    if file_extension not in extensions:
        return False
    return True


def validate_dataset_size(file, size):
    """
    Validator function to check check for dataset types

    """
    if file.size > size * 1024 * 1024:
        return False
    return True
