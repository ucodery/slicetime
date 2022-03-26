import datetime

import pytest

import slicetime


today = datetime.date.today()

@pytest.mark.parametrize(
    'dateslice,datetime', [
        (today[1:1:1], datetime.datetime.combine(today, datetime.time(1, 1, 1))),
        (today[:1:1], datetime.datetime.combine(today, datetime.time(0, 1, 1))),
        (today[1::1], datetime.datetime.combine(today, datetime.time(1, 0, 1))),
        (today[1:1:], datetime.datetime.combine(today, datetime.time(1, 1, 0))),
        (today[1::], datetime.datetime.combine(today, datetime.time(1, 0, 0))),
        (today[:1:], datetime.datetime.combine(today, datetime.time(0, 1, 0))),
        (today[::1], datetime.datetime.combine(today, datetime.time(0, 0, 1))),
        (today[::], datetime.datetime.combine(today, datetime.time(0, 0, 0))),
        (today[1:1], datetime.datetime.combine(today, datetime.time(1, 1, 0))),
        (today[1:], datetime.datetime.combine(today, datetime.time(1, 0, 0))),
        (today[:1], datetime.datetime.combine(today, datetime.time(0, 1, 0))),
        (today[:], datetime.datetime.combine(today, datetime.time(0, 0, 0))),
        (today[1], datetime.datetime.combine(today, datetime.time(1, 0, 0))),
    ]
)
def test_slice_literal(dateslice, datetime):
    assert dateslice == datetime

@pytest.mark.parametrize(
    'slice_hour,time_hour', [
        (None, 0),
        (0, 0),
        (1, 1),
        (13, 13),
        (23, 23),
    ]
)
@pytest.mark.parametrize(
    'slice_minute,time_minute', [
        (None, 0),
        (0, 0),
        (1, 1),
        (30, 30),
        (59, 59),
    ]
)
@pytest.mark.parametrize(
    'slice_second,time_second,time_microsecond', [
        (None, 0, 0),
        (0, 0, 0),
        (1, 1, 0),
        (15, 15, 0),
        (59, 59, 0),
        (0.001, 0, 1000),
        (1.0005, 1, 500),
        (7.999999, 7, 999999),
    ]
)
@pytest.mark.parametrize(
    'date', [
        datetime.date.today(),
        datetime.datetime.today(),
        datetime.datetime.now(),
    ]
)
def test_slice_func(slice_hour, time_hour, slice_minute, time_minute, slice_second, time_second, time_microsecond, date):
    assert date[slice(slice_hour, slice_minute, slice_second)] == datetime.datetime(date.year, date.month, date.day, time_hour, time_minute, time_second, time_microsecond)
