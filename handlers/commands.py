from main import dp
from aiogram.types import Message
from handlers.tasks import *
from handlers.send_task import send_task1
from handlers.send_code import send_code1


'''4'''
@dp.message_handler(commands=["send_code"])
async def send_task(msg: Message):
    title = 'Заголовок'
    description = 'описание'
    start_code = 'Код'
    comment = 'Комментарий'
    result_send_code = send_code1(title, description, start_code, comment)
    return await msg.answer(result_send_code)


'''3'''
@dp.message_handler(commands=["send_task"])
async def send_task(msg: Message):
    first_name = 'Денис'
    last_name = 'Латышев'
    answer = 'тест4'
    task_id = 52
    result_send_task = send_task1(first_name, last_name, answer, task_id)
    return await msg.answer(result_send_task)


"""1"""
@dp.message_handler(commands=["new_task"])
async def func_new_task(m: Message):
    tasks: dict = view_all_task()
    with open('last_task.txt', 'r', encoding="utf-8") as read:
        task_prev = read.read()
    for i in tasks:
        if i.get('id') > int(task_prev):
            await m.answer(f"Задание {i.get('id')}_{i.get('title')}_{i.get('date')}")
        elif i.get('id') == int(task_prev):
            await m.answer(f"Новых задании нет,последнее задание {tasks[-1]['id']}")
    with open('last_task.txt', 'w', encoding="utf-8") as write:
        write.write(f"{tasks[-1]['id']}")
    return


"""2"""
@dp.message_handler(content_types=['text'])
async def id_desc(msg: Message):
    tasks: dict = view_all_task()
    if msg.text.isdigit():
        for i in tasks:
            if i.get('id') == int(msg.text):
                return await msg.answer(f"{i.get('description')}")
        return await msg.answer(f"Таких задании нет, введите задание от {tasks[0]['id']} до {tasks[-1]['id']}")
