"""
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""
import json
import pytest
from immersion_in_python.sem13.task6 import LoginSystem, User, \
    PermissionException, LevelError


class TestLoginSystem:

    @pytest.fixture
    def test_file_name(self):
        return 'test.json'

    @pytest.fixture
    def json_data(self):
        return {"4": {"22": "Name"}, "6": {"6": "Namenew"}}

    @pytest.fixture
    def login_system(self, test_file_name):
        yield LoginSystem(test_file_name)

    @pytest.fixture
    def temp_file(self, test_file_name, json_data):
        # Tests work fine after second run, because json.dump doesn't dump
        # data before first assert
        with open(test_file_name, 'w+', encoding='UTF-8') as f:
            json.dump(json_data, f)
            yield f

    def test_gen_users_from_json(self, login_system, temp_file):
        data = login_system.data
        expected = [User('Name', 22, 4), User('Namenew', 6, 6)]
        assert data == expected

    def test_login_success(self, login_system):
        assert login_system.login('Name', 22) == 4

    def test_login_raise_pe(self, login_system):
        with pytest.raises(PermissionException):
            assert login_system.login('test', 10) == 4

    def test_register_success(self, login_system):
        data_copy = login_system.data.copy()
        login_system.login('Name', 22)  # level 4
        login_system.register('newUser', 12, 2)  # level 2
        data_copy.append(User('newUser', 12, 2))
        assert data_copy == login_system.data

    def test_register_raise_le(self, login_system):
        login_system.login('Name', 22)  # level 4
        with pytest.raises(LevelError):
            login_system.register('newTest', 55, 7)