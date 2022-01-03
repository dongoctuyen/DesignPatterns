from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self._observers = []
        self._subject_state = None

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self.notify()


class Observer:
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
