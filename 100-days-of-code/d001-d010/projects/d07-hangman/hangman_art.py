stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

win = '''
                              _       
 _   _  ___  _   _  __      _(_)_ __  
| | | |/ _ \| | | | \ \ /\ / / | '_ \ 
| |_| | (_) | |_| |  \ V  V /| | | | |
 \__, |\___/ \__,_|   \_/\_/ |_|_| |_|
 |___/                                
'''

lose = '''
                      _                
 _   _  ___  _   _   | | ___  ___  ___ 
| | | |/ _ \| | | |  | |/ _ \/ __|/ _ \\
| |_| | (_) | |_| |  | | (_) \__ \  __/
 \__, |\___/ \__,_|  |_|\___/|___/\___|
 |___/                                 
'''



line = "-"

lines = "{:-^50}".format(line)

logo = lines + logo + lines

lose = lines + lose + lines

win = lines + win + lines