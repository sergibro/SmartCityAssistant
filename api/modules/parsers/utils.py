from elasticsearch import Elasticsearch
import elasticsearch.helpers as es_helpers
from modules.utils import config

es_config = config["ES"]

es = Elasticsearch(
    hosts=[{"host": es_config["HOST"], "port": es_config["PORT"]}],
    http_auth=(es_config["USERNAME"], es_config["PASSWORD"]),
    use_ssl=True,
)

TGSTATS_URL = "https://uk.tgstat.com"
TGSTATS_POSTS_URL = TGSTATS_URL + "/posts/list"



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

def transform_post_info(post):
    postTelegramUrl = p.pop("postTelegramUrl", "")
    channel = postTelegramUrl.split("tg://resolve?domain=")[-1]
    channel, post_num = channel.split("&post=")
    post_num = int(post_num)
    res_post = {
        "_id": p.get("id"),
        "title": p.get("title": ""),
        "postTelegramUrl": postTelegramUrl,
        "views": p.get("views", -1),
        "date": datetime.strptime("2018 " + p.get("date"), "%Y %d %b, %H:%M"),
        "channel": channel,
        "post_num": post_num,
        "forwards_count": int(p.get("forwards_count", 0)),
        "url": p.get("url", "")
    }
    return res_post
