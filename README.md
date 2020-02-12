# Description
- ローカルPCで外部ライブラリを利用したAWS Lambdaを開発するサンプル

## Usage
### docker image build
```bash
docker build -t mylambda .
```

### create deploy modules
```bash
docker run --rm -v "$PWD":/var/task mylambda
```

### execute lambda function on local pc
```bash
docker run --rm -v "$PWD":/var/task -v "$PWD":/opt lambci/lambda:python3.8 lambda_function.lambda_handler
```