import time, os, sys, re

class GmailParser(object):
    def __init__(self, source, __driver):
        self.source = source
        self.__driver = __driver # Just in case
    def getEmails(self):
        try:
            #emails_raw = re.findall("", self.source)
            #return emails_raw
            emails_raw_len = self.__driver.execute_script("return document.getElementsByClassName(\"yX\").length;")
            emails_raw = [];
            for i in range(emails_raw_len):
                emails_raw.append(self.__driver.execute_script("return document.getElementsByClassName(\"yX\")[%d].innerHTML;"%i))
            return emails_raw
        except: return "??????????"
    def getEmailId(self, raw_email):
        try:
            self.raw_email = raw_email
            id = re.search("\<div id=\"(.*?)\"", self.raw_email[:30])
            return id.group(1)
        except: return "??????????"
    def getEmailName(self, raw_email):
        try:
            self.raw_email = raw_email
            name = re.search("name=\"(.*?)\" data-hovercard", self.raw_email)
            return name.group(1)
        except: return "??????????"
    def getEmailSender(self, raw_email):
        try:
            self.raw_email = raw_email
            sender = re.search("email=\"(.*?)\" name=", self.raw_email)
            return sender.group(1)
        except: return "??????????"
    def getEmailSubject(self, raw_email):
        try:
            self.raw_email = raw_email
            subject = re.search("data-legacy-last-non-draft-message-id=\"(.*?)\"\>(.+?)\</span\>", self.raw_email)
            return subject.group(2)
        except: return "??????????"
    def readEmail(self, raw_email):
        try:
            self.raw_email = raw_email
            read = re.search("class=\"afn\"\>(.+?)\<span", self.raw_email)
            if "unread" in read.group(1): return False
            else: return True
        except: return "??????????"
