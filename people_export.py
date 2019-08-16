# pip install mixpanel-api3
# python people_export.py

import config as app_conf
import datetime as datetime
import mixpanel_api

print(app_conf.credentials)

mixpanel = mixpanel_api.Mixpanel(app_conf.credentials['api_secret'])
date     = datetime.datetime.now().strftime('%Y-%m-d%--%H:%M:%s')

format   = "json"
filename = f'data/people/people-{date}.{format}'

mixpanel.export_people(filename, format=format)
