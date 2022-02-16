# ndim-colorednoise
Python package to generate multi-dimensional [colored noise](https://en.wikipedia.org/wiki/Colors_of_noise).

### Usage example

```python

dimensions = (150, 120)
beta = 1
  
noise = generate_noise(dimensions, beta)
# generates a 150x120 random matrix with frequency power law (1/f)**beta.
# in this example, since beta = 1, the generated matrix contains pink (1/f) noise 
```

### To do list
- [ ] Verify correctness
- [ ] Distribute as pip package


