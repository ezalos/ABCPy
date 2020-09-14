from flask import Flask
from config import Config


# The __name__ variable passed to the Flask class is a Python predefined
# variable, which is set to the name of the module in which it is used.
app = Flask(__name__)
app.config.from_object(Config)

# The routes module is imported at the bottom and not at the top
# It's a workaround to circular imports :
    # The routes module needs to import the app variable defined in this script,
    # so putting one of the reciprocal imports at the bottom avoids the error
    # that results from the mutual references between these two files.

from app import routes

# The app package is defined by the app directory and the __init__.py script,
#   and is referenced in the from app import routes statement. 
# The app variable is defined as an instance of class Flask in the __init__.py
#   script, which makes it a member of the app package.
