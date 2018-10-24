#-*- coding:utf-8 -*-

# yum -y install python-devel
# yum install libjpeg libjpeg-devel zlib zlib-devel freetype freetype-devel lcms lcms-devel
# yum -y install python-imaging
# pip install pillow --upgrade

from PIL import Image, ImageFont, ImageDraw
import argparse
import os
import imageio
#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-d','--duration',type = float, default = 1)#播放时间
#获取参数
args = parser.parse_args()
File = args.file
DURARION = args.duration
#像素对应ascii码

#ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list("MNHQ$OC67+>!:-. ")
#将像素转换为ascii码
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]
#将txt转换为图片
def txt2png(file_name):
    im = Image.open(file_name).convert('RGB')
    #gif拆分后的图像，需要转换，否则报错，由于gif分割后保存的是索引颜色
    raw_width = im.width   
    raw_height = im.height
    width = int(raw_width/6)
    height = int(raw_height/15)
    im = im.resize((width,height),Image.NEAREST)
    txt=""
    colors = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j,i))
            colors.append((pixel[0],pixel[1],pixel[2]))
            if(len(pixel) == 4):
                txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])
            else:
                txt += get_char(pixel[0],pixel[1],pixel[2])        
        txt += '\n' 
        colors.append((255,255,255))
    im_txt = Image.new("RGB",(raw_width,raw_height),(255,255,255))
    dr = ImageDraw.Draw(im_txt)
    font=ImageFont.load_default().font
    x=y=0
    font_w,font_h=font.getsize(txt[1])    #获取字体的宽高
    font_h *= 1.37 #调整后更佳
    #ImageDraw为每个ascii码进行上色
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x+=font_h
            y=-font_w
        dr.text([y,x],txt[i],colors[i])
        y+=font_w
    name = file_name.split('.')[0]+'-txt'+'.png'
    print(name)
    im_txt.save(name)
#拆分gif
def gif2png(file_name):
    im = Image.open(file_name)
    path = os.getcwd()
    if(not os.path.exists(path+"/Cache")):
        os.mkdir(path+"/Cache")
    os.chdir(path+"/Cache")
    try:
        while 1:
            current = im.tell()
            name = file_name.split('.')[0]+'-'+str(current)+'.png'
            im.save(name)#gif分割后保存的是索引颜色
            print(name)
            txt2png(name)
            im.seek(current+1)
    except:
        os.chdir(path)
#转换为gif
def png2gif(dir_name):
    path = os.getcwd()
    os.chdir(dir_name)
    dirs = os.listdir(dir_name)
    images = []
    num = 0
    for d in dirs:
        if d.split('-')[-1] == 'txt.png':
            images.append(imageio.imread(d))
            num += 1
    os.chdir(path)
    imageio.mimsave(d.split('-')[0]+'-txt_c.gif',images,duration = DURARION)
if __name__=='__main__':
    gif2png(File)
    path = os.getcwd()
    png2gif(path+"/Cache")


