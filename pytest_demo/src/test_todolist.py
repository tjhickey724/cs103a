import pytest
from todolist import TodoList, toDict

@pytest.fixture()
def emptydb():
    db = TodoList('testing.db')
    yield




def test_simple():
    assert 2==1+1

@pytest.mark.dict
def test_todict():
    a = toDict((1,'test','testing toDict',0))
    assert a['rowid']==1
    assert a['title']=='test'
    assert a['desc']=='testing toDict'
    assert a['completed']==0
    assert len(a.keys())==4

@pytest.mark.db
def test_emptylist():
    dbfile = 'testing.db'
    db = TodoList(dbfile)
    items = db.selectAll()
    assert len(items)==0

@pytest.mark.db
@pytest.mark.add
def test_add():
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


