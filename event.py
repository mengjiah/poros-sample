"""
    Create a python class for storing calendar event data.

    An calendar event consists of:

            start_time
            end_time
            name

    An calendar event provides the following functionality:

            return its duration
            return a string representation of the event
            an equality function that determines if two events have the same name and times
            a function that determines if two events overlap in time

"""

import logging

class Event:
    """A new calendar event."""

    def __init__(self, start_time, end_time, event_name):
        """ (Event, int, int, str) -> NoneType

        Precondition: 0 <= start_time < end_time <= 23

        Initialize a new event that starts at start_time, ends at end_time,
        and is named name.

        >>> e = Event(12, 13, 'Lunch')
        >>> e.start_time
        12
        >>> e.end_time
        13
        >>> e.name
        'Lunch'
        """

        self.start_time = start_time
        self.end_time = end_time
        self.name = event_name

        logging.info("New event instance created!")

    def duration(self):
        """ (Event) -> int

        Return the duration of this event.

        >>> e = Event(10, 11, 'Lecture')
        >>> e.duration()
        1
        """

        return self.end_time - self.start_time

    def __str__(self):
        """ (Event) -> str

        Return a string representation of this event.

        >>> e = Event(6, 7, 'Run')
        >>> str(e)
        'Run: from 6 to 7'
        """

        return "{0}: from {1} to {2}".format(self.name, self.start_time,
                                             self.end_time)

    def __eq__(self, other):
        """ (Event, Event) -> bool

        Return True iff this event has the same start time, end time,
        and name as other.

        >>> e1 = Event(6, 7, 'Run')
        >>> e2 = Event(6, 7, 'Run')
        >>> e1 == e2
        True
        """

        return self.start_time == other.start_time and \
               self.end_time == other.end_time and self.name == other.name

    def overlaps(self, other):
        """ (Event, Event) -> bool

        Return True iff this event overlaps with event other.

        >>> e1 = Event(6, 7, 'Run')
        >>> e2 = Event(0, 7, 'Sleep')
        >>> e1.overlaps(e2)
        True
        """

        # self.start_time < other.end_time and other.start_time < self.end_time

        return self.start_time <= other.start_time < self.end_time or \
               other.start_time <= self.start_time < other.end_time


if __name__ == '__main__':
    import doctest

    doctest.testmod()


