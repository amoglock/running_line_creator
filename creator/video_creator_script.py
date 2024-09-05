import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw

def create_video(input_text: str) -> None:


    # Определяем размер видео
    width, height = 100, 100

    # Задаем параметры для видео:
    # Имя файла генерируется из содержимого строки (макс длина 15 символов)
    # Формат видео mp4
    # 24 кадра в секунду
    video_result = (
        cv2.VideoWriter(f"uploads/media/{input_text[:15]}.mp4".replace(' ', '_'),
                        cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))
    )

    # Матрица для кадра
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Координаты начала текста
    x, y = width, height // 4

    # Путь к шрифту
    font_path = "creator/fonts/Roboto-Black.ttf"

    # Подключаем шрифт с помощью Pillow
    pillow_font = ImageFont.truetype(font_path, size=36)

    # Проходим по каждому кадру
    for t in range(72): # 3 секунды по 24 кадра
        # Очищаем кадр
        frame.fill(0)

        x -= int(len(input_text) / 3)  # Скорость бегущей строки

        # Используем Pillow для наложения текста
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)

        # Добавляем текст на изображение
        draw.text((x, y), input_text, font=pillow_font, fill=(255, 255, 255))

        # Преобразуем обратно в массив NumPy
        frame = np.array(img_pil)

        video_result.write(frame)

    video_result.release()