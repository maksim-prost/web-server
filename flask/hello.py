from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Debug info')
    return 'Hello  difficult World! '

@app.route('/post',methods=['POST'])
def method_post():
    print(request.get_json())
   
    return str(request.get_json().keys())

if __name__ == '__main__':
    app.run()