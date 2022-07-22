def handle_event(event, context):
    print(event)
    # generate subtask
    jobs = [{"prod": "R31", "dest-code": 9511, "quantity": 1344},
            {"prod": "S39", "dest-code": 9511, "quantity": 40},
            {"prod": "R31", "dest-code": 9833, "quantity": 12},
            {"prod": "R40", "dest-code": 9860, "quantity": 887},
            {"prod": "R40", "dest-code": 9511, "quantity": 1220}]
    event["detail"]["jobs"] = jobs
    return event
