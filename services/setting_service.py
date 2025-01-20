import logging
from models.setting import Setting
from utils.database import db

logger = logging.getLogger(__name__)

def get_setting(key_name):
    """
    Retrieve the value of a specific setting by its key name.
    :param key_name: The name of the setting.
    :return: The value of the setting or None if not found.
    """
    try:
        setting = Setting.query.filter_by(key_name=key_name).first()
        return setting.value if setting else None
    except Exception as e:
        logger.error(f"Error fetching setting {key_name}: {e}")
        return None

def update_setting(key_name, value):
    """
    Update the value of a specific setting.
    :param key_name: The name of the setting to update.
    :param value: The new value for the setting.
    :return: The updated setting or None if an error occurs.
    """
    try:
        setting = Setting.query.filter_by(key_name=key_name).first()
        if not setting:
            return None

        setting.value = value
        db.session.commit()
        return setting
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating setting {key_name}: {e}")
        return None
