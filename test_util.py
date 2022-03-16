import util

class TestUtil:
    def test_obfuscate_mongo_string_connection(self):
        test = 'mongodb://app:pass@localhost:27017/zunka?authSource=admin'
        result = test.replace('pass', 'xxxx')
        assert util.obfuscate_mongo_string_connection(test) == result


