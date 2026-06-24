from abc import ABC, abstractmethod
import random
from typing import Any, Generic, List, TypeVar

T = TypeVar('T')

class AbstractDie( Generic[T] ):
    def __init__( self, sides: List[T] ) -> None:
        self.sides: list[T] = sides

    @abstractmethod
    def roll( self ) -> T: ...

    @abstractmethod
    def __call__( self ) -> T: ...

class Die( AbstractDie[int] ):
    def __init__( self, sides: int = 0 ):
        if sides <= 1 or not isinstance( sides, int ):
            raise ValueError( f'Number of Sides of a die must be an integer and must be at least two. {sides=}' )
        super().__init__( [ side for side in range( 1, sides + 1 ) ] )

    def roll( self, advantage: bool = False, disadvantage: bool = False ) -> int:
        if advantage ^ disadvantage:
            if advantage:
                return max( random.choice( self.sides ), random.choice( self.sides ) )
            if disadvantage:
                return min( random.choice( self.sides ), random.choice( self.sides ) )
        return random.choice( self.sides )

    def __call__( self, modifier: int = 0, advantage: bool = False, disadvantage: bool = False ) -> int:
        return self.roll( advantage = advantage, disadvantage = disadvantage ) + modifier

class ExplodingDie( Die ):
    def __init__( self, sides: int = 0, exploding: bool = True ):
        super().__init__( sides )
        self.exploding = bool( exploding )

    def defuse( self ) -> None:
        self.exploding = False

    def arm ( self ) -> None:
        self.exploding = True

    @property
    def lit( self ) -> bool:
        return self.exploding

    def roll( self ) -> int:
        total = random.choice( self.sides )
        exploding = self.exploding and total == max( self.sides )
        while exploding:
            die = random.choice( self.sides )
            exploding = die == max( self.sides )
            total += die
        return total

    def __call__( self ) -> int:
        return self.roll()

class TableDie( AbstractDie[str] ):
    def __init__( self, sides: list[str] ):
        if len( sides ) <= 1:
            raise ValueError( f'Number of Sides of a TableDie must be a list of at least one string. {sides=}' )
        super().__init__( [ str(side) for side in sides ] )

    def roll( self ) -> str:
        return random.choice( self.sides )

    def __call__( self ) -> str:
        return self.roll( )

class DupelessTableDie( TableDie ):
    def __init__( self, sides: list[str] ):
        super().__init__( sides )
        self.starting_faces = self.sides[:]

    def roll( self ) -> str:
        if self.sides:
            selection = random.choice( self.sides )
            self.sides.remove( selection )
            return selection
        else:
            raise ValueError( f'{self.__class__.__name__} exhausted; no entries remaining to roll from. {self.sides} {self.starting_faces=}' )

    def reset( self ) -> None:
        self.sides = self.starting_faces[:]

class D4( Die ):
    def __init__( self ):
        super().__init__( sides = 4 )

class D6( Die ):
    def __init__( self ):
        super().__init__( sides = 6 )

class D8( Die ):
    def __init__( self ):
        super().__init__( sides = 8 )

class D10( Die ):
    def __init__( self ):
        super().__init__( sides = 10 )

class D12( Die ):
    def __init__( self ):
        super().__init__( sides = 12 )

class D20( Die ):
    def __init__( self ):
        super().__init__( sides = 20 )

class D100( Die ):
    def __init__( self ):
        super().__init__( sides = 100 )

