def validate_password(password):
    #check length of password
    if len(password) < 8:
        return False
    
    #check for uppercase letters, lowercase letters and numbers 
    if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and " " not in password:
        return True
    else:
        return False
      
    
