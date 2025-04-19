from gevent.event import Event
import gevent

evt = Event()

def waiter():
    print("Waiting for the event...")
    evt.wait()  # Block until the event is set
    print("Event has been set!")

def setter():
    gevent.sleep(2)
    print("Setting the event.")
    evt.set()   # Trigger event

gevent.joinall([
    gevent.spawn(waiter),
    gevent.spawn(setter),
])

evt.clear() # Rest the event to unset state