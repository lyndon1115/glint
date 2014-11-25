'''
Created on Nov 20, 2014

@author: ronaldjosephdesmarais
'''
import argparse

class GlintArgumentParser:
    parser=None
 
    def __init__(self):
        print "Init GlintArgumentParser"
        self.parser = argparse.ArgumentParser(description='Glint\'s Backup Argument Parser')
   
    def init_restore_arg_parser(self):
        self.parser.add_argument("-c","--cfgfile",nargs=1)
        self.parser.add_argument("-v","--version",nargs=1)
        self.parser.add_argument("-t","--tenant",nargs=1)
        self.parser.add_argument("-i","--image-name",nargs='*')
        self.parser.add_argument("-l","--list-images",action='store_true')
        
        
    def init_backup_arg_parser(self):
        self.parser.add_argument("-cfgfile",nargs=1)    

    