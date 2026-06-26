import die, json, name, random, yaml
from typing import Dict

class OCEAN:
    def create_dice( self ) -> Dict:
        Openness = [
                [ 'authoritarian', 'inflexible', 'dogmatic', 'skeptical', 'unbiased', 'philosophical', 'tolerant' ],
                [ 'intolerant', 'pessimistic', 'conservative', 'resistant', 'receptive', 'flexible', 'progressive' ],
                [ 'cynical', 'hard-headed', 'stubborn', 'realistic', 'open-minded', 'creative', 'optimistic' ],
                [ 'narrow-minded', 'prejudiced', 'traditional', 'pragmatic', 'curious', 'inquisitive', 'adventurous' ] ]
        Conscientiousness = [
                [ 'negligent', 'hedonistic', 'procrastinating', 'distracted', 'punctual', 'disciplined', 'ambitious' ],
                [ 'irresponsible', 'impulsive', 'impatient', 'casual', 'patient', 'thorough', 'persevering' ],
                [ 'careless', 'disorganized', 'unorganized', 'practical', 'responsible', 'efficient', 'methodical' ],
                [ 'lazy', 'unreliable', 'indecisive', 'diligent', 'dependable', 'goal-oriented', 'perfectionist' ] ]
        Extraversion = [
                [ 'solitary', 'reserved', 'submissive', 'aloof', 'outgoing', 'jovial', 'energetic' ],
                [ 'reclusive', 'shy', 'reflective', 'contemplative', 'sociable', 'cheerful', 'passionate' ],
                [ 'private', 'introspective', 'quiet', 'ambiverted', 'expressive', 'receptive', 'flamboyant' ],
                [ 'withdrawn', 'independent', 'serious', 'easy-going', 'lively', 'bubbly', 'flirtatious' ] ]

        Agreeableness = [
                [ 'cruel', 'selfish', 'rude', 'arrogant', 'cooperative', 'kind', 'humorous' ],
                [ 'greedy', 'boastful', 'sarcastic', 'argumentative', 'trusting', 'caring', 'forgiving' ],
                [ 'deceptive', 'jealous', 'vain', 'polite', 'honest', 'compassionate', 'charming' ],
                [ 'manipulative', 'cynical', 'competitive', 'diplomatic', 'loyal', 'generous', 'altruistic' ] ]

        Neuroticism = [
                [ 'serene', 'grounded', 'confident', 'relaxed', 'wary', 'sensitive', 'insecure' ],
                [ 'stoic', 'calm', 'focused', 'concerned', 'tense', 'irritable', 'self-critical' ],
                [ 'hardy', 'adaptable', 'stable', 'restless', 'anxious', 'moody', 'depressed' ],
                [ 'poised', 'sensible', 'resilient', 'fickle', 'vulnerable', 'nervous', 'panicky' ] ]

        dice = {
                'Openness'        : die.TableDie( Openness[random.choice( range(4) ) ] ),
                'Conscientiousness': die.TableDie( Conscientiousness[random.choice( range(4) ) ] ),
                'Extraversion'    : die.TableDie( Extraversion[random.choice( range(4) ) ] ),
                'Agreeableness'   : die.TableDie( Agreeableness[random.choice( range(4) ) ] ),
                'Neuroticism'     : die.TableDie( Neuroticism[random.choice( range(4) ) ] )
                }
        return dice

    def __init__( self ) -> None:
        self.dice = self.create_dice()
        self.Openness         =  self.dice['Openness']()
        self.Conscientiousness =  self.dice['Conscientiousness']()
        self.Extraversion     =  self.dice['Extraversion']()
        self.Agreeableness    =  self.dice['Agreeableness']()
        self.Neuroticism      =  self.dice['Neuroticism']()

    def __str__( self ) -> str:
        return f'{self.Openness}, {self.Conscientiousness}, {self.Extraversion}, {self.Agreeableness}, and {self.Neuroticism}'

class Agenda:
    def __init__( self ) -> None:
        self.Goal = die.TableDie( [
            'acquire',
            'avenge',
            'betray',
            'conceal',
            'conquer',
            'destroy',
            'discover',
            'escape',
            'expand',
            'explore',
            'gather',
            'glorify',
            'infiltrate',
            'lead',
            'learn',
            'oppose',
            'prevent',
            'reconcile',
            'restore',
            'worship' ] )()
        self.Focus = die.TableDie( [
            'adversary',
            'artefact',
            'beast',
            'child',
            'enemy',
            'idea',
            'knowledge',
            'location',
            'love',
            'neighbor',
            'NPC',
            'parent',
            'PC',
            'relationship',
            'relative',
            'revenge',
            'reward',
            'ruler',
            'structure',
            'wealth' ] )()
        self.Obstacle = die.TableDie( [
            'an alliance',
            'conflict',
            'conflicting interests',
            'a criminal past',
            'distance',
            'duty',
            'family',
            'a forbidden love',
            'health',
            'honor',
            'hostility',
            'lack of information',
            'law',
            'love',
            'mysterious circumstances',
            'an oath',
            'an opposing faction',
            'pursuers',
            'time' ] )()

    def __str__( self ) -> str:
        return f'{self.Goal} {"an" if self.Focus[0] in "aeiou" else "a"} {self.Focus}, but there are issues with {self.Obstacle}'

class DistinctionDie( die.DupelessTableDie ):
    def __init__( self ) -> None:
        super().__init__( [
            'facial scars',
            'facial birthmarks',
            'piercings',
            'tattoos',
            'a prominent nose',
            'distinctive eyebrows',
            'freckles',
            'thin lips',
            'full lips',
            'high cheekbones',
            'a round face',
            'a piercing gaze',
            'a wide nose',
            'protruding ears',
            'a cleft chin',
            'deep dimples',
            'pockmarked skin',
            'a square jaw',
            'a missing tooth',
            'a broken nose',
            'a misshapen nose' ] )

class AppearanceDie ( die.TableDie ):
    _TRAIT_DATA = {
            'height':      ( [1, 2, 4, 6, 4, 2, 1], ['very short', 'short', 'somewhat short', 'average', 'somewhat tall', 'tall', 'very tall'] ),
            'size':        ( [1, 2, 4, 6, 4, 2, 1], ['very small', 'small', 'somewhat small', 'average', 'somewhat large', 'large', 'very large'] ),
            'eyes':        ( [2, 2, 1, 2, 2, 1],    ['light blue', 'blue', 'grey', 'brown', 'dark brown', 'green'] ),
            'pate_color':  ( [2, 3, 2, 1, 2],       ['blonde', 'brown', 'auburn', 'red', 'dark'] ),
            'pate_length': ( [2, 1, 2, 1],          ['short', 'shoulder-length', 'long', 'very long'] ),
            'pate_style':  ( [2, 2, 1, 2, 2, 1],    ['loose', 'in a pony-tail', 'in a bun', 'braided', 'slicked-back', 'in dreadlocks'] ),
            'facial_hair': ( [5, 2, 1, 2, 1, 2],    ['clean-shaven', 'bearded', 'mustachioed', 'sideburnt', 'mutton-chopped', 'stubbled'] )
            }

    def __init__( self, dietype: str = None ):
        if dietype not in self._TRAIT_DATA:
            raise ValueError( f'Appearance die called with unknown type ({dietype=}).  Must be one of {", ".join( self._TRAIT_DATA.keys())}.' )
        weights, values = self._TRAIT_DATA[dietype]
        faces = []
        for weight, value in zip( weights, values ):
            faces.extend( [ value ] * weight )
        super().__init__( faces )

class NPC:
    def __init__( self, npc_name: str = None, gender: str = None ) -> None:
        match gender:
            case "M"|"Male"|"m"|"male":
                self.ey, self.em, self.eir = 'he', 'him', 'his'
                self.have = 'has'
                self.gender = 'm'
                self.to_be = 'is'
            case "F"|"Female"|"f"|"female":
                self.ey, self.em, self.eir = 'she', 'her', 'her'
                self.have = 'has'
                self.gender = 'f'
                self.to_be = 'is'
            case _:
                self.ey, self.em, self.eir = 'they', 'them', 'their'
                self.have = 'have'
                self.gender = None
                self.to_be = 'are'
        self.NameSuggestions = []
        self.Name = None
        if not npc_name:
            self.NameSuggestions = [ str( name.Name() ) for _ in range(3) ]
        else:
            self.Name = str( npc_name )
        self.Personality = OCEAN()
        self.Agenda = Agenda()
        self.Appearance = {
                'Height': AppearanceDie('height')(),
                'Size': AppearanceDie('size')(),
                'Eyes': AppearanceDie('eyes')(),
                'Pate Hair': {
                    'Color': AppearanceDie('pate_color')(),
                    'Length': AppearanceDie('pate_length')(),
                    'Style': None
                    },
                'Facial Hair': {
                    'Style': None
                    },
                'Distinctions': []
                }
        if 'long' in self.Appearance['Pate Hair']['Length']:
            self.Appearance['Pate Hair']['Style'] = AppearanceDie('pate_style')()
        if self.gender and self.gender.lower()[0] == 'm': # Male characters might have facial hair
            self.Appearance['Facial Hair']['Style'] = AppearanceDie('facial_hair')()
        elif not self.gender and die.Die(2)(-1): # So too might characters without defined gender.  Toss a coin.
            self.Appearance['Facial Hair']['Style'] = AppearanceDie('facial_hair')()
        distinction_die = DistinctionDie()
        num_distinctions = random.choice ( [ 0,0,0,1,1,1,2,2,3 ] )
        self.Appearance['Distinctions'] = [ distinction_die() for _ in range( num_distinctions ) ]

    def _to_dict( self ) -> dict:
        """Flattens the NPC into a native dictionary for future export."""
        return {
                'Name': self.Name if self.Name else '',
                'NameSuggestions': self.NameSuggestions if not self.Name else [],
                'Gender': self.gender,
                'Personality': {
                    'Openness': self.Personality.Openness,
                    'Conscientiousness': self.Personality.Conscientiousness,
                    'Extraversion': self.Personality.Extraversion,
                    'Agreeableness': self.Personality.Agreeableness,
                    'Neuroticism': self.Personality.Neuroticism
                    },
                'Agenda': {
                    'Goal': self.Agenda.Goal,
                    'Focus': self.Agenda.Focus,
                    'Obstacle': self.Agenda.Obstacle
                    },
                'Appearance': self.Appearance # Already a dict, thanks past me!
                }

    def to_yaml( self ) -> str:
        """Returns the NPC as a YAML-formatted string"""
        return yaml.safe_dump( self._to_dict(), default_flow_style=False, sort_keys=False )

    def to_json( self ) -> str:
        """Returns the NPC as a JSON-encoded string"""
        return json.dumps( self._to_dict(), indent=4 )

    def __str__( self ) -> str:
        # For convenience:
        if not self.Name:
            Name = f"An un-named NPC.  Possible suggestions: {', '.join( self.NameSuggestions )}"
        else:
            Name = self.Name
        pate = self.Appearance['Pate Hair']
        if self.Appearance['Distinctions']:
            distinct='Distinguishing facial features include: ' + ', '.join( self.Appearance['Distinctions'] ) + '.'
        else:
            distinct='There are no otherwise immediately obvious facial characteristics.'
        r = f'''This is {Name}.

{self.eir.capitalize()} stature is {self.Appearance['Height']}, with a {self.Appearance['Size']} build.

{self.ey.capitalize()} {self.have} {self.Appearance['Eyes']} eyes, and {pate['Length']}, {pate['Color']} hair'''
        if pate['Style']:
            r += f" worn {pate['Style']}."
        else:
            r += "."
        if self.Appearance['Facial Hair']['Style']:
            r += f'''

{self.eir.capitalize()} face is {self.Appearance['Facial Hair']['Style']}.\n\n'''
        else:
            r += '\n\n'
        r += f'''{distinct}

{self.ey.capitalize()} {self.to_be} {self.Personality}.

{self.eir.capitalize()} goal is to {self.Agenda}.'''
        return r


