#!flask/bin/python
def go():
	from app import app
	import sys
	if "debug" in sys.argv:
		print("Running in debug mode.")
		app.run(host='0.0.0.0')
	elif "all" in sys.argv:
		print("Running in all IP mode.")
		app.run(host='0.0.0.0')
	else:
		print("Running in normal mode.")
		app.run()

if __name__ == "__main__":
	go()
