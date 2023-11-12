import json
import os

def process_json_file(file_path):
    print("processing: ", file_path)
    # JSON 파일 읽기
    with open(file_path, 'r', encoding='latin1') as file:
        data = json.load(file)
    hun = 0
    # "오유성"이 보낸 메시지 추출
    messages_from_ouyuseong = []
    for message in data['messages']:
        sender = message['sender_name'].encode("latin1").decode("utf-8")
        content = message.get('content', '').encode("latin1").decode("utf-8")
        if sender == "오유성":
            messages_from_ouyuseong.append(content)
            hun += 1
            if (hun % 100 == 0):
                print("found message from 오유성, total: ", hun)

    return messages_from_ouyuseong

# 폴더 내의 모든 JSON 파일을 찾음
folder_path = 'C:/Users/OYS/dev/pythonProject/inbox'
all_messages = []

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.json'):
            file_path = os.path.join(root, file_name)
            messages = process_json_file(file_path)
            all_messages.extend(messages)

# 모든 메시지를 텍스트 파일로 저장
with open('ouyuseong_messages.txt', 'w', encoding='utf-8') as file:
    for message in all_messages:
        file.write(message + '\n')
