def create_pg_payload(name:str, x_position:float= 0.0, y_position:float= 0.0) -> json :
    return {
        "revision": {"version":0},
        "component": {
            "name": name,
            "position": {x_position, y_position}
        }
    }