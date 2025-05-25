import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.langgraphagenticai.main import load_langgraph_agenticai_app


if __name__=="__main__":
    load_langgraph_agenticai_app()