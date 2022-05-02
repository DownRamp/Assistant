from pysondb import db

a = db.getDb("Events/events.json")
a.addMany([{"name": "Workout", "time": "Jul-1"},
           {"name": "Go out", "time": "Dec-2"},
           {"name": "net file date start", "time": "Feb-21"},
           {"name": "last date taxes", "time": "Apr-30"},
           {"name": "self-employed last date taxes", "time": "Jun-15th"},
           ])

b = db.getDb("Boss/boss.json")
b.add({"name": "Daniel"})

c = db.getDb("Chores/daily.json")
c.addMany([{"name": "make bed", "time": "8:00 am"},
           {"name": "sweep kitchen floors", "time": "8:30 am"},
           {"name": "wipe down kitchen and bathroom", "time": "10:00 am"},
           {"name": "squeegee shower", "time": "1:00 pm"},
           {"name": "sanitize kitchen and bathroom sinks", "time": "6:00 pm"},
           ])

d = db.getDb("Chores/weekly.json")
d.addMany([{"name": "mop kitchen and bathroom floors", "time": "Monday"},
           {"name": "change bedding", "time": "Tuesday"},
           {"name": "toss expired food", "time": "Wednesday"},
           {"name": "wipe down kitchen appliances", "time": "Thursday"},
           {"name": "clean microwave", "time": "Friday"},
           {"name": "vacuum", "time": "Saturday"},
           {"name": "clean mirrors", "time": "Sunday"}
           ])

e = db.getDb("Chores/monthly.json")
e.addMany([{"name": "vacuum vents", "time": "Weekend 1"},
           {"name": "dust blinds", "time": "Weekend 2"},
           {"name": "clean dishwasher and laundry machines", "time": "Weekend 3"},
           {"name": "dust and clean lights", "time": "Weekend 4"}
           ])

f = db.getDb("Chores/quarterly.json")
f.addMany([{"name": "wipe down fridge", "time": "Month 1"},
           {"name": "wash pillows and comforters", "time": "Month 1"},
           {"name": "vacuum mattress", "time": "Month 1"},
           {"name": "wash shower curtain", "time": "Month 2"},
           {"name": "freshen drains", "time": "Month 2"},
           {"name": "clean inside oven", "time": "Month 2"},
           {"name": "clean out freezer", "time": "Month 3"},
           {"name": "clean under furniture", "time": "Month 3"},
           {"name": "clean furniture surface", "time": "Month 3"}
           ])

g = db.getDb("Chores/yearly.json")
g.addMany([{"name": "clear out gutters", "time": "Quarter 1"},
           {"name": "clean drapes and curtains", "time": "Quarter 2"},
           {"name": "clean around dryer and vents", "time": "Quarter 3"},
           {"name": "clean chimney", "time": "Quarter 3"},
           {"name": "deep clean carpet", "time": "Quarter 4"},
           {"name": "deep clean windows", "time": "Quarter 4"}
           ])
