import bottle
import json
import cache
import backend

@bottle.route('/')
def index():
  html_file = bottle.static_file("index.html", root=".")
  return html_file

@bottle.route('/permits.js')
def data_file():
  data_file = bottle.static_file("permits.js", root=".")
  return data_file

@bottle.route('/scatter_plot')
def graphA():
   scatter_data = backend.some_scatter_data(cache.read_cache('cached_data.csv'))
   ret_val1 = json.dumps(scatter_data)
   return ret_val1

@bottle.route('/pie_chart')
def graphB():
   pie_data = backend.some_pie_data(cache.read_cache('cached_data.csv'))
   ret_val2 = json.dumps(pie_data)
   return ret_val2

@bottle.route('/line_graph')
def graphC():
   line_data = backend.some_line_data(cache.read_cache('cached_data.csv'))
   ret_val3 = json.dumps(line_data)
   return ret_val3

import os.path
def load_data( ):
    csv_file = 'cached_data.csv'
    if not os.path.isfile(csv_file):
       query_str = "?$limit=10000"
       url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
       data = cache.get_data(url)
       data = cache.minimize_dictionaries(data, ['tow_date', 'tow_description', 'police_district'])
       cache.write_cache(data, csv_file)

load_data()
bottle.run(host="0.0.0.0", port=8080, debug = True)