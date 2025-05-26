import pygetwindow as gw
import keyboard
import time
import ctypes

# 選擇目標視窗名稱
target_title = "MapleStory Worlds"

# 嘗試取得視窗
def get_window():
    windows = [w for w in gw.getWindowsWithTitle(target_title) if w.visible]
    return windows[0] if windows else None

# 強制調整視窗大小
def set_window_size(win, width, height):
    ctypes.windll.user32.MoveWindow(win._hWnd, win.left, win.top, width, height, True)

print("等待 MapleStory Worlds 視窗...")
time.sleep(5)
win = get_window()

if not win:
    print("找不到 MapleStory Worlds 視窗，請確認遊戲已開啟。")
    time.sleep(3) 
    print("3秒後將自動關閉此程式")
    exit()

print("✅ 已偵測到視窗，請按按鍵（F4隱藏視窗，F5~F7 改大小，F10 關閉此程式）")

# 鍵盤事件監聽迴圈
while True:
    try:
        if keyboard.is_pressed("F5"):
            set_window_size(win, 640, 360)
            win.moveTo(0, 0)
            print("🔄 切換為 640x360")
            time.sleep(0.5)  # 防止多次觸發

        elif keyboard.is_pressed("F4"):
            set_window_size(win, 256, 144)
            win.moveTo(-256, 144)
            print("🔄 隱藏，並切換最小視窗 256x144")
            time.sleep(0.5)

        elif keyboard.is_pressed("F6"):
            set_window_size(win, 854, 480)
            win.moveTo(0, 0)
            print("🔄 切換為 854x480")
            time.sleep(0.5)

        elif keyboard.is_pressed("F7"):
            set_window_size(win, 1280, 720)
            win.moveTo(0, 0)
            print("🔄 切換為 1280x720")
            time.sleep(0.5)

        elif keyboard.is_pressed("F10"):
            print("3秒後將自動關閉此程式")
            time.sleep(3) 
            exit()
            break

        time.sleep(0.1)
    except:
        break
