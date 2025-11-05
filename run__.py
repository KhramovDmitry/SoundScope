import app
import sys

DYLD_LIBRARY_PATH="/Users/DmitryKhramov/Desktop/SoundScope/.venv/lib/python3.13/site-packages/pygame/.dylibs"

def main():
    oApp = app.Application()

    try:
        oApp.run()
    except KeyboardInterrupt:
        print('Programm Interrupted')
    finally:
        pass
        #sys.exit()


if __name__ == "__main__":
    main()

#   DYLD_LIBRARY_PATH="/Users/DmitryKhramov/Desktop/SoundScope/.venv/lib/python3.13/site-packages/pygame/.dylibs" python3 run__.py