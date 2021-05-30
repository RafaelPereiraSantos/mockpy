import os
from dotenv import load_dotenv
import webbrowser
from src import app

load_dotenv()

if __name__ == "__main__":
    debugging = os.getenv("ENVRIOMENT") == "development"
    open_browser = os.getenv("OPEN_BROWSER_ON_START") != "no"
    if not debugging and open_browser:
      webbrowser.open('http://localhost:' + os.getenv("PORT") + "/wellcome")
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=debugging)
