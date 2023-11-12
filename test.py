from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 모델과 토크나이저 불러오기
model = GPT2LMHeadModel.from_pretrained("./gpt2-finetuned")
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2-finetuned")

# 생성할 텍스트의 시작 부분
prompt = "이렇게 시작하는 메시지에 대해:"

# 텍스트 생성
inputs = tokenizer.encode(prompt, return_tensors='pt')
outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# 사용자 입력 받기
user_input = input("질문을 입력하세요: ")

# 모델이 대답 생성
inputs = tokenizer.encode(user_input, return_tensors='pt')
outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
print("AI 대답:", tokenizer.decode(outputs[0], skip_special_tokens=True))
