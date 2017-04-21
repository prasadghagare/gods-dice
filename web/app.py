from web import appl
from flask import render_template,request

#crude for the sake of trying
n1=m1 = 0
@appl.route('/',methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        n1 = request.form['n1']
        m1 = request.form['m1']
        print("n1: ",n1)
    return render_template('landing.html')

#if __name__ == '__main__':
#    app.run()
