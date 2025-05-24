from .Procces import process

class ProcManager:
    async def __init__(self) -> None:
        self.return_codes = dict()
        self.processes = dict()
    async def add_process_and_start(self, process: process):
        self.processes[process.id] = process
        process.start()
    
    async def wait_until_all_finish(self):
        for p in self.processes.values():
            p.wait()
            
    async def kill_all(self):
        for p in self.processes.values():
            p.kill()
    
    async def collect_return_codes(self):
        for p in self.processes.values():
            self.return_codes[p.id] = p.get_returncode()