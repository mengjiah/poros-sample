"""
    Create a python class that represents a calendar day

    A calendar day consists of:

            day (1-31)
            month (1-12)
            year
            a list of events

    A calendar day provides the following functionality:

            scheduling a new event
            return a string representation of this day

"""

import event
import logging

class Day:
    """A calendar day and its events."""

    def __init__(self, day, month, year):
        """ (Day, int, str, int) -> NoneType

        Initialize a day on the calendar with day, month and year,
        and no events.

        >>> d = Day(30, 'March', 2016)
        >>> d.day
        30
        >>> d.month
        'March'
        >>> d.year
        2016
        >>> d.events
        []
        """

        self.day = day
        self.month = month
        self.year = year
        self.events = []

        logging.info("New day instance created!")

    def schedule_event(self, new_event):
        """ (Day, Event) -> bool

        Schedule new_event on this day if it does not overlap with existing events.

        Return True if it was possible to schedule the event, and False otherwise.

        >>> d = Day(1, 'April', 2016)
        >>> e = event.Event(11, 13, 'Meeting')
        >>> d.schedule_event(e)
        True
        >>> d.events[0] == e
        True
        >>> e2 = event.Event(11, 12, 'Lunch')
        >>> d.schedule_event(e2)
        False
        >>> len(d.events) == 1
        True
        """

        for e in self.events:
            if e.overlaps(new_event):
                logging.warning("Overlapping events found: {} overlaps with {}".format(new_event,e))
                return False

        self.events.append(new_event)

        return True

    def __str__(self):
        """ (Day) -> str

        Return a string representation of this day.

        >>> d = Day(5, 'April', 2016)
        >>> d.schedule_event(event.Event(15, 16, 'Submit A3 work'))
        True
        >>> d.schedule_event(event.Event(16, 23, 'Celebrate!'))
        True
        >>> print(d)
        5 April 2016:
        - Submit A3 work: from 15 to 16
        - Celebrate!: from 16 to 23
        """

        result = "{0} {1} {2}:\n".format(self.day, self.month, self.year)
        for event in self.events:
            result = result + "- {0}\n".format(event)
        return result.strip()


if __name__ == '__main__':
    import doctest  
    doctest.testmod()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create 14 April 2016.
    day = Day(14, 'April', 2016)

    # Add an event "Sleep in" from 0 to 11 on 14 April 2016.
    e1 = event.Event(0, 11, 'Sleep in')
    day.schedule_event(e1)

    # Add an event "Brunch with friends" from 11 to 13 on 14 April 2016.
    e2 = event.Event(11, 13, 'Brunch with friends')
    day.schedule_event(e2)

    # Add an event "Call Mom" from 12 to 13 on 14 April 2016.
    e3 = event.Event(12, 13, 'Call Mom')
    day.schedule_event(e3)

    # Print the day 14 April 2016, including its events.
    print(day)
