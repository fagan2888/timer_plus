class Timer(timeit.Timer):

    def autorange(self, callback=None):
        """Return the number of loops and time taken so that total time >= 0.2.
        Calls the timeit method with *number* set to successive powers of
        ten (10, 100, 1000, ...) up to a maximum of one billion, until
        the time taken is at least 0.2 second, or the maximum is reached.
        Returns ``(number, time_taken)``.
        If *callback* is given and is not None, it will be called after
        each trial with two arguments: ``callback(number, time_taken)``.
        """
        for i in range(1, 10):
            number = 10**i
            time_taken = self.timeit(number)
            if callback:
                callback(number, time_taken)
            if time_taken >= 0.1:
                break
        return (number, time_taken)

    def repeat_autorange(self, repeats=7):
        self.storage = []
        for i in range(repeats):
            n, t = self.autorange()
            self.storage.append(t/n)
        return self.storage

    @property
    def statistics(self):
        if self.storage:
            return pd.Series(self.storage).describe()