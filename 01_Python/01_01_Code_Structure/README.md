# Code Structure

## Topics 
* Packages
* Modules
* Classes

## Running

```
docker run -it --name pvt -v $(pwd)/src:/scripts python:3.7 bash
```

# Sequence

* Writing modules
* Importing module on the current namespace
* Importing all modules
* Custom import name
* Writing packages
* Exploring modules
* __code__ will get a code object and co_name and co_varnames will return the parameter list