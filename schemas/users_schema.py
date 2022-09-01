from voluptuous import Schema

users_list = Schema({
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [
        {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        }
    ],
    "support": {
        "url": str,
        "text": str
    }
})
