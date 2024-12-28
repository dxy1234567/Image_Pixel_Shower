import cv2
import numpy as np

# 鼠标事件回调函数
def show_pixel_value(event, x, y, flags, param):
    global img_copy
    img_copy = img.copy()  # 每次刷新绘制时从原图复制
    if event == cv2.EVENT_MOUSEMOVE:  # 鼠标移动时触发
        if len(img.shape) == 2:  # 灰度图像
            value = img[y, x]
            text = f"({x}, {y}): {value}"
        elif len(img.shape) == 3:  # 彩色图像
            b, g, r = img[y, x]
            text = f"({x}, {y}): B={b}, G={g}, R={r}"
        
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        text_width, text_height = text_size

        # 在图像上方增加10个像素的高度
        new_height = img.shape[0] + 2 * text_height
        new_width = img.shape[1]
        new_img = np.zeros((new_height, new_width), dtype=np.uint16)
        new_img[:img.shape[0], :img.shape[1]] = img.copy()
        new_img[-2 * text_height:, :] = 65535  # 白色背景

        text_x = (new_width - text_width) // 2
        text_y = new_height - text_height // 2

        # 在图像上方显示像素值
        cv2.putText(new_img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

        # 更新显示的图像
        img_copy = new_img

# 主程序
def main():
    global img, img_copy
    # 读取图像（将路径替换为你的图像路径）
    img_path = "imgs\Image0144.png"
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    if img is None:
        print("无法加载图像，请检查路径！")
        return

    img_copy = img.copy()  # 备份原始图像，用于绘制
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", show_pixel_value)

    while True:
        # 显示图像
        cv2.imshow("Image", img_copy)

        # 按下键盘 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放窗口
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
