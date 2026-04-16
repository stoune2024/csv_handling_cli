class AppError(Exception):
    """Базовое исключение."""


class FileReadError(AppError):
    """Вызывается когда CSV file не может быть обработан."""


class UnknownReportError(AppError):
    """Вызывается когда название отчета не зарегестрировано."""
