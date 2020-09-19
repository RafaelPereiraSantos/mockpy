import os
from dotenv import load_dotenv
import webbrowser
from src import app

load_dotenv()

if __name__ == "__main__":
    debugging = os.getenv("ENVRIOMENT") == "development"
    # if not debugging:
      # webbrowser.open('http://localhost:' + os.getenv("PORT") + "/hi-there")
    app.run(port=os.getenv("PORT"), debug=debugging)
