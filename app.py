from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return u'<h1>%s，多喝热水！</h1><img src="http://helloflask.co\
m/totoro.gif">' % name

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（在命令行窗口查看输入的URL）
    print(url_for('hello'))

    print(url_for('user_page',name = '路人甲'))

    print(url_for('user_page',name = 'guestA'))

    print(url_for('test_url_for'))

    print(url_for('test_url_for',num=2))

    return 'Test Page'
