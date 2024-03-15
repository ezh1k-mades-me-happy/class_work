import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {"entity": "Elf Humboldt", "gift": "a glass casket"},
        {"entity": "blue kobold", "gift": "quid pro quo"},
        {"entity": "forest fairy", "gift": "the scent of magic"},
        {"entity": "dwarf", "gift": "a pot of gold"},
        {"entity": "troll from the hills", "gift": "baton"},
        {"entity": "elf Ariel", "gift": "the ringing of the higher spheres"},
        {"entity": "hobbit Baggins", "gift": "a hearty breakfast"}
    ]

    server = Server('127.0.0.1', 8080, data)
    with server.run():
        while (row := input('Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')) != 'stop':
            ...