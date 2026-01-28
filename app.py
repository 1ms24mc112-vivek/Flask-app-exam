from flask import Flask
app=Flask()

@app.route('/')
def home():
	return "flask application is running successfully"

if __name__ = "__main__":
	return('host=0.0.0.0',port=5000)

