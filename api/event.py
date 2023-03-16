from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

EVENT = {
    "1111": {
        "event_title": "Carnaval 2",
        "event_id": "1111",
        "event_description": "pessoas, musica essas paradas",
        "user_id": "1000",
        "event_date": get_timestamp(),


    },
    "2222": {
        "event_title": "Game Awards",
        "event_id": "2222",
        "event_description": "pessoas, jogos essas paradas",
        "user_id": "2000",
        "event_date": get_timestamp(),

    },
    "3333": {
        "event_title": "Osca",
        "event_id": "3333",
        "event_description": "pessoas, filmes essas paradas",
        "user_id": "3000",
        "event_date": get_timestamp(),
    }
}

def read_all():
    return list(EVENT.values())


def create(event):
    event_id = event.get("event_id")
    event_title = event.get("event_title", "")
    event_description = event.get("event_title", "")
    event_date = event.get("event_title", "")
    user_id = event.get("event_title", "")

    


    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            "event_id": event_id,
            "event_title": event_title,
            "event_description":event_description,
            "event_date": event_date,
            "user_id": user_id,
            "timestamp": get_timestamp(),
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f"Event with last title {event_id} already exists",
        )


def read_one(event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(
            404, f"Person with ID {event_id} not found"
        )


def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_title"] = event.get("event_title", EVENT[event_id]["event_title"])

        EVENT[event_id]["event_description"] = event.get("event_description", 
                                                         EVENT[event_id]["event_description"])
        
        EVENT[event_id]["event_date"] = event.get("event_date", EVENT[event_id]["event_date"])
        
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )


def delete(event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )