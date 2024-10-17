import hashlib,json
from pathlib import Path
from .common import atomic_json,dumps
class Registry:
    def __init__(self,path):self.path=Path(path)
    def promote(self,model,score,baseline,min_score=.7):
        if score<min_score or score<baseline:return False
        payload={'model':model,'score':score};checksum=hashlib.sha256(dumps(payload).encode()).hexdigest()
        atomic_json(self.path,{'payload':payload,'sha256':checksum});return True
    def load(self):
        data=json.loads(self.path.read_text())
        if hashlib.sha256(dumps(data['payload']).encode()).hexdigest()!=data['sha256']:raise ValueError('registry checksum mismatch')
        return data['payload']
