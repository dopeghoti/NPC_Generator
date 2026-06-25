import die

class Name:
    ConsonantDie = die.TableDie( [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'w', 'x', 'z', 'th', 'ch' ] )
    VowelDie = die.TableDie( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )

    def Phoneme( self, ending_consonant: bool = False ) -> str:
        suffix = ''
        if ending_consonant:
            suffix = self.ConsonantDie()
        return self.ConsonantDie() + self.VowelDie() + suffix

    def __init__( self, given_name: str = None ) -> None:
        if given_name:
            self.name = given_name
        else:
            d2 = die.Die(2)
            syllables = d2() + d2(-1)
            name = ''
            for _ in range( syllables ):
                if _  == syllables - 1:
                    name += self.Phoneme( True )
                else:
                    name += self.Phoneme()
            self.name = name.capitalize()

    def __str__( self ) -> str:
        return self.name
