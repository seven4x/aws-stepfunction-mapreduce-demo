
def handle_event(event, context):
    # do one subtask
    print(event)
    record = event['parcel']
    record["result"] = record["quantity"] * 2
    return event

