import requests


def send_code1(title: str, description: str, start_code: str, comment: str):
    send_link = "https://api.imsr.su/add_request"
    headr = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome / '
                           '96.0.4664.174 YaBrowser / 22.1.4.837 Yowser / 2.5 Safari / 537.36'}
    big_data = {'title': title, 'description': description, 'start_code':start_code, 'comment': comment}
    sess = requests.session()
    if sess.post(send_link, headers=headr, data=big_data).status_code == 200:
        sess.post(send_link, headers=headr, data=big_data)
        return "Отправлено успешно"
    else:
        return "Потерпело неудачу"
