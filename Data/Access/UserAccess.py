import json

#region access to parent folder of the solution
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#endregion

from DataContext import DataContext
from Entities.User import User
from Util.DateTimeEncoder import DateTimeEncoder

class UserAccess(DataContext):

    def GetUsers(self):
        users = []
        data = self.Get("Select * from user order by username")

        for obj in data:
            users.append(json.loads(json.dumps(obj, cls=DateTimeEncoder), object_hook=User))
        return users

    def GetUser(self, id):
        sql = "Select * from user where id = %s"
        data = self.GetById(sql, (id,))
        return json.loads(json.dumps(data, cls=DateTimeEncoder), object_hook=User)

    def InsertUser(self, user):
        sql = "INSERT user (username, password, last_login, attempt, status, email) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user.username, user.password, user.last_login, user.attempt, user.status, user.email)
        return self.Execute(sql, val)

    def UpdateUser(self, input):
        sql = "UPDATE user SET username = %s, password = %s, last_login = %s, attempt = %s, status = %s, email = %s WHERE id = %s"
        val = (input.username, input.password, input.last_login, input.attempt, input.status, input.email, input.id)
        return self.Execute(sql, val)
    
    def DeleteUser(self, id):
        sql = "DELETE from user WHERE id = %s"
        return self.Execute(sql, (id,))