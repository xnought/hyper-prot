<img width="200px" src="https://github.com/user-attachments/assets/de4296da-3d2d-428a-99a2-a0dc1d4153ba" />

---

Extending protein search for many proteins vs. many other proteins. Visualized with a hypergraph.

## TODO

- [ ] Experiment
     - [x] Use foldseek in python
     - [ ] Use foldseek on external database PDB for single-many search
     - [ ] Visualize a graph of the proteins
     - [ ] Use foldseek on external database PDB for many-many search
     - [ ] Visualize a graph of the proteins (By Friday)
     - [ ] Extend the graph to similar of similar, ...
     - [ ] Visualize hypergraph somehow to simplify things
     - [ ] Parse the output graph with paper, bio data, structure from PDB
     - [ ] Use Graph RAG on the structures and paper to come up with function hypotheses (by Monday)
- [ ] Create user interface for anyone to use this process (By next Friday)
- [ ] Write the paper (By next Monday)



## Development

Install the foldseek executable based on your system from https://github.com/steineggerlab/foldseek directly into the `exec/` folder. Or if you have it installed globally, you can change the executable path config option (TODO). This is just so we can call Foldseek from Python.

## References

- https://github.com/steineggerlab/foldseek
- https://venome.cqls.oregonstate.edu/proteins
