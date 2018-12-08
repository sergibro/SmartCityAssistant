from modules.parsers.utils import *

class OnlineParser(AtimicParser):
    def __init__(self):
        AtimicParser.__init__(self)

    def get_top_posts(self, search_term="", top_n=10):
        data = form_data(search_term)
        resp_list = self.api_call(data).get("items", [])
        res_list = []
        for p in resp_list:
            p = transform_post_info(p)
            res_list.append(p)
        es_helpers.bulk(es, [{**{
            "_index": INDEX_NAME,
            "_type": "doc",
            }, **p, **{'parsed_time': datetime.now()}} for p in res_list])
        # for p in res_list[:top_n]:
        #     pass
        res_list = res_list[:top_n]
        return res_list
