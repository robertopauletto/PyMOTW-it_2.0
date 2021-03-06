#!/usr/bin/env python
# encoding: utf-8

import cmd

class Illustrate(cmd.Cmd):
    "Illustra l'uso dei metodi base della classe."
    
    def cmdloop(self, intro=None):
        print 'cmdloop(%s)' % intro
        return cmd.Cmd.cmdloop(self, intro)
    
    def preloop(self):
        print 'preloop()'
    
    def postloop(self):
        print 'postloop()'
        
    def parseline(self, line):
        print 'parseline(%s) =>' % line,
        ret = cmd.Cmd.parseline(self, line)
        print ret
        return ret
    
    def onecmd(self, s):
        print 'onecmd(%s)' % s
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        print 'emptyline()'
        return cmd.Cmd.emptyline(self)
    
    def default(self, line):
        print 'default(%s)' % line
        return cmd.Cmd.default(self, line)
    
    def precmd(self, line):
        print 'precmd(%s)' % line
        return cmd.Cmd.precmd(self, line)
    
    def postcmd(self, stop, line):
        print 'postcmd(%s, %s)' % (stop, line)
        return cmd.Cmd.postcmd(self, stop, line)
    
    def do_greet(self, line):
        print 'Salve,', line

    def do_EOF(self, line):
        "Uscita"
        return True

if __name__ == '__main__':
    Illustrate().cmdloop('Illustrazione dei metodi di cmd.Cmd')