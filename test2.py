# py_ad_4_3 : 완성된 패키지 임포트
from test import GifConverter as gfc

# 클래스 생성
c = gfc("./project/images/*.png", './project/image_out/result.gif', (320,240))

# 실행
c.convert_gif()