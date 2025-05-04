import os

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".shellix")
CREDENTIALS_FILE = os.path.join(CONFIG_DIR, "credentials")
DEFAULT_MODEL = "gpt-4.1"


def ensure_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR, exist_ok=True)
    if not os.path.exists(CREDENTIALS_FILE):
        setup_credentials()


def setup_credentials():
    # Check and add .shellix_memory.json to system-wide gitignore
    gitignore_global = os.path.expanduser('~/.gitignore_global')
    if os.path.exists(gitignore_global):
        with open(gitignore_global, 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            if '.shellix_memory.json\n' not in lines:
                f.write('.shellix_memory.json\n')
    else:
        with open(gitignore_global, 'w', encoding='utf-8') as f:
            f.write('.shellix_memory.json\n')
    os.system('git config --global core.excludesfile ~/.gitignore_global')
    print("Shellix Initial Setup")
    openai_key = input("Enter your OpenAI API key (https://platform.openai.com/docs/overview): ").strip()
    tavily_key = input("Enter your Tavily Search API key (Get it for free here: https://tavily.com/): ").strip()

    model_choice = input("Enter OpenAI model (press Enter for default gpt-4o): ").strip()
    selected_model = model_choice if model_choice else DEFAULT_MODEL

    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        f.write(f"OPENAI_KEY={openai_key}\n")
        f.write(f"TAVILY_KEY={tavily_key}\n")
        f.write(f"OPENAI_MODEL={selected_model}\n")

    print(f"Credentials and model selection saved to {CREDENTIALS_FILE}")


def load_credentials():
    ensure_config()

    credentials = {}
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            credentials[key] = value

    credentials.setdefault("OPENAI_MODEL", DEFAULT_MODEL)
    os.environ['TAVILY_API_KEY'] = credentials.get('TAVILY_KEY', '')
    return credentials
