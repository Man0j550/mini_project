from flask import  Flask,render_template,request
import pandas as pd 

data = pd.read_excel("Copy of miniprojectdata.xlsx")


def get_product(product):
    product=product.split()
    for item in product:
        found = data[data['Product_name'].str.contains(item, case=False, na=False, regex=True)]
        if not found.empty:
            found=found.iloc[0].to_dict()
            found['Price']='₹'+str(found['Price'])
            return found
    return 'Null'

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/catogary1')
def catogary1():
    return render_template('Electronics.html')
@app.route('/catogary2')
def catogary2():
    return render_template('Automobiles.html')
@app.route('/catogary3')
def catogary3():
    return render_template('Fashion.html')
@app.route('/catogary4')
def catogary4():
    return render_template('Foodandbevarages.html')
@app.route('/catogary5')
def catogary5():
    return render_template('Groceries.html')
@app.route('/catogary6')
def catogary6():
    return render_template('Furniture.html')
@app.route('/catogary7')
def catogary7():
    return render_template('Basicneed.html')
@app.route('/catogary8')
def catogary8():
    return render_template('Consumereducation.html')
@app.route('/catogary9')
def catogary9():
    return render_template('Information.html')
@app.route('/catogary10')
def catogary10():
    return render_template('Makechoice.html')
@app.route('/catogary11')
def catogary11():
    return render_template('Safety.html')
@app.route('/catogary12')
def catogary12():
    return render_template('Seekredressal.html')
@app.route('/chat')
def chat():
    return render_template('Chat.html')
@app.route('/chatBot',methods=['GET','PoST'])
def chatBot():
    product=request.form.to_dict()['product']
    #print(product)
    product=product.lower()
    if product in ['bye','goodbye']:
        return render_template('Chat.html',result='Goodbye!',mi=product)
    if product in ['hi','hello']:
        return render_template('Chat.html',result='Hello! how can i help you?',mi=product)
    item=get_product(product)
    if item != 'Null':
        #print(item)
        return render_template('Chat.html',result=item, mi=product)
    else:
        return render_template('Chat.html',result="No products were found, search for Product.",mi=product)
if __name__=="__main__":
    app.run(debug=True)