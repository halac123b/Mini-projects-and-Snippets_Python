import yaml

to_write = {{"users": "userinfo"}}
# Bytes, save 1 obj (dict, list,..) dưới dạng byte
## default_flow_style: bool, True: ghi file yaml dạng có indent rõ ràng đẹp, nhưng tốn dung lượng hơn
### False: ghi dạng tất cả nằm trên 1 dòng
byteData = yaml.safe_dump(to_write, default_flow_style=False, encoding='utf-8', allow_unicode=True)
print(byteData.decode("utf-8")) # Sau khi lưu dạng byte có thể decode để xem string

with open("yamlPath", 'r') as file:
    # Parse data từ file YAML
    ## Tuỳ vào nội dung và loader sẽ return kết quả tương ứng
    ## Loader=yaml.SafeLoader: chuyên parse các obj đơn giản như list, dict
    yamlData = yaml.load(file, Loader=yaml.SafeLoader)