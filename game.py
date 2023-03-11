"""
Lab_4, Task_5 (module with classes for main.py (game))
"""


class Room:
    """
    The class create room
    """

    def __init__(self, room_name: str):
        """
        The function set param
        :param room_name: name of room
        """
        self.room_name = room_name
        self.description = ''
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description: str):
        """
        The func do something
        :param description:
        :return:
        """
        self.description = description

    def set_character(self, enemy):
        """
        Te function set character
        :param enemy:
        :return:
        """
        self.character = enemy

    def get_description(self):
        """
        The func return description
        :return:
        """
        return self.description

    def get_character(self):
        """
        The func return character
        :return:
        """
        return self.character

    def link_room(self, linked_room, direction: str):
        """
        The func do something
        :return:
        """
        self.linked_rooms.update({linked_room: direction})

    def get_details(self):
        """
        The func do something
        :return:
        """
        print(self.room_name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {self.room_name} is {self.linked_rooms[direction]}")

        # print(self.name)
        # print("--------------------")
        # print(self.description)
        # for direction in self.linked_rooms:
        #     room = self.linked_rooms[direction]
        #     print("The " + room.name + " is " + direction)

    def set_item(self, item):
        """
        The func set rooms
        :return:
        """
        self.item = item

    def get_item(self):
        """
        The function return something
        :return:
        """
        return self.item

    def move(self, direction: str):
        """
        The function do something
        :return:
        """
        for i in self.linked_rooms.items():
            if i[1] == direction:
                return i[0]
        return self


class Character:
    """
    The class create character
    """

    def __init__(self, name: str, description: str):
        """
        The func set param
        """
        self.description = description
        self.name = name

    def describe(self):
        """
        The func describe character
        :return:
        """
        print(f"{self.name} is here!")
        print(self.description)


class Enemy(Character):
    """
    The class create enemy
    """
    defeated = 0

    def __init__(self, name: str, description: str):
        """
        The func set param
        """
        super().__init__(name, description)
        self.weakness = None
        self.conversation = None

    def set_weakness(self, weakness: str):
        """
        The func find weakness of enemy
        :return:
        """
        self.weakness = weakness

    def set_conversation(self, conversation: str):
        """
        The func do something
        :param conversation:
        :return:
        """
        self.conversation = conversation

    def fight(self, fight_with):
        """
        The function do something
        :return:
        """
        return self.weakness == fight_with

    def talk(self):
        """
        The func determine what character need to talk
        :return: string
        """
        print(f"[{self.name} says:] : {self.conversation}")

    def get_defeated(self):
        """
        The func do something
        :return:
        """
        Enemy.defeated += 1
        return Enemy.defeated


class Friend:
    """
    class do something
    """

    def __init__(self, name: str, description: str):
        """
        The func do something
        """
        super().__init__(name, description)


class Item:
    """
    Thr class
    """

    def __init__(self, name: str):
        """
        The func set param
        """
        self.name = name
        self.description = ''

    def get_name(self):
        """
        The func return name
        :return:
        """
        return self.name

    def set_description(self, description):
        """
        The func do something
        :param description:
        :return:
        """
        self.description = description

    def get_description(self):
        """
        The fun return description
        :return:
        """
        return self.description

    def describe(self):
        """
        The func do something
        :return:
        """
        print(f'The {self.name} is here - {self.description}')
