cllab -- Cottage Labs library
================

This is a library of functions that reusable across projects.

* no business logic from other project should be included here
* if writing some wrapper or extension functions for other third party libraries (e.g. requests, bs4), add the dependency related library version in `steup.py`'s `project.optional-dependencies` instead of `project.dependencies` 
* `project.dependencies` should be always empty
* split to other library if part of module too big