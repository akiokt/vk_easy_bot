import vk_api
import json
import os
from vk_api.longpoll import VkLongPoll, VkEventType

config = open("config.json")
config = json.load(config)

API_KEY = config['api']
API_VER = config['version']

session = vk_api.VkApi(token=API_KEY, api_version=API_VER)
longpoll = VkLongPoll(session)
vk = session.get_api()
commands = open("commands.json")
commands = json.load(commands)

try:
    for event in longpoll.listen():
        while True:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message = event.text.lower()
                if commands.get[message] and message.startswith(commands['start_with']):
                    vk.messages.send(
                        user_id=event.user_id,
                        message=commands[message]
                    )
                elif not commands.get[message]:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Я не знаю такой команды!"
                    )
except Exception:
    location = os.getcwd()
    os.system(f"python3 {location}/bot.py")