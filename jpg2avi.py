import cv2
import os

def image_to_video(input_path, output_path):
    file = input_path  # 图片目录
    output = output_path  # 生成视频路径
    num = os.listdir(file)  # 生成图片目录下以图片名字为内容的列表
    height = 1200
    weight = 1920
    fps = 40
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G') # 用于avi格式的生成
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 用于mp4格式的生成
    videowriter = cv2.VideoWriter(output, fourcc, fps, (weight, height))  # 创建一个写入视频对象
    # for i in range(272, 1323):
    for i in num:
        name = i
    # for name in num:
        if name[-4:] == '.jpg':
            path = os.path.join(file, name)
            print(path)
            frame = cv2.imread(path)
            # print(frame)
            videowriter.write(frame)
        else:
            continue

    videowriter.release()


if __name__ == '__main__':
    input_root = r'/data/xiaochaosui/dataset/BF_001_infer/0_BF_001/All_Results'
    output_root = r'/data/xiaochaosui/dataset/BF_001_infer/0_BF_001/All_Results'
    # for name in os.listdir(input_root):
        # print(name)
        # print(os.path.join(input_root, name), os.path.join(output_root, name+'.avi'))
        # image_to_video(os.path.join(input_root, name), os.path.join(output_root, name+'.avi'))

    image_to_video(os.path.join(input_root, 'JPEGImages'),
                   os.path.join(output_root, 'output.avi'))


