koropokkur.sandbox
========================================

individual scaffolding template set.

pyramid
----------------------------------------

```sh
# pip install korpokkur
python setup.py develop
korpokkur create --logging=DEBUG pyramid[mako]
```

if package name is "foo"

```sh
cd foo
python setup.py develop
alembic -c alembic.ini upgrade head
pserve development.ini 
## http://localhost:6543
```

