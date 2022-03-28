import datetime

import pytest
import pytest_cases

import slicetime


today = datetime.date.today()


slice_hour, time_hour = pytest_cases.param_fixtures(
    'slice_hour,time_hour', [
        (None, 0),
        (0, 0),
        (1, 1),
        (13, 13),
        (23, 23),
    ]
)


slice_minute, time_minute = pytest_cases.param_fixtures(
    'slice_minute,time_minute', [
        (None, 0),
        (0, 0),
        (1, 1),
        (30, 30),
        (59, 59),
    ]
)


slice_second, time_second, time_microsecond = pytest_cases.param_fixtures(
    'slice_second,time_second,time_microsecond', [
        (None, 0, 0),
        (0, 0, 0),
        (1, 1, 0),
        (15, 15, 0),
        (59, 59, 0),
        (0.001, 0, 1000),
        (1.0005, 1, 500),
        (5.00000001, 5, 0),
        (59.999999, 59, 999999),
    ]
)


@pytest.mark.parametrize(
    'date', [
        datetime.date.today(),
        datetime.datetime.today(),
        datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-8))),
    ]
)
def test_slice_date(slice_hour, time_hour, slice_minute, time_minute, slice_second, time_second, time_microsecond, date):
    assert date[slice(slice_hour, slice_minute, slice_second)] == datetime.datetime(date.year, date.month, date.day, time_hour, time_minute, time_second, time_microsecond)


def test_slice_time(slice_hour, time_hour, slice_minute, time_minute, slice_second, time_second, time_microsecond):
    assert datetime.time[slice(slice_hour, slice_minute, slice_second)] == datetime.time(time_hour, time_minute, time_second, time_microsecond)


@pytest.mark.parametrize(
    'slice,call', [
        (datetime.time[1:1:1], datetime.time(1, 1, 1)),
        (datetime.time[:1:1], datetime.time(0, 1, 1)),
        (datetime.time[1::1], datetime.time(1, 0, 1)),
        (datetime.time[1:1:], datetime.time(1, 1, 0)),
        (datetime.time[1::], datetime.time(1, 0, 0)),
        (datetime.time[:1:], datetime.time(0, 1, 0)),
        (datetime.time[::1], datetime.time(0, 0, 1)),
        (datetime.time[::], datetime.time(0, 0, 0)),
        (datetime.time[1:1], datetime.time(1, 1, 0)),
        (datetime.time[1:], datetime.time(1, 0, 0)),
        (datetime.time[:1], datetime.time(0, 1, 0)),
        (datetime.time[:], datetime.time(0, 0, 0)),
        (datetime.time[1], datetime.time(1, 0, 0)),
    ]
)
def test_slice_literal(slice, call):
    assert slice == call
