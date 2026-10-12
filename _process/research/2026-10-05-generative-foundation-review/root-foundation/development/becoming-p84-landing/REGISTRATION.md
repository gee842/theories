P84 landing suggestions (not applied; no existing module is changed)

New file: tree/Becoming/Transmission.lean -> Becoming/Transmission.lean (imports Becoming.Premises only).

1. Becoming.lean: add `import Becoming.Transmission` (after `import Becoming.Premises` or at the end of the import list), and this bullet after the `Becoming.Premises` bullet:

* `Becoming.Transmission` (L3): transmission is a law of how dependence forms at coming to
  stand. It is inheritance, a descendant's dependence at its first standing step held by its
  giver at the giving step, with the need within a bound; where the descendant held no
  dependence before it stood, inheritance is the law of forming, and splitting it into forming
  and holding is exact where the earlier holding is decided, asked of every descent excluded
  middle. Under balance inheritance forms no new dependence by descent; the evolution laws need
  it only at the descent they use, and at a relatum coming to stand only from some supported
  giver. Wherever transmission binds, dropping one dependence of the giver keeps every other
  premise and breaks it, so no law kept by dropping a dependence derives it, a reading of the
  exchange among them. A reading of the descendant's dependence off what its givers draw on,
  with drawing being depending, gives inheritance, each needed; with activity needing support
  and every relatum embodied the need half follows within a bound on levels, so in a finite,
  balanced, dissipative world transmission is exactly inheritance. The readings are the AI's,
  pending Ren.

2. check_becoming.py: add "Becoming.Transmission" to CORE (e.g. after "Becoming.Premises").

3. Evolution.lean docstring (optional, wording only, no proof change): the sentence "That
   descendants carry their parents' dependences is a premise (`Flow.TransmitsWithin`), as
   reconstruction is in the theory of evolution; the spine does not derive it." could point to
   `Becoming.Transmission`, which states what derives it and proves the boundary. Not needed
   for the module to compile.
