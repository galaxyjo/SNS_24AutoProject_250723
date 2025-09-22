import os

from PIL import Image, ImageDraw, ImageFont

from decorators.log_trace import log_trace


@log_trace
def create_images_from_text(posts):
    output_dir = "outputs/instagram_uploaded"
    os.makedirs(output_dir, exist_ok=True)

    font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 지원 폰트 경로
    font = ImageFont.truetype(font_path, 24)

    image_paths = []
    for i, text in enumerate(posts):
        img = Image.new("RGB", (800, 800), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text((50, 100), text, fill=(0, 0, 0), font=font)
        image_path = os.path.join(output_dir, f"post_{i+1}.png")
        img.save(image_path)
        image_paths.append(image_path)

    print(f"✅ 이미지 생성 완료: {image_paths}")
    return image_paths
