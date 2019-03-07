# IEngine
Inference engine for propositional logic, forward chaining and backward chaining.

Given a knowledge base of the format 

```
p2=> p3; p3 => p1; c => e; (b&e) => f; (f&g) => h; p1=>d; p1&p3 => c; p2; b; a;
```

We want to able to tell if the given knwoledge base i,e KB entails a variable. This can be expressed in the form 

```
kb |= d
```

This project uses three methods:

[Inference](https://en.wikipedia.org/wiki/Inference)

[Forward Chaining](https://en.wikipedia.org/wiki/Forward_chaining)

[Backward Chaining](https://en.wikipedia.org/wiki/Backward_chaining)


### Other data samples

```
TELL
p2=> p3; p3 => p1; c => e; (b&e) => f; (f&g) => h; p1=>d; p1&p3 => c; p2; b; a; 
ASK
d

TELL
p2=> p3; p3 => p1; c => e; (b&e) => f; (f&g) => h; p1=>d; p1&p3 => c; p2; b; a; 
ASK
a => b


TELL
p2=> p3; p3 => p1; c => e; (b&e) => f; (f&g) => h; p1=>d; p1&p3 => c; p2; b; a; 
ASK
e & f

```

### Output
For clause 1 the output should be true because the given knowledge base entails d.

More information https://en.wikipedia.org/wiki/Logical_consequence
