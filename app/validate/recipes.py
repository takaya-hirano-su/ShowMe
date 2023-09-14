register_recipe_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "thumbnail_url": {"type": "string"},
        "recipe_category_id": {"type": "string"},
        "description": {"type": "string"},
        "is_public": {"type": "boolean"},
        "is_draft": {"type": "boolean"},
        "foods": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "food_id": {"type": "string"},
                    "amount": {"type": "number"},
                },
                "required": ["food_id", "amount"],
            },
        },
    },
    "required": [
        "title",
        "recipe_category_id",
        "description",
        "is_public",
        "is_draft",
        "foods",
    ],
}

update_recipe_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "thumbnail_url": {"type": "string"},
        "recipe_category_id": {"type": "string"},
        "description": {"type": "string"},
        "is_public": {"type": "boolean"},
    },
}
