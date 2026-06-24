import npc

def main():
    print( "To demonstrate the type of output this module will generate, I will now create three NPCs:" )
    print( "One named 'Alex' with no gender set, and two un-named with genders set." )
    print( npc.NPC( npc_name='Alex') )
    print()
    print( npc.NPC( gender = 'm' ) )
    print()
    print( npc.NPC( gender = 'Female' ) )
    print()

if __name__ == "__main__":
    main()
