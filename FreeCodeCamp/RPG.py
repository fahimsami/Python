full_dot = '●'
empty_dot = '○'

def create_character(name = 'None', strength = '1', intelligence = '1', charisma = '1'):
    if name != str(name):
        print('Name must be a string.')
        raise TypeError('Name must be a string.')
    elif name == '':
        raise ValueError('Character should have a name')
    elif len(name)>10:
        raise ValueError('Name should be less than 10 characters')
    elif name.count(' ') != 0:
        raise ValueError('Name should not contain spaces')
    if strength != int(strength) or intelligence != int(intelligence) or charisma != int(charisma):
        raise TypeError("All stats must be integers.")
    if strength < 1 or intelligence < 1 or charisma < 1 :
        raise ValueError("All stats must be no less than 1.")   
    if strength > 4 or intelligence > 4 or charisma > 4:
        raise ValueError("All stats must be no more than 4.")
    if sum([strength, intelligence, charisma]) != 7:
        raise ValueError("Total stats must equal 7.")

    print(f"Name: {name}")
    print(f"Strength: {full_dot * strength}{empty_dot * (10 - strength)}")
    print(f"Intelligence: {full_dot * intelligence}{empty_dot * (10 - intelligence)}")
    print(f"Charisma: {full_dot * charisma}{empty_dot * (10 - charisma)}")
    
    
    
    
create_character('ren', 4,2, 1)   

num = list(range(1,21))
print([(n, 'Even') if n % 2 == 0 else (n, 'Odd') for n in num])