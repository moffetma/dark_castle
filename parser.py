import os
import json

class Parse:
  def __init__(self):
    self.verbs = {'grab':'grab', 'get':'get', 'take':'take', 'pick':'pick up', 'pick up':'pick up',
          'drop':'drop', 'go':'go',
          'look at':'look at',
          'look under':'look under',
          'unlock':'unlock',
          'try on':'try on',
          'move':'go',
          'open':'open',
          'read':'read',
          'enter':'enter',
          'watch':'watch',
          'turn on':'turn on',
          'use':'use',
          'activate':'activate',
          'cut':'cut',
          'rescue':'rescue',
          'talk to':'talk to'
    }
    self.determiner = [
          'a',
          'an',
          'some',
          'that',
          'the',
          'these'
          'this',
          'those'
    ]
    self.direction = {
          'down':'down',
          'e':'east',
          'east':'east',
          'north':'north',
          'n':'north',
          'south':'south',
          's':'south',
          'up':'up',
          'west':'west',
          'w':'west',
          'above':'up',
          'below':'down'
    }

    self.characters = [
      'sansa', 'luke', 'rick and morty', 'jon stark', 'arya stark', 'roose bolton', 'tyrion lannister', 'jon aryn'
    ]

    self.items = [ 'key', 'paper', 'desk', 'fountain', 'button', 'computer', 'lamp']

    self.prepositions = ["about", "above", "across", "after", "against", "along", "among", "around", "at",
                        "before", "behind", "below", "beneath", "beside", "between", "by", "down", "during", 
                        "except", "for", "from", "front", "in", "inside","instead", "into", "like", "near", "of", 
                        "off", "on", "onto", "out", "outside", "over", "past","since", "through", "to", "top", 
                        "toward", "under", "underneath", "until", "up", "upon", "with", "within", "without"]

    self.rooms = ['sky light', 'french doors', 'revolving door', 'creeky stairs', 'blood soaked kitchen']

  def parse_user_input(self, input_string):
    if self.is_string_empty(input_string):
      return(None, None, None, None, None)
    
    word_list = self.convert_string_to_word_list(input_string.lower())
    word_list = self.remove_definitive_articles(word_list)
    
    if len(word_list) == 0:
      return None, None, None, None, None
    
    cmd = self.get_command_prompt(word_list)

    if len(word_list) == 0:
      return None, None, None, None, None

    if cmd is None:
      cmd = 'go'
    elif cmd == 'go':
      cardinal_direction = self.get_direction(word_list)
      room = self.match_noun(word_list, self.rooms)

      if cardinal_direction and room is None:
        return cmd, None, cardinal_direction, None, None

      if cardinal_direction is None and room:
        return cmd, room, None, None, None

      if cardinal_direction and room:
        return None, None, None, None, None

    character = self.match_noun(word_list, self.characters)
    item = self.match_noun(word_list, self.items)

    return cmd, None, None, item, character

  def match_noun(self, user_input_list, reference_list):
    number_of_user_input_elements = len(user_input_list)
    for word in reference_list:
      new_word_list = self.convert_string_to_word_list(word)
      
      for index in range(number_of_user_input_elements):
        if new_word_list == user_input_list[index:(index + len(new_word_list))]:
          return ' '.join(new_word_list)
    
    return None

  def convert_string_to_word_list(self, string):
    return string.split()
  
  def remove_definitive_articles(self, word_list):
    return [word for word in word_list if word not in self.determiner]

  def get_command_prompt(self, word_list):

    cmd = None
    preposition = None
    if len(word_list) > 1:
      preposition = self.match_noun([word_list[1]], self.prepositions)
      print("prep: ", preposition)

    if word_list[0] in self.verbs:
      cmd = self.verbs[word_list[0]]
      del word_list[0]
      if preposition:
        new_action = cmd + ' ' + preposition
        print("new action: ", new_action)
        if new_action in self.verbs:
          cmd = self.verbs[new_action]
          del word_list[0]

    elif len(word_list) > 1 and cmd is None and preposition is not None:
      new_action = word_list[0] + ' ' + preposition
      if new_action in self.verbs:
        cmd = self.verbs[new_action]
        del word_list[0]
        del word_list[0]

    return cmd
  
  def get_direction(self, word_list):
    direction = None
    if word_list[0] in self.direction:
      direction = self.direction[word_list[0]]
    
    return direction

  def is_string_empty(self, string):
    if string is None:
      return True
    else:
      return False

def main():
  parser = Parse()
  while True:
    prompt = input("What Move Would You Like to Do? ")
    if prompt ==  'q':
      break
    action, room, direction, room_item, character = parser.parse_user_input(prompt)
    print("This is the action: ", action)
    print("This is the direction: ", direction)
    print("This is the room: ", room) 
    print("This is the room_item: ", room_item) 
    print("This is the character: ", character) 

main()