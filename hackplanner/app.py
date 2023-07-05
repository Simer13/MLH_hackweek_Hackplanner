from Flask import Flask, render_template, request, redirect

app=Flask(__name__)

items =[]
db+path = 'checklist.db'
def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''create table if not exists checklist 
              (if integer primary key autocorrect, item text)''')
    conn.coomit()
    conn.close()
    
 
@app.route('/')
def checklist():
    return render_template('checklist.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item=request.form['item']
    items.append(item)
    return redirect('/')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item=items[item_id-1]
    if request.method == 'POST':
        new_item = request.form['item']
        items[item_id -1]= new_item
        return redirect('/')
    
    return render_template('edit.html', items=item, item_id=item_id)

@app.rpute('/delete/<int:item_id>')
def delete_item(item_id):
    del items[item_id -1]
    return redirect('/')

