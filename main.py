import os
# import json
# import signal
import socket
import secrets
import string
# import requests
import webbrowser
import multiprocessing
# from pprint import pprint
from ui_main import Ui_From
# from PySide2.QtGui import QIcon, QPainter, QPixmap
# from web.start_web import start_web
# from PySide2.QtUiTools import QUiLoader
from PyQt5.QtCore import pyqtSignal, QObject
from web.websocket_server import start_websocket_func
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget


class Communicate(QObject):
    show_log = pyqtSignal(str)


def start_web():
    os.system('python web/app.py')
    # os.system(f'{os.getcwd()}/web/app.exe')


class LANCOM(QWidget):
    def __init__(self):
        super().__init__()
        self.process = None
        self.getcwd = os.getcwd()
        self.com = Communicate()
        self.ui = Ui_From()
        self.ui.setupUi(self)
        self.ipv4_ip = self.ui.local_host.currentText()
        # self.ipv4_ip = socket.gethostbyname_ex(socket.gethostname())[2][-1]
        self.ui.start_or_stop_btn.clicked.connect(self.start_or_stop_func)
        self.ui.update_btn.clicked.connect(self.check_server)
        self.com.show_log.connect(self.show_log_func)
        self.ui.clear_all_btn.clicked.connect(self.clear_all_func)
        self.ui.history_info.clicked.connect(self.show_history_info_func)
        self.ui.picture.clicked.connect(self.show_picture_func)
        self.ui.local_host.currentIndexChanged.connect(self.change_local_host_func)
        # 初始化内网IP地址
        self.init_local_host_list()

    def init_local_host_list(self):
        local_host_list = socket.gethostbyname_ex(socket.gethostname())[2]
        self.ui.local_host.addItems(local_host_list)

    def change_local_host_func(self):
        self.ipv4_ip = self.ui.local_host.currentText()

    def clear_all_func(self):
        is_clear_all = QMessageBox.question(self, 'Clear', 'Are you sure you want to delete all the history?', QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
        if is_clear_all == QMessageBox.Yes:
            with open('web/session/session.json', 'w+', encoding='utf-8') as f:
                f.write('')
            # 删除所有的历史文件和图片
            save_path_file = 'web/static/upload/file'
            save_path_img = 'web/static/upload/image'
            save_path_video = 'web/static/upload/video'
            self.delete_files(save_path_file)
            self.delete_files(save_path_img)
            self.delete_files(save_path_video)
        else:
            pass

    def show_history_info_func(self):
        # start_directory = f'{self.getcwd}\\web\\session'
        # os.system(f"explorer.exe {start_directory}")
        with open('web/session/secure_chars', 'r+', encoding='utf-8') as f:
            randm_key = f.read()
        webbrowser.open(f"http://{self.ipv4_ip}:5000/{randm_key}?history=all")

    def show_picture_func(self):
        start_directory = f'{self.getcwd}\\web\\static\\upload'
        os.system(f"explorer.exe {start_directory}")

    def delete_files(self, path):
        for foldName, subfolders, filenames in os.walk(path):  # 用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
            if filenames:
                for filename in filenames:  # 遍历列表下的所有文件名
                    os.remove(os.path.join(foldName, filename))  # 删除符合条件的文件
                    # print("{} deleted.".format(filename))
                    self.com.show_log.emit(f'[*] {filename[-10:]} deleted.')
            else:
                self.com.show_log.emit(f'[*] {path} is NULL.')

    def show_log_func(self, in_str):
        self.ui.show_log.append(in_str)

    # 生成7个安全的随机字符
    def create_secure_chars(self):
        secure_chars = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(7))
        with open('web/session/secure_chars', 'w+', encoding='utf-8') as f:
            f.write(secure_chars)

    def start_or_stop_func(self):
        self.ui.show_log.clear()
        if self.ui.start_or_stop_btn.text() == 'Open':
            servers_pid = self.check_server()
            flask_pid = servers_pid['flask_pid']
            websocket_pid = servers_pid['websocket_pid']
            if not flask_pid and not websocket_pid:
                self.create_secure_chars()
                web_process = multiprocessing.Process(target=start_web, args=())
                web_process.start()
                select_host = self.ui.local_host.currentText()
                multiprocessing.Process(target=start_websocket_func, args=(select_host,)).start()
                self.process = web_process
                # print(f'[+] websocket已开启...')
                # print(f'[+] flask服务器已开启,pid={web_process.pid}')
                with open('web/session/secure_chars', 'r+', encoding='utf-8') as f:
                    randm_key = f.read()
                # print(randm_key)
                self.com.show_log.emit(f'[+] websocket已开启...')
                self.com.show_log.emit(f'[+] flask服务器已开启, pid={web_process.pid}')
                self.com.show_log.emit(f'[+] Running on <font color=skyblue>http://{self.ipv4_ip}:5000/{randm_key}<font>')
                # 更新样式
                self.ui.start_or_stop_btn.setText('Close')
                self.ui.start_or_stop_btn.setStyleSheet('background-color: rgb(0, 255, 127);')
            else:
                if flask_pid:
                    # print(f'[*] 还有flask服务在运行, 请先关闭它')
                    self.com.show_log.emit(f'[*] 还有flask服务在运行, 请先关闭它')
                if websocket_pid:
                    # print(f'[*] 还有websocket服务在运行, 请先关闭它')
                    self.com.show_log.emit(f'[*] 还有websocket服务在运行, 请先关闭它')
                pass
        elif self.ui.start_or_stop_btn.text() == 'Close':
            self.stop_server_func()
        # process.kill()

    def check_server(self):
        flask_pid = None
        websocket_pid = None
        # self.ui.show_log.clear()
        # 检查是否存在存活flask服务
        res = os.popen('netstat -ano | findstr 5000').read()
        for line in res.splitlines():
            new_line = [i for i in line.split(' ') if i != '']
            if new_line[0] == 'TCP' and (new_line[1] == '0.0.0.0:5000' or new_line[1] == '127.0.0.1:5000') and new_line[3] == 'LISTENING':
                flask_pid = int(new_line[-1])
                break
        # 检查是否存在存活websocket服务
        websocket_res = os.popen('netstat -ano | findstr 8305').read()
        for line in websocket_res.splitlines():
            new_line = [i for i in line.split(' ') if i != '']
            if new_line[0] == 'TCP' and new_line[1].split(':')[1] == '8305' and new_line[3] == 'LISTENING':
                websocket_pid = int(new_line[-1])
                break
        if not flask_pid and not websocket_pid:
            self.ui.start_or_stop_btn.setText('Open')
            self.ui.start_or_stop_btn.setStyleSheet('background-color: rgb(255, 0, 127);')
        else:
            self.ui.start_or_stop_btn.setText('Close')
            self.ui.start_or_stop_btn.setStyleSheet('background-color: rgb(0, 255, 127);')
        if flask_pid:
            self.com.show_log.emit('[+] flask服务最正在运行...')
        else:
            self.com.show_log.emit('[-] 没有flask服务运行...')
        if websocket_pid:
            self.com.show_log.emit('[+] websocket服务正在运行...')
        else:
            self.com.show_log.emit('[-] 没有websocket服务运行...')
        return {'flask_pid': flask_pid, 'websocket_pid': websocket_pid}

    def stop_server_func(self):
        self.ui.show_log.clear()
        servers_pid = self.check_server()
        flask_pid = servers_pid['flask_pid']
        websocket_pid = servers_pid['websocket_pid']
        if flask_pid:
            if not os.system(f'taskkill /pid {flask_pid} /f'):
                # print('[+] flask web 服务退出成功')
                self.com.show_log.emit('[+] flask web 服务退出成功')
            else:
                is_ok = 0
                all_pids = os.popen(f'wmic process get processid,parentprocessid | findstr/i {flask_pid}').read()
                for line in all_pids.splitlines():
                    c_pid = [i for i in line.split(' ') if i != '']
                    if c_pid:
                        for pid in c_pid:
                            if not os.system(f'taskkill /pid {pid} /f'):
                                # 如果退出成功则退出程序逻辑
                                is_ok = 1
                                # print('[+] flask web 服务退出成功')
                                self.com.show_log.emit('[+] flask web 服务退出成功')
                            else:
                                continue
                    if is_ok:
                        break
                if not is_ok:
                    # print('[-] flask web 服务退出失败')
                    self.com.show_log.emit('[-] flask web 服务退出失败')
        # print(f'[-] 没有找到Flask服务...')
        if websocket_pid:
            if not os.system(f'taskkill /pid {websocket_pid} /f'):
                # print('[+] websocket 服务退出成功')
                self.com.show_log.emit('[+] websocket 服务退出成功')
            else:
                # print('[+] websocket 服务退出失败')
                self.com.show_log.emit('[+] websocket 服务退出失败')
        else:
            # print('[*] 没有WebSocket服务')
            self.com.show_log.emit('[*] 没有WebSocket服务')
        # 最后更新样式
        self.ui.start_or_stop_btn.setText('Open')
        self.ui.start_or_stop_btn.setStyleSheet('background-color: rgb(255, 0, 127);')


if __name__ == "__main__":
    multiprocessing.freeze_support()    # 是在exe模式下防止出现多个窗口
    app = QApplication([])
    stats = LANCOM()
    # stats.ui.show()
    stats.show()
    app.exec_()