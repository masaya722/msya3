from typing import Any


class FixedStack:
    """固定長スタッククラス"""

    class Empty(Exception):
        """空のFixedStackに対してpopあるいはpeekが呼び出されたときに送出する例外"""
        pass

    class Full(Exception):
        """満杯のFixedStackに対してpushが呼び出されたときに送出する例外"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """初期化"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        """スタックは満杯か"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """スタックにvalueをプッシュ"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """スタックからデータをポップ (頂上のデータを取り出す)"""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr -1]
    
    def clear(self) -> None:
        self.ptr = 0
    
    def find(self, value: Any)-> Any:
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c+=1
        return c
    
    def __contains__(self,value: Any) -> bool:
        return self.count(value)
    
    def dump(self) -> None:
        if self.is_empty():
            print('スタックは空です。')
        else:
            print(self.stk[:self.ptr])

from enum import Enum

Menu = Enum('Menu',['プッシュ','ポップ','ピーク','探索','ダンプ','終了'])
def select_menu() ->Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'現在のデータ数：{len(s)}/{s.capacity}')
    menu = select_menu()

    if menu == Menu.プッシュ:
        x = int(input('データ：'))
        try:
            s.push(x)
        except FixedStack.Full:
            print('スタックが満杯です。')    
    elif menu == Menu.ポップ:
        try:
            x = s.pop()
            print(f'ポップしたデータは{x}です。')
        except FixedStack.Empty:
            print('スタックが空です。')
    elif menu == Menu.ピーク:
        try:
            x = s.peek()
            print(f'ピークしたデータは{x}です。')
        except FixedStack.Empty:
            print('スタックが空です。')

    elif menu == Menu.探索:
        x = int(input('値：'))
        if x in s:
            print(f'{s.count(x)}個含まれ先頭の位置は{s.find(x)}')
        else:
            print('その値は含まれません。')
    
    elif menu == Menu.ダンプ:
        s.dump()

    else:
        break


