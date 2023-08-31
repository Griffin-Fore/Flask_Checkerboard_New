from flask_app import app 
from flask_app.controllers import users # controllers go here #replace rename_controller with your controller file name. 
                                                    # Do not include .py

if __name__=='__main__':
    app.run(debug=True, port=5001) # debug needs to be set to False when deployed