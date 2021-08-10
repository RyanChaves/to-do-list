from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

list_one = {
    "name":"list one",
    "contents":[
        "item 1", "item 2", "item 3"
    ]
}
list_two = {
    "name":"list two",
    "contents":[
        "item 1", "item 2", "item 3"
    ]
}
list_three = {
    "name":"list three",
    "contents":[
        "item 1", "item 2", "item 3"
    ]
}
list_four = {
    "name":"list four",
    "contents":[
        "item 1", "item 2", "item 3"
    ]
}



@app.route('/')
def index():

    return render_template("index.html", list_one=list_one, list_two=list_two, list_three=list_three, list_four=list_four)


@app.route('/add/<list_num>')
def add_item(list_num):
    global list_one,list_two,list_three,list_four
    print('er')
    if list_num=='1':
        list_one['contents'].append("")
        print(list_one)
    elif list_num=='2':
        list_two['contents'].append("")
    elif list_num == '3':
        list_three['contents'].append("")
    elif list_num == '4':
        list_four['contents'].append("")
    return redirect(url_for('index'))

@app.route('/delete/')
def delete_item():
    global list_one,list_two,list_three,list_four
    list_num=request.args.get('list_num')
    item_num=int(request.args.get('item_num'))
    print(list_one)

    if list_num=='1':
        del list_one['contents'][item_num]
    elif list_num=='2':
        del list_two['contents'][item_num]
    elif list_num=='3':
        del list_three['contents'][item_num]
    elif list_num=='4':
        del list_four['contents'][item_num]
    print(list_one)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)