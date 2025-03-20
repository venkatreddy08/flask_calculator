from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<operation>', methods=['GET', 'POST'])
def calculate(operation):
    result = None
    operation_name = {
        "add": "Addition",
        "sub": "Subtraction",
        "mult": "Multiplication",
        "div": "Division"
    }.get(operation, "Operation")

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mult":
                result = num1 * num2
            elif operation == "div":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        except ValueError:
            result = "Invalid input"

    return render_template('calculate.html', operation_name=operation_name, result=result, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)
