# ResizeWindow - Windows 限定 視窗縮放控制器

這是一個用 Python 製作的輕量級工具，可調整 **MapleStory Worlds** 視窗的位置與大小，並透過熱鍵快速切換尺寸或隱藏視窗，適合在多工環境下靈活使用。

> 📌 本工具不會修改遊戲內容，只影響視窗外觀設定。

---

## 🧩 功能介紹

* 🔍 自動偵測「特定名稱」視窗
* 🫥 最小化視窗並移出畫面以達到「隱藏」效果
* ⌨️ 持續監聽熱鍵，直到手動退出為止

---

## ⌨️ 熱鍵對應

| 熱鍵    | 功能                  |
| ----- | ------------------- |
| `F4`  | 隱藏視窗（256x144 並移出畫面） |
| `F5`  | 切換為 640x360         |
| `F6`  | 切換為 854x480         |
| `F7`  | 切換為 1280x720        |
| `F10` | 結束程式                |

---

## 🛠️ 安裝方式

### 1. 安裝必要套件

```bash
pip install pygetwindow pywin32 keyboard
```

### 2. 執行腳本

```bash
python resize_window.py
```

> 請確認該程式視窗已經啟動，再執行本程式。

---

## 📦 打包成 EXE（可選）

若希望無需 Python 環境即可執行，可使用 PyInstaller 打包：

```bash
pip install pyinstaller
pyinstaller --onefile resize_window.py
```

打包後的 `.exe` 將位於 `dist/` 資料夾中。

---

## ⚠️ 注意事項

* 僅支援 Windows 作業系統
* 視窗名稱須為 `MapleStory Worlds`（可依視窗實際名稱調整）
* 若視窗無反應，請確認程式有足夠權限，或視窗未被其他工具鎖定

---

## 🧑‍💻 作者

本專案由 \[daron0811] 製作，屬於 `daron-python-tool-colleaction` 的一部分。

歡迎貢獻、討論或 Fork 修改！
