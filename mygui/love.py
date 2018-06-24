import tkinter as tk
import time
import tkinter.messagebox


def Love():
    love = tk.Toplevel(window)
    love.geometry('300x200')
    love.title("好巧,我也是")
    lable = tk.Label(love, text="好巧,我也是", font=("微软雅黑", 24))
    btn = tk.Button(love, text="确定", width=8, font=("微软雅黑", 12))
    btn.config(command=lambda: closelove(love))
    lable.pack()
    love.protocol('WM_DELETE_WINDOW', closeall)
    btn.pack()


def NoLove():
    no_love = tk.Toplevel(window)
    no_love.geometry('300x200')
    no_love.title("在考虑考虑呗")
    lable = tk.Label(no_love, text="在考虑考虑呗", font=("微软雅黑", 24))
    btn = tk.Button(no_love, text="确定", width=8, font=("微软雅黑", 12))
    btn.config(command=lambda: closenolove(no_love))
    lable.pack()
    btn.pack()


def closeWindow():
    tkinter.messagebox.showerror(title="警告", message="不许关闭,好好回答!")
    return


def closeall():
    window.destroy()


def closelove(love):
    window.destroy()

def closenolove(no_love):
    no_love.destroy()


window = tk.Tk()
window.geometry('500x300')
window.title('你喜欢我吗?')
window.protocol('WM_DELETE_WINDOW', closeWindow)

lable1 = tk.Label(window, text="hey,二晶同学", font=("微软雅黑", 14))
lable2 = tk.Label(window, text="你喜欢我吗?", font=("微软雅黑", 28))

photo = tk.PhotoImage(file='1.gif')
imgLabel = tk.Label(window, imag=photo)

btn1 = tk.Button(window, text="喜欢", width=8, font=("微软雅黑", 12))
btn1.config(command=Love)
btn2 = tk.Button(window, text="不喜欢", width=8, font=("微软雅黑", 12))
btn2.config(command=NoLove)

lable1.pack()
lable2.pack()
imgLabel.pack()
btn1.pack(padx=80, pady=10, side=tk.LEFT)
btn2.pack(padx=10, pady=10, side=tk.LEFT)

window.mainloop()
