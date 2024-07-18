import sentence_transformers
import PIL

# Download và sử dụng 1 model đã đc train sẵn (cần Internet)
## Hoặc download sẵn và paste vào folder cache của package
## Thường đc download từ Hugging Face Model Hub

# clip-ViT-B-32: thuộc nhóm model CLIP: Contrastive Language–Image Pretraining, chuyên xử lí ảnh, text đc build bởi OpenAI
## Riêng model này chuyên xử lí text
model = sentence_transformers.SentenceTransformer("clip-ViT-B-32")

img1 = PIL.Image.open("path1")
img2 = PIL.Image.open("path2")
image_data = [img1, img2]

# Transform data input thành dạng vector, chức năng chính của package
## batch_size: size của data mỗi lần xử lí, càng lớn chạy càng nhanh nhưng ngốn performance
## convert_to_tensor: output đc convert sang Pytorch tensor, hữu ích khi ta tiếp tục dùng Pytorch xử lí data sau đó
## show_progress_bar: hiển thị progress trên terminal
encoded_image = model.encode(
    image_data, batch_size=128, convert_to_tensor=True, show_progress_bar=True
)

# Tiến hành so sánh các vector vừa đc transform, so sánh và tìm ra các vector giống nhau
## Return: list chứa các cặp vector giống nhau
processed_images = sentence_transformers.util.paraphrase_mining_embeddings(
    encoded_image
)
