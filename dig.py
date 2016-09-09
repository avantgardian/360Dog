import cfg
import irc_core as IRC
from random import randint
import db_stuff

def dig():
    bones = randint(0, 10)
    username = IRC.get_sender(IRC.line[0])
    usercheck = db_stuff.get_user(username)
    if usercheck:
        db_stuff.set_bones(username, bones)
    else:
        db_stuff.create_user(username, bones)
    IRC.send_message(cfg.CHAN, 'diggy diggy ' + str(bones) + ' bones')

def chill_command():
    IRC.send_message(cfg.CHAN, db_stuff(IRC.get_sender(IRC.line[0])))

def pyramid(): # dank memes for the future
    pyramid_message = pyramid_split(IRC.line)
    IRC.send_message(cfg.CHAN, pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message + ' ' + pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message + ' ' + pyramid_message + ' ' + pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message + ' ' + pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message)

def pyramid2(): # haha this is so stupid, haha
    IRC.send_message(cfg.CHAN, 'a')
    IRC.send_message(cfg.CHAN, 'av')
    IRC.send_message(cfg.CHAN, 'ava')
    IRC.send_message(cfg.CHAN, 'avan')
    IRC.send_message(cfg.CHAN, 'avant')
    IRC.send_message(cfg.CHAN, 'avan')
    IRC.send_message(cfg.CHAN, 'ava')
    IRC.send_message(cfg.CHAN, 'av')
    IRC.send_message(cfg.CHAN, 'a')

def pyramid3():
    IRC.send_message(cfg.CHAN, 'goran pls OpieOP')

def pyramid_split(msg):
    result = IRC.get_message(msg)
    # this method is for noobs written by an equal noob:
    # result = result.lstrip('!pyramid ')
    result = result[8:]
    return result
