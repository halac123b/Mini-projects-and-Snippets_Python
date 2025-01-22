import setuptools

# Chạy Setup để install package vào list package của Python dưới local
setuptools.setup(
    name="aj",
    version="1.0.0",
    python_requires=">=3",
    install_requires=["package_name"],  # From requirement.txt
    description="Desc for the package",
    long_description="Long desc for the package",
    author="Duy Ha",
    author_email="halac123game@gmail.com",
    url="URL_website",  # URL đến page của package (homepage, document)
    packages=setuptools.find_packages(),  # List các package, sub-package trong folder để build package hiện tại
    # Thông thường setuptool chỉ install package gồm các file code, nếu muốn install kèm các format khác (data, text, image) cần setting này
    # Các file này cần đc list trong file MANIFEST.in và file đc list trong option "package_data"
    include_package_data=True,
    # List thêm các file k phải code khác để install vào package
    package_data={
        "aj": [
            "aj/static/images/*",
        ],
    },
)
