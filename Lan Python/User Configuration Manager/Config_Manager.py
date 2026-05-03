def add_setting(setting, setting_value):
    key, value = setting_value
    
    key = key.lower()
    value = value.lower()
    
    if key in setting:
        return f"Setting {key} already exists! Cannot add a new setting with this name."
    
    setting[key]=value
    return f'Setting {key.lower()} added with value {value.lower()} successfully!'
   
def update_setting(setting, setting_value):
    key, value = setting_value
    
    key = key.lower()
    value = value.lower()   
    
    if key in setting:
        setting[key]=value
        return f"Setting {key.lower()} updated to {value.lower()} successfully!"   
    if key not in setting:
        return f"Setting {key.lower()} does not exist! Cannot update a non-existing setting."

def delete_setting(setting, setting_value):
    
    key = setting_value
    key = key.lower()
    
    if key in setting:
        del setting[key]
        return f"Setting {key.lower()} deleted successfully!"  
    if key not in setting:
        return "Setting not found!"
    
def view_setting(setting):
    if not setting:
        return "No settings available!"
    if setting:
        return f"Current User Settings:\n" + "\n".join([f"{key.capitalize()} : {value}" for key, value in setting.items()])
    
test_setting = { 'theme': 'dark', 'notifications': 'enabled' }
print(add_setting(test_setting, ('language', 'english')))
print(update_setting(test_setting, ('theme', 'light')))
print(update_setting(test_setting, ('theme', 'dark')))
print(view_setting(test_setting))