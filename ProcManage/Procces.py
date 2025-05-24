import subprocess

class process:
    def __init__(self, command, id,capture_output=True, text=True):
        """
        Initializes the SubprocessManager.

        Args:
            command (list or str): The command to execute (as a list of arguments
                                     or a string if shell=True).
            capture_output (bool): Whether to capture stdout and stderr.
            text (bool): Whether to decode the output as text.
        """
        self.id = id
        self.command = command
        self.capture_output = capture_output
        self.text = text
        self.process = None
        self.stdout = None
        self.stderr = None
        self.returncode = None
        
    async def start(self):
        """
        Starts the subprocess.
        """
        self.process = subprocess.Popen(self.command, stdout=subprocess.PIPE if self.capture_output else None,
                                        stderr=subprocess.PIPE if self.capture_output else None, text=self.text)
        self.stdout, self.stderr = self.process.communicate()
    
    async def wait(self):
        """
        Waits for the subprocess to complete.
        """
        self.returncode = self.process.wait()
        return self.returncode
    async def terminate(self):
        """
        Terminates the subprocess.
        """
        self.process.terminate()
        self.returncode = self.process.wait()
        return self.returncode
    async def kill(self):
        """
        Kills the subprocess.
        """
        self.process.kill()
        self.returncode = self.process.wait()
        return self.returncode      
    
    def get_returncode(self):
        """
        Returns the return code of the subprocess.
        """
        return self.returncode