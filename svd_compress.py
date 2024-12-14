import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def svd_compress(image_path, k):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img_array = np.array(img)

    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :,
                                                      2]  # Разделяем изображение на три канала (R, G, B)

    def compress_channel(channel, k):  # Функция для сжатия одного канала с использованием SVD
        U, S, Vt = np.linalg.svd(channel, full_matrices=False)
        # Оставляем только первые k сингулярных значений
        U_k = U[:, :k]
        S_k = np.diag(S[:k])
        Vt_k = Vt[:k, :]
        return np.dot(U_k, np.dot(S_k, Vt_k))

    r_compressed = compress_channel(r, k)
    g_compressed = compress_channel(g, k)
    b_compressed = compress_channel(b, k)

    compressed_img_array = np.stack((r_compressed, g_compressed, b_compressed), axis=-1).astype(np.uint8)

    return Image.fromarray(compressed_img_array)


image_path = 'apple.jpg'
k_values = [1, 10, 20, 50, 100]

plt.figure(figsize=(20, 4))
for i, k in enumerate(k_values):
    compressed_image = svd_compress(image_path, k)
    plt.subplot(2, len(k_values), i + 1)
    plt.imshow(compressed_image)
    plt.title(f'Compressed with k={k}')
    plt.axis('off')

plt.show()
