import os
import importlib.util
import sys
import time
from pathlib import Path

class CogSystem:
    def __init__(self, modules_dir="modules"):
        self.modules_dir = modules_dir
        self.modules = []
        self.shared_data = {} 
        self.load_modules()
    
    def set_shared_data(self, **kwargs):
        """Set data to be shared with all modules"""
        self.shared_data.update(kwargs)
        #print(f"Shared data set: {list(self.shared_data.keys())}")
    
    def load_modules(self):
        """Load all Python modules from the modules directory"""
        if not os.path.exists(self.modules_dir):
            print(f"Modules directory '{self.modules_dir}' not found!")
            return
        
        module_files = [
            f for f in os.listdir(self.modules_dir) 
            if f.endswith('.py') and f != '__init__.py'
        ]
        
        if not module_files:
            print(f"No Python modules found in '{self.modules_dir}'")
            return
        
        for module_file in module_files:
            try:
                module_name = module_file[:-3] 
                module_path = os.path.join(self.modules_dir, module_file)
                
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                self.modules.append({
                    'name': module_name,
                    'module': module,
                    'path': module_path
                })
                #print(f"Loaded module: {module_name}")
                
            except Exception as e:
                print(f"Failed to load {module_file}: {e}")
    
    def run_modules(self):
        """Run all loaded modules sequentially with shared data"""
        if not self.modules:
            print("No modules to run!")
            return
        
       # print(f"\nRunning {len(self.modules)} modules with shared data: {self.shared_data}")
       # print("=" * 60)
        
        for module_info in self.modules:
            module_name = module_info['name']
            module = module_info['module']
            
           # print(f"\n[+] Running module: {module_name}")
           # print("-" * 30)
            try:
                start_time = time.time()
                
                if hasattr(module, 'main'):
                    module.main(self.shared_data)
                elif hasattr(module, 'main') and hasattr(module.main, '__code__'):
                    param_count = module.main.__code__.co_argcount
                    if param_count > 0:
                        module.main(self.shared_data)
                    else:
                        module.main()
                        
                else:
                    print(f"Warning: Module '{module_name}' has no main() function")
                
                end_time = time.time()
               # print(f"Completed in {end_time - start_time:.2f} seconds")
                
            except Exception as e:
                print(f"Error in module '{module_name}': {e}")
        
    #    print("\n" + "=" * 60)
        print("All modules completed!")


def printLogo():
    print(r"""
      ___           ___           ___     
     /  /\         /  /\         /  /\    
    /  /::\       /  /:/_       /  /:/_   
   /  /:/\:\     /  /:/ /\     /  /:/ /\  
  /  /:/~/::\   /  /:/ /::\   /  /:/ /:/_ 
 /__/:/ /:/\:\ /__/:/ /:/\:\ /__/:/ /:/ /\
 \  \:\/:/__\/ \  \:\/:/~/:/ \  \:\/:/ /:/
  \  \::/       \  \::/ /:/   \  \::/ /:/ 
   \  \:\        \__\/ /:/     \  \:\/:/  
    \  \:\         /__/:/       \  \::/   
     \__\/         \__\/         \__\/    

Hello {}. I see you are using ASE framework which is a modular OSINT
""".format(os.getlogin()))

def main():
    printLogo()
    cog_system = CogSystem()
    username = input("Enter username: ").strip()
    outputfile = input("Enter Output file name: ").strip() 
    cog_system.set_shared_data(username=username, output=outputfile +".txt")    
    cog_system.run_modules()

if __name__ == "__main__":
    main()
