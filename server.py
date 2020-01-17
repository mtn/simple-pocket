import requests
import pandas as pd
import json
import pocket

import pdb

consumer_key = "89436-e402aa463514bd722869e257"
request_token = "a863f0dd-2575-8c2b-f61d-a0f17f"
access_token = "2854e845-912e-c21d-cd12-3f8480"

pocket_instance = pocket.Pocket(consumer_key, access_token)


def get_active_articles(pocket_instance):
    articles = pocket_instance.get()[0]["list"]
    return {
        articles[a]["resolved_title"]: articles[a]["resolved_url"] for a in articles
    }


def get_archived_articles(pocket_instance):
    articles = pocket_instance.get(state="archive")[0]["list"]
    return {
        articles[a]["resolved_title"]: articles[a]["resolved_url"] for a in articles
    }


articles = get_active_articles(pocket_instance)
archived = get_archived_articles(pocket_instance)
print(articles.keys())
print(archived.keys())
