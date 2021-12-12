from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# バケットの属性

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    """ハッシュを構成するバケット"""

    def __init__(self, key: Any = None, value: Any = None,
                        stat: Status = Status.EMPTY) -> None:
        """初期化"""
        self.key = key
        self.value = value
        self.stat = stat
    
    def set(self, key: Any, value: Any, stat: Status) -> None:
        """全フィールドに値を設定"""
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self, stat: Status) -> None:
        """属性を設定"""
        self.stat = stat

class OpenHash:
    """オープンアドレス法を実現するハッシュクラス"""

    def __init__(self,capacity:int) -> None:
        """初期化"""
        self.capacity = capacity
        self.table = [Bucket()]*self.capacity

    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(),16)%self.capacity)

    def rehash_value(self, key: Any) -> int:
        """再ハッシュ値を求める"""
        return (self.hash_value(key)+1)%self.capacity

    def search_node(self,key:Any) ->Any:
        """キーがkeyであるバケットの探索"""
        hash = self.hash_value(key)
        p = self.table[hash]
        for _ in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None
    
    def search(self,key:Any) -> Any:
        """キーkeyをもつ要素の探索 (値を返却)"""
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
    
    def add(self, key: Any, value:Any) -> bool:
        """キーがkeyで値がvalueの要素の追加"""
        if self.search(key) is not None:
            return False
        hash = self.hash_value(key)
        p = self.table[hash]
        for _ in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat ==Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False
    
    def remove(self, key: Any) -> int:
        """キーkeyを持つ要素の削除"""
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        """ハッシュ表をダンプ"""
        for i in range(self.capacity):
            print(f'{i:2}', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 未登録 --')
            elif self.table[i].stat == Status.DELETED:
                print('-- 削除済み --')


from enum import Enum
Menu = Enum('Menu',['追加','削除','探索','ダンプ','終了'])
def select_menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.追加:
        key = int(input('キー：'))
        val = input('値：')
        if not hash.add(key,val):
            print('追加失敗！')
    
    elif menu == Menu.削除:
        key = int(input('キー：'))
        if not hash.remove(key):
            print('追加失敗！')

    elif menu == Menu.探索:
        key = int(input('キー：'))
        t = hash.search(key)
        if t is not None:
            print(f'そのキーをもつ値は{t}です。')
        else:
            print('該当するデータはありません。')
    
    elif menu == Menu.ダンプ:
        hash.dump()
    else:
        break


