import cfg
import irc_core as IRC
from random import randint

def dig():
    bones = randint(0, 10)
    IRC.send_message(cfg.CHAN, 'i need to heal my own bones before i can dig :(), otherwise i\'d dig you ' + str(bones) + ' bones')

def chill_command():
    IRC.send_message(cfg.CHAN, 'who is that swaden noob? His name is ' + IRC.get_sender(IRC.line[0]))

def pyramid():
    pyramid_message = pyramid_split(IRC.line)
    IRC.send_message(cfg.CHAN, pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message + ' ' + pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message + ' ' + pyramid_message + ' ' + pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message + ' ' + pyramid_message)
    IRC.send_message(cfg.CHAN, pyramid_message)

def pyramid2():
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


def xml_whatever():
    IRC.send_message(cfg.CHAN, parse_xml())


def pyramid_split(msg):
    result = IRC.get_message(msg)
    # this method is for noobs written by an equal noob:
    # result = result.lstrip('!pyramid ')
    result = result[8:]
    return result

def parse_xml():
    parsestr = ET.parse('test.xml')
    root = parsestr.getroot()

    # result = root.tag #return parent tag
    # result = root.attrib #return parent attribute
    #for child in root:
    #if root[0].attrib > 9:
    return root[0][1].text
    #return root[0].text
