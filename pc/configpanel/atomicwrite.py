import os

class AtomicWrite(object):

    @staticmethod
    def writeFile(filename, content):
        tmpfilename = filename + "-tmp"
        f_tmp = open(tmpfilename, "w")
        f_tmp.write(content)
        f_tmp.flush()
        os.fsync(f_tmp.fileno())
        f_tmp.close()
        if os.path.isfile(filename):
            #print("File gia` esistente, lo cancello.")
            os.remove(filename)
        os.rename(tmpfilename, filename)
