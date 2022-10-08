
# Resampling and Interpolation: from grid to swath in space and time  

Python based spatio-temporal resampling of gridded data onto satellite swaths; this work has
been developed in the context of a wind retrievals processor using radiometers from 
EUMETSAT's Ocean and Sea Ice [OSISAF](https://osi-saf.eumetsat.int/) where [KNMI](https://www.knmi.nl/over-het-knmi/about) as one of its cooperating members. The intend 
is the development of a scientific software framework using modern tooling; the main 
goals are:
- Code Maintainability
- Continuous Quality Improvement
- Open Science development: Open Source and Transparency


Contains a few snippets of code to interpolate/resample 
ECMWF data (say on a grid) to a swath; this should be useful
to interpolate in space and time the forecasts used as 
apriori data for Optimal Estimation of wind speed (and
other parameters).

## Resampling and Interpolation, parts and routines

This repo contains a main Jupyter notebook (ExtractApriori_v1.ipynb);
in there we make a walk-through from preparing the datasets using the simplicity
of [xarray](https://docs.xarray.dev/en/stable/)'s interface, to the power
of [pyresample](https://pyresample.readthedocs.io/en/latest/).
The repo also contain some supporting routines and the areas.yaml file useful
to get maps/projections information. 
 

## Purpose of this repo

- Provide a practical example on the use of modern geoscience python stacks: [PyTroll](https://pytroll.github.io/) and [pangeo](https://pangeo.io/packages.html#packages).
- Practical way to communicate with stakeholders, interested scientists and developers.
- Sandbox.


## Documentation

For now we use the markdown standard for Jupyter Notebooks.


## Acknowledgement

This work was kicked off in the context of a project of EUMETSAT's Ocean and Sea Ice [OSISAF](https://osi-saf.eumetsat.int/) and we highly apprecieate their support. Many thanks to my colleague Anton Verhoef for useful discussions on the topic.

## Citation and Contribution

Please consider citing the repo when you find it insightful.

If you want to contribute feel free to do so: ideas, proposals (e.g. via pull request) and constructive criticism are always welcome.









