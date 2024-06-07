from src import app


def test_lambda_handler():
    assert app.lambda_handler(event={}, context=None) == {
        "statusCode": 200,
        "body": "Hello world!",
    }
