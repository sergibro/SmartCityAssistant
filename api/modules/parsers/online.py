import time
from datetime import datetime
from requests import Session

class OnlineParser():
    URL = "https://uk.tgstat.com/posts/list"

    def __init__(self):
        self.s = Session()

    @staticmethod
    def form_data(search=""):
        data = {
        #     "sort": "",
        #     "sort_direction": "",
        #     "period": "prev_year",
        #     "category": "",
        #     "language": "english",
            "country": "ua",
            "search": search
        }
        return data

    def api_call(self, data, num_try=5):
        r = {"error": {"message": {"Unknown error"}}}
        for i in range(num_try):
            try:
                r = self.s.post(self.URL, data=data)
                if r.status_code == 200:
                    r = r.json()
                    break
            except Exception as e:
                if i == num_try - 1:
                    r = {"error": {"message": {str(e)}}}
                time.sleep(i)
        return r

    def get_top_posts(self, search_term="", top_n=5):
        data = OnlineParser.form_data(search_term)
        resp_list = self.api_call(data).get("items", [])
        res_list = []
        for p in resp_list[:top_n]:
            p = {
                "postTelegramUrl": p.get("postTelegramUrl", ""),
                "views": p.get("views", -1),
                "date": p.get("date", "")  # datetime.strptime("2018 " + p.get("date", ""), "%Y %d %b, %H:%M")
            }
            res_list.append(p)
        return res_list
