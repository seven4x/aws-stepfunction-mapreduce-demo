
def handle_event(event, context):
    print(event)
    record = event['parcel']
    record["result"] = record["quantity"] * 2
    return event

