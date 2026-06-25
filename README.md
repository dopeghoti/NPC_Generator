A System- and Setting-agnostic Instant NPC Generator

Inspired by [this post](https://ttrpg-hangout.social/@enfors/116777956457888181) on Mastodon, I took it upon myself to knock out a quick library that can be used to generate NPCs in near-real-time.  If you simply execute `main.py` it will generate three example characters.  If you import the `npc.py` module you can instantiate an `NPC` object which you can then `print()` or export for procedural consumption with `.to_json()` or `.to_yaml()`.

Example output:
```txt
This is Steven.

His stature is short, with a somewhat large build.

He has light blue eyes, and shoulder-length, dark hair.

His face is stubbled.

Distinguishing facial features include: pockmarked skin.

He is adventurous, perservering, outgoing, manipulative, and self-critical.

His goal is to discover an artefact, but there are issues with an opposing faction.
```
