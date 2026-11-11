# Data structures examples

Python and C examples for the fifteen sessions, filed in the same order as the book.

Python files are MIT, from [The Algorithms](https://github.com/TheAlgorithms/Python), commit `574d100b7181956e9c8384552fd078165e4cc326`. The license is [LICENSE-MIT.md](LICENSE-MIT.md).

C files are GPL-3.0, from [The Algorithms C](https://github.com/TheAlgorithms/C), commit `e5dad3fa8def3726ec850ca66a7f51521f8ad393`. They sit in `session04-stacks/c` and `session05-queues-and-deques/c`. The license is [LICENSE-GPL-3.0](LICENSE-GPL-3.0).

The Python files that match an Easy program carry comments that name the Easy procedure and the Easy lines each block matches, for example `# Easy Push: top <- top + 1; slot(top) <- x`. Apart from those comments, the only edits wrap three long lines inside their brackets and move two upstream comments onto their own line, to fit the book's print width. The code runs exactly as upstream.

Where no upstream Python file matched an Easy program, the session's `easy/` folder holds a Python twin written for the book, under the Easy license: `euclid.py`, `hanoi.py`, `walks.py` (session 6), `digits.py`, `atoms.py`, and `bst.py`. The other Python functions written for the book are printed in the book and are not in this repository.

Each session has an `easy/` folder. Those procedures are original, MIT, copyright Joel Bryan Juliano. The license is [LICENSE-EASY.md](LICENSE-EASY.md). They are separate from the Python and C files above. Run one with the interpreter at [jjuliano/easy-lang](https://github.com/jjuliano/easy-lang):

```
python3 -m easy session03-algorithms/easy/insertion.easy
```

| Session | Directory |
| --- | --- |
| 1. Basic concepts | [session01-basic-concepts](session01-basic-concepts) |
| 2. Mathematical preliminaries | [session02-mathematical-preliminaries](session02-mathematical-preliminaries) |
| 3. Algorithms | [session03-algorithms](session03-algorithms) |
| 4. Stacks | [session04-stacks](session04-stacks) |
| 5. Queues and deques | [session05-queues-and-deques](session05-queues-and-deques) |
| 6. Binary trees | [session06-binary-trees](session06-binary-trees) |
| 7. Applications of binary trees | [session07-applications-of-binary-trees](session07-applications-of-binary-trees) |
| 8. Trees and forests | [session08-trees-and-forests](session08-trees-and-forests) |
| 9. Graphs | [session09-graphs](session09-graphs) |
| 10. Applications of graphs | [session10-applications-of-graphs](session10-applications-of-graphs) |
| 11. Linear lists | [session11-linear-lists](session11-linear-lists) |
| 12. Generalized lists | [session12-generalized-lists](session12-generalized-lists) |
| 13. Sequential tables | [session13-sequential-tables](session13-sequential-tables) |
| 14. Binary search trees | [session14-binary-search-trees](session14-binary-search-trees) |
| 15. Hash tables | [session15-hash-tables](session15-hash-tables) |

Each session README names the upstream path. `UPSTREAM.txt` records the commits.
