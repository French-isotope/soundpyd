from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

player_one = str(parser.get('CHARACTERS', 'PLAYER_1'))
player_two = str(parser.get('CHARACTERS', 'PLAYER_2'))

if __name__ == "__main__":
    print (player_one + ", I'd like for you to meet " + player_two + ".")
    print (player_two + ", this is your cousin " + player_one + ".\n")
