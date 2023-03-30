from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

USER = {
    "1000": {
        "user_name": "Peixe da terra",
        "user_email": "Peixe@gmail.com",
        "user_password": "123",
        "user_id": "1000",
        "user_status": 0,
        "timestamp": get_timestamp(),
    },
    "2000": {
        "user_name": "olucas cruz",
        "user_email": "olucas@gmail.com",
        "user_password": "123",
        "user_id": "2000",
        "user_status": 0,
        "timestamp": get_timestamp(),
    },
    "3000": {
        "user_name": "Farao do senegal",
        "user_email": "farao@gmail.com",
        "user_password": "123",
        "user_id": "3000",
        "user_status": 0,
        "timestamp": get_timestamp(),
    }
}



def read_all():
    return list(USER.values())

def login(user):
    user_email = user.get("user_email")
    user_password = user.get("user_password")
    for user in USER:
        if user_email == USER[user]["user_email"] and user_password in USER[user]["user_password"]:            
                USER[user]["user_status"] = 1
                return USER[user]["user_id"], 200
    
    abort(
        406,
        "Not exists",
    )

def logout(user_id):
    for user in USER:
        if user_id == USER[user]["user_id"]:
            user[user_id]["user_id"] = 0
            return user[user_id], 200
        
def create(user):
    user_id = user.get("user_id")
    user_name = user.get("user_name", "")

    if user_id and user_id not in USER:
        USER[user_id] = {
            "user_id": user_id,
            "user_name": user_name,
            "timestamp": get_timestamp(),
        }
        return USER[user_id], 201
    else:
        abort(
            406,
            f"User with last name {user_id} already exists",
        )


def read_one(user_id):
    if user_id in USER:
        return USER[user_id]
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )


def update(user_id, user):
    if user_id in USER:
        USER[user_id]["user_name"] = user.get("user_name", USER[user_id]["user_name"])
        USER[user_id]["timestamp"] = get_timestamp()
        return USER[user_id]
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )


def delete(user_id):
    if user_id in USER:
        del USER[user_id]
        return make_response(
            f"{user_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )