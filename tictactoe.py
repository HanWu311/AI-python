"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    player 函数应该以棋盘状态作为输入，并返回轮到哪个玩家（X 或 O）。
    在初始游戏状态下，X 获得第一步。随后，玩家交替进行每一个动作。
    如果提供结束棋盘状态作为输入（即游戏已经结束），则任何返回值都是可接受的。
    """


    raise NotImplementedError


def actions(board):
    """
    actions 函数应该返回一组在给定的棋盘状态上可以采取的所有可能的操作。

    每个动作都应该表示为元组 (i，j) ，其中 i 对应于移动的行（0、1 或 2）， j 对应于行中的哪个单元格对应于移动（也是 0、1、或 2）。
    可能的移动是棋盘上任何没有 X 或 O 的单元格。
    如果提供结束棋盘状态作为输入，则任何返回值都是可接受的。
    """
    raise NotImplementedError


def result(board, action):
    """
    result 函数以一个棋盘状态和一个动作作为输入，并且应该返回一个新的棋盘状态，而不修改原始棋盘。
    如果 action 函数接受了一个无效的动作，你的程序应该raise an exception.
    返回的棋盘状态应该是从原始输入棋盘，并让轮到它的玩家在输入动作指示的单元格处移动所产生的棋盘。
    重要的是，原始棋盘应该保持不变：因为 Minimax 最终需要在计算过程中考虑许多不同的棋盘状态。
    这意味着简单地更新棋盘上的单元格本身并不是 result 函数的正确实现。在做出任何更改之前，你可能需要先对棋盘状态进行deep copy。
    """
    raise NotImplementedError


def winner(board):
    """
    winner 函数应该接受一个棋盘作为输入，如果游戏结束，则返回游戏的获胜者。

    如果 X 玩家赢得了游戏，函数应该返回 X。如果 O 玩家赢得了比赛，函数应该返回 O。
    一个人可以通过水平、垂直或对角连续三次移动赢得比赛。
    你可以认为最多会有一个赢家（也就是说，没有一个棋盘会同时有两个玩家连着三个，因为这将是一个无效的棋盘状态）。
    如果游戏没有赢家（要么是因为游戏正在进行，要么是因为比赛以平局结束），函数应该返回 None 。
    """
    raise NotImplementedError


def terminal(board):
    """
    terminal 函数应该接受一个棋盘作为输入，并返回一个布尔值，指示游戏是否结束。

    如果游戏结束，要么是因为有人赢得了游戏，要么是由于所有单元格都已填充而没有人获胜，则函数应返回 True 。
    否则，如果游戏仍在进行中，则函数应返回 False 。
    """
    raise NotImplementedError


def utility(board):
    """
    utility 函数应接受结束棋盘状态作为输入，并输出该棋盘的分数。

    如果 X 赢得了比赛，则分数为 1。如果 O 赢得了比赛，则分数为 -1。如果比赛以平局结束，则分数为 0。
    你可以假设只有当 terminal(board) 为 True 时，才会在棋盘上调用 utility 。
    """
    raise NotImplementedError


def minimax(board):
    """
    如果该棋盘是结束棋盘状态，则 minimax 函数应返回 None 。 
    
    对于所有接受棋盘作为输入的函数，你可以假设它是一个有效的棋盘（即，它是包含三行的列表，每行都有三个值 X、O 或 EMPTY）。
    你不应该修改所提供的函数声明（每个函数的参数的顺序或数量）。 一旦所有功能都得到了正确的实现，你就应该能够运行 python runner.py 
    并与你的人工智能进行比赛。
    """
    raise NotImplementedError
