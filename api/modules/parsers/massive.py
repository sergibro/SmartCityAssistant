from utils import *

class MassiveParser(AtimicParser):
    def __init__(self):
        AtimicParser.__init__(self)

    def by_word(self, word=""):
        for period in PERIOD_OPTIONS:
            data = form_data(word, period)
            resp_list = self.api_call(data).get("items", [])
            res_list = []
            for p in resp_list:
                p = transform_post_info(p, year="201" + ("8" if period != "prev_year" else "7"))
                res_list.append(p)
            es_helpers.bulk(es, [{**{
                "_index": INDEX_NAME,
                "_type": "doc",
                }, **p, **{'parsed_time': datetime.now()}} for p in res_list])
