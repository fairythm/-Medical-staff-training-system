from flask import Flask,url_for,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        message = {'text1':text1,'text2':text2}
        return render_template('result.html',message=message)
    return redirect('/')

@app.route('/Adios/')
def adios():
    return 'Adios!'

@app.route('/user/<username>/')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<float:post_id>')
def show_post(post_id):
    return 'Post: %.2f' % post_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')