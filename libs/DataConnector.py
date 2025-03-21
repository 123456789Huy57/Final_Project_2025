from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.Client import Client
from FinalProject.models.Location import Location
from FinalProject.models.PersonalTrainer import PersonalTrainer
from FinalProject.models.User import User


class DataConnector:
    def get_all_client(self):
        jff = JsonFileFactory()
        # The issue is likely in this path - updating to use absolute path or correct relative path
        filename = "../dataset/client.json"  # Remove the leading ../
        clients = jff.read_data(filename, Client)
        return clients

    def get_all_personaltrainer(self):
        jff = JsonFileFactory()
        # Update path here too
        filename = "../dataset/personaltrainer.json"  # Remove the leading ../
        pts = jff.read_data(filename, PersonalTrainer)
        return pts

    def get_all_location(self):
        jff = JsonFileFactory()
        # Update path here too
        filename = "../dataset/location.json"  # Remove the leading ../
        locate = jff.read_data(filename, Location)
        return locate

    def get_all_user(self):
        jff = JsonFileFactory()
        # Update path here too
        filename = "../dataset/user.json"  # Remove the leading ../
        user = jff.read_data(filename, User)
        return user

    def get_all_manager(self):
        jff = JsonFileFactory()
        # Update path here too
        filename = "../dataset/manager.json"  # Remove the leading ../
        manager = jff.read_data(filename, User)
        return manager

    def get_user_by_username(self, username):
        users = self.get_all_user()
        result = []
        for u in users:
            if u.username == username:
                result.append(u)
        return result

    def login(self,username,password):
        clients=self.get_all_client()
        for e in clients:
            if e.Username.lower()==username and e.Password==password:
                return e
        return None

    def get_pt_by_regisID(self, RegisID):
        pts = self.get_all_personaltrainer()
        result = []
        for p in pts:
            if p.RegisID == RegisID:
                result.append(p)
        return result

    def login_personal_trainer(self, username, password):
        personal_trainers = self.get_all_personaltrainer()
        for p in personal_trainers:
            if p.Username.lower() == username and p.Password == password:
                return p
        return None

    def login_manager(self, username, password):
        manager = self.get_all_manager()
        for m in manager:
            if m.Username.lower() == username and m.Password == password:
                return m
        return None
