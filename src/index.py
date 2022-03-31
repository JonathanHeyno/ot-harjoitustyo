import sys
from ui.app import App

def main():
    args = sys.argv[1:]
    if len(args) > 0:
        print("args:", args)
    
    app = App()
    app.run()

if __name__ == "__main__":
    main()
