from user import models


def test_models_insert():
    models.insert('백두산', 'hundredhead@gmail.com', '1234', 'female')


def test_models_find():
    result = models.findby_email_and_password('seafood@gmail.com', '1234')
    print(result)


test_models_insert()
test_models_find()
