import time
from datetime import datetime
from requests import Session
from modules.parsers.utils import *

index_name = es_config['INDEX_NAME']

class OnlineParser():
    def __init__(self):
        self.s = Session()

    def api_call(self, data, num_try=5):
        r = {"error": {"message": {"Unknown error"}}}
        for i in range(num_try):
            try:
                r = self.s.post(TGSTATS_POSTS_URL, data=data)
                if r.status_code == 200:
                    r = r.json()
                    break
            except Exception as e:
                if i == num_try - 1:
                    r = {"error": {"message": {str(e)}}}
                time.sleep(i)
        return r

    def get_top_posts(self, search_term="", top_n=5):
        data = form_data(search_term)
        resp_list = self.api_call(data).get("items", [])
        res_list = []
        for p in resp_list:
            p = transform_post_info(p)
            res_list.append(p)
        es_helpers.bulk(es, [{
            "_index": index_name,
            "_type": "doc",
            "_id": p.pop("id"),
            "body": p
            } for p in res_list])
        for p in res_list[:top_n]:
            pass
        return res_list
