import pytest
from todolist import TodoList, toDict


@pytest.fixture
def small_db(tmpdir):
    ''' create a small database, and tear it down later'''
    db = TodoList(tmpdir.join('testing2.db'))
    todo1 = {'title':'testing 1','desc':'see if it works','completed':0}
    todo2 = {'title':'testing 2','desc':'does it work','completed':1}
    todo3 = {'title':'testing 3','desc':'yes, it works','completed':0}
    db.add(todo1)
    db.add(todo2)
    db.add(todo3)
    yield db
    db.deleteAll()


def test_simple():
    assert 2==1+1

def test_todict():
    a = toDict((1,'test','testing toDict',0))
    assert a['rowid']==1
    assert a['title']=='test'
    assert a['desc']=='testing toDict'
    assert a['completed']==0
    assert len(a.keys())==4


def test_emptylist():
    dbfile = 'testing.db'
    db = TodoList(dbfile)
    items = db.selectAll()
    assert len(items)==0


def test_add():
    ''' add a task to an empty dict, the select it, then delete it'''
    dbfile = 'testing.db'
    db = TodoList(dbfile)
    todo = {'title':'testing',
            'desc':'see if it works',
            'completed':0}
    db.add(todo)
    items = db.selectAll()
    assert len(items)==1
    item = items[0]
    assert item['title']=='testing'
    assert item['desc']=='see if it works'
    assert item['completed']==0
    db.delete(item['rowid'])
    items = db.selectAll()
    assert len(items)==0


def test_add_fix(small_db):
    todo = {'title':'alternate add',
            'desc':'does it work',
            'completed':0}
    items = small_db.selectAll()
    small_db.add(todo)
    items2 = small_db.selectAll()
    assert len(items2) == len(items)+1


