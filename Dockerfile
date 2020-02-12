FROM lambci/lambda:build-python3.8

ENV AWS_DEFAULT_REGION ap-northeast-1

# コンテナ側にコピー
COPY lambda_function.py .
COPY requirements.txt .

# ./pythonに向けて pip install して 搭載モジュール.zipとlayer.zipを作成する
CMD pip3 install -r requirements.txt -t ./python && \
    zip -9yr lambda.zip lambda_function.py requirements.txt Dockerfile && \
    zip -9r layer.zip ./python
