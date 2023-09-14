# {
#   "food_id": "1",
#   "amount": 5,
#   "deadline": "2017-07-21T17:32:28Z",
#   "expired_at": "2020-01-01T17:32:28Z"
# }
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
