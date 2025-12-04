# 服务器端
import os
import re
import socket
import time
import json
import base64
import asyncio
import websockets
from html import escape, unescape
from datetime import datetime

# 保存所有已连接的客户端
clients = set()
server_ip = None


# def get_server_ip():
#     ipv4_ip = socket.gethostbyname_ex(socket.gethostname())[2][-1]
#     return ipv4_ip


def find_new_file(dir_path):
    '''查找目录下最新的文件'''
    try:
        file_lists = os.listdir(dir_path)
        file_lists.sort(key=lambda fn: os.path.getmtime(dir_path + "\\" + fn)
                        if not os.path.isdir(dir_path + "\\" + fn) else 0)
        # print('最新的文件为： ' + file_lists[-1])
        return file_lists[-1]
    except Exception as e:
        return None


def isAssetTypeAnImage(ext):
    f_ext_s = ['WEBP','BMP','PCX','TIF', 'GIF', 'JPGE', 'JPG', 'JPEG', 'TGA','EXIF','FPX','SVG','PSD','CDR','PCD','DXF', 'UFO', 'EPS', 'AI', 'PNG', 'HDRI', 'RAW', 'WMF','FLIC','EMF', 'ICO']
    if ext.upper() in f_ext_s:
        return True
    return False


def isAssetTypeAnVideo(ext):
    f_ext_s = ['mp4','m4v','avi','mkv', 'mov','wmv','flv', 'f4v', 'webm','mpeg','mpg','m2ts','3gp','ogv','ts','mts', 'rm', 'rmvb', 'vob', 'asf', 'mov', 'mxf', 'raw','cin','ani', 'swf']
    if ext.lower() in f_ext_s:
        return True
    return False

async def chat(websocket, path):
    print(websocket, path)
    # 将新连接的客户端添加到集合中
    clients.add(websocket)
    # server_ip = get_server_ip()
    user_ip = websocket.remote_address[0]
    # print(server_ip,user_ip)
    file_name = ''
    file_content = ''
    save_path = ''
    try:
        # 接收客户端发送的消息
        async for message in websocket:
            # 转发消息给所有已连接的客户端
            if server_ip == user_ip:
                avatar = 'me'
            else:
                avatar = 'she'
            avatar_img = f'/static/images/{avatar}.png'
            c_time = datetime.now().ctime()
            # {"type": "text", "content": msg_text}
            # print(message)
            # 在这里处理接收到的文本数据
            if isinstance(message, str):
                message = json.loads(message)
                if message['type'] == 'file_name':
                    file_suffix = message['content'].split('.')[-1]
                    # file_name = f'{int(time.time()*1000)}.{file_suffix}'
                    # print(file_name)
                    file_name = escape(message['content'])
                    if isAssetTypeAnImage(file_suffix):
                        save_path = f'web/static/upload/image/{file_name}'
                    elif isAssetTypeAnVideo(file_suffix):
                        save_path = f'web/static/upload/video/{file_name}'
                    else:
                        save_path = f'web/static/upload/file/{file_name}'
                    # 除了视频
                    if not isAssetTypeAnVideo(file_suffix):
                        with open(save_path, 'wb+') as f:
                            f.write(b'')
                    # new_file_name = find_new_file(save_path)
                else:
                    # message = json.loads(message)
                    # print(message)
                    c_type = message['type']
                    content = ''
                    img_src = ''
                    file_path = ''
                    file_type = ''
                    if c_type == 'image':
                        img_src = f'static/upload/image/{file_name}'
                    elif c_type == 'video':
                        file_path = f'static/upload/video/{file_name}'
                    elif c_type == 'file':
                        file_path = f'static/upload/file/{file_name}'
                        ext = file_name.split('.')[-1].lower()
                        if ext in ['txt']:
                            file_type = 'TXT.png'
                        elif ext in ['xlsx', 'xls', 'csv', 'ppt', 'pptx']:
                            file_type = 'Excel.png'
                        elif ext in ['pdf']:
                            file_type = 'pdf文件.png'
                        elif ext in ['doc', 'docx']:
                            file_type = 'word.png'
                        elif ext in ['zip', 'rar', 'tar', 'bz2', 'gz']:
                            file_type = '文件压缩包.png'
                        else:
                            file_type = '无法识别文件.png'
                    else:
                        content = message['content']
                        # print('content:', escape(content))
                    mess_body = {
                        "type": c_type,
                        "avatar": avatar,
                        "avatar_img": avatar_img,
                        "c_time": c_time,
                        "text": escape(content),
                        "img_src": img_src,
                        "file_name": file_name,
                        "file_path": file_path,
                        "file_type": file_type
                    }
                    with open('web/session/session.json', 'r+', encoding='utf-8') as f:
                        seesion = f.read().strip()
                    with open('web/session/session.json', 'w+', encoding='utf-8') as f:
                        seesion = [] if seesion == '' else json.loads(seesion)
                        seesion.append(mess_body)
                        f.write(json.dumps(seesion))
                    await asyncio.wait([client.send(json.dumps(mess_body)) for client in clients])
            # 在这里处理接收到的二进制数据类型
            elif isinstance(message, bytes):
                # save_path = f'web/static/upload/video/{file_name}'
                if save_path:
                    while True:
                        try:
                            # print('bytes: ', len(message))
                            with open(save_path, 'ab') as f:
                                f.write(message)
                                break
                        except Exception:
                            time.sleep(1)
                            continue
            else:
                pass
    except Exception as e:
        # 客户端断开连接时，从集合中移除
        print(e)
        clients.remove(websocket)
    finally:
        clients.remove(websocket)
    print(file_content)


# 启动服务器
def start_websocket_func(s_host):
    global server_ip
    server_ip = s_host
    if s_host:
        start_server = websockets.serve(chat, s_host, 8305)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    else:
        print('[-] 服务器地址不能为空')


if __name__ == "__main__":
    start_websocket_func('192.168.2.5')