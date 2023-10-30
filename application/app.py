from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calculate_compound_interest():
    returns = ''
    form_data = {}  # Create an empty dictionary to store form data

    if request.method == 'POST':
        form_data['principal'] = float(request.form.get('principal'))
        form_data['rate'] = float(request.form.get('rate'))
        form_data['times'] = int(request.form.get('times'))
        form_data['num_of_years'] = int(request.form.get('num_of_years'))
        
        returns = round(form_data['principal'] * (1 + (form_data['rate'] / form_data['times']) / 100) ** (form_data['times'] * form_data['num_of_years']), 2)

    return render_template('index.html', returns=returns, form_data=form_data)
    
@app.route('/stock_calculator', methods=['POST', 'GET'])
def calculate_stock_return():
    Tg_Percen = ''
    SL_Percen = ''
    form_data = {}
    if request.method == 'POST':
        form_data['CMP_Decimal'] = float(request.form.get('cmp'))
        form_data['Tg_Decimal'] = float(request.form.get('tg'))
        form_data['SL_Decimal'] = float(request.form.get('sl'))

        Tg_Percen = round(((form_data['Tg_Decimal'] - form_data['CMP_Decimal']) * 100 / form_data['CMP_Decimal']), 2)
        SL_Percen = round(((form_data['CMP_Decimal'] - form_data['SL_Decimal']) * 100 / form_data['CMP_Decimal']), 2)

    return render_template('stock_calculator.html', Tg_Percen=Tg_Percen, SL_Percen=SL_Percen, form_data=form_data)


if __name__ == '__main':
    app.run(debug=True)
