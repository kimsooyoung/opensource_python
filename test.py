import glob
import logging
from PIL import Image

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.WARN,
    datefmt="%Y-%m-%d %H:%M:%S"
)

class GifConverter:
    """
    여러 장의 이미지를 애니메이션 효과가 있는 단일 GIF 이미지로 변경 하는 클래스
    """
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        path_in  : 원본 여러 이미지 경로(Ex : images/*.png)
        path_out : 결과 이미지 경로(Ex : output/filename.png)
        resize   : 리사이징 크기((320,240))
        """
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize

print(GifConverter.__init__.__doc__)