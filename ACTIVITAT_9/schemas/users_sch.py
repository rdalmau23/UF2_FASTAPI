def user_schema(user) -> dict:
    return {
        "id": user["id"],
        "name": user["name"],
        "surname": user["surname"]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]
