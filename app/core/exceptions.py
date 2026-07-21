class BaseAPIException(Exception):
    """Base class for all custom API exceptions."""

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code


class NotFoundException(BaseAPIException):
    def __init__(self, resource_name: str, resource_id: int | str):
        super().__init__(
            message=f"{resource_name} with ID/Identifier '{resource_id}' was not found.",
            status_code=404
        )


class DuplicateResourceException(BaseAPIException):
    def __init__(self, resource_name: str, field_name: str, field_value: str):
        super().__init__(
            message=f"{resource_name} with {field_name} '{field_value}' already exists.",
            status_code=409
        )
