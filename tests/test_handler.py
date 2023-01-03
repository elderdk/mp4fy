import unittest
from downloader import download
from exceptions import VideoTooBigError

class TestHandlerCase(unittest.TestCase):

    def test_download(self):
        url = "https://www.youtube.com/watch?v=z5JKXbhtSY8"
        filename, info = download(url)
        self.assertEqual(info['title'], "Over The Garden Wall Official Soundtrack | Adelaide Parade – The Blasting Company | WaterTower")

    def test_video_too_big(self):
        url = "https://www.youtube.com/watch?v=L_LUpnjgPso&ab_channel=Fireplace10hours"
        self.assertRaises(VideoTooBigError, download, url)

if __name__ == '__main__':
    unittest.main()
