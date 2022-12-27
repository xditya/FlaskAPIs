import pytz
from datetime import datetime


def get_date_and_time(timezone):
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezones = pytz.all_timezones
        return {
            "ok": "error",
            "error": "Unknown timezone",
            "available_timezones": timezones,
        }
    data = datetime.now(tz)
    date = data.strftime("%d-%m-%Y")
    time = data.strftime("%H:%M:%S")
    return {"ok": "true", "date": date, "time": time}


get_date_and_time("asia/kolkata")
