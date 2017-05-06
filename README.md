# TanbyNote
local memo app used database
![image](https://github.com/yusuketanabe/TanbyNote/blob/master/image)

1. Run 'python3 note.py' command on terminal then 'note.db' created. 
2. Input table column data by running python command. Move to current directory and start python interactive mode.
```python
>>> from note.database import db_session, Memo
>>> VAR = Memo("TITLE", "BODY")
>>> db_session.add(VAR)
>>> db_session.commit()
```
3. Open browser and input 'localhost:5000'. You get local notebook!
