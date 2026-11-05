"""SKU normalization."""


def normalize_sku(value: str) -> str:
    """Return an uppercase, whitespace-trimmed SKU for labels and lookup."""
    if not value or not value.strip():
        raise ValueError("SKU must not be blank")
    return value.strip().upper()
