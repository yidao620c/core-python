import io
import os
import sys
import zipfile
from pathlib import Path

from gooey import Gooey, GooeyParser

# 设置全局UTF-8编码环境
os.environ["PYTHONUTF8"] = "1"

# 处理 sys.stdout 为 None 的情况
if sys.stdout is None:
    # 禁用控制台时，输出重定向到空设备（避免错误）
    sys.stdout = open(os.devnull, 'w', encoding='utf-8')
elif sys.stdout.encoding != 'UTF-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


@Gooey(program_name='文件夹图片搜集器', language='chinese', encoding='utf-8')
def main():
    parser = GooeyParser(description='将一个文件夹中所有图片打包成一个zip')
    parser.add_argument('Dir', help='文件夹', widget='DirChooser')
    parser.add_argument('Output', help='输出文件名', widget='FileSaver')
    args = parser.parse_args()

    def real_work():
        # 执行耗时操作
        file_list = os.listdir(args.Dir)
        images = []
        for file in file_list:
            extension = Path(file).suffix
            if extension in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                images.append(os.path.join(args.Dir, file))

        zip_path = f'{args.Output}'
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for image_path in images:
                zipf.write(image_path, arcname=image_path.split(os.sep)[-1])

        print(f'压缩成功到：{zip_path}')

    real_work()


if __name__ == '__main__':
    main()
