from datetime import datetime
from library_enums import LibraryEnums


# TODO: Add docstrings to all methods
# TODO: Add type hinting to properties and return values of methods

class Item(object):
    def __init__(self):
        self._title = ""
        self._location = ""
        self._status = LibraryEnums.CHECKED_IN
        self.type = LibraryEnums.UNKNOWN
        self._last_checked_out = None
        self._last_checked_in = datetime.now()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # TODO: add type casting to make sure the value becomes a string before assigning _title
        # TODO: add improper symbol check (#, /, -, %, ...)
        self._title = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        # TODO: add location validation and formatting checks
        ...

    @property
    def last_checked_out(self):
        return self._last_checked_out

    @property
    def last_checked_in(self):
        return self._last_checked_in

    def check_in(self):
        # TODO: change status to CHECKED_IN if status is CHECKED_OUT, otherwise don't change
        ...

    def check_out(self):
        # TODO: change status to CHECKED_OUT if status is CHECKED_IN, otherwise, show an error message don't raise and exception though
        ...