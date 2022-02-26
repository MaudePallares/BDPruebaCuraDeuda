from distutils.log import debug
from PagWeb import Flask, crearApp


app = crearApp()

if __name__ == '__main__':
    app.run(debug=True)




