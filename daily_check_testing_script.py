from pysondb import db

a = db.getDb("ToDo/todo.json")
a.addMany([{"task": "Film clocks video", "quad": "4"},
           {"task": "Clean room", "quad": "4"}
           ])