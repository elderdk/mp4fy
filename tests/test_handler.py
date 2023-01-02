import unittest
from downloader import download


class TestHandlerCase(unittest.TestCase):

    def test_download(self):
        url = "https://www.youtube.com/watch?v=z5JKXbhtSY8"
        filename, info = download(url)
        self.assertEqual(info['title'], "Over The Garden Wall Official Soundtrack | Adelaide Parade – The Blasting Company | WaterTower")

if __name__ == '__main__':
    unittest.main()
