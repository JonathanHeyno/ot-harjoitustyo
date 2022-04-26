class Human():
    """dummy algoritmi joka ei tee mitään kun vuorossa on ihmispelaaja
    """

    def __init__(self):
        self._diff = 0

    @property
    def difficulty(self):
        return self._diff

    @difficulty.setter
    def difficulty(self, difficulty):
        self._diff = difficulty
