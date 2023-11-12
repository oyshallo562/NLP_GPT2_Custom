from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
import torch

print(torch.cuda.is_available())

# 토크나이저 및 모델 초기화
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# 대화 데이터셋 준비
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="ouyuseong_messages_cl.txt",
    block_size=128)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False)

# 훈련 설정
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# 훈련 실행
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# 모델 훈련
trainer.train()

# 모델 저장
model.save_pretrained("./gpt2-finetuned")

# 토크나이저 저장
tokenizer.save_pretrained("./gpt2-finetuned")
