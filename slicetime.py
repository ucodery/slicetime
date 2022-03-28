"""Create time and datetime objects using slice notation"""
import datetime as dt

__all__ = ["date", "datetime", "time"]

def _slice_to_time(clock):
    if isinstance(clock, int):
        hours = clock
        minutes = 0
        seconds = 0
        microseconds = 0
    elif isinstance(clock, slice):
        # TODO: support __index__
        if not isinstance(clock.start, (int, type(None))) or not isinstance(clock.stop, (int, type(None))):
            raise TypeError("time slice start and stop must be an integer or None, not "
                            f"{type(clock.start) if not isinstance(clock.start, (int, type(None))) else type(clock.stop)}")
        if not isinstance(clock.step, (int, float, type(None))):
            raise TypeError("time slice step must be an integer, float, or None, not {type(clock.step)}")
        hours = clock.start if clock.start is not None else 0
        minutes = clock.stop if clock.stop is not None else 0
        seconds = clock.step if clock.step is not None else 0
        if isinstance(seconds, float):
            microseconds = round(seconds % 1 * 1000000)
            seconds = int(seconds // 1)
        else:
            microseconds = 0
    else:
        raise TypeError(f"time indices must be integers or slices, not {type(clock)}")
    return dt.time(hours, minutes, seconds, microseconds)


class date(dt.date):
    def __getitem__(self, clock):
        time = _slice_to_time(clock)
        return dt.datetime.combine(self, time)

class datetime(dt.datetime):
    def __getitem__(self, clock):
        time = _slice_to_time(clock)
        return self.combine(self, time)

class time(dt.time):
    def __class_getitem__(cls, clock):
        return _slice_to_time(clock)

dt.date = date
dt.datetime = datetime
dt.time = time
