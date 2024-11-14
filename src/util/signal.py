class Signal:
    """
    "Event" class that can be used to emit signals to multiple listeners.
    Essentially a simple implementation of the observer pattern.
    """

    def __init__(self):
        self.observers = set()

    def add(self, target_function):
        self.observers.add(target_function)

    def remove(self, target_function):
        if target_function in self.observers:
            self.observers.remove(target_function)
        else:
            print(f"Warning: Tried to remove {target_function} from signal, but it wasn't there.")

    def remove_all(self):
        self.observers.clear()

    def trigger(self, *args, **kwargs):
        # Iterate over a copy of the observers set to allow for removal of observers during iteration
        for target_function in self.observers.copy():
            target_function(*args, **kwargs)
