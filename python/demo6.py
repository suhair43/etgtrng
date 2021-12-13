class task:
 def __init__(self,taskname,tdesc,tstatus,tpriority,tnotes,tbm,townid,tcrid,tcrton,tmodon):
    self.name = taskname
    self.desc = tdesc
    self.status = tstatus
    self.priority = tpriority
    self.notes = tnotes
    self.bookmark = tbm
    self.ownid = townid
    self.crid = tcrid
    self.crton = tcrton
    self.modon = tmodon


 def changepriority(self,priority):
     self.tpriority = priority
     return self.tpriority

task1 = task("abc","abc","progress","low","yes","zzz",1000,211,"1/1/2021","1/2/2021")
a = task1.changepriority("high")
print(a)
'''print(hasattr(task1,"name"))
print(getattr(task1,"ownid"))
setattr(task1, 'crid', 8)
print(getattr(task1,"crid"))
print(task.__bases__)'''

class TechEmployee:
    count =100
    def __init__(self,towner, taskname,tstatus,tpriority,tnotes,tbm,townid,tcrid,tcrton,tmodon):
        super().__init__(towner,taskname,tstatus,tpriority,tnotes,tbm,townid,tcrid,tcrton,tmodon)
        self.owner = towner


#task1 = task("abc","abc","progress","low","yes","zzz",1000,211,"1/1/2021","1/2/2021")
temp1 = TechEmployee("suhair","abc","abc","progress","low","yes","zzz",1000,211,"1/1/2021","1/2/2021")
print(task1)
print(temp1)