import sys
from PyQt5.QtCore import QUrl  # QUrlをインポート
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("URLビューワー")
        self.setGeometry(100, 100, 800, 600)

        # レイアウトの作成
        layout = QVBoxLayout()

        # URL入力ボックス
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("URLを入力してください...")
        layout.addWidget(self.url_input)

        # 開くボタン
        open_button = QPushButton("開く", self)
        open_button.clicked.connect(self.open_url)
        layout.addWidget(open_button)

        # WebEngineView（埋め込みブラウザ）の設定
        self.browser = QWebEngineView(self)
        layout.addWidget(self.browser)

        # レイアウトの設定
        self.setLayout(layout)

    def open_url(self):
        url = self.url_input.text()  # 入力されたURLを取得
        if url:
            # "http://" または "https://" が指定されていなければ、追加する
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
            self.browser.setUrl(QUrl(url))  # QUrl型に変換して設定

# アプリケーションの実行
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebApp()
    window.show()
    sys.exit(app.exec_())
