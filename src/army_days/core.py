from datetime import datetime

from .models import ComputedEventModel, DaysModel


def compute_results(days: DaysModel) -> list[ComputedEventModel]:
    results = []
    now = datetime.now()
    current = datetime(now.year, now.month, now.day)
    for entry in days.entries:
        tmp_date = entry.date.astimezone()  # force it to local time
        event_date = datetime(tmp_date.year, tmp_date.month, tmp_date.day)
        time_delta = (event_date - current).days
        new_computed_event = ComputedEventModel(title=entry.title, date=tmp_date, days=time_delta)
        if time_delta > 0 and days.config.use_army_butt_days and now.hour >= 12:
            new_computed_event.days -= 0.5
        if time_delta >= 0 or days.config.show_completed:
            results.append(new_computed_event)
    results.sort(key=lambda x: x.date)
    return results
