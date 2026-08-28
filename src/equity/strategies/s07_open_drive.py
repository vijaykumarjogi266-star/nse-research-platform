class S07_OpenDrive:
    id="S07"; name="Open Drive"
    def signal(self, df):
        if len(df)<5: return 0
        o = df.iloc[-1].get('open', df.iloc[-1]['close'])
        c = df.iloc[-1]['close']
        return 1 if c>o*1.002 else -1 if c<o*0.998 else 0
