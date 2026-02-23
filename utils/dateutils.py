from datetime import datetime, timedelta

# Get datetime as ISO 8601 timestamp
def getTimestamp(secondsBack):
    return (datetime.now() - timedelta(seconds=secondsBack)).astimezone().isoformat()

# Check whether timestamp conforms to ISO 8601 standard
def isValidISO8601(timestamp):
    try:
        datetime.fromisoformat(timestamp)
        return True
    except ValueError:
        return False