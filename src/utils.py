def hour_to_minutes(hour: str) -> int:
    """Converter a hora para minutos desde a meia-noite."""
    h, m = map(int, hour.split(":"))  # type:ignore
    return h * 60 + m
