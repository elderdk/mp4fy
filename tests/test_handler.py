import unittest
from downloader import download
from exceptions import VideoTooBigError

class TestHandlerCase(unittest.TestCase):

    def test_download(self):
        url = "https://www.youtube.com/watch?v=z5JKXbhtSY8"
        filename, info = download(url)
        self.assertEqual(info['title'], "Over The Garden Wall Official Soundtrack | Adelaide Parade – The Blasting Company | WaterTower")

    def test_video_too_big(self):
        url = "https://www.youtube.com/watch?v=BcbmFxbdsJ0&ab_channel=%EB%AA%BD%ED%82%A4%EB%B9%84%EC%A7%80%EC%97%A0MONKEYBGM"
        self.assertRaises(VideoTooBigError, download, url)

if __name__ == '__main__':
    unittest.main()
