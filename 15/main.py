import sentence_transformers

# Download và sử dụng 1 model đã đc train sẵn (cần Internet)
## Hoặc download sẵn và paste vào folder cache của package
## Thường đc download từ Hugging Face Model Hub
model = sentence_transformers.SentenceTransformer("clip-ViT-B-32")
