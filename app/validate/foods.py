register_food_schema = {
    "type": "object",
    "properties": {
        "food_category_id": {"type": "string"},
        "name": {"type": "string"},
        "icon_url": {"type": "string"},
        "deadline": {"type": "string", "format": "date-time"},
    },
    "required": ["food_category_id", "name", "icon_url", "deadline"],
}
