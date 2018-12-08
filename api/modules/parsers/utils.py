import time
from datetime import datetime
from requests import Session
from elasticsearch import Elasticsearch
import elasticsearch.helpers as es_helpers
from modules.utils import config

es_config = config["ES"]

es = Elasticsearch(
    hosts=[{"host": es_config["HOST"], "port": es_config["PORT"]}],
    http_auth=(es_config["USERNAME"], es_config["PASSWORD"]),
    use_ssl=True,
)

INDEX_NAME = es_config['INDEX_NAME']

TGSTATS_URL = "https://uk.tgstat.com"
TGSTATS_POSTS_URL = TGSTATS_URL + "/posts/list"

PERIOD_OPTIONS = {
    "prev_year",
    "current_year",
    "prev_month",
    "current_month",
    "prev_week",
    "current_week",
    "7days",
    "yesterday2",
    "yesterday",  # default
    "today"
}
COUNTRY_OPTIONS = {
    "global"  # default (all)
    "ru",
    "ua",
#     todo
}
LANGUAGE_OPTIONS = {
    "global",  # default (all)
    "english",
#     todo
}
CATEGORY_OPTIONS = {  # default all
    "crypto",
    "adult",
    "music",
    "telegram"
    "tech",
    "education",
    "sales",
    "entertainment",
    "other",
    "business",
    "video",
    "gaming",
    "news",
    "sport",
    "language",
    "blogs",
    "economics",
    "books",
    "beauty",
    "quotes",
    "design",
    "marketing",
    "catalogs",
    "travels",
    "auto",
    "politics",
    "health",
    "food",
    "psychology",
    "lifehack",
    "animals",
    "career",
    "stickers",
    "handmade",
    "babies"
}
SORT_OPTIONS = {
    "views_count",  # default
    "ic_count",  # shared count for lifetime
    "date"
}
SORT_DIRECTION_OPTIONS = {
    "desc",  # default
    "asc"
}


class AtimicParser():
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


def form_data(search="", period="yesterday", country="ua",
    en=False, category="", sort="", sort_direction=""):
    data = {
        "search": search,
        "country": country,
        "period": period,
        "category": category,
        "sort": sort,
        "sort_direction": sort_direction
    }
    if en:
        data["language"] = "english"
    return data

def transform_post_info(post, year="2018"):
    postTelegramUrl = post.pop("postTelegramUrl", "")
    channel = postTelegramUrl.split("tg://resolve?domain=")[-1]
    channel, post_num = channel.split("&post=")
    post_num = int(post_num)
    res_post = {
        "_id": post.get("id"),
        "title": post.get("title", ""),
        "postTelegramUrl": postTelegramUrl,
        "views": post.get("views", -1),
        "date": datetime.strptime(year + " " + post.get("date"), "%Y %d %b, %H:%M"),
        "channel": channel,
        "post_num": post_num,
        "forwards_count": int(post.get("forwards_count", 0)),
        "url": post.get("url", "")
    }
    return res_post
