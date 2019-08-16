# pip install mixpanel-api3
# python event_export.py

import config
import datetime
from mixpanel_api import Mixpanel

m    = Mixpanel(config.credentials['api_secret'])
date = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")

format   = 'csv'
filename = f'data/event/export_event-{date}.{format}'

print(filename)
m.export_events(filename, {'from_date':'2019-08-14','to_date':'2019-08-15'}, format=format)
