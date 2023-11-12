# 원본 파일 경로와 새로운 파일 경로 설정
original_file_path = 'ouyuseong_messages.txt'
new_file_path = 'ouyuseong_messages_cl.txt'

# 원본 파일 열기 (읽기 모드)
with open(original_file_path, 'r', encoding='utf-8') as original_file:
    lines = original_file.readlines()

# 빈 줄 제거
lines = [line.strip() for line in lines if line.strip()]

# 새로운 파일에 저장 (쓰기 모드)
with open(new_file_path, 'w', encoding='utf-8') as new_file:
    new_file.writelines('\n'.join(lines))
