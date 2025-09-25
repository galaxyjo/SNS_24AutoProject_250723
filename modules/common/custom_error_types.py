class FFIError(Exception):
    """Custom exception for FFI-related errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"FFIError: {self.message}"
