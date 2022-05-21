import requests


def send_task1(first_name: str, last_name: str, answer: str, task_id: int):
    send_link = "https://api.imsr.su/add_answer"
    headr = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome / '
                           '96.0.4664.174 YaBrowser / 22.1.4.837 Yowser / 2.5 Safari / 537.36'}
    big_data = {'first_name': first_name, 'last_name': last_name, 'answer': answer, 'task_id': task_id}
    sess = requests.session()
    if sess.post(send_link, headers=headr, data=big_data).status_code == 200:
        sess.post(send_link, headers=headr, data=big_data)
        return "Отправлено успешно"
    else:
        return "Потерпело неудачу"
