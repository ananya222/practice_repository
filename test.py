from flask import Flask, request, render_template
import csv


app=Flask(__name__)

with open("temperatures.csv", 'r') as file:
  csvreader = csv.reader(file)
  rows=[]
  for row in csvreader:
    rows.append(row)

def get_temp(city):
    for row in rows:
        if row[0]==city:
            return row[1]

def palindrome(num):
    num_str=str(num)
    for i in range(0,len(num_str)):
        if num_str[i]!=num_str[-(i+1)]:
            return False
    return True

@app.route('/palindrome', methods=['GET','POST']) 
def is_palindrome(): 
    if request.method == 'POST':
        num = request.form.get('num')
        message = str(palindrome(num))
        return render_template('palindrome.html',message=message)
    return render_template('palindrome.html')

@app.route('/temperature', methods=['GET','POST']) 
def get_temperature(): 
    if request.method == 'POST':
        city = request.form.get('city')
        message = get_temp(city)
        return render_template('temperature.html',message=message)
    return render_template('temperature.html')

if __name__ == '__main__':
    app.run(debug=True)