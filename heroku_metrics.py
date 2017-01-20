import os

import conf


url_templ = 'https://dashboard.heroku.com/apps/{}/metrics/{}?starting=24-hours-ago'

for app_name in conf.app_names:
  for worker_name in conf.worker_names:
    os.system('open {}'.format(url_templ.format(app_name, worker_name)))
