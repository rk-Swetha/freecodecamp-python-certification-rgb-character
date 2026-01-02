"""
Build a User Configuration Manager
Part of the freeCodeCamp Python Certification Course

Author: Swetha R.K.
"""

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

def add_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings,pair):
    key = pair[0].lower()
    value = pair[1].lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
    
def delete_setting(settings,key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = ["Current User Settings:"]
    for key, value in settings.items():
        result.append(f"{key.capitalize()}: {value}")

    return "\n".join(result) + "\n"

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
