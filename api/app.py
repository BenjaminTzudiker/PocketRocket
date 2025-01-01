'''Main executable to start a backend server'''

from routes import app

print('PocketRocket backend is running')

if __name__ == "__main__":
    app.run()
