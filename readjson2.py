import json

# JSON 파일 읽기
with open('your_file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 메시지 목록 추출
messages = data['messages']

# '질문-답변' 형식으로 변환
formatted_data = []
for i in range(len(messages) - 1):
    # 이전 메시지를 '질문'으로, 현재 메시지를 '답변'으로 간주
    question = messages[i]["content"].encode('latin1').decode('utf-8')
    answer = messages[i + 1]["content"].encode('latin1').decode('utf-8')
    formatted_data.append(f"질문: {question}\n답변: {answer}\n")

# 결과 출력 (예시)
for item in formatted_data[:5]:  # 처음 5개의 '질문-답변' 쌍만 출력
    print(item)
