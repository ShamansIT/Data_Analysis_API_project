class ApiResourceManager:
    def __init__(self):
        self.base_urls = {
            'YTTD2015': 'https://data.cityofnewyork.us/resource/2yzn-sicd.csv',
            'YTTD2016': 'https://data.cityofnewyork.us/resource/uacg-pexx.csv',
            'YTTD2017': 'https://data.cityofnewyork.us/resource/biws-g3hs.csv',
            'YTTD2018': 'https://data.cityofnewyork.us/resource/t29m-gskq.csv',
            'YTTD2019': 'https://data.cityofnewyork.us/resource/2upf-qytp.csv',
            'YTTD2020': 'https://data.cityofnewyork.us/resource/kxp8-n2sj.csv',
            'YTTD2021': 'https://data.cityofnewyork.us/resource/m6nq-qud6.csv',
            'YTTD2022': 'https://data.cityofnewyork.us/resource/qp3b-zxtp.csv',
            'GTTD2015': 'https://data.cityofnewyork.us/resource/gi8d-wdg5.csv',
            'GTTD2016': 'https://data.cityofnewyork.us/resource/hvrh-b6nb.csv',
            'GTTD2017': 'https://data.cityofnewyork.us/resource/5gj9-2kzx.csv',
            'GTTD2018': 'https://data.cityofnewyork.us/resource/w7fs-fd9i.csv',
            'GTTD2019': 'https://data.cityofnewyork.us/resource/q5mz-t52e.csv',
            'GTTD2020': 'https://data.cityofnewyork.us/resource/pkmi-4kfn.csv',
            'GTTD2021': 'https://data.cityofnewyork.us/resource/djnb-wcxt.csv',
            'GTTD2022': 'https://data.cityofnewyork.us/resource/qp3b-zxtp.csv',
            'FTTD2015': 'https://data.cityofnewyork.us/resource/7dfh-3irt.csv',
            'FTTD2016': 'https://data.cityofnewyork.us/resource/yini-w76t.csv',
            'FTTD2017': 'https://data.cityofnewyork.us/resource/avz8-mqzz.csv',
            'FTTD2018': 'https://data.cityofnewyork.us/resource/am94-epxh.csv',
            'FTTD2019': 'https://data.cityofnewyork.us/resource/u6nh-b56h.csv',
            'FTTD2020': 'https://data.cityofnewyork.us/resource/m3yx-mvk4.csv',
            'FTTD2021': 'https://data.cityofnewyork.us/resource/a444-au9b.csv',
            'FTTD2022': 'https://data.cityofnewyork.us/resource/vgi6-tcdb.csv',
        }

    def api_resource(self, base_name):
        # Check if the base_name exists in the base_urls dictionary
        if base_name in self.base_urls:
            # Construct the API URL using the base URL and the year
            api_url = self.base_urls[base_name]
            return api_url
        else:
            return "Base name not found"
        