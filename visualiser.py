import soccerdata as sd

#soccerdata.WhoScored(leagues=None, seasons=None, proxy=None, no_cache=False, no_store=False, data_dir=PosixPath('/home/docs/soccerdata/data/WhoScored'), path_to_browser=None, headless=False)

ws = sd.WhoScored(leagues="ENG-Championship", seasons=2023-24)

events = ws.read_events(match_id=1731785)
events.head()
