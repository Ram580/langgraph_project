from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file=None):
        # Use os.path for cross-platform compatibility
        if config_file is None:
            config_file = os.path.join(
                "C:/Users/LENOVO/OneDrive - Manipal Academy of Higher Education/GEN AI/Langgraph/langgraph_project/src/langgraphagenticai/ui",
                "uiconfigfile.ini"
            )
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")