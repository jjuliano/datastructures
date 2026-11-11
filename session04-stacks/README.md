# Session 4. Stacks

Python package, MIT. Relative imports need the `src` tree.

```
cd session04-stacks
PYTHONPATH=src python -m data_structures.stacks.balanced_parentheses
```

- `src/data_structures/stacks/stack.py`
- `src/data_structures/stacks/stack_with_singly_linked_list.py`
- `src/data_structures/stacks/balanced_parentheses.py`

C, GPL-3.0, from The Algorithms C repository. See `c/` and the root `LICENSE-GPL-3.0`.

Upstream Python commit `574d100b7181956e9c8384552fd078165e4cc326`.

Easy procedures in `easy/` are original, MIT, copyright Joel Bryan Juliano. See [LICENSE-EASY.md](../LICENSE-EASY.md). Run with [jjuliano/easy-lang](https://github.com/jjuliano/easy-lang).

- `easy/pile.easy` — an array stack pops 4, 1, 3
- `easy/linked_pile.easy` — a linked stack pops 4, 1, 3
- `easy/brackets.easy` — `([])` is true, and `([)]` is false
