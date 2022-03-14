import pytest
from todolist import TodoList, toDict

@pytest.fixture
def dbfile(tmpdir):
    return tmpdir.join('testing2.db')

@pytest.fixture
def small_db(dbfile):
    ''' create a small database, and tear it down later'''
    db = TodoList(dbfile)
    todo1 = {'title':'testing 1','desc':'see if it works','completed':0}
    todo2 = {'title':'testing 2','desc':'does it work','completed':1}
    todo3 = {'title':'testing 3','desc':'yes, it works','completed':0}
    id1=db.add(todo1)
    id2=db.add(todo2)
    id3=db.add(todo3)
    yield db
    db.delete(id3)
    db.delete(id2)
    db.delete(id1)

@pytest.fixture
def med_db(small_db,dbfile):
    rowids=[]
    # add 10 todos
    for i in range(10):
        s = str(i)
        todo ={'title':'name'+s,
               'desc':'description '+s,
               'completed':i%2}
        rowid = small_db.add(todo)
        rowids.append(rowid)

    yield small_db

    # remove those 10 todos
    for j in range(10):
        small_db.delete(rowids[j])




    
        


@pytest.mark.simple
def test_simple():
    assert 2==1+1

@pytest.mark.simple
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

@pytest.mark.add
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

@pytest.mark.add_fix
def test_add_fix(small_db):
    todo = {'title':'alternate add',
            'desc':'does it work',
            'completed':0}
    items = small_db.selectAll()
    small_db.add(todo)
    items2 = small_db.selectAll()
    assert len(items2) == len(items)+1

@pytest.mark.delete
def test_deleteAll(small_db):
    items = small_db.selectAll()
    assert len(items)>0
    small_db.deleteAll()
    items2 = small_db.selectAll()
    assert len(items2) == 0

@pytest.mark.delete
def test_delete(small_db):
    '''
    delete one item and see that the total goes down by one
    '''
    items = small_db.selectAll()
    assert len(items)>0
    small_db.delete(items[1]['rowid'])
    items2 = small_db.selectAll()
    assert len(items2) == len(items)-1

@pytest.mark.delete
def test_delete_completed(med_db):
    ''' check that selectAll,Active,Completed have right sizes
        delete the completed ones and check that only active remain    
    '''
    itemsAll = med_db.selectAll()
    itemsCompleted = med_db.selectCompleted()
    itemsActive = med_db.selectActive()
    assert len(itemsAll) == len(itemsCompleted) + len(itemsActive)
    for i in range(len(itemsCompleted)):
        item = itemsCompleted[i]
        med_db.delete(item['rowid'])
    items2 = med_db.selectAll()
    assert len(items2)==len(itemsActive)

