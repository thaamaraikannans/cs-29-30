import requests

# url = "https://kannan-s3-bucket.s3.ap-south-1.amazonaws.com/Vilangu+.+2022+.+S01+EP01%EA%9E%89+Section+174.mkv"


def file_download(url, name):
    response = requests.get(url, stream=True)
    with open(name, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f" {name} file download successful")

for num in range(1, 68):
    url = f"https://kannan-s3-bucket.s3.ap-south-1.amazonaws.com/images/image{num}.jpeg"
    file_download(url=url, name=f"dhoni{num}.jpeg")