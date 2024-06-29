import os
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv
from yookassa import Configuration

from wireguard_tools.wireguard_config import WireguardConfig

MY_TG_ID = 506954303

VPN_BOT_DIR = Path(__file__).parent
WORK_DIR = VPN_BOT_DIR.parent

load_dotenv(WORK_DIR / ".env")

DEBUG = os.environ.get("DEBUG") == "True"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_TG_URL = os.environ.get("BOT_URL")

DATABASE_URL = os.environ.get("DATABASE_URL")

PATH_TO_CLIENTS_FILES = VPN_BOT_DIR / "tmp_client_files/"
SYNC_CONFIG_FILE_PATH = WORK_DIR / "wireguard_tools/sync_config.sh"

WG_CONFIGS_PATH = Path(os.environ.get("WG_CONFIGS_PATH"))
_WG0_CONFIG_PATH = WG_CONFIGS_PATH / "wg0.conf"
_WG1_CONFIG_PATH = WG_CONFIGS_PATH / "wg1.conf"

_wg0_config = WireguardConfig()
_wg1_config = WireguardConfig()

_wg0_config.set_config(
    interface="wg0",
    private_key=os.environ.get("WG0_SERVER_PRIVATE_KEY"),
    endpoint=os.environ.get("WG0_SERVER_ENDPOINT"),
    config_path=_WG0_CONFIG_PATH,
    sync_config_file_path=SYNC_CONFIG_FILE_PATH,
    debug=DEBUG,
)

_wg1_config.set_config(
    interface="wg1",
    private_key=os.environ.get("WG1_SERVER_PRIVATE_KEY"),
    endpoint=os.environ.get("WG1_SERVER_ENDPOINT"),
    config_path=_WG1_CONFIG_PATH,
    sync_config_file_path=SYNC_CONFIG_FILE_PATH,
    debug=DEBUG,
)

WIREGUARD_CONFIG_MAP: Dict[str, WireguardConfig] = {
    "wg0": _wg0_config,
    "wg1": _wg1_config,
}

# YOOKASSA
YOOKASSA_OAUTH_TOKEN = os.environ.get("YOOKASSA_OAUTH_TOKEN")
Configuration.configure_auth_token(YOOKASSA_OAUTH_TOKEN)

ALLOWED_IPS = {
    "127.0.0.1",
    "localhost",
    "192.168.65.1",
    "185.71.76.0",
    "185.71.76.0/27",
    "185.71.77.0",
    "185.71.77.0/27",
    "77.75.153.0",
    "77.75.153.0/25",
    "77.75.156.11",
    "77.75.156.35",
    "77.75.154.128",
    "77.75.154.128/25",
    "2a02:5180::/32",
}
