register_dish_schema = {
    "type": "object",
    "properties": {
        "recipe_id": {"type": "string"},
    },
    "required": ["recipe_id"],
}

update_dish_schema = {
    "type": "object",
    "properties": {
        "recipe_id": {"type": "string"},
    },
    "required": ["recipe_id"],
}
