import setuptools

# Chạy Setup để install package vào list package của Python dưới local
setuptools.setup(
    name="aj",
    version="1.0.0",
    python_requires=">=3",
    install_requires=["package"],
    description="Desc for the package",
    author="Duy Ha",
    author_email="halac123game@gmail.com",
    url="absolute_link",  # URL đến page của package
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "aj": [
            "aj/static/images/*",
        ],
    },
)
