"""
Class generatre connection reference api.
        
Author: Serhii Spitsyn
"""

class ApiResourceManager:
    def __init__(self):
        self.base_urls = {
            # Yellow Taxi
            'YTTD2009': 'https://data.cityofnewyork.us/resource/f9tw-8p66.csv',
            'YTTD2010': 'https://data.cityofnewyork.us/resource/74wj-s5ij.csv',
            'YTTD2011': 'https://data.cityofnewyork.us/resource/uwyp-dntv.csv',
            'YTTD2012': 'https://data.cityofnewyork.us/resource/kerk-3eby.csv',
            'YTTD2013': 'https://data.cityofnewyork.us/resource/t7ny-aygi.csv',
            'YTTD2014': 'https://data.cityofnewyork.us/resource/gkne-dk5s.csv',
            'YTTD2015': 'https://data.cityofnewyork.us/resource/2yzn-sicd.csv',
            'YTTD2016': 'https://data.cityofnewyork.us/resource/uacg-pexx.csv',
            'YTTD2017': 'https://data.cityofnewyork.us/resource/biws-g3hs.csv',
            'YTTD2018': 'https://data.cityofnewyork.us/resource/t29m-gskq.csv',
            'YTTD2019': 'https://data.cityofnewyork.us/resource/2upf-qytp.csv',
            'YTTD2020': 'https://data.cityofnewyork.us/resource/kxp8-n2sj.csv',
            'YTTD2021': 'https://data.cityofnewyork.us/resource/m6nq-qud6.csv',
            'YTTD2022': 'https://data.cityofnewyork.us/resource/qp3b-zxtp.csv',
            # Green Taxi
            'GTTD2013': 'https://data.cityofnewyork.us/resource/ghpb-fpea.csv',
            'GTTD2014': 'https://data.cityofnewyork.us/resource/2np7-5jsg.csv',
            'GTTD2015': 'https://data.cityofnewyork.us/resource/gi8d-wdg5.csv',
            'GTTD2016': 'https://data.cityofnewyork.us/resource/hvrh-b6nb.csv',
            'GTTD2017': 'https://data.cityofnewyork.us/resource/5gj9-2kzx.csv',
            'GTTD2018': 'https://data.cityofnewyork.us/resource/w7fs-fd9i.csv',
            'GTTD2019': 'https://data.cityofnewyork.us/resource/q5mz-t52e.csv',
            'GTTD2020': 'https://data.cityofnewyork.us/resource/pkmi-4kfn.csv',
            'GTTD2021': 'https://data.cityofnewyork.us/resource/djnb-wcxt.csv',
            'GTTD2022': 'https://data.cityofnewyork.us/resource/qp3b-zxtp.csv',

        }

    def api_resource(self, base_name):
        # Check if the base_name exists in the base_urls dictionary
        if base_name in self.base_urls:
            # Construct the API URL using the base URL and the year
            api_url = self.base_urls[base_name]
            return api_url
        else:
            return "Base name not found"
        