<img width="200px" src="website/public/logo.svg" />

---

Extending protein search for many proteins vs. many other proteins. Visualized with a hypergraph.

## TODO

- [ ] Experiment
     - [x] Use foldseek in python
     - [x] Visualize a graph of the proteins
     - [ ] Select group on click
     - [ ] Query PDB for the clicked group
     - [ ] Parse the output graph with paper, bio data, structure from PDB
     - [ ] Use Graph RAG on the structures and paper to come up with function hypotheses (by Monday)
- [ ] Create user interface for anyone to use this process (By next Friday)
- [ ] Write the paper (By next Monday)



## Development

Install the foldseek executable based on your system from https://github.com/steineggerlab/foldseek directly into the `exec/` folder. Or if you have it installed globally, you can change the executable path config option (TODO). This is just so we can call Foldseek from Python.

## References

- https://github.com/steineggerlab/foldseek
- https://venome.cqls.oregonstate.edu/proteins
- https://github.com/upphiminn/jLouvain
