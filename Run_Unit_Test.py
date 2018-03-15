import unittest
import os

case_path=os.path.join(os.getcwd(),"Tests")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())