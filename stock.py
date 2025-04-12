class Stock:
    def __init__(self, ticker: str, pct_change: float):
        self._ticker = ticker
        self._pct_change = pct_change

    # Getter for ticker
    @property
    def ticker(self) -> str:
        return self._ticker

    # Setter for ticker
    @ticker.setter
    def ticker(self, value: str):
        self._ticker = value

    # Getter for pct_change
    @property
    def pct_change(self) -> float:
        return self._pct_change

    # Setter for pct_change
    @pct_change.setter
    def pct_change(self, value: float):
        self._pct_change = value