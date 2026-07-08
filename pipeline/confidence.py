def get_confidence(context):

    if len(context) > 1200:
        return 98

    elif len(context) > 800:
        return 94

    elif len(context) > 500:
        return 90

    return 80