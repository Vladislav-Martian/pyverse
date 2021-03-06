
pyvorse
=======

Simple essentials extension library of additions to vanilla python.
-------------------------------------------------------------------

----

Includes:
^^^^^^^^^


* [core]:

  * @attribute - converts any function with (arg: str) to attribute processor
  * w. - attribute processor to faster writing short words, dont use it in speed is important. For obvious reasons, such a word notation is guaranteed to conform to python's naming conventions. w.var_name = "var_name"
  * class: basis - extended base class
  * @throws(*exceptions_cls) - marks function with classes, that can be thrown
  * isthrows(exception_cls) - test function to be marked with ``@throws()``
  * trycall(func, *args, **kwargs) -> tuple[result, exception] - catches exceptions in function call
  * @safe - converts function to its copy, but automatically called inside ``trycall()``\ , and returns tuple[result, exception]
  * Operators - enum for @calloperators
  * @calloperators(op: Operators = Operators.All) - converts function to object, that calls with secon operand and returns result of it function on using operator, selected in argument. Operand still can be called as function.
  * reprint() - operand-variation of print function, can be called like ``reprint - w.text_to_show``. If prints only one value, value will be returned as result.
  * @functor - allows function to be called with self object as first argument. to work with its fields as example.
  * class: unibox - class, that locks value inside field ``.inbox``\ , and contains dict for metadata, and can be stopped with ``.stop()``\ , and be test for it by ``.stopped``\ , or ``.isStopped()``
  * copyAllProps(dest, source) - function copies all attributes from source to dest, but ignores attributes with name starting with duble underscore '__'

* [data]:

  * //ALL_FROM_SUBMODULES//
  * [deep]

    * deep - Implements a simplified version of javascript objects based on the "dict" class. Can be created directly or through a class of similar objects that extends "dci". Prototypal inheritance. All methods to look deeper starts with word ??deep??, like ``.deepget(name)``. More details on the wiki.
    * dci - empty base deepclass, use its ``.extend(new_prototype: deep, *names: str)`` method, that returns new deepclass object
    * class: DeepCalss - *ignore it, nothing more then python`s class of ??dci??*

  * [positioned]

    * class: poslist - list, based on dict. Aloows to contain skips inside.

  * [simple]

    * class: loop - list, but handles index overload like list is lopped
    * class: scope - dict, but allows get-access to items like access to attributes, and attribute-like set access, but onky for keys, already present in dict. Allows to find item by number of a key (it automatically sorted in dicts). Allows getting values dynamic/ Value is a function to be called with self dict as first argument. ``.getDynamic(key)`` 
    * class: stack - list, extended only, no changes. ``.setvalidation(validator: Callable)`` - validates values on pushing to the stack. ``.push(value)`` and ``.leftpush(value)``\ , ``.pushes(value)`` and ``.leftpushes(value)``. Raises ValueError, if loses validation. ``.pull()`` and ``.leftpull(value)`` - works like default ``.pop()`` but without arguments, for last and first element.

  * [smart]

    * class: smartlist - list, but with additional methods. find, select, filtered (iter), filter, any, all, astuole, asslist, asset, foreach, mapper, reducer, sort, sliced, slicedstart, slicedend. Working with predicates and callbacks. Details on wiki.
    * class: handle - Primitive handlers container, simplest pipeline. Objects can be used as decorators, or called with callback passed. On each step calls callback with box on first argument.
    * class: objectAddress - Create, object ``adr = objectAddress()``\ , write your way ``adr["Configs"]["chances"]["spawn"](lambda pos: pos[SNEED])``\ , and use it on data structire ``adr.use(CONFIGS_ROOT)``. It returns same for ``CONFIGS_ROOT["Configs"]["chances"]["spawn"][SNEED]``\ , but can be used nultiple times and dynamically.

  * [spiders]

    * class: spider(seeker: Callable, worker: Callable) - spiders can work with complex data structures. Seeker selexts new node, worker does something here. Seeker and worker will be called with (struct, dot, box). Use ``box.stop()`` to finish spiders`s walk. But worker will be called even if you stop it in seeker. 

  * [table]

    * class: Table - contains headers and rows. use ``table[index_column][index_row]`` or better ``table.getitem(row:int, col:int)`` for extracting values. Use ``adddefaultheader(self, name: str, align: int = 0, default=None)`` to add new column. You can use ``.getdynamic(row:int, col:int)`` to work with dynamic values. functions, that will be called with (table: Table, row:int, col:int). For example - auto-numerations. Rendering method not presented! Inherit class, and add any render you want, markdown or html for example.
    * class: Column - saves names and align for headers. Saves default values for tables.
    * class: Row: poslist - class represents rows in the table

* [mathematics] - Whole default math, but with 2 new functions. ``trin(n)`` for triangular number and count of diagonals in any shape. ``hexcount(n)`` - for calculatinc number of hexagonal cells in radius from one.
* [pipeline] - simple tools for complex piplines

  * //ALL_FROM_SUBMODULES//
  * [datacell]

    * class: dcell: core.unibox - just container for value in pipeline.

  * [mains] - Default pipline functions containers:

    * DictionaryPipeline
    * ListPipeline

  * [routers] - full pipeline conveyor build. Cotains static metadata. Uses pointer to select new function, and it can be method from pipeline container.

    * class: router - Read on wiki! Use ``r.launch(cell)`` or ``r(cell)``. All functions in pipeline will be called with ``(cell, staticmeta)``\ , with staticmeta from router.

* [tests]

  * //ALL_FROM_SUBMODULES//
  * [exprs]

    * iterable(o) - allows to get iterator from object, and using ``o`` inside for..in cycle
    * nextable(o) - allows to use ``next(o)``
    * forable(o) - deeper version of ``iterable(o)`` test.
    * instanceof(o, *cls) - alternative notation to isinstance, like ``instanceof(my_num, int, float, complex)``
    * withable(o) - allows with.. as..
    * awithable(o) - allows async with.. as..
    * isinrange(_list, index) - test index for a range in the index

  * [other]

    * hashable(o) - can be used as key for dictionary or not.
    * haskey(o, key) - like hasattr, but tests for ``o[key]``
    * isand(o, *t) - tests o to be all of *\ t
    * isor(o, *t) - tests o to be any of *\ t
    * eqand(o, *t) - tests o to be equal to all of *\ t
    * eqor(o, *t) - tests o to be equal to any of *\ t
    * haslen(o) - can be item used in ``len(o)`` or not.
