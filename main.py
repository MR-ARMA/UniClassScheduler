import tkinter as tk
from gui.app import App
import logging

def main():
    """Launch the University Class Scheduler application."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        logging.error(f"Failed to launch application: {str(e)}")
        raise

if __name__ == "__main__":
    main()