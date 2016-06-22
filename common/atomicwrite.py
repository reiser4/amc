import os

class AtomicWrite(object):

    @staticmethod
    def writeFile(filename, content):
        tmpfilename = filename + "-tmp"
        if True: #isinstance(content, str):
            with open(tmpfilename, 'w') as f_tmp:
                f_tmp.write(content)
                f_tmp.flush()
                os.fsync(f_tmp.fileno())
            os.rename(tmpfilename, filename)
            #print "File scritto"
        else:
            print ("ERRORE: il valore passato non e' una stringa", filename, content)