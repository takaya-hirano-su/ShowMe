register_user_food_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "food_id": {"type": "string"},
        "amount": {"type": "number"},
        "deadline": {"type": "string"},
        "expired_at": {"type": "string"},
    },
    "required": ["name", "food_id", "amount", "deadline", "expired_at"],
}

update_user_food_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "food_id": {"type": "string"},
        "amount": {"type": "number"},
        "deadline": {"type": "string"},
        "expired_at": {"type": "string"},
    },
    "required": ["name", "food_id", "amount", "deadline", "expired_at"],
}
