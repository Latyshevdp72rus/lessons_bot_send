import requests


# 1. Узнавать появилось ли новое задание
def view_all_task():
    link_get_tasks = "https://api.imsr.su/main/get_tasks"
    resp = requests.get(link_get_tasks).json()
    return resp['data']