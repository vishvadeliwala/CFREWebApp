import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/myapp')

from myapp import app as application

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=5002)
