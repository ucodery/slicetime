import datetime as dt

def __getitem__(self, key):
    if isinstance(key, int):
        hours = key
        minutes = 0
        seconds = 0
        microseconds = 0
    elif isinstance(key, slice):
        # TODO: support __index__
        if not isinstance(key.start, (int, type(None))) or not isinstance(key.stop, (int, type(None))):
            raise TypeError("time slice start and stop must be an integer or None, not "
                            f"{type(key.start) if not isinstance(key.start, (int, type(None))) else type(key.stop)}")
        if not isinstance(key.step, (int, float, type(None))):
            raise TypeError("time slice step must be an integer, float, or None, not {type(key.step)}")
        hours = key.start if key.start is not None else 0
        minutes = key.stop if key.stop is not None else 0
        seconds = key.step if key.step is not None else 0
        if isinstance(seconds, float):
            microseconds = round(seconds % 1 * 1000000)
            seconds = int(seconds // 1)
        else:
            microseconds = 0
    else:
        raise TypeError(f"time indices must be integers or slices, not {type(key)}")

    time = dt.time(hours, minutes, seconds, microseconds)

    return dt.datetime.combine(self, time)

class date(dt.date):
    pass
date.__getitem__ = __getitem__

class datetime(dt.datetime):
    pass
datetime.__getitem__ = __getitem__

dt.date = date
dt.datetime = datetime
