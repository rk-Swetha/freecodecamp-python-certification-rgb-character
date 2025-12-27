def create_character(name, strength, intelligence, charisma):
    # 1. Name validation (Must NOT end with a period)
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'

    # 2. Stats validation 
    # Use type() instead of isinstance() to strictly reject Booleans
    stats = [strength, intelligence, charisma]
    for s in stats:
        if type(s) is not int:
            return 'All stats should be integers'
    
    # 3. Value range and sum validation
    if any(s < 1 for s in stats):
        return 'All stats should be no less than 1'
    if any(s > 4 for s in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'

    # 4. Stat visualization using dots
    full_dot = '●'
    empty_dot = '○'
    
    # Building the lines precisely as requested
    res = f"{name}\n"
    res += f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
    res += f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
    res += f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    
    return res
