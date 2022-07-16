import time


class Game:
    def __init__(self):
        self._reset = True
        self._on = True

    def setup(self):
        self._ref_speed = 0.15
        self._delta_speed = 0.1
        self.speed = self._ref_speed
        self._reset = False
        self._over = False

    def delay(self):
        try:
            time.sleep(self.speed)
        except ValueError as e:
            self.speed = self._ref_speed
            time.sleep(self.speed)

    def inc_tempo(self):
        self._speed += self._delta_speed

    def dec_tempo(self):
        self._speed -= self._delta_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, value):
        self._on = value

    @property
    def over(self):
        return self._over

    @over.setter
    def over(self, value):
        self._over = value

    @property
    def resetter(self):
        return self._reset

    def resetter_on(self):
        self._reset = True

    def resetter_off(self):
        self._reset = False

    def quit(self):
        self.on = False
