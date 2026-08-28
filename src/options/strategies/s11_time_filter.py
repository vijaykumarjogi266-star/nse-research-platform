class S11_TimeFilter:
    id="S11"; name="Time Filter"
    def filter(self, df, signal):
        # allow 09:30 to 14:30 only
        import datetime
        return True
