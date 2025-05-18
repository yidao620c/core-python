from gooey import Gooey, GooeyParser


@Gooey(program_name='测试项目', language='chinese', encoding='utf-8')
def main():
    parser = GooeyParser(description='这里是程序介绍')
    parser.add_argument('File', help='文件介绍', widget='FileChooser')
    parser.add_argument('Date', help='日期介绍', widget='DateChooser')
    args = parser.parse_args()

    with open(args.File, 'rb') as f:
        res = f.read()
        print(f'获取的文件内容是 {res}')

    print(f'获取的日期是 {args.Date}')


if __name__ == '__main__':
    main()