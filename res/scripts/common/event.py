# 2016.08.04 19:55:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Event.py
from debug_utils import LOG_CURRENT_EXCEPTION

class Event(object):
    """
    Allows delegates to subscribe for the event and to be called when event
    is triggered.
    
    Clearing events without event manager:
        onEvent1 = Event()
        onEvent2 = Event()
        ...
        onEvent1.clear()
        onEvent2.clear()
    
    Clearing events with event manager:
        em = EventManager()
        onEvent1 = Event(em)
        onEvent2 = Event(em)
        ...
        em.clear()
    """

    def __init__(self, manager = None):
        """
        :param manager - event manager that is used to clear all events thereby
        break all references.
        """
        self.__delegates = []
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, *args, **kwargs):
        for delegate in self.__delegates[:]:
            try:
                delegate(*args, **kwargs)
            except:
                LOG_CURRENT_EXCEPTION()

    def __iadd__(self, delegate):
        if delegate not in self.__delegates:
            self.__delegates.append(delegate)
        return self

    def __isub__(self, delegate):
        if delegate in self.__delegates:
            self.__delegates.remove(delegate)
        return self

    def clear(self):
        del self.__delegates[:]

    def __repr__(self):
        return 'Event(%s):%s' % (len(self.__delegates), repr(self.__delegates))


class Handler(object):
    """
    Similar to Event. Difference is Handler allows only one delegate to be
    subscribed. One event manager could be used both for handlers and events.
    """

    def __init__(self, manager = None):
        """
        :param manager - event manager that is used to clear all handlers
        thereby break all references.
        """
        self.__delegate = None
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, *args, **kwargs):
        if self.__delegate is not None:
            return self.__delegate(*args, **kwargs)
        else:
            return

    def set(self, delegate):
        self.__delegate = delegate

    def clear(self):
        self.__delegate = None
        return


class EventManager(object):
    """
    Event manager that is used to clear all events thereby break all references.
    """

    def __init__(self):
        self.__events = []

    def register(self, event):
        self.__events.append(event)

    def clear(self):
        for event in self.__events:
            event.clear()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\event.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:55:16 St�edn� Evropa (letn� �as)
