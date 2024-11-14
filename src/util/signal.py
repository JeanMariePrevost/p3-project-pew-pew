class Signal:
    """
    "Event" class that can be used to emit signals to multiple listeners with priority.
    Essentially a simple implementation of the observer pattern with dynamic payloads.

    Example usage:
    my_signal = Signal()
    my_signal.add(my_function)
    my_signal.trigger("some payload")
    """

    def __init__(self):
        self.observers = []

    def add(self, target_function, priority=0):
        """
        Add a function to the list of observers.
        :param target_function: The function to call when the signal is triggered.
        :param priority: The order of execution, higher priority functions are called first.
        """
        if not callable(target_function):
            raise ValueError("target_function must be a callable function")
        if not isinstance(priority, int):
            raise ValueError("priority must be an integer")

        # Check if the function is already in observers
        for i, (p, func) in enumerate(self.observers):
            if func == target_function:
                # Update priority if function exists
                self.observers[i] = (priority, target_function)
                break
        else:
            # Add as a new entry if not already present
            self.observers.append((priority, target_function))

        # Sort on priority
        self.observers.sort(key=lambda x: x[0], reverse=True)

    def add_once(self, target_function, priority=0):
        """
        Add a function to the list of observers, but remove it after the first call.
        :param target_function: The function to call when the signal is triggered.
        :param priority: The order of execution, higher priority functions are called first.
        """

        # Define a wrapper that removes the target function after it's called
        def one_time_wrapper(*args, **kwargs):
            target_function(*args, **kwargs)
            self.remove(one_time_wrapper)  # Remove itself after the first call

        # Add the wrapper function instead of the original
        self.add(one_time_wrapper, priority)

    def remove(self, target_function):
        # Find and remove the function, preserving the sorted structure
        self.observers = [(priority, func) for priority, func in self.observers if func != target_function]

    def remove_all(self):
        self.observers.clear()

    def trigger(self, *args, **kwargs):
        """Trigger the signal, calling all observers in order of priority with the provided arguments."""
        for _, target_function in self.observers:
            target_function(*args, **kwargs)
