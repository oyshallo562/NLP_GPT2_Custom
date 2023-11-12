import json
import os

def create_qa_pairs(file_path):
    with open(file_path, 'r', encoding='latin1') as file:
        data = json.load(file)

    # 질문-답변 쌍을 저장할 리스트
    qa_pairs = []

    # 이전 메시지를 저장하는 변수
    previous_message = None

    for message in data['messages']:
        # 메시지 정보 추출
        sender = message['sender_name'].encode("latin1").decode("utf-8")
        content = message.get('content', '').encode("latin1").decode("utf-8")

        # "오유성"이 보낸 메시지를 답변으로 사용
        if sender == "오유성" and previous_message:
            question = previous_message
            answer = content
            qa_pairs.append(f"질문: {question}\n답변: {answer}\n")

        # 현재 메시지를 다음 루프에서의 이전 메시지로 저장
        previous_message = content

    return qa_pairs

# 폴더 내의 모든 JSON 파일을 찾음
folder_path = 'C:/Users/OYS/dev/pythonProject/inbox'
all_qa_pairs = []

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.json'):
            file_path = os.path.join(root, file_name)
            qa_pairs = create_qa_pairs(file_path)
            all_qa_pairs.extend(qa_pairs)

# 모든 질문-답변 쌍을 텍스트 파일로 저장
with open('qa_pairs.txt', 'w', encoding='utf-8') as file:
    for pair in all_qa_pairs:
        file.write(pair)
