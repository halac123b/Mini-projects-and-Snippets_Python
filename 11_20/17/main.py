import gradio


def test_func():
    return "Hello world"


# Tạo obj UI của gradio, giống 1 component trong các framework frontend
## fn: hàm nhận vào input và return output, là core của Interface để xử lí input
## inputs=Image: ô nhập input sẽ là UI nhận ảnh của gradio (có sẵn rất nhiều option từ dropdown, copy, upload)
## outputs=Label: dạng chuyên để hiển thị output của các bài toán phân loại, biểu diễn % của các label
### num_top_classes: hiện 3 label có tỉ lệ cao nhất
## title: title nằm ở đầu component
## description: phần mô tả nằm dưới title
## examples: các ví dụ mà user có thể chọn để nhập vào input
### Ở đây input là ảnh nên example là list chứa path đến các image để chọn
web_ui = gradio.Interface(
    fn=test_func,
    inputs=gradio.Image(),
    outputs=gradio.Label(num_top_classes=3),
    title="This is title",
    description="A detailed description.",
    examples=[[]],
)
# Cuối cùng khởi động component lên web
web_ui.launch()
