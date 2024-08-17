# coding=utf-8
import Tkinter
import os
from Saper.constants import *


class Ceil(object):
    """
    Класс ячейки
    """

    number_in_row = 0

    number_in_all = 0
    """Номер ячейки по порядку,среди всех ячеек"""

    is_mine = False
    is_open = False

    is_user_select_mine = False
    """ Поставил ли пользователь сюда мину или нет"""

    count_mine_around = 0
    """ кол-во мин вокруг ячейки"""

    _row = None
    """:type: Saper.Row"""

    event_right_click = None
    event_left_click = None

    def __init__(selfself, number_in_row,tk_frame_parent):
        """

        :param number_in_row: Номер в строке
        :tepe number_in_row: int
        :param tk_frame_parent: Основной Frame Tkinter
        :type tk_frame_parent:  """
