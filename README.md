# slicetime
Create time and datetime objects using slice notation.

Importing slicettime overrides the standard library datetime objects
so be sure to place it before actually using datetime. Otherwise, continue
to use `date`, `datetime`, and `time` as before. But when you need an instance
with a new time, use the digital clock notation to create it
`[hh:mm:ss.mmmmmm]`

When the `time` class is called with this new notation, a new time instance
is created and returned. When an existing either `date` or `datetime` is
called with this new notation, a new `datetime` instance is returned that
has the same date as the original instance, but the time specified in the
slice.

### Example
```python
import datetime
import slicetime

new_time = datetime.time[12:30:5.55]
assert new_time.hour == 12
assert new_time.minute == 30
assert new_time.second == 5
assert new_time.microsecond == 55
```
